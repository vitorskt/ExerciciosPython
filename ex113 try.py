import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen('https://www.facebook.com')

except urllib.error.URLerror:
    print('O site facebook não está acessivel no momento.')

else:
    print('consegui acessar o site facebook com sucesso!')
