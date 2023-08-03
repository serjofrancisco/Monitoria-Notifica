import requests
from bs4 import BeautifulSoup as bs
import os
from dotenv import load_dotenv
load_dotenv()


def get_content():
        request = requests.get(os.environ['url'])
        content = bs(request.text,"html.parser")
        with open('content.txt', 'w') as f:
            f.write(content.prettify())
        print("Arquivo criado")

get_content()