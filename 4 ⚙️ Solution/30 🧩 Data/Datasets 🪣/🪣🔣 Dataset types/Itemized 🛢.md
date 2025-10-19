<!-- TODO -->

# 🛢🪣 Itemized datasets

> Relates to [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>)

<br/>

1. **Whats the simplest syntax for itemized schemas?**

    ```yaml
    # No parents nor children
    Name: <name>
    Key: <k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<name>` | Dataset name | `Orders`
    |`<k1>[,<kN>]`  | Key combination | `Col1` `Col1,Col2`

    ---
    <br/>    

1. **Whats the syntax with a parent dataset?**

    ```yaml
    # With parents
    Name: <name>
    Key: <k1>[,<kN>]
    Parents:
        <parent-alias>: <parent-set>|<k2>[,<kZ>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<parent-alias>` | Added property  | `Customer`
    | `<parent-set>` | Parent dataset  | `AllCustomers`
    | `<k2>[,<kZ>]`  | Matching child | `CustomerID`
    
    ---
    <br/>    

1. **Whats the syntax with a child dataset?**    
    
    ```yaml
    # With children
    Name: <name>
    Key: <k1>[,<kN>]
    Children:
        <child-alias>: <child-set>|<k2>[,<kZ>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<child-alias>`  | Added property  | `Items`
    | `<child-set>`  | Child dataset  | `AllItems`
    | `<k2>[,<kZ>]`  | Matching child | `OrderID`

    ---
    <br/>

1. **Whats the syntax with a grand-children?**    

    ```yaml
    # With grand-children
    Name: <name>
    Key: <k1>[,<kN>]
    Children:
        <child-alias>: <child-set>|<k1>[,<kN>]
        <grand-alias>: .<child-alias>|<grand-set>|<k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<grand-alias>`  | Added property  | `Category`
    | `<grand-set>`  | Grand-children  | `Categories`
    
    ---
    <br/>

1. **What's an example of an itemized schema?**

    |Dataset 🪣|Key | Data |Link 🪣|Link 🪣  | Usage
    |-|-|-|-|-|-
    |`Orders`|ID| Date |CustID |    | `$o.Date`
    |`Customers`|ID|City   |   |  | `$o.Customer.City`
    |`OrderLines`|ID|Qtt|OrderID | ItemID | `$o.Lines[0].Qtt`
    |`Catalog`|ID|Name    |        || `$o.Items[0].Name`

    ```yaml
    Name: Orders
    Key: ID

    Parents:

        # For each Order, link the Customer
        # Usage: $o.Customer.City
        Customer: Customers|CustID
    
    Children:

        # For each Order, link the Lines
        # Usage: $o.Lines[0].Qtt
        Lines: OrderLines|OrderID
        
        # For each Line, link the Item
        # Usage: $o.Items[0].Name
        Items: .Lines|Catalog|ItemID
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