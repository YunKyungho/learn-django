from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )
        # fields - 열 지정
        # exclude - 제외 열 지정
        # fields = "__all__" - 모든 열 지정
