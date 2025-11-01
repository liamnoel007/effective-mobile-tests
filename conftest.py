import pytest
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def main_page(page):
    print("Fixture BEFORE")
    main = MainPage(page)
    main.open()
    return main
