    #creating a personal finance tracker which maintains record of my monthly expences
import pandas as pd
from datetime import datetime
import logging

class Finance_Tracker():
        
        def __init__(self):
            
            self.valid_PAY_Category=["food","rent","travel","entertainment","savings","others"] 
            try:
                self.df=pd.read_csv("PF_data.csv")
                if not self.df.empty:
                    self.a_balance=self.df["BALANCE"].iloc[-1]
                else:
                    self.a_balance=40000
            except:
                self.df=pd.DataFrame(columns=["TYPE","DATE","CATEGORY","AMOUNT","BALANCE"])
                self.df.to_csv("PF_data.csv",index=False)
                self.a_balance=40000
                
        def debit(self,category,amount):
            if amount>self.a_balance:
                logging.warning("transaction amount has exceded account balance")
            elif category not in self.valid_PAY_Category:
                logging.warning(f"select a valid category in {self.valid_PAY_Category}")
            else:
                self.a_balance-=amount
                date_time=datetime.now().replace(microsecond=0)

                new_entry={"TYPE":"DEBIT","DATE":date_time,"CATEGORY":category,"AMOUNT":amount,"BALANCE":self.a_balance}
                self.df=pd.concat([self.df,pd.DataFrame([new_entry])],ignore_index=True)
                self.df.to_csv("PF_data.csv",index=False)
                logging.info("SUCESS")
        
        def credit(self,category,amount):
            self.a_balance+=amount
            date_time=datetime.now().replace(microsecond=0)

            new_entry={"TYPE":"CREDIT","DATE":date_time,"CATEGORY":category,"AMOUNT":amount,"BALANCE":self.a_balance}
            self.df=pd.concat([self.df,pd.DataFrame([new_entry])],ignore_index=True)
            self.df.to_csv("PF_data.csv",index=False)
            logging.info("SUCESS")


            

