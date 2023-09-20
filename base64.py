import json
import base64
a=""
print(json.dumps(base64.b64decode(a).decode('ascii')))
b=""
print(base64.b64encode(b.encode('ascii')).decode('ascii'))