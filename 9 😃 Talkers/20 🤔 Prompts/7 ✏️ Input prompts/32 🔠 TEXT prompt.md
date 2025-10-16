# 🔠 TEXT prompt

> Part of [blocking input prompts 🤔](<../1 📘 Prompt specs/09 ✏️ as Input.md>)

<br/>

1. **What's a TEXT prompt?**

    A `TEXT` 
    * is a blocking input [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) 
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
    |🤵 [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)| To search for the right agent for a job.
    🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/🔎🫥 Finder agent.md>) | To search for a host of a service or place.
    🧭 [Navigator](<../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | To report on something suspicious.
    |[💖 Vitalogist](<../../../4 ⚙️ Solution/50 🫥 Agents/95 💖 Vitalogists/$ 💖🫥 Vitalogist agent.md>)| To register food intake.

    ---
    <br/>
1. **What are business cases?**

    |Category|Use case
    |-|-
    |`Curator`| [Order a burger at a fast food 🍔](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/21 🪑 Seat: Order burger 🍔.md>)
    |`Reviewer`| [Get details on a bad review ⭐](<../../../3 🤝 Use Cases/04 🛒 Shop/01 🛍️ Shop for clothes/01 Customer @ Item/01 Item price.md>)
    |`Broker`| [Delegate finding a bar 🍸](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    |`Finder` | [Ask alternatives to navigate 🧭](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    |`Generic`|[Report an accident 🆘](<../../../3 🤝 Use Cases/08 🏛️ Public Services/01 🆘 Call emergency/1 @ Anywhere/10. Emergency.md>)

    ---
    <br/>


1. **How do emojis work?**

   |Emoji|Usage
   |-|-
   |💬| The speech emoji 💬 represents the chat's [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) and any [Helper 🤲 domains](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) that it may [invite ⏩](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🛠️.md>).
   |💭| The thought emoji 💭 represents user [Agent 🫥 vaults](<../../../4 ⚙️ Solution/50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>).

    ---
    <br/>




1. **What features does TEXT implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../1 📘 Prompt specs/09 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>



1. **What's the syntax on a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    TEXT|<statement> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<statement>`| Message to show to the user
    | `$placeholder`| Optional [$placeholder 💾](<../../30 🗃️ Talker data/10 💾 $Placeholder.md>) with the user's answer
    
    ```yaml
    # Comprehensive.
    TEXT >> $placeholder:
        Statement: <statement>
        
        # Specific optional properties
        Output: string
        Pattern: string
        MinLength: int
        MaxLength: int

        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Nullable: bool
        Appendix: {function}
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `Output` | Optional HTML format for outputs | `990.990.990.990`
    | `Pattern`| Optional HTML regular expression | `^...$`
    | `MinLength` | Optional [minimum length 📋](<../2 ✏️ Input specs/13 📋 Input validation.md>) | `1`
    | `MaxLength` | Optional [maximum length 📋](<../2 ✏️ Input specs/13 📋 Input validation.md>) | `5`
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../1 📘 Prompt specs/04 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Nullable` | Optional [skip flag ⏭️](<../2 ✏️ Input specs/12 ⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `<uuid>`
    
    
    ---
    <br/>


1. **What's an example of a `TEXT` prompt?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 💬 How are you today? | `I'm fine`
    | [🤲 Helper](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) | 💬 How are you today? | `I'm fine`
    | [🫥 Agent](<../../../4 ⚙️ Solution/50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | 💭 How are you today? | `I'm fine`
    |
   
    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - TEXT|How are you today? 
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEXT
    Statement: 💬 How are you today?
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: I'm fine
    ```

    ---
    <br/>

1. **What's an example of an IPv4 address input?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 💬 What's the IP address? [-] <br/> > Hint: `123.123.123.123` | `300.010.000.001`
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ❌ Invalid input! Retry.
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 💬 What's the IP address? [+] <br/>  | `255.010.000.001`
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ✅ You entered `255.10.0.1`
    |

    <br/>
   
    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Explicit, not recommended, just for the exercise.
    - TEXT|What's the IP address? >> $ip:
        Output: 990.990.990.990
        Pattern: ^((25[0-5]|2[0-4][0-9]|[01]?...{4}$
        Details: "Hint: 123.123.123.123"
    ```
    
    ```yaml
    # Built-in alternative, preferred.
    - TEXT|What's the IP address? >> $ip:
        Pattern: IPv4
    ```

    ```yaml
    # Formatted output
    - SUCCESS|You entered `$ip`
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEXT
    Statement: 💬 What's the IP address? 
    Details: "Hint: `123.123.123.123`"
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

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

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 💬 How much? [-] <br/> > Hint: `$1.23` | `bla 45.6`
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ❌ Invalid input! Retry.
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 💬 How much? [+] <br/>  | `4,,5,67.8`
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ✅ You entered `4,567.80`
    |
   
    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Explicit, not recommended, just for the exercise.
    - TEXT|How much? >> $money:
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
    - SUCCESS|You entered `$money`
    ```

    | [Command ⌘](<../../40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | 💰 [`AMOUNT`](<43 💰 AMOUNT prompt.md>) | To collect a structured currency value.
    | ✅ [`SUCCESS`](<../4 ⚠️ Status prompts/23 ✅ SUCCESS prompt.md>) | To show the formatted collected value.

    ---