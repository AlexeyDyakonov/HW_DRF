from rest_framework.serializers import ValidationError


class YouTubeValidator:
    """Проверка ссылок на сторонние ресурсы, кроме youtube.com"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_url = dict(value).get(self.field)
        if bool(dict(value).get("video_url")) and not bool("youtube.com" in video_url):
            raise ValidationError("Недопустимая ссылка")
