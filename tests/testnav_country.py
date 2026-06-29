from selenium import webdriver
from Internship_task.pages.nav_country import Nav_Country

class TestNav_Country:
    def test_specificcountry(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.SC=Nav_Country(self.driver)
        self.SC.click_country()
        self.SC.select_specificcountry("Canada")
        self.SC.select_masters()
        self.SC.select_scholarship("united-world")
        self.SC.select_faq()
