from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_FEED_HEADING = (By.XPATH, './/div[contains(@class, "OrderFeed")]/h1')
    FIRST_ORDER_IN_ORDER_FEED_LIST = (By.XPATH, './/ul[contains(@class, "OrderFeed_list")]'
                                                '/li[contains(@class, "listItem")][1]')
    ORDER_DETAILS_WINDOW = (By.XPATH, './/div[contains(@class, "Modal_orderBox")]/ancestor::section')
    COMPLETED_FOR_ALL_TIME_COUNTER = (By.XPATH, './/p[text()="Выполнено за все время:"]'
                                                '/parent::div/p[contains(@class, "OrderFeed_number")]')
    COMPLETED_TODAY_COUNTER = (By.XPATH, './/p[text()="Выполнено за сегодня:"]'
                                         '/parent::div/p[contains(@class, "OrderFeed_number")]')
    ORDER_NUMBER_IN_ORDER_FEED = (By.XPATH, './/li//div[contains(@class, "textBox")]/p[text()="{}"]')
    ORDER_NUMBER_IN_WORK = (By.XPATH, './/ul[contains(@class, "orderListReady")]/li[text()="{}"]')
