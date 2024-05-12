from selenium.webdriver.common.by import By


class HeaderLocators:
    PROFILE_LINK_BUTTON = (By.XPATH, './/a[@href="/account"]')
    CONSTRUCTOR_LINK_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, './/a[@href="/feed"]')
