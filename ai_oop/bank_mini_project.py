from abc import ABC, abstractmethod


# ১. Abstraction: BankAccount একটি Abstract Class, এর সরাসরি অবজেক্ট বানানো যাবে না।
class BankAccount(ABC):
    def __init__(self, name, account_no, balance):
        self.name = name  # Public Data
        self.account_no = account_no  # Public Data
        self.__balance = balance  # ২. Encapsulation: Private Data (লুকানো)

    # Encapsulation: Private ডেটা দেখার জন্য Getter Method
    def get_balance(self):
        return self.__balance

    # Private ডেটা পরিবর্তন করার জন্য Setter Method (যাতে লজিক প্রয়োগ করা যায়)
    def _set_balance(self, new_balance):
        self.__balance = new_balance

    # টাকা জমা দেওয়ার সাধারণ মেথড
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.name}-এর অ্যাকাউন্টে {amount} টাকা জমা হয়েছে। নতুন ব্যালেন্স: {self.__balance} টাকা।")
        else:
            print("ভুল অ্যামাউন্ট!")

    # Abstraction: টাকা তোলার নিয়ম একেক অ্যাকাউন্টে একেক রকম, তাই এটি Abstract Method
    @abstractmethod
    def withdraw(self, amount):
        pass


# ৩. Inheritance: BankAccount থেকে বৈশিষ্ট্য নিচ্ছে SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, name, account_no, balance, interest_rate):
        super().__init__(name, account_no, balance)  # প্যারেন্ট ক্লাসের __init__ কল করা
        self.interest_rate = interest_rate

    # ৪. Polymorphism: Abstract Method-কে নিজের মতো ওভাররাইড করা
    def withdraw(self, amount):
        # শর্ত: তোলার পর যেন অন্তত ৫০০ টাকা থাকে
        if amount > 0 and (self.get_balance() - amount) >= 500:
            self._set_balance(self.get_balance() - amount)
            print(f"Savings Account থেকে {amount} টাকা তোলা হয়েছে। বর্তমান ব্যালেন্স: {self.get_balance()} টাকা।")
        else:
            print("পর্যাপ্ত ব্যালেন্স নেই! অ্যাকাউন্টে ন্যূনতম ৫০০ টাকা রাখতে হবে।")

    # নিজস্ব একটি মেথড (লভ্যাংশ যোগ করা)
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)


# ৩. Inheritance: BankAccount থেকে বৈশিষ্ট্য নিচ্ছে CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, name, account_no, balance, overdraft_limit):
        super().__init__(name, account_no, balance)
        self.overdraft_limit = overdraft_limit

    # ৪. Polymorphism: একই withdraw মেথড, কিন্তু কাজ করার নিয়ম আলাদা
    def withdraw(self, amount):
        # শর্ত: মূল ব্যালেন্স + ওভারড্রাফট লিমিট পর্যন্ত তোলা যাবে
        if amount > 0 and (self.get_balance() + self.overdraft_limit) >= amount:
            self._set_balance(self.get_balance() - amount)
            print(f"Checking Account থেকে {amount} টাকা তোলা হয়েছে। বর্তমান ব্যালেন্স: {self.get_balance()} টাকা।")
        else:
            print(f"ওভারড্রাফট লিমিট ({self.overdraft_limit} টাকা) পার হয়ে যাচ্ছে!")


print("--- Savings Account টেস্টিং ---")
rahim_acc = SavingsAccount("Rahim", "SAV-101", 2000, 5) # ৫% লভ্যাংশ
rahim_acc.deposit(500)      # ২৫০০ হবে
rahim_acc.withdraw(2100)    # ফেইল করবে, কারণ 500 টাকা রাখতে হবে
rahim_acc.withdraw(1000)    # পাস করবে, ব্যালেন্স ১৫০০ হবে
rahim_acc.add_interest()    # লভ্যাংশ যোগ হবে

print("\n--- Checking Account টেস্টিং ---")
karim_acc = CheckingAccount("Karim", "CHK-202", 1000, 2000) # ২০০০ টাকা ওভারড্রাফট লিমিট
karim_acc.withdraw(1500)    # পাস করবে (ব্যালেন্স -৫০০ হবে), কারণ লিমিট ২০০০
karim_acc.withdraw(2000)    # ফেইল করবে, কারণ লিমিট ক্রস করছে