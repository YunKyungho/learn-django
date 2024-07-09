from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):

    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
        )


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    # 관계가 있는 모델을 연결 시켜서 데이터를 주고 싶을 때
    # 방의 주인을 이용자가 직접 설정할 수 있게 해서는 안 되기에 read_only 설정을 준다.
    # owner는 view 호출 시 request 인자를 통해 확인한다.
    amenities = AmenitySerializer(read_only=True, many=True,)
    category = CategorySerializer(read_only=True,)

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1
        # 모든 관계를 1 만큼 확장시키라는 의미.

