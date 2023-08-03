import filecmp
import requests
from bs4 import BeautifulSoup as bs
import smtplib
import email.message
import os
from dotenv import load_dotenv
load_dotenv()


def get_data():
    print(os.environ['email'])
    try:
        request = requests.get('https://coreseflores.studio/')
        content = bs(request.text,"html.parser")
        compare = test_data(content.prettify())
        print(compare)
    except:
        print("Fora do ar")



def test_data(text):
    with open('newContent.txt', 'w') as f:
            f.write(text)
            match = filecmp.cmp('content.txt', 'newContent.txt', shallow=False)
    return(match)

def change_default(text):
    with open('content.txt', 'w') as f:
            f.write(text)
# codigo abaixo é de autoria do hashtagTreinamentos
def enviar_email():  
    corpo_email = """
    <p>Tem Algum problema no site, verifique</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Problema no site"
    msg['From'] = os.environ['email']
    msg['To'] =  os.environ['receiver']
    password = os.environ['password']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')





get_data()