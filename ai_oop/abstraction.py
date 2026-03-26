# abc মডিউল ইমপোর্ট করা
from abc import ABC, abstractmethod


# Abstract Class তৈরি করা
class Payment(ABC):

    # এটি একটি Abstract Method (এর কোনো বডি বা ভেতরের কাজ নেই)
    @abstractmethod
    def pay(self, amount):
        pass


# Child Class 1: Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"ক্রেডিট কার্ডের মাধ্যমে {amount} টাকা পেমেন্ট করা হয়েছে।")


# Child Class 2: Bkash Payment
class BkashPayment(Payment):
    def pay(self, amount):
        print(f"বিকাশের মাধ্যমে {amount} টাকা পেমেন্ট করা হয়েছে।")


# Object তৈরি এবং ব্যবহার
# p = Payment()  # এটি এরর দিবে! কারণ Abstract Class এর অবজেক্ট হয় না।

payment1 = CreditCardPayment()
payment1.pay(500)  # আউটপুট: ক্রেডিট কার্ডের মাধ্যমে 500 টাকা পেমেন্ট করা হয়েছে।

payment2 = BkashPayment()
payment2.pay(1000)  # আউটপুট: বিকাশের মাধ্যমে 1000 টাকা পেমেন্ট করা হয়েছে।