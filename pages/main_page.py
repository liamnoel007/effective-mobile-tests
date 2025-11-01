from playwright.sync_api import Page, expect
import allure


class MainPage:

    BASE_URL = "https://effective-mobile.ru/"

    def __init__(self, page: Page):
        self.page = page

        self.about_link = page.locator(".tn-atom").get_by_text("[ О нас ]")
        self.moreinfo_link = page.locator(".tn-atom").get_by_text("[ Услуги ]")
        self.cases_link = page.locator(".tn-atom").get_by_text("[ Проекты ]")
        self.reviews_link = page.locator(".tn-atom").get_by_text("[ Отзывы ]")
        self.contacts_link = page.locator(".tn-atom").get_by_text("[ Контакты ]")

        self.about_title = page.locator('[field="tn_text_1680508197707"]')
        self.more_info_title = page.locator('[field="tn_text_1680510339488"]')
        self.cases_title = page.locator('[field="tn_text_1680611816671"]')
        self.reviews_title = page.locator("strong").get_by_text("ОТЗЫВЫ КЛИЕНТОВ")
        self.contacts_title = page.locator('[field="tn_text_1680516225306"]')

    def open(self):
        with allure.step("Открываем главную страницу"):
            self.page.goto(self.BASE_URL)

    def go_to_about(self):
        with allure.step("Переходим в раздел О нас"):
            self.about_link.click()

    def go_to_more_info(self):
        with allure.step("Переходим в раздел Услуги"):
            self.moreinfo_link.click()

    def go_to_cases(self):
        with allure.step("Переходим в раздел Проекты"):
            self.cases_link.click()

    def go_to_reviews(self):
        with allure.step("Переходим в раздел Отзывы"):
            self.reviews_link.click()

    def go_to_contacts(self):
        with allure.step("Переходим в раздел Контакты"):
            self.contacts_link.click()

    def check_about(self):
        with allure.step("Проверяем раздел О нас"):
            expect(self.page).to_have_url("https://effective-mobile.ru/#about")
            expect(self.about_title).to_be_visible()
            expect(self.about_title).to_have_text("о нас")

    def check_more_info(self):
        with allure.step("Проверяем раздел Услуги"):
            expect(self.page).to_have_url("https://effective-mobile.ru/#moreinfo")
            expect(self.more_info_title).to_be_visible()
            expect(self.more_info_title).to_have_text("услуги")

    def check_cases(self):
        with allure.step("Проверяем раздел Проекты"):
            expect(self.page).to_have_url("https://effective-mobile.ru/#cases")
            expect(self.cases_title).to_be_visible()
            expect(self.cases_title).to_have_text("проекты")

    def check_reviews(self):
        with allure.step("Проверяем раздел Отзывы"):
            expect(self.page).to_have_url("https://effective-mobile.ru/#reviews")
            expect(self.reviews_title).to_be_visible()
            expect(self.reviews_title).to_have_text("ОТЗЫВЫ КЛИЕНТОВ")

    def check_contacts(self):
        with allure.step("Проверяем раздел Контакты"):
            expect(self.page).to_have_url("https://effective-mobile.ru/#contacts")
            expect(self.contacts_title).to_be_visible()
            expect(self.contacts_title).to_have_text("контакты")
