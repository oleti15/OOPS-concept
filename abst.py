# from abc import ABC,abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         print("paid", amount ," using Google Pay")
#         pass
# class Googlepay(Payment):
#     def pay(self,amount):
#         print("paid", amount ," using Google Pay")
#         pass
# ob=Googlepay()
# ob.pay(9000)

# create  a abst cls bank the properties of amount,with draw amount,balance amount which includes child classes 
# as payment gateway google pay ,phone pay, credit,debit,netbanking ,upi
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def pay(self,amount,withdraw):
        print(amount)
        print(withdraw)
class Googlepay(Bank):
    def pay(self,amount,withdraw):
        print("The Total Amount is",amount)
        print("The withDraw amount  is",withdraw)
        print("the Balance amount is ",amount-withdraw)

class UPI(Bank):
    def pay(self,amount,withdraw):
        print("The Total Amount is",amount)
        print("The withDraw amount  is",withdraw)
        print("the Balance amount is ",amount-withdraw)
class PhonePay(Bank):
    def pay(self,amount,withdraw):
        print("The Total Amount is",amount)
        print("The withDraw amount  is",withdraw)
        print("the Balance amount is ",amount-withdraw)
class Creadit(Bank):
    def pay(self,amount,withdraw):
        print("The Total Amount is",amount)
        print("The withDraw amount  is",withdraw)
        print("the Balance amount is ",amount-withdraw)
class Debit(Bank):
    def pay(self,amount,withdraw):
        print("The Total Amount is",amount)
        print("The withDraw amount  is",withdraw)
        print("the Balance amount is ",amount-withdraw)
class NetBanking(Bank):
    def pay(self,amount,withdraw):
        print("The Total Amount is",amount)
        print("The withDraw amount  is",withdraw)
        print("the Balance amount is ",amount-withdraw)
op=input("Enter option:")
match(op):
    case "Googlepay":
        ob=Googlepay()
        ob.pay(50000,3000)
    case "UPI":
        ob1=UPI()
        ob1.pay(40000,200)
    case "PhonePay":
        ob2=PhonePay()
        ob2.pay(20000,100)
    case "Creadit":
        ob3=Creadit()
        ob3.pay(4992,121)
    case "Debit":
        ob4=Debit()
        ob4.pay(23000,2300)
    case "NetBanking":
        ob5=NetBanking()
        ob5.pay(240000,2400)






