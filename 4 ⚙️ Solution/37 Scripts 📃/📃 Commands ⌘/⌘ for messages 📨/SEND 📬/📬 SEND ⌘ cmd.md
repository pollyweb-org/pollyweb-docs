# 😃📬 Talker `SEND` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **What is a SEND command?**

    A `SEND`
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that sends a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).

    ---
    <br/>


1. **What's the SEND syntax?**

    ```yaml
    SEND|$context >> $response:
        Header:
            To: <domain>
            Subject: <subject>
        Body:
            {body}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `$context` | Optional input [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)  | `$p`
    |`To`| Destination domain | `any-broker.dom`
    |    | Defaults to [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)`.Domain`
    | `Subject` | Message subject | `Unbound@Vault`
    | `{body}` | `Body` property dictionary  | `{A:1, B:2}`
    | `$response` | Response [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) <br/> for [Synchronous Calls 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Calls 🚀.md>) | `$r`

    ---
    <br/>


1. **What's an example of SEND?**

    Consider the following [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    - SEND:
        Header:
            To: any-domain.dom
            Subject: Any@Role
        Body:
            A: 1
            B: 2
    ```

    This results in the following [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) being sent.

    ```yaml
    Header:

        # Original Header properties
        To: any-domain.dom
        Subject: Any@Role

        # Added Header properties
        From: my-domain.dom
        Timestamp: 2018-12-10T13:45:00.000Z
        Correlation: 125a5c75-cb72-43d2-9695-37026dfcaa48
        DKIM: pk1

    Body:

        # Original Body properties
        A: 1
        B: 2

    # Added authentication stamp
    Hash: ee6ca2a43ec05d...
    Signature: Lw7sQp6zkOGyJ+OzGn+B...
    ```

    ---
    <br/>

1. **How to use the context?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
    ```yaml
    📃 Example:
    
    # Create a holder
    - PUT|{A:1,B:2} >> $context

    # Without context
    - SEND:
        Header:
            To: any-domain.dom
            Subject: Any@Subject
        Body:
            A: $context.A
            B: $context.B

    # With context
    - SEND|$context:
        Header:
            To: any-domain.dom
            Subject: Any@Subject
        Body:
            A: A
            B: B
    ```
    Uses: [`CALL`](<../../⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)

    ---
    <br/>

1. **Are the head and body really necessary?**

    No, they can be omitted. 
    * The properties `To` and `Subject` is assigned to the `Header`.
    * Every other property is assumed to belong to the `Body`.

    ```js
    ┌────────────────────────────┬────────────────────────┐
    │ Comprehensive              │ Simplified             │ ├────────────────────────────┼────────────────────────┤
    │ SEND >> $response:         │ SEND >> $response:     │
    │   Header:                  │   To: any-domain.dom   │
    │       To: any-domain.dom   │   Subject: Any@Subject │
    │       Subject: Any@Subject │   A: 1                 │
    │   Body:                    │   B: 2                 │
    │       A: 1                 │                        │
    │       B: 2                 │                        │
    └────────────────────────────┴────────────────────────┘
    ```
    ---
    <br/>
   
1. **How to send a request to it self?**

    Omit the `To` property.

    ```yaml
    SEND >> $response:
        Subject: Any@Role
        A: 1
        B: 2
    ```

    ---
    <br/>

1. **How does SEND behave with Itemizer items?**

    The `SEND` command does not expose [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) items directly.
    * If an item is returned, the default `$` is sent instead.
    * If an [Item 🛢 Child](<../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) is returned, the field value (typically a UUID) is sent.
    * If none of the above is available, an error is raised for security reasons.

    ---
    <br/>
