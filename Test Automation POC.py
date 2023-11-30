import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAppTestCase1(unittest.TestSuite):
    def setUp(self):
        # set up url then driver
        self.url = "https://linerider.com"
        self.driver = webdriver.Chrome()
        print("Chrome Driver Loaded -:" + self.url)

        # Wait for the search box to be visible
        self.wait = WebDriverWait(self.driver, 100)

    def test_start_game(self):
        try:
            # click play
            self.driver.get(self.url)

            # sleep 5 seconds for page load
            time.sleep(5)
            play_button = self.driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/div[2]/div[2]/button[2]/span[1]')
            assert play_button.is_displayed()
            print("Found play button element")

            # click play button
            play_button.click()
            print("Play button clicked")

            # Delay the program for a certain amount of time
            print("Delaying 100 seconds")
            time.sleep(100)  # Wait for 100 seconds

        except AssertionError as e:
            print("AssertionError:", e)

    #def test_draw_line(self):
        #try:
            # draw first line



unittest.main(verbosity=2)