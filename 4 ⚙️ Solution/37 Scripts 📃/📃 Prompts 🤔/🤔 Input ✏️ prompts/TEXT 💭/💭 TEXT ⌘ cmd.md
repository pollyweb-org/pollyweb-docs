# 💭 TEXT prompt

> Part of [blocking input prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)

## FAQ

1. **What's a TEXT prompt?**

    `TEXT` 
    * is a blocking input [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) 
    * that allows the user to type something 
    * instead of having to follow a structured format.

    It allows for GenAI large-language models (LLMs) 
    * to interpret the user's intent from natural language text, 
    * while also providing a structured input to facilitate the user's interaction;
    * e.g., a user may select the `Yes` option, or type `that's fine` in the textbox.

    ---
    <br/>

1. **What agents implement text?**
   
    |Agent| Purpose
    |-|-
    |🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)| To search for the right agent for a job.
    🔎 [Finder](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | To search for a host of a service or place.
    🧭 [Navigator](<../../../../50 🫥 Agent domains/Navigators 🧭/$ 🧭🫥 Navigator agent.md>) | To report on something suspicious.
    |[💖 Vitalogist](<../../../../50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>)| To register food intake.

    ---
    <br/>
1. **What are business cases?**

    |Category|Use case
    |-|-
    |`Curator`| [Order a burger at a fast food 🍔](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/21 🪑 Seat: Order burger 🍔.md>)
    |`Reviewer`| [Get details on a bad review ⭐](<../../../../../3 🤝 Use Cases/04 🛒 Shop/01 🛍️ Shop for clothes/01 Customer @ Item/01 Item price.md>)
    |`Broker`| [Delegate finding a bar 🍸](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    |`Finder` | [Ask alternatives to navigate 🧭](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    |`Generic`|[Report an accident 🆘](<../../../../../3 🤝 Use Cases/08 🏛️ Public Services/01 🆘 Call emergency/1 @ Anywhere/10. Emergency.md>)

    ---
    <br/>


1. **How do emojis work?**

   |Emoji|Usage
   |-|-
   |💬| The speech emoji 💬 represents the chat's [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) and any [Helper 🤲 domains](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) that it may [invite ⏩](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>).
   |💭| The thought emoji 💭 represents user [Agent 🫥 vaults](<../../../../50 🫥 Agent domains/$/🫥🗄️ Agent vault.md>).

    ---
    <br/>




1. **What features does TEXT implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>



1. **What's the syntax on a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    # Simplest.
    TEXT|<text> >> $holder
    ```

    | Input| Purpose 
    |-|-
    | `<text>`| Message to show to the user
    | `$holder`| Optional [holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the user's answer
    
    ```yaml
    # Comprehensive.
    TEXT >> $holder:
        Text: <text>
        
        # Specific optional properties
        Output: string
        Pattern: string
        MinLength: int
        MaxLength: int

        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Nullable: bool
        Appendix: {...}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `Output` | Optional HTML format for outputs | `990.990.990.990`
    | `Pattern`| Optional HTML regular expression | `^...$`
    | `MinLength` | Optional [minimum length 📋](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/📋 Input validation.md>) | `1`
    | `MaxLength` | Optional [maximum length 📋](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/📋 Input validation.md>) | `5`
    | `Details` | Optional [expandable details ⊕](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/4 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Nullable` | Optional [skip flag ⏭️](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | `{/...}`
    
    
    ---
    <br/>


1. **What's an example of a `TEXT` prompt?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 How are you today? | `I'm fine`
    | [🤲 Helper](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | 💬 How are you today? | `I'm fine`
    |  [🗄️ Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | 💭 How are you today? | `I'm fine`
    |
   
    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    📃 Example:
    - TEXT How are you today? 
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: TEXT
    Emoji: 💬
    Text: How are you today?
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: I'm fine
    ```

    ---
    <br/>

1. **What's an example of an IPv4 address input?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 What's the IP address? [-] <br/> > Hint: `123.123.123.123` | `300.010.000.001`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ❌ Invalid input! Retry.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 What's the IP address? [+] <br/>  | `255.010.000.001`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ You entered `255.10.0.1`
    |

    <br/>
   
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    # Explicit, not recommended, just for the exercise.
    - TEXT What's the IP address? >> $ip:
        Output: 990.990.990.990
        Pattern: ^((25[0-5]|2[0-4][0-9]|[01]?...{4}$
        Details: "Hint: 123.123.123.123"
    ```
    
    ```yaml
    # Built-in alternative, preferred.
    - TEXT What's the IP address? >> $ip:
        Pattern: IPv4
    ```

    ```yaml
    # Formatted output
    - DONE: You entered `$ip`
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: TEXT
    Emoji: 💬
    Text: What's the IP address? 
    Details: "Hint: `123.123.123.123`"
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: 300.010.000.001
    ```

    ---
    <br/>

1. **What are the available pre-built patterns?**

    | Pattern | Details
    |-|-
    | `IPv4` | IP address in version 4.
    | `IPv6` | IP address in version 6.

    ---
    <br/>


1. **What's an example for currencies?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 How much? [-] <br/> > Hint: `$1.23` | `bla 45.6`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ❌ Invalid input! Retry.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 How much? [+] <br/>  | `4,,5,67.8`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ You entered `4,567.80`
    |
   
    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    # Explicit, not recommended, just for the exercise.
    - TEXT How much? >> $money:
        Hint: $1.23
        Output: $#,##0.00
        Pattern: ^\(?\$?-?\s?...)?$
    ```
    
    ```yaml
    # Built-in, preferred.
    - AMOUNT|How much? >> $money:
        Locale: en-US
        MaxValue: 1000.00
    ```


    ```yaml
    # Formatted output
    - DONE: You entered `$money`
    ```

    | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 💰 [`AMOUNT`](<../AMOUNT 💰/💰 AMOUNT ⌘ cmd.md>) | To collect a structured currency value.
    | ✅ [`DONE`](<../../🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) | To show the formatted collected value.

    ---