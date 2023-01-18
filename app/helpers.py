import hmac
from hashlib import sha256
import base64


def generate_base64_encoded_hmac(client_secret, payload_string):

    bytes_client_secret = client_secret.encode('utf-8')
    payload_bytes = payload_string.encode('utf-8')
    hmac_payload = hmac.new(bytes_client_secret, payload_bytes, sha256)
    base64_hashed_string = base64.b64encode(hmac_payload.digest()).decode()

    return base64_hashed_string

