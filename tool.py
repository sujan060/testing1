import requests as reqs
paramStr = input('Enter the wifi SSID:  ')
print(paramStr)
url = "http://secretwebsite007.000webhostapp.com/api.php"
paramDict = {'ssid':paramStr}
response = reqs.get(url,params=paramDict)
print(response.status_code)
print(response.text)
