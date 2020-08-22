from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import os
import pyautogui
import time
import random

user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
ROOT_DIR = "c:\\Users\\Rajdeep\\Desktop\\Projects\\Instagram Meme Page Automation BOT\\memes\\"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)
driver.set_window_size(360, 640)


class Insta:
    user = ""
    passw = ""

    def __init__(self, username, password):
        self.user = username
        self.passw = password

    def Login(self):
        driver.get(
            "https://www.instagram.com/accounts/login/?source=auth_switcher")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
        finally:
            driver.find_element_by_name("username").send_keys(self.user)
            driver.find_element_by_name("password").send_keys(self.passw)
            driver.execute_script(
                'document.getElementsByClassName("sqdOP  L3NKy   y3zKF")[1].removeAttribute("disabled");')
            driver.find_elements_by_xpath(
                "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button")[0].click()

            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[contains(text(), 'Not Now')]")))

            NotNowButton = driver.find_elements_by_xpath(
                "//*[contains(text(), 'Not Now')]")
            if len(NotNowButton) > 0:
                NotNowButton[0].click()

    def post(self, PostInfo):

        filename = ROOT_DIR + PostInfo['Title']+getExtention(PostInfo['Url'])

        if os.path.exists(filename):
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '[aria-label="New Post"]'))
                )

            finally:

                driver.find_elements_by_css_selector(
                    '[aria-label="New Post"]')[0].click()

                try:
                    ImageLoad = driver.find_element_by_css_selector(
                        "input[type='file']")
                    ImageLoad.send_keys(filename)
                    pyautogui.press('esc')
                except:
                    return

                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//*[contains(text(), 'Next')]"))
                    )
                finally:

                    Expand = driver.find_elements_by_xpath(
                        "//*[contains(text(), 'Expand')]")

                    if len(Expand) > 0:
                        Expand[0].click()

                    driver.find_elements_by_xpath(
                        "//*[contains(text(), 'Next')]")[0].click()

                    try:
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located(
                                (By.CLASS_NAME, "UP43G"))
                        )

                    finally:
                       # time.sleep(1)
                        caption = driver.find_element_by_tag_name('textarea')
                      #  time.sleep(2)
                        caption.send_keys(PostInfo['Title'])
                        pyautogui.press('enter')
                        caption.send_keys("Credits : "+PostInfo['PostLink'])

                        button = driver.find_elements_by_class_name(
                            "UP43G")
                        button[0].click()
                        time.sleep(3)

    def exi(self):
        driver.quit()


def getExtention(PostLink):
    return "."+PostLink.split(".")[-1]
