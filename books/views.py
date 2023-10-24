from django.db.models import Q
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.permissions import IsLibrarian
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class CategoriesCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoriesChangeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class BooksCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]
    parser_classes = (MultiPartParser,)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        isPossibleToOrder = serializer.validated_data["isPossibleToOrder"]
        if serializer.validated_data["quantity"] == 0:
            isPossibleToOrder = False

        serializer.save()
        return Response({'message': 'Book created successfully'},
                        status=HTTP_201_CREATED)



class BooksListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        category = request.GET.get("category")
        less_orders = request.GET.get("less_orders")
        more_orders = request.GET.get("more_orders")
        author = request.GET.get("author")
        title = request.GET.get("title")
        book_id = request.GET.get("book_id")

        if book_id:
            self.queryset = self.queryset.filter(id=book_id)

        if category:
            category = category.capitalize()
            self.queryset = self.queryset.filter(category__title=category)
        if less_orders:
            self.queryset = self.queryset.filter(orders__lte=less_orders)
        if more_orders:
            self.queryset = self.queryset.filter(orders__gte=more_orders)

        if author:
            self.queryset = self.queryset.filter(Q(author__icontains=author))
        elif title:
            self.queryset = self.queryset.filter(Q(title__icontains=title))

        return super().get(request)


class BooksChangeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]
