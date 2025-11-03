# Item 🛢 Parents

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **Whats the syntax with a parent dataset?**

    ```yaml
    # With parents
    Table: <name>

    Parents:
        <alias>: 
            <parent>.<key1>: <name>.<link1>
            <parent>.<keyN>: <name>.<linkN>
    ```

    |Input|Details|Example
    |-|-|-
    | `<alias>` | New parent property  | `CUSTOMER`
    | `<parent>` | Parent dataset  | `CUSTOMERS`
    | `<key>`  | Matching parent field | `ID`
    | `<link>` | Matching child field | `CUST_ID`

    ---
    <br/>

1. **Whats an example of a parent dataset?**

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS

    Parents:
        CUSTOMER: 
            CUSTOMERS.ID: ORDERS.CUST_ID
    ```
    
    ---
    <br/>    


