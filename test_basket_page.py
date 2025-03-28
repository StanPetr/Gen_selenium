from .pages.basket1_page import BaskettPage


def test_guest_can_use_promocode(browser):
    link = "https://basket.genotek.ru/"
    promocode = "genotek5"
    page = BaskettPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.guest_can_add_promo_code(promocode)
