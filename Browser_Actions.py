from Product_Profile import productPro
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

class runInBrowser:
    from Get_Info import getDetails

    chrome_options = Options()
    chrome_options.add_argument("--headless")


    def __init__ (self):
        self.start_time = None
        self.browser = webdriver.Chrome(executable_path='/Users/jonathan/downloads/chromedriver') #chrome_options = self.chrome_options
        self.pTypeElem = None
        self.pNameElem = None
        self.pSizeElem = None
        self.addElem = None
        self.pTypeHref = None
        self.pNameHref= None
        self.pSizeHref = None
        self.hRef = 'href'
        self.pType = None
        self.pName = None
        self.pSize = None
        self.getDetails()

    def goToType(self):

         self.pTypeElem = self.browser.find_element_by_partial_link_text(self.pType)

         self.pTypeHref = self.pTypeElem.get_attribute('href')

         self.browser.get(self.pTypeHref)

    def goToName(self):

        self.pNameElem = self.browser.find_element_by_link_text(self.pName)

        self.pNameHref = self.pNameElem.get_attribute('href')

        self.browser.get(self.pNameHref)

    def selectSize(self):
        self.pSizeElem = Select(self.browser.find_element_by_id('s'))
        self.pSizeElem.select_by_visible_text(self.pSize)

    def addToCart(self):

        self.addElem = self.browser.find_element_by_name('commit')

        self.addElem.click()

    def goToCheckOut(self):

        self.browser.find_element_by_css_selector('a.button.checkout').click()

    def getItem(self):
        self.start_time = time.time()
        self.browser.get('https://www.supremenewyork.com/shop/all/pants')
        #self.goToType()
        self.goToName()
        self.selectSize()
        self.addToCart()
        self.goToCheckOut()
        print(" %s seconds" % (time.time() - self.start_time))








