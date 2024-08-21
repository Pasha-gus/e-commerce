from src.product_class import Product


class Category:
    """Класс для определения категорий"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_products} шт."

    def add_product(self, product):
        """Добавляет один продукт в категорию и обновляет счетчик товаров."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Можно добавлять только объекты класса Product или его подклассов.")

    @property
    def products_list(self):
        """Выводит список товаров в виде строк в формате 'Название продукта, цена руб. Остаток: шт.'"""
        return "\n".join(str(product) for product in self.__products)
