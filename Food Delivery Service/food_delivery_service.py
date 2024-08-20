from typing import List, Dict
from uuid import uuid4
from customer import Customer
from restaurant import Restaurant
from order import Order, OrderStatus
from delivery_partner import DeliveryPartner
from menu_item import MenuItem


class FoodDeliveryService:
    _instance = None

    def __init__(self):
        if FoodDeliveryService._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            FoodDeliveryService._instance = self
            self.customers = {}
            self.restaurants = {}
            self.delivery_partners = {}
            self.orders = {}

    @staticmethod
    def get_instance():
        if FoodDeliveryService._instance is None:
            FoodDeliveryService()
        return FoodDeliveryService._instance

    def register_customer(self, customer: Customer):
        self.customers[customer.id] = customer

    def register_restaurant(self, restaurant: Restaurant):
        self.restaurants[restaurant.id] = restaurant

    def register_delivery_partner(self, agent: DeliveryPartner):
        self.delivery_partners[agent.id] = agent

    def get_available_restaurants(self) -> List[Restaurant]:
        return list(self.restaurants.values())

    def get_restaurant_menu(self, restaurant_id: str) -> List[MenuItem]:
        return self.restaurants.get(restaurant_id, [])

    def place_order(
        self, customer_id: str, restaurant_id: str, items: List[MenuItem]
    ) -> Order:
        customer = self.customers.get(customer_id)
        restaurant = self.restaurants.get(restaurant_id)

        if customer and restaurant:
            order_id = self.generate_order_id()
            order = Order(order_id, customer, restaurant)
            for item in items:
                order.add_item(item)
            self.orders[order_id] = order
            self.notify_restaurant(order)
            return order

    def update_order_status(self, order_id, status: OrderStatus):
        order = self.orders.get(order_id)
        if order:
            order.status = status
            self.notify_customer(order)
            if status == OrderStatus.CONFIRMED:
                self.assign_delivery_partner(order)

    def assign_delivery_partner(self, order: Order):
        for delivery_partner in self.delivery_partners.values():
            if delivery_partner.available:
                delivery_partner.available = False
                order.delivery_partner = delivery_partner
                self.notify_delivery_partner(order)
                break

    def cancel_order(self, order_id: str):
        order = self.orders.get(order_id)
        if order and order.status == OrderStatus.PENDING:
            order.status = OrderStatus.CANCELLED
            self.notify_customer(order)
            self.notify_restaurant(order)

    def notify_customer(self, order: Order):
        # Send notification to the customer about the order status update
        pass

    def notify_restaurant(self, order: Order):
        pass

    def notify_delivery_partner(self, order: Order):
        # Send notification to the customer about the order status update
        pass

    def generate_order_id(self):
        return "ORD" + uuid4().hex[:8].upper()
