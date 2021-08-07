# PlayStation5-Bot

Due to the scalpers reselling the new PlayStation above market price, I decided to make a tool to (hopefully) combat this. This Python bot constantly scrapes the Amazon Playstation5 page and when in stock, immediately adds one console to the cart and notifies the user of the action. The bot can also notify and auto-cart nearly every other Amazon product (with the exception of items that force the user to pick a size). 

# Table of Contents

1. [Requirements](#Requirements)
2. [Setup](#Setup)
3. [Usage](#Usage)
4. [Help/Troubleshooting](#Help/Troubleshooting)
5. [Demo](https://youtu.be/NCndmVCOSxQ)

# Requirements

1. Google Chrome
2. [Chrome Driver](https://chromedriver.chromium.org/)
3. Windows 10
4. A throwaway chrome profile
5. PiPy (installed with "pip install pypi-install")
6. All packages specified in the script (can easily be installed with pip, PiPy must be installed before this!)

# Setup

1. Open main.py script and replace my chrome data with yours, the fields needed should be clearly described in the comments.
2. Be Sure to change the `options.add_argument("profile-directory=Profile 6")` to your throwaway profile directory.
3. You can keep the throwaway account as the default sender (recommend) or change it (requires quite a bit of extra setup).
4. Change the receiver email as needed.
5. Optional: You can remove the `sendMailAlert()` method, as well as it's mentions if it is too much of a hassle to set up.

# Usage

1. Simply keep, change or, add links in the `urlArr` section in the script.
2. Run and enjoy, you will be notifiied when one of your desired items are found.

# Help/Troubleshooting

1. [Creating a throwaway profile for use.](https://stackoverflow.com/questions/52394408/how-to-use-chrome-profile-in-selenium-webdriver-python-3/52399027#52399027)
2. If the first solution does not work: [How to open a chrome profile in python.](https://stackoverflow.com/questions/52394408/how-to-use-chrome-profile-in-selenium-webdriver-python-3/52399027#52399027)
3. Feel free to submit an issue for help/suggestions!
