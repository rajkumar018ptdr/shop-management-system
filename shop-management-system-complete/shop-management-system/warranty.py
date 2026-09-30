from datetime import date,timedelta
from storage import load_json,save_json,next_id
from validators import text,integer

class Warranty:
    FILE="warranties.json"
    def __init__(self): self.data=load_json(self.FILE,{})
    def save(self): save_json(self.FILE,self.data)
    def add(self):
        wid=next_id(self.data,"W"); d=text("Purchase date YYYY-MM-DD: "); months=integer("Warranty months: ",1)
        try: start=date.fromisoformat(d)
        except ValueError: print("Invalid date."); return
        expiry=start+timedelta(days=months*30)
        self.data[wid]={"customer":text("Customer: "),"product":text("Product: "),"purchase_date":d,"months":months,"expiry_date":expiry.isoformat()}
        self.save(); print("Warranty ID:",wid,"Expiry:",expiry)
    def display(self):
        for wid,w in self.data.items(): print(f"{wid}: {w['customer']} | {w['product']} | {w['purchase_date']} -> {w['expiry_date']}")
    def search(self):
        q=text("Search: ").lower()
        for wid,w in self.data.items():
            if q in w['customer'].lower() or q in w['product'].lower(): print(wid,w)
    def expiring(self):
        days=integer("Within days: "); today=date.today(); limit=today+timedelta(days=days)
        for wid,w in self.data.items():
            try: d=date.fromisoformat(w['expiry_date'])
            except ValueError: continue
            if today<=d<=limit: print(wid,w)
