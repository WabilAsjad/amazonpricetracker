import requests
from bs4 import BeautifulSoup
import smtplib
import time 

URL = "https://www.amazon.com/dp/B07R3HYDVW/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B07R3HYDVW&pd_rd_w=fK0yx&pf_rd_p=c83c55b0-5d97-454a-a592-a891098a9709&pd_rd_wg=bEJlN&pf_rd_r=RP83G0QJ3MCE5TJYYB9V&pd_rd_r=16e28d4b-1b27-4be9-ad77-46bda62b0272&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNSFdUNjJKWFpRVVgmZW5jcnlwdGVkSWQ9QTAxNjIyMjQzVDQ5TFdJUFdRVkpWJmVuY3J5cHRlZEFkSWQ9QTAzNDczMjJBRFo1TkVQNDJPWkYmd2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWMmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"



    
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