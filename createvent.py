import datetime

class Event:
    def __init__(self, event_type: str, timestamp: datetime.datetime = None):
        self.type = event_type
        self.timestamp = timestamp if timestamp else datetime.datetime.now()

    def to_dict(self):
        return self.__dict__

class OrderCreatedEvent(Event):
    def __init__(self, order_id: str, user_id: str, items: list, total_amount: float, timestamp: datetime.datetime = None):
        super().__init__("OrderCreated", timestamp)
        self.order_id = order_id
        self.user_id = user_id
        self.items = items  # [{'product_id': 'P101', 'quantity': 2, 'price': 10.0}]
        self.total_amount = total_amount

    def __repr__(self):
        return f"OrderCreatedEvent(order_id='{self.order_id}', user_id='{self.user_id}', total_amount={self.total_amount})"

# Example usage for OrderCreatedEvent:
order_items = [
    {'product_id': 'PROD001', 'quantity': 2, 'price': 25.50},
    {'product_id': 'PROD002', 'quantity': 1, 'price': 100.00}
]
example_order_created = OrderCreatedEvent(
    order_id='ORD12345',
    user_id='USER987',
    items=order_items,
    total_amount=151.00
)
print(f"OrderCreatedEvent structure defined: {example_order_created.to_dict()}")