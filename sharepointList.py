
from shareplum import Site
from requests_ntlm import HttpNtlmAuth

url = "https://augt.sharepoint.com/sites/EngagementLettersUAT"
listName = "AllItems"

auth = HttpNtlmAuth('username', 'password')
site = Site(url, auth=auth)