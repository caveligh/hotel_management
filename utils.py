# Module: utils.py
from typing import Callable

def customer_exists(func: Callable) -> Callable:
    def wrapper(self, customer_id: int, *args, **kwargs):
        if customer_id not in self.customers:
            raise ValueError(f"Cliente con ID {customer_id} no encontrado.")
        return func(self, customer_id, *args, **kwargs)
    return wrapper


