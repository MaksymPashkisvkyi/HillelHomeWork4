from product import Product


class Order:
    """
    Represents a customer order.

    Attributes:
        _product_list (list[Product]): List of products in the order.
        _total_amount (float): Total cost of the order.

    Methods:
        add_product(product: Product) -> None:
            Add a product to the order.
        calculate_total_amount() -> None:
            Calculate and update the total order amount.
    """

    def __init__(self):
        """
        Initialize an empty Order instance.
        """
        self._product_list: list[Product] = []
        self._total_amount: float = 0.0

    @property
    def product_list(self) -> list[Product]:
        """
        Return the list of products in the order.

        Returns:
            list[Product]: Products included in the order.
        """
        return self._product_list

    @product_list.setter
    def product_list(self, value: list[Product]) -> None:
        """
        Set the list of products in the order.

        Args:
            value (list[Product]): New list of Product instances.

        Raises:
            TypeError: If value is not a list.
            TypeError: If any item in the list is not a Product instance.
        """
        if not isinstance(value, list):
            raise TypeError("value must be a list of Product instances.")

        if not all(isinstance(item, Product) for item in value):
            raise TypeError("All items in product_list must be Product instances.")
        self._product_list = value

    @property
    def total_amount(self) -> float:
        """
        Return the total cost of the order.

        Returns:
            float: Total order amount.
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value: float) -> None:
        """
        Set the total cost of the order.

        Args:
            value (float): New total order amount.

        Raises:
            ValueError: If value is less than zero.
        """
        if value < 0:
            raise ValueError("Total order amount cannot be less than 0.")
        self._total_amount = value

    def add_product(self, product: Product):
        """
        Add a product to the order and decrease its stock quantity by one.

        Args:
            product (Product): Product to be added to the order.
        """
        self.product_list.append(product)  # в список додаємо новий товар
        product.change_quantity(-1)  # віднімаємо одну одиницю товару зі складу

    def calculate_total_amount(self):
        """
        Calculate and update the total order amount
        based on the prices of all products in the order.
        """
        self.total_amount = sum(product.price for product in self.product_list)
