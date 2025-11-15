# Item 🛢 Parents

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **Whats the syntax with a parent dataset?**

    ```yaml
    # With parents
    Table: <name>

    Parents:

        # Parent mapped by property matching
        <alias-1>: 
            <parent>.<key1>: <name>.<link1>
            <parent>.<keyN>: <name>.<linkN>
    
        # Parent mapped by the parent of a parent
        <alias-x>:
            <alias-1>.<elder>
    ```

    |Input|Details|Example
    |-|-|-
    | `<alias>` | New parent property  | `CUSTOMER`
    | `<parent>` | Parent dataset  | `CUSTOMERS`
    | `<key>`  | Matching parent field | `ID`
    | `<link>` | Matching child field | `CUST_ID`
    | `<elder>` | Direct grand parent    | `CITY` 

    ---
    <br/>

1. **Whats an example of a parent dataset?**

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS

    Parents:
        
        # Parent mapped by matching fields
        CUSTOMER: 
            CUSTOMERS.ID: ORDERS.CUST_ID

        # Direct grandparent reference,
        #  assuming that CITY is a also a parent
        CITY:
            CUSTOMER.CITY
    ```
    
    ---
    <br/>    


