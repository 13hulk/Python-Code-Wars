import urllib.request
import urllib.parse

values = {'q':'vikas zingade'}
data = urllib.parse.urlencode(values)
url = "https://www.google.com/search?"+data

head = {'User-Agent':"Mozilla/5.0 (X11; Linux i686)"}

req = urllib.request.Request(url, headers = head)
res = urllib.request.urlopen(req)
print(res.read())

print("hi")

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum
