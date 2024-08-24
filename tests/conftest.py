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
