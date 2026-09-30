from datetime import datetime
from storage import load_json, save_json, next_id
from validators import text, integer

class Billing:
    FILE="bills.json"
    def __init__(self,inventory,customers): self.inventory=inventory; self.customers=customers; self.bills=load_json(self.FILE,{})
    def save(self): save_json(self.FILE,self.bills)
    def create(self):
        cart=[]
        while True:
            self.inventory.display()
            pid=input("Product ID (DONE to finish): ").strip().upper()
            if pid=="DONE": break
            if pid not in self.inventory.products: print("Not found."); continue
            p=self.inventory.products[pid]; qty=integer("Quantity: ",1)
            if qty>p['quantity']: print("Insufficient stock."); continue
            cart.append({"product_id":pid,"name":p['name'],"quantity":qty,"selling_price":p['selling_price'],"buying_price":p['buying_price'],"subtotal":round(p['selling_price']*qty,2),"cost":round(p['buying_price']*qty,2)})
            print("Added.")
        if not cart: print("Empty cart."); return
        cid=input("Customer ID (blank=walk-in): ").strip().upper()
        if cid and cid not in self.customers.data: print("Customer not found."); return
        mode=input("Payment (cash/online/udhaar): ").strip().lower()
        if mode not in {"cash","online","udhaar"}: mode="cash"
        if mode=="udhaar" and not cid: print("Udhaar needs a customer."); return
        total=round(sum(x['subtotal'] for x in cart),2); cost=round(sum(x['cost'] for x in cart),2)
        for x in cart: self.inventory.decrease(x['product_id'],x['quantity'])
        bid=next_id(self.bills,"B"); now=datetime.now()
        bill={"bill_id":bid,"date":now.strftime('%Y-%m-%d'),"time":now.strftime('%H:%M:%S'),"customer_id":cid,"items":cart,"total":total,"cost":cost,"profit":round(total-cost,2),"payment_mode":mode}
        self.bills[bid]=bill
        if mode=="udhaar": self.customers.add_pending(cid,total)
        self.save(); self.print_bill(bill)
    def print_bill(self,b):
        print("\n"+"="*55); print("BILL",b['bill_id'],b['date'],b['time']); print("="*55)
        for x in b['items']: print(f"{x['name'][:28]:28} x{x['quantity']:<3} {x['subtotal']:>9.2f}")
        print("-"*55); print(f"TOTAL: {b['total']:.2f} | PAYMENT: {b['payment_mode']} | PROFIT: {b['profit']:.2f}")
    def bills_list(self):
        for bid,b in self.bills.items(): print(f"{bid} | {b['date']} {b['time']} | {b['total']:.2f} | {b['payment_mode']}")
    def search(self):
        bid=text("Bill ID: ").upper(); b=self.bills.get(bid)
        if b: self.print_bill(b)
        else: print("Bill not found.")
    def totals(self): return sum(b['total'] for b in self.bills.values()),sum(b['profit'] for b in self.bills.values())
