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

    def add_product(self, product):
        """Добавляет один продукт в категорию и обновляет счетчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_list(self):
        """Выводит список товаров в виде строк в формате 'Название продукта, цена руб. Остаток: шт.'"""
        result = ""
        for product in self.__products:
            result += (
                f"Название продукта: {product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт.\n"
            )
        return result.strip()
