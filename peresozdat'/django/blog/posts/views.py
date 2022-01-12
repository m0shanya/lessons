import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def post_index(request):
    value = request.GET.get("key")
    logger.info(value)
    return HttpResponse("Post index view")

