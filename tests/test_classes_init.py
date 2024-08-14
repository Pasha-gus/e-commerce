import pytest

from src.category_class import Category
from src.product_class import Product


def test_new_product():
    product_data = {
        "name": "Тестовый продукт",
        "description": "Описание тестового продукта",
        "price": 99.99,
        "quantity": 5,
    }
    product = Product.new_product(product_data)

    assert product.name == "Тестовый продукт"
    assert product.description == "Описание тестового продукта"
    assert product.price == 99.99
    assert product.quantity == 5


def test_set_price_valid():
    product = Product("Тест", "Описание теста", 50.0, 10)
    product.price = 75.0
    assert product.price == 75.0


def test_set_price_invalid():
    product = Product("Тест", "Описание теста", 50.0, 10)

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = -10  # Изменено с set_price() на price

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = 0  # Изменено с set_price() на price


def test_get_price():
    product = Product("Тест", "Описание теста", 50.0, 10)
    assert product.price == 50.0  # Изменено с get_price() на price


# Тесты класса Category
def test_initial_category_count(setup_category):
    """Тестируем начальное количество категорий."""
    assert Category.category_count == 1


def test_add_product(setup_category):
    """Тестируем добавление нового продукта."""
    product3 = Product.new_product({"name": "Планшет", "description": "Таблетка", "price": 15000, "quantity": 5})
    setup_category.add_product(product3)
    assert setup_category.products_list.endswith("Планшет, 15000 руб. Остаток: 5 шт.")


def test_products_list(setup_category):
    """Тестируем вывод списка продуктов."""
    expected_output = "Телефон, 8000 руб. Остаток: 15 шт.\n" "Ноутбук, 50000 руб. Остаток: 7 шт."
    assert setup_category.products_list == expected_output


def test_addition_of_two_products():
    """Тестируем сложение двух продуктов."""
    product1 = Product("Телефон", "Смартфон", 8000, 15)
    product2 = Product("Ноутбук", "Игровой ноутбук", 50000, 7)

    total_cost = product1 + product2
    expected_cost = (product1.price * product1.quantity) + (product2.price * product2.quantity)

    assert total_cost == expected_cost


def test_addition_of_product_and_zero_quantity():
    """Тестируем сложение продукта с продуктом, у которого ноль в количестве."""
    product1 = Product("Телефон", "Смартфон", 8000, 15)
    product2 = Product("Планшет", "Таблетка", 15000, 0)

    total_cost = product1 + product2
    expected_cost = product1.price * product1.quantity

    assert total_cost == expected_cost


def test_addition_of_two_products_with_zero_quantity():
    """Тестируем сложение двух продуктов, у которых ноль в количестве."""
    product1 = Product("Телефон", "Смартфон", 8000, 0)
    product2 = Product("Ноутбук", "Игровой ноутбук", 50000, 0)

    total_cost = product1 + product2
    expected_cost = 0

    assert total_cost == expected_cost
