class Product:
    """
    Represents a product.

    Attributes:
        __name (str): Product name.
        __category (str): Product category (e.g., "soft toy", "constructor").
        __price (float): Product price.
        __quantity (int): Quantity of the product in stock.

    Methods:
        change_price(price: float) -> None:
            Change the product price.
        change_quantity(quantity: int):
            Change the quantity of the product in stock.
    """

    def __init__(self, name: str, category: str, price: float = 0.0, quantity: int = 0):
        """
        Initialize a Product instance.

        Args:
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
            quantity (int): Initial quantity in stock.
        """
        self.__name = str(name)
        self.__category = str(category)
        self.__price = float(price)
        self.__quantity = int(quantity)

    @property
    def name(self) -> str:
        """
        Return the product name.

        Returns:
            str: Product name.
        """
        return self.__name

    @property
    def category(self) -> str:
        """
        Return the product category.

        Returns:
            str: Product category.
        """
        return self.__category

    @property
    def price(self) -> float:
        """
        Return the product price.

        Returns:
            float: Product price.
        """
        return self.__price

    @price.setter
    def price(self, value) -> None:
        """
        Set the product price.

        Args:
            value (float): New product price.

        Raises:
            ValueError: If the price is less than zero.
        """
        if value < 0:
            raise ValueError("Price cannot be less than 0.")
        self.__price = value

    @property
    def quantity(self) -> int:
        """
        Return the quantity of the product in stock.

        Returns:
            int: Product quantity in stock.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """
        Set the quantity of the product in stock.

        Args:
            value (int): New product quantity.

        Raises:
            ValueError: If the quantity is less than zero.
        """
        if value < 0:
            raise ValueError("Quantity cannot be less than 0.")

        self.__quantity = int(value)

    def change_price(self, price: float) -> None:
        """
        Change the product price.

        Args:
            price (float): New price of the product.
        """
        self.price = price

    def change_quantity(self, quantity: int) -> None:
        """
        Change the quantity of the product in stock.

        Args:
            quantity (int): Amount to add to (or subtract from) stock.
        """
        self.quantity += int(quantity)
