import os.path

from src.utils import transaction_amount
from src.external_api import currency_conversion

#


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "operations.json")
transaction1 = transaction_amount(file_path)


for transaction in transaction1:
    rub_amount = currency_conversion(transaction)
    print(f"Transaction amount in RUB: {rub_amount}")
