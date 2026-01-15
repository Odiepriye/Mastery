class BankAccount:
    __balance: str

    def __init__(self, balance: str):
        self.__balance = balance

    def get_balance(self) -> str:
        return self.__balance

    def set_balance(self, balance: str) -> None:
        self.__balance = balance

    def deposit(self, amount: str) -> None:
        self.__balance += amount
account = BankAccount("100")
print(f"Balance: {account.get_balance()}")
"".join(account.get_balance())