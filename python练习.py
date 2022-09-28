import urllib.request

myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())   # 200

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)   # 404
    else:
        print(200)
