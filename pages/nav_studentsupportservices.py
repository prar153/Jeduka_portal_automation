from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Nav_StudentSupportservices:
    studentsupport_xpath="//a[normalize-space()='Student Support Services']"
    accom_xpath="//a[normalize-space()='Accommodation']"
    roomessens_xpath="//a[normalize-space()='Room Essentials']"
    rem_xpath="//a[normalize-space()='Remittance']"
    internationalsim_xpath="//a[normalize-space()='International SIM']"
    forex_xpath="//a[normalize-space()='Forex']"
    educationloan_xpath="//a[normalize-space()='Education Loan']"
    airporttransfer_xpath="//a[normalize-space()='Airport Transfer']"
    travelinsurance_xpath="//a[normalize-space()='Travel Insurance']"
    flight_offer_xpath="//a[normalize-space()='Flight Offers']"
    guarantor_xpath="//a[normalize-space()='Guarantor']"
    universityliving_xpath="//a[normalize-space()='University Living']"
    amberstudent_xpath="//a[normalize-space()='Amber Student']"
    ethiad_xpath="//a[normalize-space()='ETIHAD']"

    # applyxpath
    fullname_xpath = "//input[@id='vName']"
    email_xpath = "//input[@id='vEmail']"
    mobile_xpath = "//input[@id='vMobile']"
    country_xpath = "//select[@id='vCountry']"
    state_xpath = "//select[@id='vState']"
    city_xpath = "//select[@id='vCity']"
    preferred_country_xpath = "//select[@id='iCountryId']"
    preferred_state_xpath = "//select[@id='iStateId']"
    preferred_city_xpath = "//select[@id='iCityId']"
    preferred_university_xpath="//select[@id='iSchoolId']"
    remarks_xpath="//textarea[@id='vComment']"
    submittbtn_xpath = "//button[@title='Submit To Get Call Back']"
    homepage_xpath = "//a[@id='Continuetohomepage']"

    def __init__(self,driver):
        self.driver = driver

    def hovernav_studentsupport(self):
        c = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.studentsupport_xpath)))
        act = ActionChains(self.driver)
        act.move_to_element(c).click().perform()

    def click_accomodation(self):
        acc=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.accom_xpath)))
        acc.click()

    def click_roomessentials(self):
        room=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.roomessens_xpath)))
        room.click()

    def click_remittance(self):
        rem=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.rem_xpath)))
        rem.click()

    def click_internationalsim(self):
        isim=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.internationalsim_xpath)))
        isim.click()

    def click_forex(self):
        fore=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.forex_xpath)))
        fore.click()

    def click_educationloan(self):
        el=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.educationloan_xpath)))
        el.click()

    def click_airporttransfer(self):
        at=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.airporttransfer_xpath)))
        at.click()

    def click_travelinsurance(self):
        ti=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.travelinsurance_xpath)))
        ti.click()

    def click_flightoffers(self):
        fo=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.flight_offer_xpath)))
        fo.click()

    def click_guarantor(self):
        gr=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.guarantor_xpath)))
        gr.click()

    def click_universityliving(self):
        ul=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.universityliving_xpath)))
        ul.click()

    def click_amberstudent(self):
        ast=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.amberstudent_xpath)))
        ast.click()

    def click_ethiad(self):
        et=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.ethiad_xpath)))
        et.click()

    def afterapply(self, fname, email, mobile, ccountry, cstate, ccity, pcountry, pstate, pcity,puni,remarks):
        full = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fullname_xpath)))
        full.send_keys(fname)

        e = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_xpath)))
        e.send_keys(email)

        m = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mobile_xpath)))
        m.send_keys(mobile)

        cc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.country_xpath)))
        Select(cc).select_by_visible_text(ccountry)

        cs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.state_xpath)))
        Select(cs).select_by_visible_text(cstate)

        cct = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_xpath)))
        Select(cct).select_by_visible_text(ccity)

        pc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.preferred_country_xpath)))
        Select(pc).select_by_visible_text(pcountry)

        pco = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.preferred_state_xpath)))
        Select(pco).select_by_visible_text(pstate)

        css = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.preferred_city_xpath)))
        Select(css).select_by_visible_text(pcity)

        uss=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.preferred_university_xpath)))
        Select(uss).select_by_visible_text(puni)

        re=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.remarks_xpath)))
        re.send_keys(remarks)

        sbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submittbtn_xpath)))
        sbtn.click()

        hpbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.homepage_xpath)))
        hpbtn.click()