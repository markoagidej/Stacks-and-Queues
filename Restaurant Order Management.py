# Task 1 Design a queue-based data structure to represent the kitchen's order queue, where orders are processed in the order they are received. The first order in is the first one out.

class KitchenOrderQueue:
    def __init__(self):
        self.orders = []

# Task 2 Implement functions to add new orders to the kitchen's order queue and remove orders when they are completed.

    def push(self, order):
        self.orders.append(order)

    def pop(self):
        self.orders.pop(0)

    def view(self):
        for order in self.orders:
            print(order)


kitchenOrders = KitchenOrderQueue()
kitchenOrders.push({"customer": "Person", "minutes_waiting": 5, "order_items": ["bread", "water"], "order_complexity": "medium"})
kitchenOrders.push({"customer": "Person2", "minutes_waiting": 5, "order_items": ["bread"], "order_complexity": "simple"})
kitchenOrders.push({"customer": "Person3", "minutes_waiting": 5, "order_items": ["water"], "order_complexity": "simple"})
kitchenOrders.view()
kitchenOrders.pop()
print("After order removal:")
kitchenOrders.view()