# Module: payments.py
import asyncio
import random

async def process_payment(customer_name: str, amount: float) -> bool:
    if amount <= 0:
        raise ValueError("El monto del pago debe ser mayor a cero y exacto.")
    print(f"Procesando pago de {customer_name} por ${amount}...")
    await asyncio.sleep(random.randint(1, 3))  # Simula una operación de pago
    print(f"Pago de ${amount} completado para {customer_name}")
    return True