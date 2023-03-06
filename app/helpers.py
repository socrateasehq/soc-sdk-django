import hmac
from hashlib import sha256
import base64
import requests


def generate_base64_encoded_hmac(client_secret, payload_string):

    bytes_client_secret = client_secret.encode('utf-8')
    payload_bytes = payload_string.encode('utf-8')
    hmac_payload = hmac.new(bytes_client_secret, payload_bytes, sha256)
    base64_hashed_string = base64.b64encode(hmac_payload.digest()).decode()

    return base64_hashed_string


def get_socratease_credentials():

    from .settings import SOC_CLIENT_SECRET, SOC_CLIENT_ID

    credentials_string = '{0}:{1}'.format(SOC_CLIENT_ID, SOC_CLIENT_SECRET)
    credentials_bytes = credentials_string.encode('utf-8')

    base64_bytes = base64.b64encode(credentials_bytes)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string


def make_soc_request(url, method='GET', data=None):

    soc_credentials_string = get_socratease_credentials()

    headers = {'Authorization': 'SOC {0}'.format(
        soc_credentials_string
        )}

    if method == 'GET':
        soc_results = requests.get(url, headers=headers, timeout=10)
    elif method == 'POST':
        soc_results = requests.post(url, json=data, headers=headers, timeout=15)
    elif method == 'DELETE':
        soc_results = requests.delete(url, headers=headers, timeout=10)
    elif method == 'PATCH':
        soc_results = requests.patch(url, json=data, headers=headers, timeout=10)
    else:
        soc_results = None

    return soc_results
