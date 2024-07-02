from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        # 필터의 선택 사항, 버튼을 구성해주는 함수
        return [
            ("재밌었", "재밌었"),
            ("좋았", "좋았"),
            ("나쁘", "나쁘"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        return reviews
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
        # 외래 키 기반으로 필터 생성도 가능하다.
    )
