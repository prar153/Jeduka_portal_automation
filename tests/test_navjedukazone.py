from selenium import webdriver

from Internship_task.pages.nav_jedukazone import Nav_Jedukazone


class TestNav_jedukazone:
    def test_navjedukazone(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.NJZ = Nav_Jedukazone(self.driver)
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_loaneduaction("USA")
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_tips("Medical")
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_LOR("Masters")
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_events()
        self.driver.back()
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_cv()
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_studentvisa()
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_about()
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_askaques()
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_chat()
        self.NJZ.hovernav_jedukazone()
        self.NJZ.click_contactus()
        self.NJZ.afterapply("Prarthana Manandhar","manandharprarthana@gmail.com","9876545696","Nepal","Bagmati","Kathmandu","Australia","Information Technology (IT)","IT")
        self.NJZ.contactus("Prarthana Manandhar","manandharprarthana@gmail.com","9876545696","Nepal","Bagmati","Kathmandu","Australia","Information Technology (IT)","IT")