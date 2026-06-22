from selenium import webdriver

from Internship_task.pages.select_Page import SelectPage


class TestSelectPage:
    def testselectpage(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.SC=SelectPage(self.driver)
        self.SC.select_country("Australia")
        self.SC.select_course("Law")
        self.SC.select_coursetype("Corporate Law")
        self.SC.clickSearchbtn()
