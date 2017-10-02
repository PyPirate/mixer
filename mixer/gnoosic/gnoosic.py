import requests
import sys

payload = {
    "skip": 1,
    "Fave01": "Daft Punk",
    "Fave02": "Daft Punk",
    "Fave03": "Daft Punk"}

url = 'http://www.gnoosic.com/faves.php'
url_art = 'http://www.gnoosic.com/artist/'



with requests.Session() as s:
    s.headers.update({'Cookie': 's=45699428'})
    s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    s.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'})
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
    s.headers.update({'referer': url})
    r = (s.post(url, data=payload))
