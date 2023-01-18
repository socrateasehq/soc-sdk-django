import json

from django.http import HttpResponse
from django.shortcuts import render
from .helpers import generate_base64_encoded_hmac
from .settings import SOC_CLIENT_ID, SOC_CLIENT_SECRET, SOC_VERSION


def index(request):

    return HttpResponse("Hello, world!")


def socratease(request):

    payload_dict = {
        'username': 'user@gmail.com',
        'user_details': {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'user@gmail.com'
            },
        'route_prefix': "/assessments",
        'path': "/cms/home"
        }

    payload_string = json.dumps(payload_dict, separators=(',', ':'))
    hmac_payload = generate_base64_encoded_hmac(client_secret=SOC_CLIENT_SECRET, payload_string=payload_string)

    return render(
        request, 'socratease-entry.html', {
            'payload_string': payload_string, 'hmac_payload': hmac_payload, 'client_id': SOC_CLIENT_ID,
            'soc_version': SOC_VERSION
            })
