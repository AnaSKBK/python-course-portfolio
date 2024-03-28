from django.http import HttpRequest
from author.models import Author


def author(request: HttpRequest) -> dict:
    """
    Информация об авторе
    """
    return {"author": Author.objects.last()}