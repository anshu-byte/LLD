from typing import List
from orderStatus import OrderStatus
from delivery_partner import DeliveryPartner
from customer import Customer
from restaurant import Restaurant
from menu_item import MenuItem


class Order:
    def __init__(self, order_id: str, customer: Customer, restaurant: Restaurant):
        self._id = order_id
        self._customer = customer
        self._restaurant = restaurant
        self._items: List[MenuItem] = []
        self._status = OrderStatus.PENDING
        self._delivery_partner = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def status(self) -> OrderStatus:
        return self._status

    @status.setter
    def status(self, status: OrderStatus):
        self._status = status

    @property
    def delivery_partner(self) -> DeliveryPartner:
        return self._delivery_partner

    @delivery_partner.setter
    def delivery_partner(self, delivery_partner: DeliveryPartner):
        self._delivery_partner = delivery_partner

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)
