from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from users.permissions import IsStudent, IsLibrarianOrStudent
from .models import Order, ORDER_STATUS
from .serializers import OrderSerializer, LibrarianOrderSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["owner"] = request.user
        books = serializer.validated_data["books"]

        for book in books:
            if book.quantity <= 0:
                book.isPossibleToOrder = False
            if not book.isPossibleToOrder:
                return Response({"message": f"К сожалению вы не можете забронировать книгу {book.title} на данный момент"})

        order = serializer.save()

        for book in order.books.all():
            if not book.isPossibleToOrder:
                continue
            book.orders += 1
            book.quantity -= 1
            book.save()

        return Response(serializer.data, status=HTTP_201_CREATED)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.status == "Student":
            return Order.objects.filter(owner=user)

        return Order.objects.all()


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrStudent]

    def put(self, request, *args, **kwargs):
        order = self.get_object()

        if order.status not in [status[0] for status in ORDER_STATUS]:
            return Response({"error": "Неверный статус заказа"})

        if (
                request.user.status == "Student"
                and order.status == ORDER_STATUS[0][1]
                and order.owner == request.user
        ):
            return super().put(request, *args, **kwargs)

        if request.user.status == "Librarian":
            self.serializer_class = LibrarianOrderSerializer
            return super().put(request, *args, **kwargs)

        return Response(
            {"message": "У вас нет разрешения на изменение этого заказа"},
            status=HTTP_403_FORBIDDEN,
        )

    def delete(self, request, *args, **kwargs):
        order = self.get_object()

        if (
                request.user.status == "Student"
                and order.status == ORDER_STATUS[0][1]
                and order.owner == request.user
        ):
            order.delete()
            return Response(
                {"message": "Заказ удален успешно"}, status=HTTP_204_NO_CONTENT
            )

        if (
                request.user.status == "Librarian"
                and order.status == ORDER_STATUS[2][1]
        ):
            order.delete()
            return Response(
                {"message": "Заказ удален успешно"}, status=HTTP_204_NO_CONTENT
            )

        return Response(
            {"message": "У вас нет разрешения на удаление этого заказа"}, status=HTTP_403_FORBIDDEN
        )
