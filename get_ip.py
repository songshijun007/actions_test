import requests

url = "http://pv.sohu.com/cityjson"
rep = requests.get(url)

print(rep.text)
