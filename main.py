import filecmp
import requests
from bs4 import BeautifulSoup as bs


def get_data():
    try:
        request = requests.get('https://coreseflores.studio/')
        content = bs(request.text,"html.parser")
        compare = testData(content.prettify())
        print(compare)
    except:
        print('Fora do ar')



def testData(text):
    with open('newContent.txt', 'w') as f:
            f.write(text)
            mismatch = filecmp.cmp('content.txt', 'newContent.txt', shallow=False)
    return(mismatch)


get_data()