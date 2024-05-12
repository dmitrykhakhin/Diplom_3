from selenium.webdriver.common.by import By


class ProfilePageLocators:
    INFORMATION_PARAGRAPH = (By.XPATH, ".//p[contains(@class, 'Account_text')]")
    ORDER_HISTORY_LINK = (By.XPATH, './/li[contains(@class, "Account_listItem")]/a[@href="/account/order-history"]')
    NUMBER_OF_LAST_ORDER = (By.XPATH, './/ul[contains(@class, "OrderHistory_profileList")]/li[last()]'
                                      '//div[contains(@class, "textBox")]/p[contains(@class, "type_digits")]')
    BURGER_NAME_IN_LAST_ORDER = (By.XPATH, './/ul[contains(@class, "OrderHistory_profileList")]/li[last()]//h2')
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')
