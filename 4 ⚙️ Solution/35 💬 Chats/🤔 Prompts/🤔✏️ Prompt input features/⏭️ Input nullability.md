# ⏭️ Input nullability

> Part of [✏️ Input prompts](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

<br/>


1. **How to define a mandatory input?**

    Inputs are mandatory by default.

    ---
    <br/>

1. **Can users reject a mandatory input prompt?**

    No. Like in a conversation between two persons, 
    * users can only stay silent 
    * or [abandon the conversation 👉](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Chats 💬/💬🤵 Abandon 💬.md>).

    ---
    <br/>


1. **What does a mandatory input look like?**

    Here's a [Chat 💬](<../../💬 Chats/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ❌ Required input.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the code? | `0123`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Your code is `0123`
    |

    <br/>
    
    Here's the [Script 📃](<../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    # 😃 Talker
    - DIGITS|What's the code? >> $code
    - SUCCESS|Your code is `{$code}`
    ```
    
    ---
    <br/>



1. **How to define optional inputs?**

    [Input prompts ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) 
    * can be made optional 
    * by setting the property `Nullable` to `True` or `Yes`.
    
    ---
    <br/>



1. **What does an optional input look like?**

    Here's a [Chat 💬](<../../💬 Chats/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the code? | ` `
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ You didn't provide a code.
    |

    <br/>

    Here's the [Script 📃](<../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    # 😃 Talker
    - DIGITS|What's the code? >> $code:
        Nullable: True
    - IF|$code:
        Then: SUCCESS|Your code is `{$code}`
        Else: SUCCESS|You didn't provide a code.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: DIGITS
    Emoji: 😃 
    Text: What's the code?
    ```

    ---
    <br/>
