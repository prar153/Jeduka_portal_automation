from selenium import webdriver

from Internship_task.pages.nav_exam import Nav_exam


class TestNavExam:
    def testnavexam(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.NV=Nav_exam(self.driver)
        self.NV.hovernav_exam()
        self.NV.click_about("TOEFL")
        # self.NV.click_syllabus("Duolingo")
        # self.NV.click_exampattern("Duolingo")
        # self.NV.click_preparations("Duolingo")
        # self.NV.click_registrations("Duolingo")
        self.NV.click_ineligibility()
        self.NV.click_insyllabus()
        self.NV.click_inexampattern()
        self.NV.click_inpreparation()
        self.NV.click_inexamfees()
        self.NV.click_inexamdates()
        self.NV.click_inregister()
        self.NV.click_inscore()
        # self.NV.click_readingsection("TOEFL")
        # self.NV.click_writingsection("TOEFL")
        # self.NV.click_listeningsection("TOEFL")
        # self.NV.click_speakingsection("TOEFL")
        # self.NV.click_dos("TOEFL")
        # self.NV.click_mistakes("TOEFL")
        # self.NV.click_tips("toefl")