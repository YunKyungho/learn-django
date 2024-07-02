from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    # row 생성 날짜 자동 생성
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    # row 수정 날짜 자동 수정

    class Meta:
        abstract = True
        # 위 코드로 django에게 추상 모델이라고 알려주고 DB에 저장되지 않게 함.
