from selenium.webdriver.common.by import By


class LocatorsOrderPageScooter:
    header_order_form_about_user = [By.XPATH, './/div[text() = "Для кого самокат"]']
    first_name_field = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[@placeholder = "* Имя"]')
    last_name_field = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[@placeholder = "* Фамилия"]')
    address_field = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Адрес")]')
    station_subway_field = (By.XPATH, './/input[@placeholder = "* Станция метро"]/ parent::div')
    phone_number_field = (By.XPATH, './/div[contains(@class, "Order_Form")]//input[contains(@placeholder, "Телефон")]')
    order_next_button = (By.XPATH, './/div[contains(@class, "NextButton")]/button[text() = "Далее"]')

    @staticmethod
    def choose_station_subway(station_subway):
        return By.XPATH, f'.//li[@class = "select-search__row"]//div[text() = "{station_subway}"]'

    date_field = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    rental_period_field = (By.CLASS_NAME, 'Dropdown-arrow')

    @staticmethod
    def choose_rental_period(period):
        return By.XPATH, f'.//div[contains(@class, "Order_Form")]//div[@class = "Dropdown-menu"]/div[text() = "{period}"]'

    @staticmethod
    def choose_color(color):
        return By.ID, f'{color}'

    order_button = (By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')
    yes_button = (By.XPATH, '//div[@class = "Order_Modal__YZ-d3"]//button[text() = "Да"]')
    order_success_message = (By.XPATH, './/div[(@class = "Order_ModalHeader__3FDaJ") and (contains(text(), "Заказ оформлен"))]')

