from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from secrets import username, password

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login (self):
        self.driver.get('https://tinder.com')

        sleep(2)

        first_click = self.driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
        first_click.click()

        sleep (1)

        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element(By.ID, 'loginbutton')
        login_btn.click()

        self.driver.switch_to.window(base_window)


        popup_1 = self.driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="gamepadLike"]')
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
