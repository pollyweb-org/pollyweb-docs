# ↕️ QUANTITY prompt

> Part of [blocking input prompts 🤔](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)


<br/>

1. **What's an QUANTITY prompt?**

    It's a [Prompt 🤔](<../🤔 Prompt.md>) that shows up and down arrows - e.g.:
    * [Book a restaurant table online 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    * [Split the bill at a restaurant ✂️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>)
    * [Walk into a full restaurant 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/44 🚪 Door: Walk in full.md>)

    ---
    <br/>


1. **What features does QUANTITY implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax on a [Talker 😃](<../../😃 Talkers/😃 Talker.md>)?**

    ```yaml
    # Simplest.
    QUANTITY|<statement> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<statement>`| Message to show to the user
    | `$placeholder`| Optional [placeholder 🧠](<../../😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) with the user's answer 

    ```yaml
    # Comprehensive.
    QUANTITY >> $placeholder:
        Statement: <statement>

        # Specific optional properties
        Precision: int
        Locale: string
        MinValue: decimal
        MaxValue: decimal
        
        # Generic optional properties
        Emoji: emoji
        Details: string
        Nullable: bool
        Appendix: {function}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Precision`| Rounded decimals (default is 0) | `0`
    | `Locale`   | Optional CLDR locale <br/> - defaults to the [Chat 💬](<../../💬 Chats/💬 Chat.md>) language | `en-US`
    | `MinValue` | Optional [minimum value 📋](<../🤔✏️ Prompt input features/13 📋 Input validation.md>) | `-100`
    | `MaxValue` | Optional [maximum value 📋](<../🤔✏️ Prompt input features/13 📋 Input validation.md>) | `100`
    | `Emoji` | Optional [alternative emoji 😶](<../🤔✏️ Prompt input features/14 😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../🤔✏️ Prompt input features/12 ⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `<uuid>`
    
    
    
    ---
    <br/>


1. **What's an example?**

    Here's a [Chat 💬](<../../💬 Chats/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 How many? | ↕️ 123
    [🫥 Agent](<../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | 🫥 How many? | ↕️ 123
    | [🤲 Helper](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | 🫥 How many? | ↕️ -54
    |
    
    <br/>

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    - QUANTITY >> $qt:
        Statement: How many? 
        MinValue: -100
        MaxValue: 100
        Precision: 1    # Server-side only
        Locale: en-US   # Server-side only
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: QUANTITY
    Statement: 😃 How many?
    MinValue: -100
    MaxValue: 100
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: -54
    ```

    ---
    <br/>



1. **How to default quantities in a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**

    Use the [`ONE`](<53 1️⃣ ONE prompt.md>) prompt.

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Table reservation.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 For how many? [1, 2, more] | > more
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 How many exactly? | ↕️ 8
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ⏳ Checking availability... 
    |

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Walk-in:
    
    - INFO:
        Statement: Table reservation.
    
    - ONE >> $p:
        Statement: For how many?
        Options: 1,2,more

    - CASE|{$p}:
        more: 
          - QUANTITY|How many exactly? >> $p:
                MinValue: 3
                MaxValue: 12

    - TEMP|Checking availability...
    ```

    | [Command ⌘](<../../😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../🤔📢 Prompt status/INFO ℹ️ prompt.md>) | To show the result.
    | 1️⃣ [`ONE`](<53 1️⃣ ONE prompt.md>) | To show the options.
    | ⏯️️ [`CASE`](<../../😃 Talkers/😃⚙️ Talker cmds/for control/CASE ⏯️.md>) | To check the selected option.
    | ⏳ [`TEMP`](<../🤔📢 Prompt status/TEMP ⏳ prompt.md>) | To show work in progress.
    

    ---
    <br/>



1. **How does Precision work?**

    When collecting a [`QUANTITY`](<42 ↕️ QUANTITY prompt.md>) input, [Talkers 😃](<../../😃 Talkers/😃 Talker.md>) 
    * round up the input based on the precision, 
    * and ask confirmation to the user if the value differs.

    <br/>

    Here's a [Chat 💬](<../../💬 Chats/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 How much? | ↕️ 01234.5
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You entered `1,234.50`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 How much? | ↕️ 4.5678   
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 OK with `4.57`? [Yes, No] | > Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You entered `4.57`
    |

    <br/>

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    - QUANTITY|How much? >> $p:
        Precision: 2  
    - INFO|You entered $p
    - REPEAT
    ```

    | [Command ⌘](<../../😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../🤔📢 Prompt status/INFO ℹ️ prompt.md>) | To show the message.
    | 🔁 [`REPEAT`](<../../😃 Talkers/😃⚙️ Talker cmds/for control/REPEAT 🔁.md>) | To repeat the input cycle forever.
     

    ---
    <br/>


1. **What's contained in the QUANTITY placeholder?**

    ```yaml
    # 😃 Talker
    - QUANTITY|How much? >> $p:
    ```

    | Argument| Content | Example
    |-|-|-
    | `$p.Text` | Text answered | `1234.5678`
    | `$p.Decimal` | Decimal rounded to `Precision` | `1234.57`
    | `$p.Pretty` | Decimal formatted to `Locale` | `1,234.57`
    | `$p.Locale` | CLDR locale used to format | `en-US`
    | [`$p.$`](<../../😃 Talkers/😃⚙️ Talker cmds/for data/{Function} 🐍.md>) | The value of `$p.Pretty` | `1,234.57`
    | `$p` | The [default value](<../../😃 Talkers/😃⚙️ Talker cmds/for data/{Function} 🐍.md>) `$p.$` | `1,234.57`

    ---
    <br/>


1. **What's an example of a QUANTITY default property?**

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Give me a quantity  | ↕️ 1234
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ I'm storing `1,234`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Although you typed `1234`
    |

    <br/>

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).
        
    ```yaml
    # 😃 Talker 
    💬 Example:
    - QUANTITY|Give me a quantity >> $p
    - INFO|I'm storing `{$p}`
    - INFO|Although you typed `{$p.Text}`
    ```


    ---
    <br/>


