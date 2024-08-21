class Product:
    """Класс для определения продуктов"""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(self, type(other)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Товары должны быть из одинаковых классов продуктов")

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта"""
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, price: float):
        """Задает цену товара"""
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
