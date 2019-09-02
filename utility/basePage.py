# from utility.get_driver import driver
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self,browser):
        self.driver=browser
    def transfer_method(self,method):
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        if method:
            if method==ID or method==ID.upper():
                mehtod=By.ID
            elif method==XPATH or method==XPATH.upper():
                mehtod=By.XPATH
            elif method==LINK_TEXT or method==LINK_TEXT.upper():
                mehtod=By.LINK_TEXT
            elif method==PARTIAL_LINK_TEXT or method==PARTIAL_LINK_TEXT.upper():
                mehtod=By.PARTIAL_LINK_TEXT
            elif method==NAME or method==NAME.upper():
                method=By.NAME
            elif method==TAG_NAME or method==TAG_NAME.upper():
                method=By.TAG_NAME
            elif method==CLASS_NAME or method==CLASS_NAME.upper():
                method=By.CLASS_NAME
            elif method=='css' or method=='CSS' or method==CSS_SELECTOR or method==CSS_SELECTOR.upper():
                method=By.CSS_SELECTOR
        return method


