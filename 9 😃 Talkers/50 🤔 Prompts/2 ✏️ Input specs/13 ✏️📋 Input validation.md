# 📋 Input validation

> Part of [✏️ Input prompts](<../1 📘 Prompt specs/09 ✏️ Input behavior.md>)

<br/>


1. **How do client-side validations work?**

    NLWeb does not guarantee client-side validations.

    * It's close to impossible to enforce [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to comply with the rules across a large landscape of vendors and user interface (UI) technologies: 
        * e.g., web browsers, mobile operating systems, shell consoles.
  
    * Even if enforcing would be possible, [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) developers would still have a hard time guessing the nuanced behaviors across vendors:
        * e.g., consider the different behaviors of Chrome, Safari, and Firefox, even with global standards like HTML5.

    ---
    <br/>

1. **How to implement client-side validations?**

    When applicable, only minimum and maximum values are eventually implemented by [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) on a best-effort basis, given that this interval is useful when rendering HTML sliders.

    |Restriction| Type |  Details
    |-|-|-
    | `MinValue` | int | Optional minimum value
    | `MaxValue` | int | Optional maximum value
    |


    Here's a [Talker 😃](<../../10 📘 Talker specs/01 😃 Talker.md>).

    ```yaml
    - QUANTITY|How many players? >> $qt:
        MinValue: 2
        MaxLength: 10
    ```
    
    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: QUANTITY
    Message: How many players
    MinValue: 2
    MaxValue: 10
    ```

    ---
    <br/>


1. **How do built-in Talker validations work?**

    Consider the following [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? [-]<br/>> This is a 6 digit number | `0123`
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ Enter a 6 digit number.
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? [+]<br/> | `012345`
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code validated!

    Here's the [Talker 😃](<../../10 📘 Talker specs/01 😃 Talker.md>).

    ```yaml
    # Talker 😃
    - DIGITS|What's the code? >> code:
        MinLength: 6
        MaxLength: 6
    - SUCCESS|Code validated!
    ```

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: DIGITS
    Message: 😃 What's the code?
    Details: This is a 6 digit number
    ```


    ---
    <br/>

1. **How to implement custom validations in code handlers?**

    Here's a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 What's the code? [-]<br/>> This is a 6 digit number | `0123`
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ❌ Enter a 6 digit number
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 What's the code? [+]<br/> | `012345`
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code validated!
    |

    Here's the [Talker 😃](<../../10 📘 Talker specs/01 😃 Talker.md>).

    ```yaml
    # Talker 😃

    💬 Form:
    - RUN|get-code
    - SUCCESS|Code validated!

    get-code:
    - TEXT|What's the code? >> $code:
        Details: This is a 6 digit number
    - IF|{IsInvalid($code)}|failure-proc

    failure-proc:
    - FAILURE|Enter a 6 digit number
    - RUN|get-code
    ```

    Here's the [Function 🐍 handler](<../../30 💾 Talker data/12 🐍 {Function}.md>).

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
        match args['Function']:
            case 'IsInvalid':
                s = args['Input']
                return not (len(s) == 6 and s.isdigit())
    ```
    
    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEXT
    Message: 💬 What's the code? 
    Details: This is a 6 digit number
    ```
    
    ---
    <br>
