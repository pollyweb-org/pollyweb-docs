# 🛢🪣 Itemized datasets

> Part of [Dataset 🪣](<../🪣 Dataset.md>)

> Implemented by the [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🤲 Itemizer helper.md>)
 with [`Build@Itemizer`](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Tables/👥🐌🛢 Build.md>) 

<br/>

1. **What is an Itemized dataset?**

    It's a [Dataset 🪣](<../🪣 Dataset.md>) managed by an [Itemizer 🛢 helper domain](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🤲 Itemizer helper.md>).

    ---
    <br/>

1. **What are use cases of itemized dataset?**

    | Example | Feature
    |---------|--------
    | 🪣 [`Notifiers`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Notifiers table.md>)  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | With a named key
    | 🪣 [`Binds`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Binds table.md>) at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | With parents
    | 🪣 [`Notifiers`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Notifiers table.md>) at  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | With children
    | 🪣 [`Wallets`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Wallets table.md>) at  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | With grand children
    

    ---
    <br/>


1. **What's the simplest syntax for itemized schemas?**

    ```yaml
    # First column is the key.
    # No parents, children, or distincts.
    Table: <name>
    ```

    |Argument|Details|Example
    |-|-|-
    | `<name>` | Dataset name | `ORDERS`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    ```

    ---
    <br/>

1. **Whats the syntax for complex keys?**

    ```yaml
    # Complex keys
    Table: <name>
    Key: <k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    |`<k1>[,<kN>]`  | Key combination | `ID` `COL1,COL2`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    Key: ID
    ```


    ---
    <br/>    

1. **Whats the syntax with a parent dataset?**

    ```yaml
    # With parents
    Table: <name>

    Parents:
        <alias>: 
            <parent>.<key1>: <name>.<link1>
            <parent>.<keyN>: <name>.<linkN>
    ```

    |Argument|Details|Example
    |-|-|-
    | `<alias>` | New parent property  | `CUSTOMER`
    | `<parent>` | Parent dataset  | `CUSTOMERS`
    | `<key>`  | Matching parent field | `ID`
    | `<link>` | Matching child field | `CUST_ID`
    |

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

1. **Whats the syntax with a child dataset?**    
    
    ```yaml
    # With children
    Table: <name>

    Children:
        <alias>: 
            <child>.<link1>: <name>.<key1>
            <child>.<linkN>: <name>.<keyN>
    ```

    |Argument|Details|Example
    |-|-|-
    | `<alias>`  | Added property  | `LINES`
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

1. **Whats the syntax with distincts?**    

    ```yaml
    # With distincts
    Table: <name>
    Children:
        <child>: 
            <child-set>.<link>: <name>.<key>
    Distincts:
        <distinct>: <child>.<property>
    ```

    |Argument|Details|Example
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

1. **What's an example of an itemized schema?**

    |Dataset 🪣|Key | Data |Link 🪣|Link 🪣  | Usage
    |-|-|-|-|-|-
    |`CUSTOMERS`|ID|CITY   |   |  | `$o.CUSTOMER.CITY`
    |`ORDERS`|ID| DATE |CUST_ID |    | `$o.DATE`
    |`ORDER_LINES`|ID|QTT|ORDER_ID | PROD_ID | `$o.LINES[0].QTT`

    ```yaml
    Table: ORDERS
    Key: ID

    Parents:
        # For each Order, link the Customer
        # Usage: $o.Customer.City
        CUSTOMER:
            CUSTOMERS.ID: ORDERS.CUST_ID
    
    Children:
        # For each Order, link the Lines
        # Usage: $o.Lines[0].Qtt
        LINES: 
            ORDER_LINES.ORDER_ID: ORDERS.ID
        
    Distincts:
        # Group the product IDs
        # Usage: $o.Products[0]
        PRODUCTS: LINES.PROD_ID
    ```

    ---
    <br/>
   
1. **How to block updates?**

    Here's the table definition.

    ```yaml
    NoUpdates: True  # it's False by default
    ```

    Here's a [Talker 😃](<../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>) excerpt from [`Grab@Printer`](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Grab.md>)

    ```yaml
    SAVE|AnyTable:
        OnBlocked: REEL|409
    ```

    |Action|Condition|Behavior
    |-|-|-
    | 💾 [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) | Same value | Allows multiple  idempotent saves
    | |Different | Blocked, raises an error
    | 🗑️ [`DELETE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/DELETE/DELETE 🗑️ item.md>) | - | Allows multiple idempotent times

    ---
    <br/>


1. **How to work with triggers?**

    Triggers 
    * are set on the [`Build@Itemized` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Tables/👥🐌🛢 Build.md>)
    * and are consumed by the [`Triggered@Talker` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🔔 Itemizer events/🛢🔔 Triggered.md>)

    ---
    <br/>



1. **What are the possible triggers?**
    
    |Value|Description|
    |-|-|
    | `ADDED`   | Item inserted on the [Itemized 🛢 dataset](<../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) on a [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>)
    | `CHANGED` | The content of the item has changed on a [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>)
    | `EXPIRED` | Item removed automatically due to a [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE/SAVE 💾 item.md>) expiration
    | `DELETED` | Item deleted on a [`DELETE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/DELETE/DELETE 🗑️ item.md>), either soft or hard
    | `PURGED`  | Item removed automatically due to an [`UNDO`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/UNDO/UNDO ↩️.md>) timeout
    |

1. **How to register a Trigger?**

    ```yaml
    Table: <name>
    Triggers:
        <handler>: <trigger-list>
    ```

    |Argument|Details|Example
    |-|-|-
    | `<handler>` | Name of the [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/Script 📃.md>) to handle | `MyHandler`
    | `<trigger-list>` | Triggers to handle | `ADDED,PURGED`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    Triggers: 
        OnTimeout: EXPIRED, PURGED
        OnChange: ADDED, CHANGED, DELETED
    ```

    ---
    <br/>