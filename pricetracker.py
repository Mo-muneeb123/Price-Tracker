import requests
from bs4 import BeautifulSoup
import smtplib
# import time


URL = 'https://www.nike.com/t/dunk-low-retro-mens-shoes-87q0hf/DD1391-100?nikemt=true&cp=35640345119_search_--x-20429762868---c-----9016911-13095480-00194502876055&gad_source=1&gclid=CjwKCAiA4smsBhAEEiwAO6DEjT_J10xrSTWtqaextMF6iu0ZU3et460gXGhG55Q2a8zE6Ex5FEvdbRoCUkUQAvD_BwE&gclsrc=aw.ds'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' }

def priceCheck(): 
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find(id="pdp_product_name").get_text()
    price = soup.find('div', class_='product-price css-11s12ax is--current-price css-tpaepq').get_text()
    cleaned_price = price.replace('$', '').replace(',', '')


    priceFinal = float(cleaned_price[0:5])

    if(priceFinal < 100):
        mailSend()


    print(priceFinal)
    print(name.strip())

    if(priceFinal < 100):
        mailSend()


def mailSend():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('user@gmail.com', 'password' )

    subject = "Price drop"
    body = "Check the link for the shoe: https://www.nike.com/t/dunk-low-retro-mens-shoes-87q0hf/DD1391-100?nikemt=true&cp=35640345119_search_--x-20429762868---c-----9016911-13095480-00194502876055&gad_source=1&gclid=CjwKCAiA4smsBhAEEiwAO6DEjT_J10xrSTWtqaextMF6iu0ZU3et460gXGhG55Q2a8zE6Ex5FEvdbRoCUkUQAvD_BwE&gclsrc=aw.ds "

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '12345.com',
        '6789.com',
        msg
    )
    print("Email has been sent")

    server.quit()

# while(True):
#   priceCheck()
#    time.sleep(86400)


