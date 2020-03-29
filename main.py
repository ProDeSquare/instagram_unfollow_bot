'''
# Hamza Mughal's automation script for instagram
================================================
# This bot logs in to instagram and unfollow everyone you follow
# To be used with web
# Tested on Arch Linux with Chromium web browser on 03-29-2020
# Coded while quarntined at home due to corona virus
# more at: https://prodesquare.com
'''

from selenium import webdriver
from time import sleep
from pathlib import Path
from dotenv import load_dotenv
from os import getenv as env


load_dotenv(verbose=True)


class InstagramUnfollowBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(env('LINK_TO_INSTAGRAM'))

        sleep(3)

        self.driver.find_element_by_name('username').send_keys(env('USERNAME'))
        self.driver.find_element_by_name('password').send_keys(env('PASSWORD'))
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        sleep(5)

        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()

    def getFollowings(self):
        self.driver.find_element_by_xpath(
            "//a[contains(@href, '/{}')]".format(env('USERNAME'))).click()

        sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()

        sleep(2)

        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1

        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, scroll_box)

        unfollow_buttons = scroll_box.find_elements_by_tag_name('button')
        for unfollow_button in unfollow_buttons:
            sleep(1)
            unfollow_button.click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Unfollow')]").click()


print("Instagram Unfollow bot by Hamza Mughal (https://prodesquare.com)")
my_bot = InstagramUnfollowBot(env('USERNAME'), env('PASSWORD'))
my_bot.getFollowings()
sleep(5)
