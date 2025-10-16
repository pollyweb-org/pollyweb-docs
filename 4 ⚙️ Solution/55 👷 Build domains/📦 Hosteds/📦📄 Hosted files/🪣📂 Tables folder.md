# 🪣📂 Tables folder

> Part of [Hosted 📦 domain](<../📦👥 Hosted domain.md>)

> Read with [`MAP` command](<../../../35 💬 Chats/😃 Talkers/😃💾 Talker data/61 🪣 MAP item.md>)

<br/>

1. **Whats the syntax for table files?**

    ```yaml
    # <table-name>.yaml
    Key: <property-1> [,<property-n>]
    Parents:
        <alias-1>: <property-1> > <parent-table-1>
        <alias-n>: <property-n> > <parent-table-n> 
    Children:
        <child-table-1>: <property-in-child-1>
        <child-table-n>: <property-in-child-n>
        <grand-children-x>: <my-child-x>.<their-child-z>
    ```
    
    ---
    <br/>

1. **What's an example of a table file?**

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
   
1. **What are use cases of table files?**

    | Example | Feature
    |---------|--------
    | 🪣 [`Vaults@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🪣 Broker tables/Vaults 🪣.md>) | With a named key
    | 🪣 [`Binds@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🪣 Broker tables/Binds 🪣.md>) | With parents
    | 🪣 [`Vaults@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🪣 Broker tables/Vaults 🪣.md>) | With children
    | 🪣 [`Wallets@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🪣 Broker tables/Wallets 🪣.md>) | With grand children
    

    ---
    <br/>