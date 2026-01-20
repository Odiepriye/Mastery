import math

def getUpdatedBalance(balance: float, day: int) -> float:
    balance += day * 0.01

    # daily interest (5% AER)
    if balance > 0.01:
        daily_rate = 0.05 / 365
        balance += balance * daily_rate

    return balance


def getFinalBalance() -> float:
    balance = 0.0
    for day in range(1, 366):
        balance = getUpdatedBalance(balance, day)
    return balance


print(round(getFinalBalance(), 2))
