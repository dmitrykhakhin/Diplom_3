from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_LINK = (By.XPATH, './/a[@href="/forgot-password"]')
    EMAIL_INPUT_FIELD = (By.XPATH, './/label[text()="Email"]/parent::div/input')
    PASSWORD_INPUT_FIELD = (By.XPATH, './/input[@type="password"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    LOGIN_PAGE_HEADING = (By.XPATH, './/div[contains(@class, "Auth_login")]/h2')
