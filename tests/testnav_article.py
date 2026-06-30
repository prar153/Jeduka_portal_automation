from selenium import webdriver

from Internship_task.pages.nav_article import Nav_Article


class TestNav_article:
    def testnavarticle(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.NV=Nav_Article(self.driver)
        self.NV.hovernav_article()
        # self.NV.click_topreasons("USA")
        # self.NV.click_usatophundred()
        # self.NV.click_canadatoptwenty()
        # self.NV.click_toprank("France")
        # self.NV.click_stayback("Germany")
        # self.NV.click_howtoapplycanadaandswitzerland("Switzerland")
        # self.NV.click_howtoapply("UK")
        # self.NV.click_staybackusacanadaandfrance("France")
        self.NV.click_staybackctry("Netherlands")
        # self.NV.afterapply("Prarthana Manandhar","manandharprarthana@gmail.com","9876545696","Nepal","Bagmati","Kathmandu","Australia","Information Technology (IT)","IT")

