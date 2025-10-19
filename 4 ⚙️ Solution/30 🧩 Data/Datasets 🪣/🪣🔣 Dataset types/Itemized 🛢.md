<!-- TODO -->

# 🛢🪣 Itemized datasets

> Relates to [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>)

<br/>

1. **Whats the simplest syntax for itemized schemas?**

    ```yaml
    # First column is the key.
    # No parents, children, or distincts.
    Name: <name>
    ```

    |Argument|Details|Example
    |-|-|-
    | `<name>` | Dataset name | `ORDERS`
    |

    Here's an example.

    ```yaml
    # Example
    Name: ORDERS
    ```

    ---
    <br/>

1. **Whats the syntax for complex keys?**

    ```yaml
    # Complex keys
    Name: <name>
    Key: <k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    |`<k1>[,<kN>]`  | Key combination | `ID` `COL1,COL2`
    |

    Here's an example.

    ```yaml
    # Example
    Name: ORDERS
    Key: ID
    ```


    ---
    <br/>    

1. **Whats the syntax with a parent dataset?**

    ```yaml
    # With parents
    Name: <name>

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
    Name: ORDERS

    Parents:
        CUSTOMER: 
            CUSTOMERS.ID: ORDERS.CUST_ID
    ```
    
    ---
    <br/>    

1. **Whats the syntax with a child dataset?**    
    
    ```yaml
    # With children
    Name: <name>

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
    Name: ORDERS

    Children:
        LINES: 
            ORDER_LINES.ORDER_ID: ORDERS.ID
    ```

    ---
    <br/>

1. **Whats the syntax with distincts?**    

    ```yaml
    # With distincts
    Name: <name>
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
    Name: ORDERS

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
    Name: ORDERS
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
   


1. **What are use cases of itemized schemas?**

    | Example | Feature
    |---------|--------
    | 🪣 [`Notifiers@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Notifiers.md>) | With a named key
    | 🪣 [`Binds@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Binds.md>) | With parents
    | 🪣 [`Notifiers@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Notifiers.md>) | With children
    | 🪣 [`Wallets@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Wallets.md>) | With grand children
    

    ---
    <br/>