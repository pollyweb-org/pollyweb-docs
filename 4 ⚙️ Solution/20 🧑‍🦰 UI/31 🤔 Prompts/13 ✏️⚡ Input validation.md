> Part of [✏️ Input prompts](<11 ✏️ Input behavior.md>)


1. **How to implement client-side validations?**

    Enter one or more client-side restrictions, when supported.
    
    |Restriction| Type |  Details
    |-|-|-
    | `MinLength` | int | Optional minimum length
    | `MaxLength` | int | Optional maximum length
    | `MinValue` | int | Optional minimum value
    | `MaxValue` | int | Optional maximum value
    |


    On a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>):

    ```yaml
    INT|Enter a 6-digit code >> $code:
        MinLength: 6
        MaxLength: 6
    ```
    
    On the [Prompted@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method:

    ```yaml
    Format: INT
    Message: Enter a 6-digit code
    MinLength: 6
    MaxLength: 6
    ```

    ---
    <br/>

1. **How to implement server-side validations?**

    Consider the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) as an example.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? [-]<br/>> This is a 6 digit number | `0123`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ Enter a 6 digit number
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? [+]<br/> | `012345`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code validated!

    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) would be.

    ```yaml
    💬 Form:
    - RUN|get-code
    - RUN|get-something-else

    get-code:
    - INT|What's the code? >> $code:
        Details: This is a 6 digit number
    - IF|{invalid($code)}|failure-proc

    failure-proc:
    - FAILURE|Enter a 6 digit number
    - RUN|get-code
    ```

    ---
    <br>
