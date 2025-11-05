# 📋 Input validation

> Part of [✏️ Input prompts](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

<br/>


1. **How do client-side validations work?**

    NLWeb does not guarantee client-side validations.

    * It's close to impossible to enforce [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to comply with the rules across a large landscape of vendors and user interface (UI) technologies: 
        * e.g., web browsers, mobile operating systems, shell consoles.
  
    * Even if enforcing would be possible, [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) developers would still have a hard time guessing the nuanced behaviors across vendors:
        * e.g., consider the different behaviors of Chrome, Safari, and Firefox, even with global standards like HTML5.

    ---
    <br/>

1. **How to implement client-side validations?**

    When applicable, only minimum and maximum values are eventually implemented by [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) on a best-effort basis, given that this interval is useful when rendering HTML sliders.

    |Restriction| Type |  Details
    |-|-|-
    | `MinValue` | int | Optional minimum value
    | `MaxValue` | int | Optional maximum value
    |


    Here's a [Script 📃](<../../Scripts 📃/Script 📃.md>).

    ```yaml
    - QUANTITY|How many players? >> $qt:
        MinValue: 2
        MaxLength: 10
    ```
    
    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: QUANTITY
    Text: How many players
    MinValue: 2
    MaxValue: 10
    ```

    ---
    <br/>


1. **How do built-in Talker validations work?**

    Consider the following [Chat 💬](<../../Chats 💬/💬 Chat.md>) as an example.

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What's the code? [-]<br/>> This is a 6 digit number | `0123`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ❌ Enter a 6 digit number.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 What's the code? [+]<br/> | `012345`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Code validated!

    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    - DIGITS|What's the code? >> code:
        MinLength: 6
        MaxLength: 6
    - SUCCESS|Code validated!
    ```

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: DIGITS
    Emoji: 😃 
    Text: What's the code?
    Details: This is a 6 digit number
    ```


    ---
    <br/>

1. **How to implement custom validations in code handlers?**

    Here's a [Chat 💬](<../../Chats 💬/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 What's the code? [-]<br/>> This is a 6 digit number | `0123`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ❌ Enter a 6 digit number
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 What's the code? [+]<br/> | `012345`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Code validated!
    |

    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

    ```yaml
    # Talker 😃

    💬 Form:
    - RUN|get-code
    - SUCCESS|Code validated!

    get-code:
    - TEXT|What's the code? >> $code:
        Details: This is a 6 digit number
    - IF|{IsInvalid($code)}|failure-script

    failure-script:
    - FAILURE|Enter a 6 digit number
    - RUN|get-code
    ```

    Here's the [Function 🐍 handler](<../../Scripts 📃/Function 🐍.md>).

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
        match args['Function']:
            case 'IsInvalid':
                s = args['Input']
                return not (len(s) == 6 and s.isdigit())
    ```
    
    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: TEXT
    Emoji: 💬 
    Text: What's the code? 
    Details: This is a 6 digit number
    ```
    
    ---
    <br>
