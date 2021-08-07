# PlayStation5-Bot

Due to the scalpers reselling the new PlayStation above market price, I decided to make a tool to (hopefully) combat this. This Python bot constantly scrapes the Amazon Playstation5 page and when in stock, immediately adds one console to the cart and notifies the user of the action.

# Requirements

1. Google Chrome
2. [Chrome Driver](https://chromedriver.chromium.org/)
3. Windows 10
4. PiPy (installed with "pip install pypi-install")
5. All packages specified in the script (can easily be installed with pip, PiPy must be installed before this!)

# Instructions

1. Open main.py script and replace my chrome data with yours, the fields needed should be clearly described in the comments.
2. You can keep the throwaway account as the default sender (recommend) or change it (requires quite a bit of extra setup).
3. Change the receiver email as needed.
4. Optional: You can remove the `sendMailAlert()` method, as well as it's mentions if it is too much of a hassle to set up.

# Help/Troubleshooting

Feel free to submit an issue.
