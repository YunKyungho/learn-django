from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    # admin action 함수는 3개의 인자를 받음.
    print(model_admin)
    # model_admin은 이 액션을 호출한 클래스 (admin model)
    print(request.user)
    # request는 이 함수를 호출한 대상에 대한 정보가 담김. admin만 호출 가능한 함수를 만든다던지 할 수 있음.
    for room in rooms.all():
        room.price = 0
        room.save()

    # 주로 데이터를 엑셀로 export 할 때도 쓰이며 단체로 값 수정 하는 등의 용도로 사용가능하다.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (
        reset_prices,
    )

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "^name",
        # 앞에 ^를 붙히면 startwith 조건으로 검색한다.
        "=price",
        # 앞에 =를 붙히면 extract match 조건으로 검색한다.
        "owner__username",
        # 위 같은 형식으로 연결된 외래키의 속성으로 검색도 가능하다.
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
