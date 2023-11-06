from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ("owner", "books", "status", "comment", "due_time", "created_time")
