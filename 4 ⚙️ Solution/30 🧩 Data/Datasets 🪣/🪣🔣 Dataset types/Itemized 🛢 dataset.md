# 🛢🪣 Itemized datasets

> Flow
* Part of [Dataset 🪣](<../🪣 Dataset.md>)

> Implementation
* Implemented by the [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢 Itemizer helper/🛢🤲 Itemizer helper.md>)
    * with the [`Build@Itemizer` 🐌 msg](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>).


## FAQ

1. **What is an Itemized dataset?**

    It's a [Dataset 🪣](<../🪣 Dataset.md>) managed by an [Itemizer 🛢 helper domain](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢 Itemizer helper/🛢🤲 Itemizer helper.md>).

    ---
    <br/>

1. **How to use an Itemized dataset?**

    [Message 📨](<../../Messages 📨/📨 Message/📨 Message.md>) | [Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-|-
    |[`Read@Itemizer`](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Item Read 👥🚀🛢/🛢 Read 🚀 call.md>)|[`READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)  | Retrieves an item
    |[`Save@Itemizer`](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Item Save 👥🚀🛢/🛢 Save 🚀 call.md>)|[`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)   | Inserts or updates an item
    |[`Delete@Itemizer`](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)|[`DELETE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) | Deletes an item
    
    ---
    <br/>


1. **What are use cases of itemized dataset?**

    | Example | Feature
    |---------|--------
    | 🪣 [`Notifiers`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers 📣 table/🪣 Notifiers/🤵 Broker.Notifiers 🪣 table.md>)  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | With a named key
    | 🪣 [`Binds`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | With parents
    | 🪣 [`Notifiers`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Notifiers 📣 table/🪣 Notifiers/🤵 Broker.Notifiers 🪣 table.md>) at  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | With children
    | 🪣 [`Wallets`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) at  at [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | With grand children
    

    ---
    <br/>

1. **What properties are available?**

    | Property| Type|  Purpose | Example
    |-|-|-|-
    | `Prefix` |text| Prefixes all mentioned table names | `Broker`
    | `Table`   |text| Name for table, without the prefix | `T` `Wallets`
    | `Item` | text | Name for item, without the prefix | `I` `Wallet`
    | `Expands` | text | Table alias to extend | `T` `Wallets`
    | [`Keys`](<../🪣🛢 Itemized datasets/Item 🛢 Keys.md>)     | list | Properties that compose the key | `k` `k1,k2`
    | [`Parents`](<../🪣🛢 Itemized datasets/Item 🛢 Parents.md>) | dict | Parent relationships | `P:{P.k:T.p}`
    | [`Propagate`](<../🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) | list | Name of parents to auto-create | `P` `P,Q`
    | [`Children`](<../🪣🛢 Itemized datasets/Item 🛢 Children.md>)| dict | Child relationships | `Cs:{C.p:T.k}`
    | [`Cascade`](<../🪣🛢 Itemized datasets/Item 🛢 Cascade.md>) | list | Name of children to auto-delete | `Cs` `Cs,Ds`
    | [`Views`](<../🪣🛢 Itemized datasets/Item 🛢 Views.md>) | dict | Filtered children | `Vs:Cs:[p=3]`
    | [`Distincts`](<../🪣🛢 Itemized datasets/Item 🛢 Distincts.md>) | dict | Unique values in child properties | `Ds:Cs.d`
    | [`Handlers`](<../🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) | dict | [Scripts 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to run on events | `{...}`
    | [`State`](<../🪣🛢 Itemized datasets/Item 🛢 State.md>) | dict | Defines handlers for states | `{...}`
    | [`Assert`](<../🪣🛢 Itemized datasets/Item 🛢 Assert.md>) | dict | [`.Assert`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) lifecycle conditions | `{...}`
    
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
    Table: ORDERS_2
    Extends: ORDERS 
    Item: ORDER
    Key: ID

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
        # Filter out the recent orders
        RECENT:
            DATE.IsIn(.Last(30 days))
        
    Distincts:
        # Group the product IDs
        # Usage: $order.Products[0]
        PRODUCTS: LINES.PROD_ID

    Handlers:
        # Handlers these OnX scripts
        OnChange: 
            Events: ALTERED
        OnSomeState:
            Events: UPDATED
            Assert: 
                Item.Expires.IsFuture:
                New.STATE: NEW_STATE
                Old.STATE: OLD_STATE
    ```
    
    Uses||
    |-|-
    |[{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.Last`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Last ⓕ.md>) [`.IsFuture`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>)

    ---
    <br/>
   
