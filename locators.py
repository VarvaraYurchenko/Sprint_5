from selenium.webdriver.common.by import By


class Locators:
    # Форма регистрации
    NAME = (By.NAME, "name") # поле ввода Имя
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле ввода Имейл
    PASSWORD = (By.NAME, "Пароль") # поле ввода Пароль
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']") # сообщение о вводе некорректного пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка Зарегистрироваться в форме регистрации
    SIGN_BUTTON = (By.LINK_TEXT, "Войти") # кнопка Войти в форме регистрации

    # Форма авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка Войти в форме авторизации
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться") # кнопка Зарегистрироваться в форме авторизации
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']") # кнопка Восстановить пароль

    # Главная страница
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт на главной странице
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # логотип Stellar Burgers

    # Личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный кабинет
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка Выход из профиля в личном кабинете

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']") # вкладка Конструктор
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # заголовок Соберите бургер
    BUNS_SECTION = (By.XPATH, '//h2[text()="Булки"]//following-sibling::ul') # секция Булки
    SAUCES_SECTION = (By.XPATH, '//h2[text()="Соусы"]//following-sibling::ul')  # секция Соусы
    FILLINGS_SECTION = (By.XPATH, '//h2[text()="Начинки"]//following-sibling::ul') # секция Начинки
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # активная вкладка выбора
