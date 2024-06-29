from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "price",
        "address",
    ]
    # 열 생성
    list_filter = ["price"]
    # 필터
    search_fields = ["address"]
    # 검색창
