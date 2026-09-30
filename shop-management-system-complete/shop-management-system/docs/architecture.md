# Architecture and Design

```text
                    main.py
                 CLI / Menus
                      |
       +--------------+--------------+
       |       |       |      |      |
   Inventory Billing Customer Warranty Reports
       |       |       |      |      |
       +-------+-------+------+------+
                      |
                  storage.py
                      |
                   JSON/data

validators.py supports validated user input.
```

## Billing workflow
```text
Start -> Select products -> Enter quantity -> Validate stock
      -> Calculate subtotal/total -> Validate payment/customer
      -> Deduct stock -> Save bill -> Display bill -> End
```

## Non-functional requirements
- Usability: menu-driven CLI
- Reliability: validation and checks for stock/customer data
- Maintainability: separate modules
- Portability: Python standard library
- Persistence: JSON files
- Resource efficiency: local file storage
