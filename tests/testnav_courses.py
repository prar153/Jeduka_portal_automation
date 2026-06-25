from selenium import webdriver
from Internship_task.pages.nav_country import Nav_Country
from Internship_task.pages.nav_courses import Nav_Courses


class TestNav_Courses:
    def test_specificcourses(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.jeduka.com/")
        self.driver.maximize_window()
        self.SCC=Nav_Courses(self.driver)
        self.SCC.hover_course()
        self.SCC.select_course('Paramedical/Nursing Studies Colleges')
        self.SCC.view_courses("university-of-washington")

