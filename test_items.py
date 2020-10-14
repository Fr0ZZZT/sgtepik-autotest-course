import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_should_have_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.is_displayed(), "The Cart Button is not present"
