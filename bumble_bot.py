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
