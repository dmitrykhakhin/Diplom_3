from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    RECOVERY_PASSWORD_HEADING = (By.XPATH, './/div[contains(@class, "Auth_login")]/h2')
    EMAIL_FIELD_PLACEHOLDER = (By.XPATH, './/input/parent::div/label')
    EMAIL_INPUT_FIELD = (By.XPATH, './/label[text()="Email"]/parent::div/input')
    RECOVERY_BUTTON = (By.XPATH, '.// button[text() = "Восстановить"]')
