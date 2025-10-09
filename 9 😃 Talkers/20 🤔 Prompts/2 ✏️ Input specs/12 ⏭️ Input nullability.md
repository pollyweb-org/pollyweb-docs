# ⏭️ Input nullability

> Part of [✏️ Input prompts](<../1 📘 Prompt specs/09 ✏️ as Input.md>)

<br/>


1. **How to define a mandatory input?**

    Inputs are mandatory by default.

    ---
    <br/>

1. **Can users reject a mandatory input prompt?**

    No. Like in a conversation between two persons, 
    * users can only stay silent 
    * or [abandon the conversation 👉](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>).

    ---
    <br/>


1. **What does a mandatory input look like?**

    Here's a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/2 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ Required input.
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | `0123`
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Your code is `0123`
    |

    <br/>
    
    Here's the [Talker 😃](<../../10 📘 Talker specs/1 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - DIGITS|What's the code? >> $code
    - SUCCESS|Your code is `{$code}`
    ```
    
    ---
    <br/>



1. **How to define optional inputs?**

    [Input prompts ✏️](<../1 📘 Prompt specs/09 ✏️ as Input.md>) 
    * can be made optional 
    * by setting the property `Nullable` to `True` or `Yes`.
    
    ---
    <br/>



1. **What does an optional input look like?**

    Here's a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/2 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ You didn't provide a code.
    |

    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/1 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - DIGITS|What's the code? >> $code:
        Nullable: True
    - IF|$code:
        Then: SUCCESS|Your code is `{$code}`
        Else: SUCCESS|You didn't provide a code.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: DIGITS
    Statement: 😃 What's the code?
    ```

    ---
    <br/>
