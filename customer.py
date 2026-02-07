from order import Order


class Customer:
    """
    Represents a customer.

    Attributes:
        _name       (str):       Customer name.
        _email      (str):       Customer email address.
        _order_list (list[Order]): List of the customer's orders.

    Methods:
        add_order(self, order: Order) -> None:
            Add a new order to the customer's order list.
    """

    def __init__(self, name: str, email: str, order_list: list[Order] = []):
        """
        Initialize a Customer instance.

        Args:
            name (str): Customer name.
            email (str): Customer email address.
            order_list (list[Order] | None): Initial list of orders.
        """
        self._name = name
        self._email = email
        self._order_list = order_list

    @property
    def name(self) -> str:
        """
        Return the customer's name.

        Returns:
            str: Customer name.
        """
        return self._name

    @property
    def email(self) -> str:
        """
        Return the customer's email.

        Returns:
            str: Customer email address.
        """
        return self._email

    @property
    def order_list(self) -> list[Order]:
        """
        Return the list of the customer's orders.

        Returns:
            list[Order]: Customer order list.
        """
        return self._order_list

    @order_list.setter
    def order_list(self, value: list[Order]) -> None:
        """
        Set the customer's order list.

        Args:
            value (list[Order]): New list of orders.

        Raises:
            TypeError: If value is not a list.
            TypeError: If any item in the list is not an Order instance.
        """
        if not isinstance(value, list):
            raise TypeError("value must be a list of Order instances.")

        if not all(isinstance(item, Order) for item in value):
            raise TypeError("All items in order_list must be Order instances.")

        self._order_list = value

    def add_order(self, order: Order) -> None:
        """
        Add a new order to the customer's order list.

        Args:
            order (Order): Order to be added.
        """
        self.order_list.append(order)
