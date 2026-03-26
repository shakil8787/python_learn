class bankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print(f"বর্তমান ব্যালেন্স: {self.__balance} টাকা")

    def diposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} টাকা জমা হয়েছে।")
        else:
            print("ভুল অ্যামাউন্ট!")

account = bankAccount("রহিম", 5000)

print(account.owner)
account.show_balance()  # Output: বর্তমান ব্যালেন্স: 5000 টাকা
account.diposit(2000)   # Output: 2000 টাকা জমা হয়েছে।
account.show_balance()  # Output: বর্তমান ব্যালেন্স: 7000 টাকা