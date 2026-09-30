from storage import load_json, save_json, next_id
from validators import text, number

class Customers:
    FILE="customers.json"
    def __init__(self): self.data=load_json(self.FILE,{})
    def save(self): save_json(self.FILE,self.data)
    def add(self):
        cid=next_id(self.data,"C")
        self.data[cid]={"name":text("Name: "),"phone":text("Phone: "),"pending":0.0,"payments":[]}
        self.save(); print("Customer ID:",cid)
    def display(self):
        if not self.data: print("No customers."); return
        for cid,c in self.data.items(): print(f"{cid}: {c['name']} | {c['phone']} | Pending={c['pending']:.2f}")
    def search(self):
        q=text("Search: ").lower()
        for cid,c in self.data.items():
            if q in cid.lower() or q in c['name'].lower() or q in c['phone'].lower(): print(cid,c)
    def add_pending(self,cid,amount):
        if cid not in self.data: raise ValueError("Customer not found")
        self.data[cid]['pending']+=amount; self.save()
    def payment(self):
        cid=text("Customer ID: ").upper()
        if cid not in self.data: print("Not found."); return
        amount=number("Payment: ")
        if amount>self.data[cid]['pending']: print("Payment exceeds pending amount."); return
        self.data[cid]['pending']-=amount; self.data[cid]['payments'].append(amount); self.save(); print("Payment recorded.")
    def pending(self):
        for cid,c in self.data.items():
            if c['pending']>0: print(f"{cid}: {c['name']} = {c['pending']:.2f}")
