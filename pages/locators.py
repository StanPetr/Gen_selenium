from selenium.webdriver.common.by import By


class BaskettPageLocators:
    ORIGIN_BUY_BUTTON = (By.XPATH, "(//a[contains(text(), 'Добавить в корзину')])[1]")
    TOTAL_PRICE = (By.XPATH, "(//priceroller)[1]")
    PROMOCODE_LINK = (By.XPATH, "//div[contains(text(), 'У меня есть промокод')]")
    PROMOCODE_FIELD = (By.XPATH, "//input[@placeholder='Введите промокод']")
    PROMOCODE_ADD_BUTTON = (By.XPATH, "//i[@class='icon-arrow-right']")
