# 🛢🪣 Itemized datasets

> Flow
* Part of [Dataset 🪣](<../🪣 Dataset.md>)

> Implementation
* Implemented by the [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🤲 Itemizer helper.md>)
    * with the [`Build@Itemizer` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>).

<br/>

## FAQ

1. **What is an Itemized dataset?**

    It's a [Dataset 🪣](<../🪣 Dataset.md>) managed by an [Itemizer 🛢 helper domain](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🤲 Itemizer helper.md>).

    ---
    <br/>

1. **What are use cases of itemized dataset?**

    | Example | Feature
    |---------|--------
    | 🪣 [`Notifiers`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers 📣 table/🤵 BrokerNotifiers 🪣 table.md>)  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | With a named key
    | 🪣 [`Binds`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Binds 🔗 table/🤵 BrokerBinds 🪣 table.md>) at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | With parents
    | 🪣 [`Notifiers`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers 📣 table/🤵 BrokerNotifiers 🪣 table.md>) at  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | With children
    | 🪣 [`Wallets`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) at  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | With grand children
    

    ---
    <br/>

1. **What properties are available?**

    | Property| Type|  Purpose | Example
    |-|-|-|-
    | `Prefix` | string | Prefixes all mentioned table names | `Broker`
    | `Table`   | string | Name for table, without the prefix | `T` `Wallets`
    | [`Keys`](<../🪣🛢 Itemized datasets/Item 🛢 Keys.md>)     | list | Properties that compose the key | `k` `k1,k2`
    | [`Parents`](<../🪣🛢 Itemized datasets/Item 🛢 Parents.md>) | map | Parent relationships | `P:{P.k:T.p}`
    | [`Propagate`](<../🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) | list | Name of parents to auto-create | `P` `P,Q`
    | [`Children`](<../🪣🛢 Itemized datasets/Item 🛢 Children.md>)| map | Child relationships | `Cs:{C.p:T.k}`
    | [`Views`](<../🪣🛢 Itemized datasets/Item 🛢 Views.md>) | map | Filtered children | `Vs:Cs:[p=3]`
    | [`Distincts`](<../🪣🛢 Itemized datasets/Item 🛢 Views.md>) | map | Unique values in child properties | `Ds:Cs.d`
    | [`NoUpdates`](<../🪣🛢 Itemized datasets/Item 🛢 NoUpdates.md>) | bool | Only allows inserts and deletes | `True`
    | [`Triggers`](<../🪣🛢 Itemized datasets/Item 🛢 Triggers.md>) | map | [Scripts 📃](<../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) to run on triggers | `S:EXPIRED`
    
    ---
    <br/>



1. **What's an example of an itemized schema?**

    |Dataset 🪣|Key | Data |Link 🪣|Link 🪣  | Usage
    |-|-|-|-|-|-
    |`CUSTOMERS`|ID|CITY   |   |  | `$o.CUSTOMER.CITY`
    |`ORDERS`|ID| DATE |CUST_ID |    | `$o.DATE`
    |`ORDER_LINES`|ID|QTT|ORDER_ID | PROD_ID | `$o.LINES[0].QTT`

    ```yaml
    # FULFILLMENT_ORDERS

    Prefix: FULFILLMENT_
    Table: ORDERS
    Key: ID

    # Block changes once saved
    NoUpdates: True

    Parents:
        # For each Order, link the Customer
        # Usage: $o.Customer.City
        CUSTOMER:
            CUSTOMERS.ID: ORDERS.CUST_ID
    
    Children:
        # For each Order, link the Lines
        # Usage: $order.Lines[0].Qtt
        LINES: 
            ORDER_LINES.ORDER_ID: ORDERS.ID

    Views:
        # Filter out the return lines
        RETURNS:
            LINES:
                - QTT < 0
        
    Distincts:
        # Group the product IDs
        # Usage: $order.Products[0]
        PRODUCTS: LINES.PROD_ID

    Triggers:
        # Triggers these OnX scripts
        OnTimeout: EXPIRED, PURGED
        OnChange: ADDED, CHANGED, DELETED
    ```

    ---
    <br/>
   
