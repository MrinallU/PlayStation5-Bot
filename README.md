# PlayStation5-Bot

Due to the scalpers reselling the new PlayStation5 above market price, I decided to make a tool to (hopefully) combat this. This Python bot constantly scrapes the Amazon and BestBuy Playstation5 pages, and when in stock, immediately adds one console to the cart and notifies the user of the action. The bot can also notify and auto-cart nearly every other Amazon/BestBuy product.

# Table of Contents

1. [Supported Platforms](#Supported-Platforms)
2. [Requirements](#Requirements)
3. [Setup](#Setup)
4. [Usage](#Usage)
5. [Help/Troubleshooting](#Help/Troubleshooting)
6. [Demo](https://youtu.be/NCndmVCOSxQ)

# Requirements

1. Google Chrome
2. [Chrome Driver](https://chromedriver.chromium.org/)
3. Windows 10
4. A throwaway chrome profile
5. The pip package manager
6. PiPy (installed with "pip install pypi-install")
7. All packages specified in the script (can easily be installed with pip, PiPy must be installed before this!)
 <br/>
 > Step 6 may be skipped if you clone the project with the PyCharm, as all packages will be installed for you.

# Setup

1. Open main.py script and replace my chrome data with yours, the fields needed should be clearly described in the comments.
2. Change `executable_path='C:/Users/uma/chromedriver.exe'` to your respective Chrome path.
3. Change `options.add_argument("profile-directory=Profile 6")` to your desired profile directory (preferably not your main profile).
4. You can keep the throwaway account as the default sender address (recommend) or change it (requires lots of extra setup).
   <br/>
   <br/>
   **If you do decide to make a new account for the sender address:**

   1. Be Sure to change the email and password to your throwaway email.
   2. Check the [Help/Troubleshooting](#Help/Troubleshooting) section for some more relavent tips.

5. Change the receiver email as needed.
6. Optional: You can remove the `sendMailAlert()` method, as well as where it is being called if you do not want email notifications or it is too much of a hassle to set up.

# Usage

1. Simply keep, change or, add links in the `urlArr` section in the script.
2. Run and enjoy, you will be notified when one of your desired items are found.

# Help/Troubleshooting

1. [Troubleshoot steps 2 and 3.](https://stackoverflow.com/questions/52394408/how-to-use-chrome-profile-in-selenium-webdriver-python-3/52399027#52399027)
2. Feel free to submit an issue for help/suggestions!

# Supported Platforms

1. BestBuy
2. Amazon
