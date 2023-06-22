import json

from django.http import HttpResponse
from django.shortcuts import render
from .helpers import generate_base64_encoded_hmac
from .settings import SOC_CLIENT_SECRET, SOC_ALLOWED_CONTENT_SCREENS, SOC_CLIENT_ID, SOC_VERSION, SOC_ROUTE_PREFIX, \
    BRAND_NAME, SOC_API_HOST


def index(request):

    return render(request, 'home.html')


def pricing(request):

    return render(request, 'pricing.html')


def about_us(request):

    return render(request, 'about-us.html')


def socratease(request):

    payload_dict = {
        'username': 'new_user@gmail.com',
        'user_details': {
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'new_user@gmail.com'
            },
        'route_prefix': "/assessments",
        'path': "/cms/home"
        }

    payload_string = json.dumps(payload_dict, separators=(',', ':'))
    hmac_payload = generate_base64_encoded_hmac(client_secret=SOC_CLIENT_SECRET, payload_string=payload_string)

    soc_allowed_content_screens = SOC_ALLOWED_CONTENT_SCREENS.split(",")
    return render(
        request, 'socratease-entry.html', {
            'payload_string': payload_string, 'hmac_payload': hmac_payload,
            'soc_allowed_content_screens': soc_allowed_content_screens, 'soc_version': SOC_VERSION,
            'soc_client_id': SOC_CLIENT_ID, 'soc_route_prefix': SOC_ROUTE_PREFIX, 'brand_name': BRAND_NAME,
            'soc_api_host': SOC_API_HOST
            })

