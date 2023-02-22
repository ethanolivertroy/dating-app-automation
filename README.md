# Automate Your Swipes on Tinder or Bumble using Python

![Copy of Copy of Copy of Flaws (4 × 3 in) (2)](https://user-images.githubusercontent.com/63926014/211109980-294b2a0f-f7c8-4530-b4d8-3071639b20d7.png)


tinder bot to practice

- Mkdir tinderbot
- DL Chrome Driver https://chromedriver.chromium.org/downloads
- brew install virtualenv https://virtualenv.pypa.io/en/latest/
- virtualenv venv
- pip install selenium
- source venv/bin/activate
- python -i tinder_bot.py



Edit `secrets.py` with facebook username and password


## Tinderbot V2

Changes made:

1. Replaced hardcoded XPaths with more reliable methods such as By.XPATH and By.NAME.
2. Added exception handling in the like() and dislike() methods.
3. Added a try-except block to catch exceptions in the auto_swipe() method and exit the loop when there are no more matches.
4. Added the close_popup() method to close popups that may appear during swiping.
5. Added the close_match() method to close the match popup.
6. Removed the slikepop() method