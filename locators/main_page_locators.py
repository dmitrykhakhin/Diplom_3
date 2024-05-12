from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    CONSTRUCTOR_HEADING = (By.XPATH, './/section[contains(@class, "BurgerIngredients")]/h1')
    FLUORESCENT_BUN = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]'
                                 '/parent::a[contains(@class, "BurgerIngredient")]')
    INGREDIENT_DETAILS_WINDOW = (By.XPATH, './/h2[text()="Детали ингредиента"]/ancestor::section')
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, './/h2[text()="Детали ингредиента"]/ancestor::section'
                                                 '//button[contains(@class, "close")]')
    ORDER_BASKET = (By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]')
    CREATE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    TEXT_FROM_CREATED_ORDER_INFO_MODAL_WINDOW = (By.XPATH, './/section[contains(@class, "modal_opened")]'
                                                           '//div[contains(@class, "text")]/p[1]')
    ORDER_WINDOW_CLOSE_BUTTON = (By.XPATH, './/p[text()="идентификатор заказа"]'
                                           '/ancestor::div[contains(@class, "modal__container")]'
                                           '/button[contains(@class, "close")]')
    ORDER_NUMBER_IN_ORDER_WINDOW = (By.XPATH, './/p[text()="идентификатор заказа"]'
                                              '/ancestor::div[contains(@class, "contentBox")]/h2')
    INGREDIENT_SECTION = (By.XPATH, './/section[contains(@class, "BurgerIngredients_ingredients")]'
                                    '//span[text()="{}"]/parent::div')
    INGREDIENT_IN_CONSTRUCTOR = (By.XPATH, './/p[text()="{}"]/parent::a[contains(@class, "BurgerIngredient")]')

    INGREDIENT_COUNTER = (By.XPATH, './/p[text()="{}"]/parent::a[contains(@class, "BurgerIngredient")]'
                                    '//p[contains(@class, "counter")]')
