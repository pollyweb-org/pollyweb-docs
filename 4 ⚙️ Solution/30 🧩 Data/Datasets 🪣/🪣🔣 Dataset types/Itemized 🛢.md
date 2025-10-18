<!-- TODO -->

# 🛢🪣 Itemized datasets

> Relates to [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>)

<br/>

1. **Whats the syntax for itemized schemas?**

    ```yaml
    # No parents nor children
    Key: <k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    |`<k1>[,<kN>]`  | Key combination | `Col1` `Col1,Col2`
    
    
    ```yaml
    # With parents
    Key: <k1>[,<kN>]
    Parents:
        <parent-alias>: <parent-table>|<k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<parent-alias>` | Added property  | `Customer`
    | `<parent-table>` | Parent table  | `AllCustomers`
    
    
    ```yaml
    # With children
    Key: <k1>[,<kN>]
    Children:
        <child-alias>: <child-table>|<k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<child-alias>`  | Added property  | `Items`
    | `<child-table>`  | Child table  | `AllItems`

    ```yaml
    # With grand-children
    Key: <k1>[,<kN>]
    Children:
        <child-alias>: <child-table>|<k1>[,<kN>]
        <grand-alias>: .<child-alias>|<grand-table>|<k1>[,<kN>]
    ```

    |Argument|Details|Example
    |-|-|-
    | `<grand-alias>`  | Added property  | `Category`
    | `<grand-table>`  | Grand-children table  | `AllCategories`
    
    ---
    <br/>

1. **What's an example of an itemized schema?**

    |Table|Key|Col2|Col3 | Usage
    |-|-|-|-|-
    |As|Aid|    | X      | `$b.MyA.X`
    |Bs|Bid|Aid | Y     | `$b.Y`
    |Cs|Cid|Bid | Did    | `$b.MyCs`
    |Ds|Did|            || `$b.MyDs`

    ```yaml
    # Bs.yaml
    Key: Bid
    Parents:
        MyA: As|Aid   
    Children:
        MyCs: Cs|Bid
        MyDs: .MyCs|Ds|Did
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