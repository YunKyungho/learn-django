from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    """
    serializer는 직역하면 직렬화다.
    데이터가 모델의 형식에 맞는지 유효성 검사를 하며
    json 데이터를 전송하기 위한 형식으로 변환 시켜주는 역할을 한다.
    역직렬화는 아마 안 할 것이다.
    받은 데이터는 유효성 검사만 하여 DB와 소통할 수 있게 해준다.
    그냥 Serializer의 경우 모델의 형식에 맞게 모든 열에 대한 데이터 정의를 해주어야 했으나
    ModelSerializer는 이러한 반복적인 작업을 하지 않게 해준다.
    """

    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )
        # fields - 열 지정
        # exclude - 제외 열 지정
        # fields = "__all__" - 모든 열 지정
