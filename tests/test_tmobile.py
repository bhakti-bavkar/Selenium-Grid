import pytest
from selenium.webdriver.support import expected_conditions as EC
from tests.BaseTest import BaseTest
from Pages.HomePage import HomePage


class TestTMOHome(BaseTest):
    @pytest.fixture()# can use autouse=True
    def home(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.wait_for_page(EC.title_contains, 'T-Mobile', 25)
        return home_page

    def test_tmo_home_page(self, home):
        home_elements = home.elements
        assert 'Cell Phones | 4G Phones | iPhone and Android Phones | T-Mobile' \
               in home.get_page_title

        logo = home.check_element_visible(self.driver, *home_elements['logo'])
        assert logo is not False
        home_link = home.check_element_visible(logo, *home_elements['link_logo'])
        assert 'www.t-mobile.com' in home_link.get_attribute('href')

        home_links = home_elements['link_menu']
        nav_links = home.get_element(home_links['parent'])
        assert nav_links is not False

        deals = home.check_element_visible(nav_links, home_links['deals'])
        assert deals is not False
        assert deals.text == 'DEALS'
        assert 'www.t-mobile.com/offers/deals-hub' in deals.get_attribute('href')

        phones = home.check_element_visible(nav_links, home_links['phones'])
        assert phones is not False
        assert phones.text == 'PHONES'
        assert 'www.t-mobile.com/cell-phones' in phones.get_attribute('href')

        plans = home.check_element_visible(nav_links, home_links['plans'])
        assert plans is not False
        assert plans.text == 'PLANS'
        assert 'www.t-mobile.com/cell-phone-plans' in plans.get_attribute('href')

        my_tmo = home.check_element_visible(nav_links, home_links['my_tmo'])
        assert my_tmo is not False
        assert my_tmo.text == 'MY T-MOBILE'
        assert 'my.t-mobile.com' in my_tmo.get_attribute('href')

        menu = home.check_element_visible(None, home_elements['side_menu'])
        assert menu is not False
        assert 'MENU' in menu.text

    def test_tmo_menu_selected(self, home):
        menu_bar = home.menu.elements
        # click Menu
        home.click_side_menu()
        menu_overlay = home.menu.check_element_visible(self.driver, menu_bar['menu_overlay'])
        assert menu_overlay is not False
        assert 'visibility: visible' in menu_overlay.get_attribute('style')

        assert home.menu.page_elements_present(menu_bar) is not False

        # Check that Home Page freezes and nothing gets clicked except in Menu Bar
        assert home.check_element_visible(self.driver, home.elements['freeze_screen'])

    def test_tmo_menu_unselected(self, home):
        menu_bar = home.menu.elements
        # click Menu
        home.click_side_menu()
        # unselect Menu
        home.unfreeze_home_screen()
        menu_overlay = home.menu.check_element_visible(self.driver, menu_bar['menu_overlay'])
        assert menu_overlay is False
        assert 'visibility: hidden' in menu_overlay.get_attribute('style')




# @pytest.fixture()
# def my_fixture(request):
#     print('\n-----------------')
#     print('fixturename : %s' % request.fixturename)
#     print('scope       : %s' % request.scope)
#     print('function    : %s' % request.function.__name__)
#     print('cls         : %s' % request.cls)
#     print('module      : %s' % request.module.__name__)
#     print('fspath      : %s' % request.fspath)
#     print('-----------------')
#
#     if request.cls is not None:
#         request.cls.name = request.function.__name__
#     if request.function.__name__ == 'test_three':
#         request.applymarker(pytest.mark.xfail)
#
#
# def test_one(my_fixture):
#     print('test_one():')
#
#
# class TestClass():
#     def test_two(self, my_fixture):
#         print('test_two()')
#         print(self.name)
#
#
# def test_three(my_fixture):
#     print('test_three()')
#     assert False