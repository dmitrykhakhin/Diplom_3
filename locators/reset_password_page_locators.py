from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    RESET_PASSWORD_HEADING = (By.XPATH, './/div[contains(@class, "Auth_login")]/h2')
    PASSWORD_FIELD_PLACEHOLDER = (By.XPATH, './/input[@type="password"]/parent::div/label')
    CODE_FIELD_PLACEHOLDER = (By.XPATH, './/input[@type="text"]/parent::div/label')
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, './/div[contains(@class, "input__icon-action")]')
    PASSWORD_INPUT_SECTION = (By.XPATH, './/label[text()="Пароль"]/parent::div')

