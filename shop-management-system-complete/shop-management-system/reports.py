class Reports:
    def __init__(self,inventory,billing,customers,warranty): self.i=inventory; self.b=billing; self.c=customers; self.w=warranty
    def dashboard(self):
        revenue,profit=self.b.totals(); units=sum(p['quantity'] for p in self.i.products.values()); low=sum(p['quantity']<=p.get('low_stock_limit',5) for p in self.i.products.values()); pending=sum(c['pending'] for c in self.c.data.values())
        print("\n--- DASHBOARD ---"); print("Products:",len(self.i.products)); print("Units:",units); print("Low stock:",low); print(f"Revenue: {revenue:.2f}"); print(f"Gross profit: {profit:.2f}"); print(f"Pending khata: {pending:.2f}"); print("Warranty records:",len(self.w.data))
