from rest_framework.serializers import ModelSerializer, SerializerMethodField
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

    rating = SerializerMethodField()
    # SerializerMethodField가 model에 정의 해놓은 method를 사용하게 해준다

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
        )

    def get_rating(self, room):
        # get_{변수명}과 같이 함수명을 만들어야지만 rating field와 매칭 된다. 
        return room.rating()

class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    # 관계가 있는 모델을 연결 시켜서 데이터를 주고 싶을 때
    # 방의 주인을 이용자가 직접 설정할 수 있게 해서는 안 되기에 read_only 설정을 준다.
    # owner는 view 호출 시 request 인자를 통해 확인한다.
    amenities = AmenitySerializer(read_only=True, many=True,)
    category = CategorySerializer(read_only=True,)
    rating = SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1
        # 모든 관계를 1 만큼 확장시키라는 의미.

    def get_rating(self, room):
        return room.rating()
