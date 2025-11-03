# Item 🛢 Distincts

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **Whats the syntax for child distincts?**    

    ```yaml
    # With distincts
    Table: <name>
    Children:
        <child>: 
            <child-set>.<link>: <name>.<key>
    Distincts:
        <distinct>: <child>.<property>
    ```

    |Input|Details|Example
    |-|-|-
    | `<grand-alias>`  | Added property  | `Category`
    | `<grand-set>`  | Grand-children  | `Categories`
    |

    Here's an example.
    
    ```yaml
    # Example
    Table: ORDERS

    Children:
        LINES: 
            ORDER_LINES.ORDER_ID: ORDERS.ID

    Distincts:
        PRODUCTS: LINES.PROD_ID
    ```

    ---
    <br/>