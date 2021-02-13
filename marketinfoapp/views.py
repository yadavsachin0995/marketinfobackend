from django.http import HttpResponse
from bhavcopyservice.redis_client import redis_client
from bhavcopyservice.utils import getcurrentDate

def index(request):
    return HttpResponse(redis_client().get('Equities'))