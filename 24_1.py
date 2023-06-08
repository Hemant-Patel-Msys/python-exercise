class Restuarent:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_order = []

    def add_item_menu(self,item):
        self.menu_items.append(item)

    def book_tables(self,table):
        self.book_table.append(table)

    def customer_orders(self,item):
        self.customer_order.append(item)

    def print_menu(self):
        return self.menu_items

    def print_table(self):
        return self.book_table

    def print_customer_order(self):
        return self.customer_order

r = Restuarent()

r.add_item_menu("Salad")
r.add_item_menu("Pizza")
r.add_item_menu("Chole-bature")
r.add_item_menu("Matar-Paneer")
r.add_item_menu("Pizza")
r.add_item_menu("Pasta")
r.add_item_menu("Rabdi")
r.add_item_menu("Cold drink")
print("Menu_items:-",r.menu_items)

r.book_tables(1)
r.book_tables(2)
r.book_tables(3)

print("book_table:-",r.book_table)


r.customer_orders("Pasta")
print("Customer_order",r.customer_order)


print("Menu",r.print_menu())
print("Table",r.print_table())
print("Custumer order",r.print_customer_order())


