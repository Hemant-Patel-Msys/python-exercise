class Restaurant:

    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_order = []

    def add_item_to_menu(self, items):
        a = self.menu_items[items]

    def book_tables(self, table):
        self.book_table.append({"table_number":table})


    def customer_orders(self,table,items):
        self.customer_order.append({"table":table,"item":items})

    def print_the_menu(self):
        print("Menu")
        for item_name in self.menu_items:
            print(item_name)


    def table_reservation(self):
        print("Reservation")
        for reseve in self.book_table:
            print(f"Table{reseve}")

    def print_customer_order(self):
        print("Customer_order")
        for order in self.customer_order:
            print(f"table order{order}")
            for item in order['items']:
                print(item)

r = Restaurant()







