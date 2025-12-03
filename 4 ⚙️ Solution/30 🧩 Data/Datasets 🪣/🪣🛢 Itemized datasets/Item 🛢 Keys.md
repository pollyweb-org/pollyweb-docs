# Item 🛢 Keys

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ


1. **How to set an automatic key?**

    ```yaml
    # Syntax for automatic ID
    Table: <name>
    ```

    |Input|Details|Example
    |-|-|-
    | `Table` | Dataset name | `ORDERS`

    ---
    <br/>


1. **How to save and read an item with an automatic key?**

    ```yaml
    # Schema
    Table: ORDERS
    ```

    Here's how to save and read an order item using an automatic ID.

    ```js
    ┌────────────────────────┐   ┌───────────────────┐ 
    │ Save without key       │   │ Read with auto ID │
    ├────────────────────────┤   ├───────────────────┤
    │ SAVE|ORDERS >> $order: │   │ READ >> $order2:  │
    │   DATE: .Today         │   │   Set: ORDERS     │
    │                        │   │   Key: $order.ID  │
    └────────────────────────┘   └───────────────────┘    
    ```
    Uses: [`READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`.Today`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Today ⓕ.md>)

    ---
    <br/>



1. **How to set a simple unique key?**

    ```yaml
    # Syntax for unique keys
    Table: <name>
    Key: <key>
    ```

    |Input|Details|Example
    |-|-|-
    | `Table` | Dataset name | `COUNTRY`
    | `Key` | Property name | `NAME`

    ---
    <br/>


1. **How to save and read an item with an automatic key?**

    ```yaml
    # Schema
    Table: COUNTRIES
    Key: NAME       
    ```

    Here's the [`SAVE` command](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>).


    ```js
    ┌─────────────────────────────┐   
    │ Save with unique key        │ 
    ├─────────────────────────────┤
    │ SAVE|COUNTRIES >> $country: │   
    │   NAME: Switzerland         │ 
    └─────────────────────────────┘   
    ```
    
    Here's the [`READ` command](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) 

    ```js
    ┌────────────────────┬────────────────────┐
    │ Read by unique key │ READ by auto ID    │ 
    ├────────────────────┼────────────────────┤
    │ READ >> $country2: │ READ >> $country2: │ 
    │   Set: COUNTRIES   │   Set: COUNTRIES   │
    │   Key: Switzerland │   Key: $country.ID │ 
    └────────────────────┴────────────────────┘    
    ```

    ---
    <br/>

1. **Whats the syntax for complex keys?**

    ```yaml
    # Syntax for complex keys
    Table: <name>
    Key: <k1>[,<kN>]
    ```

    |Input|Details|Example
    |-|-|-
    |`<k1>[,<kN>]`  | Key combination | `ID` `COL1,COL2`
    |

    ---
    <br/>    
    
1. **How to read an item with a complex key?**

    ```yaml
    # Schema
    Table: ORDER_LINES
    Key: ORDER_ID, LINE_NUMBER
    ```

    Here's the [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) command.

    ```js
    ┌───────────────────────────┐
    │ SAVE.                     │ 
    ├───────────────────────────┤
    │ SAVE|ORDER_LINES >> $line │
    │   ORDER_ID: $order.ID     │ 
    │   LINE_NUMBER: 123        │ 
    └───────────────────────────┘    
    ```

    Here's the [`READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) command.

    ```js
    ┌─────────────────────────┬────────────────────┐
    │ Ready with complex key  │ Read with auto ID  │ 
    ├─────────────────────────┼────────────────────┤
    │ READ >> $line2:         │ READ >> $line2:    │ 
    │   Set: ORDER_LINES      │   Set: ORDER_LINES │
    │   Key:                  │   Key: $line.ID    │ 
    │     ORDER_ID: $order.ID │                    │ 
    │     LINE_NUMBER: 123    │                    │ 
    └─────────────────────────┴────────────────────┘    
    ```
    
    ---
    <br/>