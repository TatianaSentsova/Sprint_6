from selenium.webdriver.common.by import By


class LocatorsOrderPageScooter:
    # Заголовок в форме заказа с личными данными пользователя
    HEADER_ORDER_FORM_ABOUT_USER = (By.XPATH, './/div[text() = "Для кого самокат"]')
    # Логотип Самоката
    SCOOTER_LOGO = (By.XPATH, './/*[contains(@class, "Header_LogoScooter")]')
    # Поле "Имя"
    FIRST_NAME_FIELD = (By.XPATH, './/input[@placeholder = "* Имя"]')
    # Поле "Фамилия"
    LAST_NAME_FIELD = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
    # Поле "Адрес"
    ADDRESS_FIELD = (By.XPATH, './/input[contains(@placeholder, "Адрес")]')
    # Поле "Станция метро"
    STATION_SUBWAY_FIELD = (By.XPATH, './/input[@placeholder = "* Станция метро"]/ parent::div')
    # Поле "Телефон"
    PHONE_NUMBER_FIELD = (By.XPATH, './/input[contains(@placeholder, "Телефон")]')
    # Кнопка "Далее"
    ORDER_NEXT_BUTTON = (By.XPATH, './/div[contains(@class, "NextButton")]/button[text() = "Далее"]')
    # Поле "Дата"
    DATE_FIELD = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    # Дропдаун поля "Срок аренды"
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-arrow')
    # Кнопка "Заказать"
    ORDER_BUTTON = (By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')
    # Кнопка подтверждения заказа
    CONFIRM_BUTTON = (By.XPATH, '//div[@class = "Order_Modal__YZ-d3"]//button[text() = "Да"]')
    # Сообщение о созданном заказе
    ORDER_SUCCESS_MESSAGE = (By.XPATH, './/div[(@class = "Order_ModalHeader__3FDaJ") and (contains(text(), "Заказ оформлен"))]')

    # Метод, возвращающий локатор станции метро
    @staticmethod
    def choose_station_subway(station_subway):
        return By.XPATH, f'.//li[@class = "select-search__row"]//div[text() = "{station_subway}"]'

    # Метод, возвращающий локатор периода аренды самоката
    @staticmethod
    def choose_rental_period(period):
        return By.XPATH, f'.//div[contains(@class, "Order_Form")]//div[@class = "Dropdown-menu"]/div[text() = "{period}"]'

    # Метод,возвращающий локатор цвета самоката
    @staticmethod
    def choose_color(color):
        return By.ID, f'{color}'
