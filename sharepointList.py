
from shareplum import Site
from requests_ntlm import HttpNtlmAuth

url = ""
listName = "AllItems"

auth = HttpNtlmAuth('username', 'password')
site = Site(url, auth=auth)
