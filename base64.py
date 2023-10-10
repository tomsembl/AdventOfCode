import json
import base64
def decode64(a):
    print(json.dumps(base64.b64decode(a).decode('ascii')))
def encode64(b):
    print(base64.b64encode(b.encode('ascii')).decode('ascii'))
decode64("")
encode64("")
