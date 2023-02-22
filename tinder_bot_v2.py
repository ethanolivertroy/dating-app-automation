from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from secrets import username, password

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        login_btn = self.driver.find_element(By.XPATH, '//span[contains(text(),"Log in")]')
        login_btn.click()

        sleep(1)

        fb_btn = self.driver.find_element(By.XPATH, '//button[@aria-label="Log in with Facebook"]')
        fb_btn.click()

        # switch to login popup
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element(By.NAME, 'email')
        email_in.send_keys(username)

        pw_in = self.driver.find_element(By.NAME, 'pass')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element(By.NAME, 'login')
        login_btn.click()

        # switch back to main window
        self.driver.switch_to.window(self.driver.window_handles[0])

        sleep(2)

        popup_1 = self.driver.find_element(By.XPATH, '//button[text()="Allow"]')
        popup_1.click()

        popup_2 = self.driver.find_element(By.XPATH, '//button[text()="Enable"]')
        popup_2.click()

    def like(self):
        try:
            like_btn = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Like"]')
            like_btn.click()
        except:
            print('Could not like')

    def dislike(self):
        try:
            dislike_btn = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Nope"]')
            dislike_btn.click()
        except:
            print('Could not dislike')

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except:
                try:
                    self.close_popup()
                except:
                    try:
                        self.close_match()
                    except:
                        print('No more matches, exiting...')
                        return

    def close_popup(self):
        try:
            popup_3 = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Close"]')
            popup_3.click()
        except:
            pass

    def close_match(self):
        try:
            match_popup = self.driver.find_element(By.XPATH, '//a[text()="Keep Swiping"]')
            match_popup.click()
        except:
            pass

bot = Tinderbot()
bot.login()
bot.auto_swipe()
