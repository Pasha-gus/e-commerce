import pytest

from src.category_class import Category
from src.product_class import Product


@pytest.fixture
def setup_category():
    """Фикстура для создания категории с продуктами."""
    product1 = Product("Телефон", "Смартфон", 8000, 15)
    product2 = Product("Ноутбук", "Игровой ноутбук", 50000, 7)
    category = Category("Электроника", "Различные электронные устройства", [product1, product2])
    return category


@pytest.fixture
def empty_category():
    return Category("Пустая категория", "Описание пустой категории", [])


@pytest.fixture
def category_with_products():
    product1 = Product("Продукт 1", "Описание продукта 1", 100, 5)
    product2 = Product("Продукт 2", "Описание продукта 2", 200, 3)
    return Category("Категория с продуктами", "Описание категории с продуктами", [product1, product2])


@pytest.fixture
def category_with_zero_price_products():
    product1 = Product("Продукт 1", "Описание продукта 1", 0, 5)
    product2 = Product("Продукт 2", "Описание продукта 2", 0, 3)
    return Category("Категория с нулевыми ценами", "Описание категории с нулевыми ценами", [product1, product2])
