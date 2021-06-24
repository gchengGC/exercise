import requests
from requests.packages import urllib3
urllib3.disable_warnings()
import re

reponse = requests.get('https://www.baidu.com/')
print(type(reponse))
print(requests.status_codes)
print(type(reponse.text))
print(reponse.text)
print(reponse.cookies)

content = '''Hello 1234567 World_This
is a Pegex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))