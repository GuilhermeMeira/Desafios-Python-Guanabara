import urllib
import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('falhou')
else:
    print('deu bom')