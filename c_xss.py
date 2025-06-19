import urllib.parse


def get_custom_payload():
    c_payload=input("ENTER XSS PAYLOAD TO ENCODE: ")
    encoded_payload=urllib.parse.quote(c_payload)
    print(encoded_payload)

