
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

order = OrderDTO(1, "Laptop", 2, 500)
service = OrderService()

service.print_order(order)
print("Total:", service.calculate_total(order))