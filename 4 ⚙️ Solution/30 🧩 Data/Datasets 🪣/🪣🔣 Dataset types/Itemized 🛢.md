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

    |Dataset|Key|Col2|Col3 | Usage
    |-|-|-|-|-
    |Customers|ID|City   |     | `$o.Customer.City`
    |Orders|ID| Date |     | `$o.Date`
    |OrderLines|ID|OrderID | ItemID | `.len($o.Lines)`
    |Items|ID|Name            || `$o.Items`

    ```yaml
    # Bs.yaml
    
    Key: B-id

    Parents:
        # For each B, link the A with the same A-id
        MyA: As|A-id   
    
    Children:
        # For each B, link Cs with the same B-id
        MyCs: Cs|B-id        
        # For each MyC, link Ds with the same D-id
        MyDs: .MyCs|Ds|D-id  
    ```

    ---
    <br/>
   
1. **What are use cases of itemized schemas?**

    | Example | Feature
    |---------|--------
    | 🪣 [`Vaults@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Vaults.md>) | With a named key
    | 🪣 [`Binds@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Binds.md>) | With parents
    | 🪣 [`Vaults@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Vaults.md>) | With children
    | 🪣 [`Wallets@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/🤵🪣 Wallets.md>) | With grand children
    

    ---
    <br/>