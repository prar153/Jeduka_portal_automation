from selenium import webdriver

from Internship_task.pages.home_Page import SelectPage


class TestSelectPage:
    def testselectpage(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.SC=SelectPage(self.driver)
        # self.SC.select_country("Australia","Law","Corporate Law")
        # self.driver.back()
        # self.SC.select_whyjeduka()

    # study abroad section
    #     self.SC.click_decidecountry()
    #     self.driver.back()
    #     self.SC.click_apply()
    #     self.driver.back()
    #     self.SC.click_preparedocuments()
    #     self.driver.back()
    #     self.SC.click_selectcourses()
    #     self.driver.back()
    #     self.SC.click_decidecountrynotselectedfirst()

    # browse countries in homepage
    #     self.SC.click_browsebycountries("France")

    # browse course in homepage
    #     self.SC.click_browsebycourse("Engineering")

    # study abroad exams section
        # self.SC.click_studyabroadexams("sat")
        # self.SC.click_about("Duolingo")
        #
        # self.SC.click_adminandassistance("Visa")

        self.SC.registernow("Prarthana Manandhar","98674532145","manandharprarthana@gmail.com","Nepal","Bagmati","Kathmandu","January to July (Spring Intake)","Australia","MBA","General Management","Bachelor Degree – 4th Year","6","TOEFL","8")

        # self.SC.click_viewallarticles("germany","everything-you-need-to-know-about-aps-certificate-for-germany")

# reachouttous section
#         self.SC.reach_tous("Prarthana Manandhar","98674532145","manandharprarthana@gmail.com","Nepal","Bagmati","Kathmandu")



