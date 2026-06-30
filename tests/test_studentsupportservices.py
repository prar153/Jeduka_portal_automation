from selenium import webdriver

from Internship_task.pages.nav_studentsupportservices import Nav_StudentSupportservices


class TestStudentsupportservices:
    def test_studentsupportservices(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.NSS= Nav_StudentSupportservices(self.driver)
        self.NSS.hovernav_studentsupport()
        self.NSS.click_accomodation()
        self.driver.back()
        self.NSS.click_forex()
        self.NSS.click_universityliving()
        self.NSS.afterapply("Prarthana Manandhar","manandharprarthana@gmail.com","9876545696","Nepal","Bagmati","Kathmandu","Australia","New South Wales","Ballina","Other","Hi")