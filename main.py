from customer import Customer
from order import Order
from product import Product


if __name__ == "__main__":
    """
    Entry point of the application.
    Simulates creating a customer order, printing a receipt,
    and updating product stock quantities.
    """

    # Read customers and products from dataset files
    customers_file = open("./dataset/customers.txt", "r")
    products_file = open("./dataset/products.txt", "r")
    raw_customers_list = customers_file.readlines()
    raw_products_list = products_file.readlines()

    # Create a Customer object using data from the dataset
    customer_name, customer_email = raw_customers_list[0].split(",")
    customer = Customer(customer_name, customer_email)

    # Create Product objects using data from the dataset
    products_list = []
    for product in raw_products_list:
        name, category, price, quantity = product.split(",")
        products_list.append(Product(name, category, price, quantity))

    # Create a new Order for the customer
    order = Order()
    customer.add_order(order)

    # Display initial stock quantities
    print("*" * 50)
    print("Початкова кількість товару, що є на складі:")
    print(f"{products_list[0].name} = {products_list[0].quantity}")
    print(f"{products_list[1].name} = {products_list[1].quantity}")
    print(f"{products_list[2].name} = {products_list[2].quantity}")
    print(f"{products_list[3].name} = {products_list[3].quantity}")
    print("*" * 50)
    print()

    # Add products to the order
    order.add_product(products_list[0])  # Add one chair priced at 100.0
    order.add_product(products_list[0])  # Add another chair priced at 100.0
    order.add_product(products_list[3])  # Add one laptop priced at 500.0
    order.add_product(products_list[2])  # Add one bed priced at 200.0

    # Print order receipt
    print("*" * 50)
    print("Імітація чеку")
    for product in order.product_list:
        print("-" * 10)
        print(f"{product.name} x 1 = {product.price}")

    # Calculate and display total order amount
    order.calculate_total_amount()
    print("-" * 20)
    print(f"Сума = {order.total_amount}")
    print("*" * 50)
    print()

    # Display remaining stock quantities
    print("*" * 50)
    print("Кількість товару, що залишилася на складі:")
    print(f"{products_list[0].name} = {products_list[0].quantity}")
    print(f"{products_list[1].name} = {products_list[1].quantity}")
    print(f"{products_list[2].name} = {products_list[2].quantity}")
    print(f"{products_list[3].name} = {products_list[3].quantity}")
    print("*" * 50)
