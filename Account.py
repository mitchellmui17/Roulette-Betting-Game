def accountBal(a):
    print("Amount $", a)
    print(a, "is your total balance.")
    global Balance
    Balance = int(a)


def winBal(b):
    Total = Balance + b
    print("Your total balance is now ", Total)
    accountBal(Total)


