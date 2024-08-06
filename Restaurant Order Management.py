# Task 1 Design a stack-based data structure to represent the kitchen's order queue, where orders are processed in the order they are received.

class kitchenOrderStack:
    def __init__(self):
        self.orders = []

# Task 2 Implement functions to add new orders to the kitchen's order queue and remove orders when they are completed.

    def push(self, order):
        self.orders.append(order)

    def pop(self):
        self.orders.pop(0)

    def view(self):
        print(self.orders)

# Task 3 Design a queue-based data structure to represent the customer order queue, where orders are prioritized based on factors such as customer waiting time and order complexity.

class cusomterOrderQueue:
    def __init__(self):
        self.orders = []

# Task 4 Implement functions to add new orders to the customer order queue, process orders, and notify customers when their orders are ready for pickup or delivery.

    def addOrder(self, order):
        self.orders.append(order)

    def finishOrder(self):
        finishedOrder = self.orders.pop(0)
        notifyCustomer(finishedOrder["customer"])

def notifyCustomer(customer):
    # Look up customer in db and send messege
    print(f"{customer} has been notified their order is ready!")
    pass

# Task 5 Test the order management system with sample orders to ensure its correctness and efficiency.

kitchenOrders = kitchenOrderStack()
kitchenOrders.push("bread")
kitchenOrders.push("water")
kitchenOrders.view()
kitchenOrders.pop()
kitchenOrders.view()

customerOrders = cusomterOrderQueue()
customerOrders.addOrder({"customer": "Person", "minutes_waiting": 5, "order_items": ["bread", "water"], "order_complexity": "medium"})
customerOrders.finishOrder()