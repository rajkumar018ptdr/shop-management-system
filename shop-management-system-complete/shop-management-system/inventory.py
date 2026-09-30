from storage import load_json, save_json, next_id
from validators import text, integer, number

class Inventory:
    FILE="products.json"
    def __init__(self): self.products=load_json(self.FILE,{})
    def save(self): save_json(self.FILE,self.products)
    def add(self):
        print("\n--- ADD PRODUCT ---")
        pid=next_id(self.products,"P")
        self.products[pid]={"name":text("Name: "),"category":text("Category: "),
            "buying_price":number("Buying price: "),"selling_price":number("Selling price: "),
            "quantity":integer("Quantity: "),"unit":text("Unit/type: "),"low_stock_limit":5}
        self.save(); print("Added:",pid)
    def display(self, products=None):
        products=self.products if products is None else products
        if not products: print("No products."); return
        print(f"{'ID':<7}{'Name':<22}{'Category':<15}{'Qty':>6}{'Sell':>10}")
        print("-"*60)
        for pid,p in products.items():
            print(f"{pid:<7}{p['name'][:21]:<22}{p['category'][:14]:<15}{p['quantity']:>6}{p['selling_price']:>10.2f}")
    def search(self):
        q=text("Search ID/name/category: ").lower()
        found={k:v for k,v in self.products.items() if q in k.lower() or q in v['name'].lower() or q in v['category'].lower()}
        self.display(found)
    def edit(self):
        pid=text("Product ID: ").upper()
        if pid not in self.products: print("Not found."); return
        p=self.products[pid]
        p['name']=input(f"Name [{p['name']}]: ").strip() or p['name']
        p['category']=input(f"Category [{p['category']}]: ").strip() or p['category']
        x=input(f"Buying price [{p['buying_price']}]: ").strip(); p['buying_price']=float(x) if x else p['buying_price']
        x=input(f"Selling price [{p['selling_price']}]: ").strip(); p['selling_price']=float(x) if x else p['selling_price']
        p['unit']=input(f"Unit [{p['unit']}]: ").strip() or p['unit']
        self.save(); print("Updated.")
    def delete(self):
        pid=text("Product ID: ").upper()
        if pid not in self.products: print("Not found."); return
        if input("Confirm delete (y/n): ").lower()=="y": del self.products[pid]; self.save(); print("Deleted.")
    def stock(self):
        pid=text("Product ID: ").upper()
        if pid not in self.products: print("Not found."); return
        self.products[pid]['quantity']=integer("New quantity: "); self.save(); print("Stock updated.")
    def decrease(self,pid,qty):
        if pid not in self.products: raise ValueError("Product not found")
        if qty>self.products[pid]['quantity']: raise ValueError("Insufficient stock")
        self.products[pid]['quantity']-=qty; self.save()
    def low_stock(self):
        self.display({k:v for k,v in self.products.items() if v['quantity']<=v.get('low_stock_limit',5)})
