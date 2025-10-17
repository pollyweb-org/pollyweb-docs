<!-- TODO -->

# 🛢🪣 Itemized datasets

> Relates to [🛢🤲 Itemizer helper](<../../../45 🤲 Helper domains/Itemizer 🛢/🛢🤲 Itemizer helper.md>)

<br/>

1. **Whats the syntax for itemized schemas?**

    ```yaml
    # <table-name>.yaml

    Key: <property-1> [,<property-n>]

    Parents:
        <alias-1>: <property-1> >> <parent-table-1>
        <alias-n>: <property-n> >> <parent-table-n> 
        
    Children:
        <child-table-1>: <property-in-child-1>
        <child-table-n>: <property-in-child-n>
        <grand-children-x>: <my-child-x>.<their-child-z>
    ```
    
    ---
    <br/>

1. **What's an example of an itemized schema?**

    ```yaml
    # MyTable.yaml

    Key: MyID

    Parents:
        ParentA: MyParentAID >> ParentATable
        ParentB: MyParentBID >> ParentBTable
        
    Children:
        ChildA: MyIDInChildA
        ChildB: MyIDInChildB
        GrandChildrenX: ChildA.TheirChildX
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