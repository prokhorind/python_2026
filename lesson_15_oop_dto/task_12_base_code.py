# ADVANCED_STARTER.py

class ItemDTO:
    # TODO
    pass

class OrderDTO:
    # TODO
    pass

class OrderService:
    def print_order(self, order):
        # TODO
        pass

    def calculate_total(self, order):
        # TODO
        pass

# --- test ---

items = [
    ItemDTO("Laptop", 500, 2),
    ItemDTO("Mouse", 50, 3)
]

order = OrderDTO(1, items)
service = OrderService()

service.print_order(order)
print("Total:", service.calculate_total(order))