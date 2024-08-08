import pytest

from src.category_class import Category
from src.product_class import Product


@pytest.fixture
def setup_category():
    """Фикстура для создания категории с продуктами."""
    product1 = {"name": "Телефон", "price": 8000, "quantity": 15}
    product2 = {"name": "Ноутбук", "price": 50000, "quantity": 7}
    category = Category("Электроника", "Различные электронные устройства", [product1, product2])
    return category
