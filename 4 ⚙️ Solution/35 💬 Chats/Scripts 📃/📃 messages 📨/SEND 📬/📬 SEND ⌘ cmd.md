# 😃📬 Talker `SEND` command

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

<br/>


1. **What is a SEND command?**

    A `SEND`
    * is a [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that sends a [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>).

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
    | `$context` | Optional input [Holder 🧠](<../../📃 basics/Holder 🧠.md>)  | `$p`
    | `To` | Destination domain | `any-broker.dom`
    | `Subject` | Message subject | `Unbound@Vault`
    | `{body}` | `Body` property dictionary  | `{A:1, B:2}`
    | `$response` | Response [Holder 🧠](<../../📃 basics/Holder 🧠.md>) <br/> for [Synchronous Requests 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Requests 🚀.md>) | `$r`

    ---
    <br/>


1. **What's an example of SEND?**

    Consider the following a [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>).

    ```yaml
    - SEND:
        Header:
            To: any-domain.dom
            Subject: Any@Role
        Body:
            A: 1
            B: 2
    ```

    This results in the following [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) being sent.

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

    Here's a [Script 📃](<../../📃 basics/Script 📃.md>)
    ```yaml
    📃 Example:
    
    # Create a holder
    - EVAL|{A:1,B:2} >> $context

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
    Commands: [`EVAL`](<../../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>)

    ---
    <br/>