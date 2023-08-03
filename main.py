import requests
from bs4 import BeautifulSoup as bs


def get_data():
    try:
        request = requests.get('https://coreseflores.studio/')
        content = bs(request.text,"html.parser")
        print(content.title.text)
    except:
        print('Fora do ar')



def testData(text):
    try:
        with open('content.txt', 'r') as f:
            content = f.read()
            print(text)
    except:
        print('Erro')
   

get_data()