from inventory import Inventory
from billing import Billing
from customer import Customers
from warranty import Warranty
from reports import Reports

def menu(title,items):
    print(f"\n--- {title} ---")
    for k,v in items: print(f"{k}. {v}")
    return input("Choose: ").strip()

def main():
    inv=Inventory(); cust=Customers(); bill=Billing(inv,cust); war=Warranty(); rep=Reports(inv,bill,cust,war)
    while True:
        c=menu("SHOP INVENTORY & BILLING SYSTEM",[(1,"Inventory"),(2,"Billing"),(3,"Bill/Sales Records"),(4,"Customers & Khata"),(5,"Warranty"),(6,"Reports"),(0,"Exit")])
        if c=="0": break
        if c=="1":
            while True:
                x=menu("INVENTORY",[(1,"Add"),(2,"View"),(3,"Search"),(4,"Edit"),(5,"Delete"),(6,"Update stock"),(7,"Low stock"),(0,"Back")])
                if x=="0": break
                elif x=="1": inv.add()
                elif x=="2": inv.display()
                elif x=="3": inv.search()
                elif x=="4": inv.edit()
                elif x=="5": inv.delete()
                elif x=="6": inv.stock()
                elif x=="7": inv.low_stock()
        elif c=="2": bill.create()
        elif c=="3":
            while True:
                x=menu("SALES",[(1,"View bills"),(2,"Search bill"),(0,"Back")])
                if x=="0": break
                if x=="1": bill.bills_list()
                elif x=="2": bill.search()
        elif c=="4":
            while True:
                x=menu("CUSTOMERS & KHATA",[(1,"Add customer"),(2,"View"),(3,"Search"),(4,"Record payment"),(5,"Pending"),(0,"Back")])
                if x=="0": break
                if x=="1": cust.add()
                elif x=="2": cust.display()
                elif x=="3": cust.search()
                elif x=="4": cust.payment()
                elif x=="5": cust.pending()
        elif c=="5":
            while True:
                x=menu("WARRANTY",[(1,"Add"),(2,"View"),(3,"Search"),(4,"Expiring"),(0,"Back")])
                if x=="0": break
                if x=="1": war.add()
                elif x=="2": war.display()
                elif x=="3": war.search()
                elif x=="4": war.expiring()
        elif c=="6": rep.dashboard()

if __name__=="__main__": main()
