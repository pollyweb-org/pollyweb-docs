# 💰 AMOUNT prompt

> Part of [blocking input prompts 🤔](<11 ✏️ Input behavior.md>)


<br/>


1. **What's an AMOUNT prompt?**

    An `AMOUNT` 
    * is a [Prompt 🤔](<01 🤔 Prompt.md>) 
    * that adds currency awareness
    * to the decimal behavior of the [`QUANTITY`](<42 🔄 QUANTITY prompt.md>) prompt.

    ---
    <br/>

1. **What are AMOUNT use cases?**

    | Industry | Use case|
    |-|-
    | `Taxi`| [A taxi driver issues a bill for a ride 👨‍✈️](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/9 🚕 Driver @ Car 👨‍✈️/03 👨‍✈️ Bill wallet.md>)

    ---
    <br/>


1. **What features does AMOUNT implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<05 🤔📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax of AMOUNT in a [Talker 😃](<../../../9 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    AMOUNT|<message> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<message>`| Message to show to the user
    | `$placeholder`| Optional placeholder with the user's answer
    

    ```yaml
    # Comprehensive.
    AMOUNT >> $placeholder:
        Message: <message>
        
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
    | `Locale`   | Optional CLDR locale <br/> - defaults to the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) language | `en-US`
    | `MinValue` | Optional [minimum value 📋](<13 ✏️📋 Input validation.md>) | `-100`
    | `MaxValue` | Optional [maximum value 📋](<13 ✏️📋 Input validation.md>) | `100`
    | `Emoji` | Optional [alternative emoji 😶](<14 ✏️😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<03 🤔⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<12 ✏️⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<05 🤔📎 with Appendix.md>) | `<uuid>`
    
    ---
    <br/>

1. **What's an AMOUNT example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**



    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 💰 1234.5678
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How much? | 💰 12345.6
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How much? | 💰 -54.456
    |

    <br/>

    Here's the [Talker 😃](<../../../9 😃 Talkers/01 😃 Talker.md>).
    
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

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: AMOUNT
    Message: 😃 How much?
    MinValue: -100.00
    MaxValue: 1000000
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

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
    | [`$p.$`](<../../../9 😃 Talkers/Functions/12 🐍 {Function}.md>) | The value of `$p.Pretty` | `$1,234.57`
    | `$p` | The [default value](<../../../9 😃 Talkers/Functions/12 🐍 {Function}.md>) `$p.$` | `$1,234.57`

    ---
    <br/>

1. **How does AMOUNT process money signs?**

    When collecting an [`AMOUNT`](<43 💰 AMOUNT prompt.md>) input, [Talkers 😃](<../../../9 😃 Talkers/01 😃 Talker.md>) 
    * identity and clean monetary characters
    * while storing the currencies in their original currency.

    Consider the following conversion table in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with locale `en-US`.

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