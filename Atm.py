import random

class Atm(object):
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin

    def cashWithdrawl(self):
        print("Cash Withdrawl completed")
    def balance(self):
        print("$", random.randint(200,500) , " remain")
        
atm = Atm("9802-4371", "9009")
atm.cashWithdrawl()
atm.balance()