import pytest
import allure


@allure.title('!!!!!!!!!!!!!!!!!')
def test_products_displayed_on_page(product_desk_page):
    product_desk_page.open_page()
    product_desk_page.products_displayed_on_page()


@allure.title('!!!!!!!!!!!!!!')
def test_search_existing_product(product_desk_page):
    product_name = 'Customizable Desk'
    product_desk_page.open_page()
    product_desk_page.search_product(product_name)
    product_desk_page.verify_products_count(1)
    product_desk_page.verify_product_in_results(product_name)


@allure.title('!!!!!!!!!!!!!!!!')
def test_search_nonexisten_product(product_desk_page):
    product_name = 'not exist'
    product_desk_page.open_page()
    product_desk_page.search_product(product_name)
    product_desk_page.verify_products_count(0)
    product_desk_page.check_product_not_exist(product_name)


@allure.title('!!!!!!!!!!!!!')
def test_filter_by_aluminium(product_desk_page):
    product_name = 'Customizable Desk'
    product_desk_page.open_page()
    product_desk_page.select_checkbox_filter_aluminium()
    product_desk_page.verify_products_count(1)
    product_desk_page.verify_product_in_results(product_name)










#
#
#
# переходим на старницу
# проверяем хлебные крошки
#
#
# 1) тест поиск существующего товара
#
#
# 2) тест поиск несуществующего твоара
#
#
# 3)тест фильтрации в мастер части