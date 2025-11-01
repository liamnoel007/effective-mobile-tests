import allure


@allure.feature("Главная стараница")
@allure.title("О нас — проверка URL и заголовка")
@allure.story("Раздел О нас")
def test_about(main_page):
    main_page.go_to_about()
    main_page.check_about()


@allure.title("Услуги — проверка URL и заголовка")
@allure.story("Раздел Услуги")
def test_more_info(main_page):
    main_page.go_to_more_info()
    main_page.check_more_info()


@allure.title("Проекты — проверка URL")
@allure.story("Раздел Проекты")
def test_cases(main_page):
    main_page.go_to_cases()
    main_page.check_cases()


@allure.title("Отзывы — проверка URL и заголовка")
@allure.story("Раздел Отзывы")
def test_reviews(main_page):
    main_page.go_to_reviews()
    main_page.check_reviews()


@allure.title("Контакты — проверка URL и заголовка")
@allure.story("Раздел Контакты")
def test_contacts(main_page):
    main_page.go_to_contacts()
    main_page.check_contacts()
