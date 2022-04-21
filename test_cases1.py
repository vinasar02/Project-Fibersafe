import time
import unittest
from selenium import webdriver
from pageObjects.LoginDashboard import LoginPage

class test_cases1(unittest.TestCase):
    exec_path = "C:\\Users\\User\\Documents\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"
    username = "PLTest0134"
    password = "Test1234"

    @classmethod
# pass in a service object driver & initialize webdriver
# open url and maximize window
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.exec_path)
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()
        time.sleep(3)

#call each function from the LoginPage class
    def test_cases(self):
        self.lp=LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(10)
        self.lp.clickcard()
        time.sleep(5)
        self.lp.selectbar()
        time.sleep(5)
        self.lp.scroll()
        time.sleep(5)
        self.lp.reportsource()
        time.sleep(5)
        self.lp.recentworklist()
        time.sleep(5)
        self.lp.Map()
        time.sleep(5)
        self.lp.searchaddress()
        time.sleep(5)
        self.lp.cabletype()
        time.sleep(5)
        self.lp.reports()
        time.sleep(5)
        self.lp.worklist()
        time.sleep(10)
        self.lp.selectfieldteammember()
        time.sleep(15)
        self.lp.management()
        time.sleep(5)
        self.lp.user()
        time.sleep(5)
        self.lp.searchuserrole()
        time.sleep(5)
        self.lp.profile()
        time.sleep(5)
        self.lp.logout()
        time.sleep(5)