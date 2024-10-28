#Module Customer.py
from utils import customer_exists
from typing import Optional


class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        if '@' not in email:
            raise ValueError("Email no válido.")
        self.customer_id = customer_id
        self.name = name
        self.email = email

class CustomerManagement:
    def __init__(self):
        self.customers: Dict[int, Customer] = {}

    def add_customer(self, customer: Customer) -> None:
        if customer.customer_id in self.customers:
            raise ValueError(f"El cliente con ID {customer.customer_id} ya existe.")
        self.customers[customer.customer_id] = customer
        print(f"Cliente {customer.name} agregado.")

    @customer_exists
    def get_customer(self, customer_id: int) -> Optional[Customer]:
        return self.customers.get(customer_id, None)

    @customer_exists
    def remove_customer(self, customer_id: int) -> None:
        del self.customers[customer_id]
        print(f"Cliente con ID {customer_id} eliminado.")

    def list_customers(self) -> None:
        for customer in self.customers.values():
            print(f"Cliente ID: {customer.customer_id}, Nombre: {customer.name}, Email: {customer.email}")
