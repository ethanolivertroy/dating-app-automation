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

## Objective: Automate Swiping on Dating Apps Using Python because Online Dating Sucks

Let's face it...dating ~~in 2020~~ in 2023 sucks. 

So to remedy this let's whip up something in python to deal with the new face of dating which is **unfortunately** online dating apps. 

At the same time we get to practice the skill of creating a python bot that could be used to automate other things as well.

### Building a Bot: Selecting and Interacting
Building this sort of bot is simply a series of selecting objects within the web app and interacting with that object via entering inputs and clicks

![image](https://github.com/ethanolivertroy/dating-app-automation/assets/63926014/1d5deb94-fb2e-4cf1-b50b-fbf2f25d556d)




<mark>It's about translating the needed actions into code steps...</mark>

### Get Stuff We Will Need to Build

#### Chrome Driver

1. Download the most recent Chrome Driver <https://chromedriver.chromium.org/downloads>
2. Move the chrome driver file into your bin
 ```bash
 mv ~/Downloads/chromedriver /usr/local/bin
 ```
#### Create a File and Virtual Environment

3. Brew install virtualenv (using <https://brew.sh/>)
<https://virtualenv.pypa.io/en/latest/>
4. Create a file for the bot
```bash
mkdir tinder_bot
touch tinder_bot.py
```
5. Create a Virtual Environment and Activate It
```bash
virtualenv venv
source venv/bin/activate
```
#### Selenium

6. Install Selenium
```bash
pip install selenium
```

#### Create a secrets file

7. Secrets will be a .py file that we will create with the username and password for the facebook login
```bash
# name this secrets.py
username = 'usernameXX'
password = 'passwordXX'
```

#### What do we need the bot to do in order to login?
1. Click on the "Login with Facebook" button
2. Enter our e-mail address
3. Enter our password
4. Click Login

### Import All Needed Libraries in tinder_bot.py

```python3
from selenium import webdriver

from selenium.webdriver.common.by import By

from time import sleep

from secrets import username, password
```

### Now we start working on the actual tinder_bot.py file. 

#### We create a new class for the bot and within that class we will start webdriver.Chrome

 ```python3
class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()
```

#### Add a login function to open the website

```python3
def login (self):
        self.driver.get('https://tinder.com')
```

I selected the buttons by finding the element by XPath. There are other ways to do this such as by ID which I'll use later.

#### Add Sleeps

```python3
        sleep(2)

        first_click = self.driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
        first_click.click()

        sleep (1)

        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
```

The sleeps are added to give the bot pause. The ☝🏾 above allows us to get in with the facebook login information held in ```secrets.py```

#### Multiple Windows

Unfortunately, we have to manage several windows

```python3
        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
```

#### Pass the secrets into the facebook login

```python3
        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw_in.send_keys(password)

```

#### Click the login button

```python3
        login_btn = self.driver.find_element(By.ID, 'loginbutton')
        login_btn.click()

        self.driver.switch_to.window(base_window)
```

#### Get Rid of Pop-ups

```python3
        popup_1 = self.driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

```

#### Define some functions for liking, disliking, and autoswipe

```python3
# like
    def like(self):
        like_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="gamepadLike"]')
        like_btn.click()
```

```python3
# dislike
    def dislike(self):
        dislike_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="gamepadDislike"]')
        dislike_btn.click()
```

```python3
# autoswipes
def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
```

#### Close some windows and finish off the code

```python3
    def close_popup(self):
        popup_3 = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="cancel"]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element(By.XPATH, '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_slikepop(self):
        slikepop = self.driver.find_element (By.XPATH, '//*[@id="q1954245907"]/div/div/button[2]')
        slikepop.click()

bot = Tinderbot()
bot.login()
```
![image](https://github.com/ethanolivertroy/dating-app-automation/assets/63926014/508dc79c-18fa-4de1-b2a0-01f3b23edf1b)

### Bumble and Hinge

This whole process works pretty much the same with any dating app that has a web app. You just have to make a few adjustments.

If one selecting method doesn't work I just rotate to another.
- XPATH
- ID
- CSS_SELECTOR

```python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from secrets import username, password

class Bumblebot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login (self):
        self.driver.get('https://bumble.com')

        sleep(2)

        first_click = self.driver.find_element(By.XPATH, '')
        first_click.click()

        sleep (1)

        fb_btn = self.driver.find_element(By.XPATH, '')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element(By.XPATH, '')
        email_in.send_keys(username)

        pw_in = self.driver.find_element(By.XPATH, '')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element(By.ID, 'loginbutton')
        login_btn.click()

        self.driver.switch_to.window(base_window)


        popup_1 = self.driver.find_element(By.XPATH, '')
        popup_1.click()

        popup_2 = self.driver.find_element(By.XPATH, '')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-qa-icon-name="floating-action-yes"]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="gamepadDislike"]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element(By.XPATH, '')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element(By.XPATH, '')
        match_popup.click()

bot = Bumblebot()
bot.login()
```
