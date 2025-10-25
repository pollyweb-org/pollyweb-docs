# 💰 AMOUNT prompt

> Part of [blocking input prompts 🤔](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>)


<br/>


1. **What's an AMOUNT prompt?**

    An `AMOUNT` 
    * is a [Prompt 🤔](<../../🤔 Prompt.md>) 
    * that adds currency awareness
    * to the decimal behavior of the [`QUANTITY`](<../QUANTITY ↕️ prompt.md>) prompt.

    ---
    <br/>

1. **What are AMOUNT use cases?**

    | Industry | Use case|
    |-|-
    | `Taxi`| [A taxi driver issues a bill for a ride 👨‍✈️](<../../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/03 👨‍✈️ Bill wallet.md>)

    ---
    <br/>


1. **What features does AMOUNT implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax of AMOUNT in a [Talker 😃](<../../../😃 Talkers/😃 Talker role.md>)?**

    ```yaml
    # Simplest.
    AMOUNT|<statement> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<statement>`| Message to show to the user
    | `$placeholder`| Optional [placeholder 🧠](<../../../😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) with the user's answer
    

    ```yaml
    # Comprehensive.
    AMOUNT >> $placeholder:
        Statement: <statement>
        
        # Specific optional properties
        Currency: string
        
        # Optional properties from QUANTITY
        MinValue: decimal   
        MaxValue: decimal   
        Precision: int      
        Locale: string      
        
        # Generic optional properties
        Emoji: emoji
        Details: string
        Nullable: bool
        Appendix: {function}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Currency` | Optional ISO 4217 currency <br/>- defaults to the locale's currency | `USD`
    | `Precision`| Rounded decimals (default is 2) | `2`
    | `Locale`   | Optional CLDR locale <br/> - defaults to the [Chat 💬](<../../../💬 Chats/💬 Chat.md>) language | `en-US`
    | `MinValue` | Optional [minimum value 📋](<../../🤔✏️ Prompt input features/📋 Input validation.md>) | `-100`
    | `MaxValue` | Optional [maximum value 📋](<../../🤔✏️ Prompt input features/📋 Input validation.md>) | `100`
    | `Emoji` | Optional [alternative emoji 😶](<../../🤔✏️ Prompt input features/😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../../🤔✏️ Prompt input features/⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `<uuid>`
    
    ---
    <br/>

1. **What's an AMOUNT example of a [Chat 💬](<../../../💬 Chats/💬 Chat.md>)?**



    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 How much? | 💰 1234.5678
    [🫥 Agent](<../../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | 🫥 How much? | 💰 12345.6
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | 🫥 How much? | 💰 -54.456
    |

    <br/>

    Here's the [Talker 😃](<../../../😃 Talkers/😃 Talker role.md>).
    
    ```yaml
    # 😃 Talker 
    - AMOUNT|How much?:
        MinValue: -100.00
        MaxValue: 1000000
        Precision: 5    # Server-side only
        Locale: en-US   # Server-side only
        Currency: USD   # Server-side only
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: AMOUNT
    Statement: 😃 How much?
    MinValue: -100.00
    MaxValue: 1000000
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: 1234.5678
    ```


    ---
    <br/>


1. **What's contained in the AMOUNT placeholder?**

    ```yaml
    # 😃 Talker
    - AMOUNT|How much? >> $p:
    ```

    | Argument| Content | Example
    |-|-|-
    | `$p.Text` | Text answered | `1234.5678`
    | `$p.Decimal` | Decimal rounded to `Precision` | `1234.57`
    | `$p.Pretty` | Decimal formatted to `Locale` | `$1,234.57`
    | `$p.Locale` | CLDR locale used to format | `en-US`
    | `$p.Currency` | ISO 4217 currency formatted | `USD`
    | [`$p.$`](<../../../😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | The value of `$p.Pretty` | `$1,234.57`
    | `$p` | The [default value](<../../../😃 Talkers/😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) `$p.$` | `$1,234.57`

    ---
    <br/>

1. **How does AMOUNT process money signs?**

    When collecting an [`AMOUNT`](<AMOUNT 💰 prompt.md>) input, [Talkers 😃](<../../../😃 Talkers/😃 Talker role.md>) 
    * identity and clean monetary characters
    * while storing the currencies in their original currency.

    Consider the following conversion table in a [Chat 💬](<../../../💬 Chats/💬 Chat.md>) with locale `en-US`.

    |Group      | Scenario| `.Text`   | `.Pretty`   | `.Currency`
    |-          | -|-:|-:|:-:
    |`Decimals` |1 decimal| 1234.5    | $1,234.50   | USD 🇺🇸
    |`Symbol`   |no sign  | 1.23      | $1.23       | USD 🇺🇸
    |           |all good | $1.23     | $1.23       | USD 🇺🇸
    |           |spaces   | $ 1.23    | $1.23       | USD 🇺🇸
    |           |sign side| 1.23$     | $1.23       | USD 🇺🇸
    |           |sign name| 1.23 USD  | $1.23       | USD 🇺🇸 
    |           |no spaces| 1.23USD   | $1.23       | USD 🇺🇸
    | `Foreign` |sign name| 1.23 EUR  | €1.23       | EUR 🇪🇺
    |           |commas   | 1,23 EUR  | €1.23       | EUR 🇪🇺
    |           |sign     | 1,23€     | €1.23       | EUR 🇪🇺
    |           |sign side| € 1,23    | €1.23       | EUR 🇪🇺


    ---
    <br/>