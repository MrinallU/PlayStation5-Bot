import ssl
import time
import smtplib

from bs4 import BeautifulSoup
from selenium import webdriver
from win10toast import ToastNotifier
from selenium.webdriver.common.by import By

# Enter Amazon URL(s) as needed
urlArr = [
    'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_3?dchild=1&keywords=ps5&qid=1628291295&sr=8-3',
    'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',
    'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161',
    'https://www.bestbuy.com/site/combo/ps5-consoles/8f146095-0a5f-4993-b123-711a1d34745b',
    'https://www.bestbuy.com/site/combo/ps5-consoles/effaa8ef-23cd-4191-8fb4-485e6f1f9875'
]

availableList = []

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\uma\\AppData\\Local\\Google\\Chrome\\User Data - Copy")  # Copying
# user data folder is required! You also must replace with your path.

options.add_argument("profile-directory=Profile 6")  # Fill this wih the profile directory that you want to use
# preferably a throwaway account).
options.add_argument('no-sandbox')
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path='C:/Users/uma/chromedriver.exe', options=options)  # Fill with your own
# chrome driver executable path

toaster = ToastNotifier()  # Initialize toast notifications (only for windows systems)


# Helper methods
def listToString(s):
    str1 = " "
    return str1.join(s)


def sendMailAlert():
    port = 465  # For SSL (No Need to Change)
    password = "Thekey2275!"  # No need to change this.

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:  # DO NOT Change this line.
        server.login("throwaway2342342342345r@gmail.com", password)  # No need to change.

        server.sendmail("throwaway2342342342345r@gmail.com", "mrinalluma@gmail.com",  # Change the 'mrinalluma@gmail.com' to your email.
                        "Ps5 is in stock and should be added in cart, check asap!")


# Bot checks and process URL.
def process(currURL):
    driver.get(currURL)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    available = soup.body.find(text="Add to Cart")

    print(available)

    if not available:
        print("The Ps5 is out of stock in this link")
    else:
        if "amazon" in currURL:
            availableList.append(currURL)
            driver.find_element(By.ID, "add-to-cart-button").click()  # Adds to cart
            print("Ps5 is in stock!")

            time.sleep(1)  # Gives the page time to load for protection plan
            try:
                driver.find_element(By.ID, "attachSiNoCoverage").click()  # If protection plan is included in the
                # product then auto refuse.
            except:
                print("No protection plan found, moving on...")
        elif "bestbuy" in currURL:
            availableList.append(currURL)
            driver.find_element_by_class_name("fulfillment-add-to-cart-button").click()  # Adds to cart
            print("Ps5 is in stock!")


while True:
    for url in urlArr:
        process(url)
        if len(availableList) > 0:
            # Send alert(s)
            sendMailAlert()
            toaster.show_toast("Ps5 is in stock!", listToString(availableList))  # Shows notification on desktop (Windows
            # systems only)

            print(listToString(availableList))  # Displays links that currently have a console in stock.
            exit()  # Terminates after adding one PS5 as I am not a scalper!
    print()
    print("Trying Again...")
    driver.minimize_window()
