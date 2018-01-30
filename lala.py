# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ytfty(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "wykop.pl"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ytfty(self):
        driver = self.driver
        driver.get("https://www.euro.com.pl/monitory-led-i-lcd.bhtml?link=mainnavi")
        driver.find_element_by_xpath("//div[@id='filter-sort']/div[9]/div").click()
        driver.find_element_by_xpath("//div[@id='filter-sort']/div[9]/div[2]/div/div[7]").click()
        driver.find_element_by_id("filter-price-from").click()
        driver.find_element_by_id("filter-price-from").clear()
        driver.find_element_by_id("filter-price-from").send_keys("1000")
        driver.find_element_by_id("filter-price-to").click()
        driver.find_element_by_id("filter-price-to").clear()
        driver.find_element_by_id("filter-price-to").send_keys("2000")
        driver.find_element_by_xpath("//label[@id='label-filter-instalment-3']/i").click()
        driver.find_element_by_xpath("//label[@id='label-filter-brand-2']/i").click()
        driver.find_element_by_xpath("//label[@id='label-filter-availability-0']/i").click()
        driver.find_element_by_xpath("//div[@id='filter-box']/div[9]/div").click()
        driver.find_element_by_xpath("//label[@id='label-filter-h-3']/i").click()
        driver.find_element_by_xpath("//div[@id='filter-box']/div[11]/div").click()
        driver.find_element_by_xpath("//label[@id='label-filter-i-2']/i").click()
        driver.find_element_by_xpath("//div[@id='filter-box']/div[12]/div").click()
        driver.find_element_by_xpath("//label[@id='label-filter-k-1']/i").click()
        driver.find_element_by_xpath("//div[@id='filter-box']/div[15]").click()
        driver.find_element_by_xpath("//div[@id='filter-box']/div[15]/div").click()
        driver.find_element_by_xpath("//label[@id='label-filter-m-0']/i").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
