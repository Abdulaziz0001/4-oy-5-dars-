# # 1-misol
# from decimal import Decimal
# from datetime import datetime
# import random
#
# class Dec:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#     def __set__(self, instance, value: Decimal):
#         if not(-50 <= value <= 50):
#             raise ValueError("Xatilik!!! Harorat ko'tarilib ketti!!!")
#         instance.__dict__[self.name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
# class Gradus:
#     gardus = Dec()
#     def __init__(self):
#         self.harorat =  random.uniform(-10, 40)
#         self.sana = datetime.now()
#
#     def get_harorat(self):
#         return f"Harorat: {self.harorat}"
#
#     def get_sana(self):
#         return f"Sana: {self.sana}"
#
# p = Gradus()
# print(p.get_harorat())
# print(p.get_sana())
#
# try:
#     raise ValueError("Xatilik!!! Harorat ko'tarilib ketti!!!")
# except ValueError as e:
#     print(e)
#
# p.gardus = 20
# print(p.get_harorat())
from collections import namedtuple
# # 2-misol
# from decimal import Decimal
# from datetime import datetime
# import random
#
# class InsufficientFundsError(Exception):
#     pass
#
# class BankAccount:
#     def __init__(self, balans):
#         self._balans = Decimal(balans)
#         self.transactions = []
#
#     @property
#     def balance(self):
#         return self._balans
#
#     def deposit(self, amount):
#         amount = Decimal(amount)
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self._balans += amount
#         transaction = {
#             'type': 'deposit',
#             'amount': amount,
#             'date': self._random_date()
#         }
#         self.transactions.append(transaction)
#
#     def withdraw(self, amount):
#         amount = Decimal(amount)
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive.")
#         if self._balans - amount < 0:
#             raise InsufficientFundsError("Xatolik: Balans yetarli emas!")
#         self._balans -= amount
#         transaction = {
#             'type': 'withdrawal',
#             'amount': amount,
#             'date': self._random_date()
#         }
#         self.transactions.append(transaction)
#
#     def _random_date(self):
#         start_date = datetime.now().replace(year=datetime.now().year - 1)
#         end_date = datetime.now()
#         random_timestamp = random.randint(int(start_date.timestamp()), int(end_date.timestamp()))
#         return datetime.fromtimestamp(random_timestamp)
#
#     def transaction_history(self):
#         return self.transactions
#
# try:
#     my_account = BankAccount("700000")
#     print(f"Hisobingiz: {my_account.balance} UZS")
#     my_account.deposit("100000")
#     print(f"Yangi balans: {my_account.balance} UZS")
#     my_account.withdraw("600000")
# except InsufficientFundsError as e:
#     print(e)
# except Exception as e:
#     print(f"Xatolik: {e}")
#
# for transaction in my_account.transaction_history():
#     print(transaction)

# # 3-misol
# from decimal import Decimal
# import random
#
# class Chiptalar:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#     def __set__(self, instance, value: Decimal):
#         if type(value) is int and value.isdecimal():
#             instance.__dict__[self.name] = value
#         else:
#             try:
#                 raise ValueError("Xatolikka yo'l qo'yildi!!!")
#             except ValueError as e:
#                 print(e)
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
# sana = []
# class Chipta:
#     def __init__(self):
#         for i in range(1, 31):
#             sana.append(f"2024.12.{i}")
#
#     def chipta(self):
#         chipta = 150000
#         return f"Chipta narxi: {chipta} UZS (Sana: {random.choice(sana)})"
#
# p = Chipta()
# print(p.chipta())

# # 4-misol
# # from decimal import Decimal
# # from datetime import datetime, timedelta
# # import random
# #
# # class Dec:
# #     def __set_name__(self, owner, name):
# #         self.name = "_" + name
# #
# #     def __set__(self, instance, value: Decimal):
# #         if type(value) is str and value.isdecimal():
# #             instance.__dict__[self.name] = value
# #         else:
# #             try:
# #                 raise ValueError("Xatolikka yo'l qo'ydingiz!!!")
# #             except ValueError as e:
# #                 print(e)
# #     def __get__(self, instance, owner):
# #         return instance.__dict__[self.name]
# # class Oylik:
# #     def __init__(self):
# #         random_days = random.randint(1, 31)
# #         self.random_date = datetime.now() + timedelta(days=random_days)
# #
# #     def user(self):
# #         oylik = "3.200.000"
# #         formated_day = self.random_date.strftime("%d.%m.%Y")
# #         return f"Ishchi oyligi: {oylik} UZS (Sana: {formated_day})"
# # p = Oylik()
# # print(p.user())