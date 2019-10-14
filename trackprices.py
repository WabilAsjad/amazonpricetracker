import requests
from bs4 import BeautifulSoup
import smtplib
import time 



def check_price():
    
    header1 = input("Please enter your User-Agent.")
    headers = {"User-Agent": str(header1)
            }
    URL = input("Hello, please provide an Amazon link to the product you are interested in.\n")
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id= "productTitle").get_text()
    
    
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id= "productTitle").get_text()

    price = soup2.find(id= "priceblock_ourprice").get_text()
    converted_price = float(price.strip("$"))
    
    given_price = float(input("Please provide the price you are looking for: $"))
    if (converted_price < given_price):
        send_mail()
    else:
        print("Sorry, the product still costs more than" + given_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  #establishes connection with other server
    server.starttls()
    server.ehlo()
    
    sender_email = input("Please log in with your gmail: ")
    sender_password = input("Please enter your password: ")
    server.login(sender_email, sender_password)
    subject = "Price decrease! "
    body = "Check the amazon link! " + URL 
    
    msg= "Subject: Price decrease!\n\n Checkout the Amazon link!\n" + URL
            
    
    receiver_email = input("Please provide the email of the receiver: ")
    server.sendmail(sender_email, receiver_email, msg)
    
    print("Email has been sent.")
    
    server.quit() 
    
while(True):
     check_price()
     time.sleep(60)
