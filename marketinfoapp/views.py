from django.http import HttpResponse, HttpResponseServerError
from bhavcopyservice.redis_client import redis_client
from bhavcopyservice.utils import getcurrentDate

def index(request):
    try:
        response = HttpResponse(redis_client().get('Equities'))
    except Exception as e:
        print('Request to Redis failed with reason : ', e)
        response = HttpResponseServerError('Something went wrong at the Server')
    return response