# Item 🛢 Children

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **Whats the syntax with a child dataset?**    
    
    ```yaml
    # With children
    Table: <name>

    Children:
        <alias>: 
            <child>.<link1>: <name>.<key1>
            <child>.<linkN>: <name>.<keyN>
    ```

    |Input|Details|Example
    |-|-|-
    | `<alias>`  | Relationship name  | `LINES`
    | `<child>`  | Child dataset  | `ORDER_LINES`
    | `<link>` | Matching child field | `ORDER_ID`
    | `<key>`  | Matching parent field | `ID`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS

    Children:
        LINES: 
            ORDER_LINES.ORDER_ID: ORDERS.ID
    ```

    ---
    <br/>


