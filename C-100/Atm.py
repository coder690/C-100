class Atm(object):
    def __init__ (self,CashWithdrawl,BalanceEnquiry):
        self.BalanceEnquiry=BalanceEnquiry
        self.CashWithdrawl=CashWithdrawl

    def WithDrawl (self):
         print("CashWithdrawl")

    def BalanceEnquiry (self):
        print("Balance")

audi=Atm("$500","$500")
print(Atm.BalanceEnquiry)

   