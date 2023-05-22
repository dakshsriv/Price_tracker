import requests
from bs4 import BeautifulSoup
import time
from email.message import EmailMessage
import ssl
import smtplib
import sqlite3
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

connection = MySQLdb.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl = {
    "ca": "/etc/ssl/certs/ca-certificates.crt"
  }
)

try:
    cur = connection.cursor()
except:
    print("error")
    os.exit()


email_sender="ptracking968@gmail.com"
#main_password = "Paudha77_L"
password = "snilqrhdolrbcrgy"
subject = "Price change!"





#email_receiver="daksh.srivastava.10@gmail.com"
#link = "https://www.amazon.com/RK-ROYAL-KLUDGE-Mechanical-Ultra-Compact/dp/B089GN2KBT/?th=1"


#Fix scope problem with email_reciever and link

def run():

    

    HEADERS = {
        'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/44.0.2403.157 Safari/537.36'),
        'Accept-Language': 'en-US, en;q=0.5'
    }


    threshold = 0.8

    while True:
        cur.execute("SELECT link, email, prevPrice FROM Products")
        lst = cur.fetchall()
        print(lst)
        if lst == []:
             time.sleep(5)
             continue

        try:
            for l in lst:
                prevprice = l[2]
                print(prevprice)

                
                
                link = l[0]
                email_receiver = l[1]
                em = EmailMessage()
                em['From'] = email_sender
                em['Subject'] = subject
                em['To'] = email_receiver
                            

                page=requests.get(link, headers=HEADERS)
                mybytes = page.text
                #print(mybytes)
                mystr = mybytes#.decode("utf8")

                #print(mystr)

                soup = BeautifulSoup(mystr, features="html.parser")
                #print(soup.prettify())
                price = float(soup.find('span', class_='a-price-whole').get_text() + soup.find('span', class_='a-price-fraction').get_text())
                print(price)
                if price <= prevprice*threshold:
                        print("New low price!")
                        body = f"""
                        The following product now has a lower price: {link}  
                        """
                        em.set_content(body)
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                            smtp.login(email_sender, password)
                            smtp.sendmail(email_sender, email_receiver, em.as_string())     
                cur.execute("UPDATE Products SET prevPrice=? WHERE link=? AND email=?", (price, link, email_receiver))
        except:
             continue

run()