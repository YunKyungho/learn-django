from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT

from categories.models import Category
from .models import Room, Amenity
from .serializers import RoomDetailSerializer, RoomListSerializer, AmenitySerializer


class Rooms(APIView):

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            # 유저 인증 함수
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError
                except Category.DoesNotExist:
                    raise ParseError
                room = serializer.save(
                    owner=request.user,
                    category=category,
                )
                # owner=request.user 해당 인자로 serializer의 create 함수 호출 시 validated_data를 자동으로 넘겨줄 것이다.
                # amentiy가 없는 방을 생성할 수 있게 room을 먼저 저장한 뒤
                # amenity를 추가하는 방식으로 만듦.
                amenities = request.data.get("amenities")
                for amenity_pk in amenities:
                    try:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                    except Amenity.DoesNotExist:
                        # 만약 잘못된(존재하지 않는) amenity가 보내졌을 시 room을 삭제하는 정책.
                        room.delete()
                        raise ParseError(f"Amenity with id {amenity_pk} not found")
                    room.amenities.add(amenity)

                serializer = RoomDetailSerializer(room)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)


class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):

    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
