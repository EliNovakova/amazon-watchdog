from bs4 import BeautifulSoup
import requests
import pprint
import lxml
import smtplib

SMTP = "smtp.gmail.com"
MY_EMAIL = "<INSERT-EMAIL>"
PASSWORD = "<INSERT-PASSWORD>"

URL = "<INSERT-PRODUCT-URL>"
PRICE = 800.00

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language":"cs-CZ,cs;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)

pprint.pprint(response.content)

soup = BeautifulSoup(response.text, "lxml")
price_item = soup.find(name="span", id="priceblock_ourprice")   # finds item price
name_item = soup.find(id="productTitle")    # finds item name
price = float(price_item.getText().split("$")[1])   # gets plain name and price
name = name_item.getText().strip()

print(price)
print(name)

if price < PRICE:  # sends email if price drops bellow 800
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{name} is now ${price}\n{URL}"
        )
