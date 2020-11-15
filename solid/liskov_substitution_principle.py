from abc import ABC, abstractmethod


class DeliveryBase(ABC):

    def __init__(self, product_ids, user):
        self.product_ids = product_ids
        self.user = user


class OfflineDelivery(DeliveryBase, ABC):

    @abstractmethod
    def get_delivery_location(self):
        pass


class OnlineDelivery(DeliveryBase, ABC):

    @abstractmethod
    def get_email(self):
        pass


class ComputerDelivery(OfflineDelivery):

    def get_delivery_location(self):
        pass


class SoftwareDelivery(OnlineDelivery):

    def get_email(self):
        pass

