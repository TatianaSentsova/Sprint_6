from selenium.webdriver.common.by import By


class LocatorsOrderPageScooter:
    HEADER_ORDER_FORM_ABOUT_USER = (By.XPATH, './/div[text() = "Для кого самокат"]')
    SCOOTER_LOGO = (By.XPATH, '//*[contains(@class, "Header_LogoScooter")]')
    FIRST_NAME_FIELD = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[@placeholder = "* Имя"]')
    LAST_NAME_FIELD = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[@placeholder = "* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Адрес")]')
    STATION_SUBWAY_FIELD = (By.XPATH, './/input[@placeholder = "* Станция метро"]/ parent::div')
    PHONE_NUMBER_FIELD = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Телефон")]')
    ORDER_NEXT_BUTTON = (By.XPATH, './/div[contains(@class, "NextButton")]/button[text() = "Далее"]')
    DATE_FIELD = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-arrow')
    ORDER_BUTTON = (By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')
    YES_BUTTON = (By.XPATH, '//div[@class = "Order_Modal__YZ-d3"]//button[text() = "Да"]')
    ORDER_SUCCESS_MESSAGE = (By.XPATH, './/div[(@class = "Order_ModalHeader__3FDaJ") and (contains(text(), "Заказ оформлен"))]')

    @staticmethod
    def choose_station_subway(station_subway):
        return By.XPATH, f'.//li[@class = "select-search__row"]//div[text() = "{station_subway}"]'

    @staticmethod
    def choose_rental_period(period):
        return By.XPATH, f'.//div[contains(@class, "Order_Form")]//div[@class = "Dropdown-menu"]/div[text() = "{period}"]'

    @staticmethod
    def choose_color(color):
        return By.ID, f'{color}'
