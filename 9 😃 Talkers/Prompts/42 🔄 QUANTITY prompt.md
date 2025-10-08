# 🔄 QUANTITY prompt

> Part of [blocking input prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>)


<br/>

1. **What's an QUANTITY prompt?**

    It's a [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) that shows up and down arrows - e.g.:
    * [Book a restaurant table online 🍽️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    * [Split the bill at a restaurant ✂️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>)
    * [Walk into a full restaurant 🍽️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/44 🚪 Door: Walk in full.md>)

    ---
    <br/>


1. **What features does QUANTITY implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/05 🤔📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax on a [Talker 😃](<../01 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    QUANTITY|<message> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<message>`| Message to show to the user
    | `$placeholder`| Optional placeholder with the user's answer 

    ```yaml
    # Comprehensive.
    QUANTITY >> $placeholder:
        Message: <message>

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
    | `Locale`   | Optional CLDR locale <br/> - defaults to the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) language | `en-US`
    | `MinValue` | Optional [minimum value 📋](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/13 ✏️📋 Input validation.md>) | `-100`
    | `MaxValue` | Optional [maximum value 📋](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/13 ✏️📋 Input validation.md>) | `100`
    | `Emoji` | Optional [alternative emoji 😶](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/14 ✏️😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/12 ✏️⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/05 🤔📎 with Appendix.md>) | `<uuid>`
    
    
    
    ---
    <br/>


1. **What's an example?**

    Here's a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../0../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Promp../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How many? | 🔄 123
    [🫥 Agent](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How many? | 🔄 123
    | [🛠️ Helper](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How many? | 🔄 -54
    |
    
    <br/>

    Here's the [Talker 😃](<../01 😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    - QUANTITY >> $qt:
        Message: How many? 
        MinValue: -100
        MaxValue: 100
        Precision: 1    # Server-side only
        Locale: en-US   # Server-side only
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: QUANTITY
    Message: 😃 How many?
    MinValue: -100
    MaxValue: 100
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: -54
    ```

    ---
    <br/>



1. **How to default quantities in a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**

    Use the [`ONE`](<53 1️⃣ ONE prompt.md>) prompt.

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../0../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Promp../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Table reservation.
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 For how many? [1, 2, more] | > more
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How many exactly? | 🔄 8
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ⏳ Checking availability... 
    |

    Here's the [Talker 😃](<../01 😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Walk-in:
    
    - INFO:
        Message: Table reservation.
    
    - ONE >> $p:
        Message: For how many?
        Options: 1,2,more

    - CASE|{$p}:
        more: 
          - QUANTITY|How many exactly? >> $p:
                MinValue: 3
                MaxValue: 12

    - TEMP|Checking availability...
    ```

    | [Command ⌘](<../Flow/10 ⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<20 Status prompts/21 ℹ️ INFO prompt.md>) | To show the result.
    | 1️⃣ [`ONE`](<53 1️⃣ ONE prompt.md>) | To show the options.
    | 🔀 [`CASE`](<../Flow/22 🔀 CASE flow.md>) | To check the selected option.
    | ⏳ [`TEMP`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/25 ⏳ TEMP prompt.md>) | To show work in progress.
    

    ---
    <br/>



1. **How does Precision work?**

    When collecting a [`QUANTITY`](<42 🔄 QUANTITY prompt.md>) in../01 😃 Talker.mders/01 😃 Talker.md>) 
    * round up the input based on the precision, 
    * and ask confirmation to the user if the value differs.

    <br/>

    Here's a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../0../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Promp../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 🔄 01234.5
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You entered `1,234.50`
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How much? | 🔄 4.5678   
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 OK with `4.57`? [Yes, No] | > Yes
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You entered `4.57`
    |

    <br/>

    Here's the [Talker 😃](<../01 😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    - QUANTITY|How much? >> $p:
        Precision: 2  
    - INFO|You entered $p
    - REPEAT
    ```

    | [Command ⌘](<../Flow/10 ⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<20 Status prompts/21 ℹ️ INFO prompt.md>) | To show the message.
    | 🔁 [`REPEAT`](<../Flow/23 🔁 REPEAT flow.md>) | To repeat the input cycle forever.
     

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
    | [`$p.$`](<../Data/12 🐍 {Function}.md>) | The value of `$p.Pretty` | `1,234.57`
    | `$p` | The [default value](<../Data/12 🐍 {Function}.md>) `$p.$` | `1,234.57`

    ---
    <br/>


1. **What's an example of a QUANTITY default property?**

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompt../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md/01 🧑‍🦰 Wal../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a quantity  | 🔄 1234
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ I'm storing `1,234`
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Although you typed `1234`
    |

    <br/>

    Here's the [Talker 😃](<../01 😃 Talker.md>).
        
    ```yaml
    # 😃 Talker 
    💬 Example:
    - QUANTITY|Give me a quantity >> $p
    - INFO|I'm storing `{$p}`
    - INFO|Although you typed `{$p.Text}`
    ```


    ---
    <br/>


