# 😃⬇️ Talker `PUT` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What's an PUT command?**

    `PUT` ⬇️
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that puts content into a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ---
    <br/>

1. **What's the [`PUT`](<⬇️ PUT ⌘ cmd.md>) syntax?**

    |Variation| Behavior
    |-|-|
    | `PUT\|$in >> $out` | Puts the content of a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) in another
    || Equals `PUT >> $out: $in`
    | `PUT\|*{$in}* >> $out` | Interpolates [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) into a [Text 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/Text holders.md>)
    || Equals `PUT >> $out: *{$in}*`
    | `PUT\|$lst >> $out: *` | Formats a [List 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/List holders.md>) with [`.Format`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Format}.md>)
    || Equals [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>)`\|`[`.Format`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Format}.md>)` >> $out: $lst,*`
    | `PUT\|* +> $lst` | Appends items to a [List 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/List holders.md>) with [`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>)
    || Equals `PUT +> $lst: *`
    || Equals [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>)`\|`[`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>)` >> $lst: $lst,*`
    `PUT\|$l1,$l2 >> $out` | Merges two [List 🧠 holders](<../../../📃 Holders 🧠/🧠 Holder types/List holders.md>) with [`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>)
    || Equals `PUT >> $out: $l1 $l2`
    || Equals [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>)`\|`[`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>)` >> $out: $l1,$l2`  
    | `PUT\|* >> $out` | Puts any other content in a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    || Equals `PUT >> $out: *` 
    | `PUT\|.f >> $out: *` | Equals [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>)`\|.f >> $out: *`  
    | `PUT\|$in: *` | Equals [`SET`](<../SET ↘️/↘️ SET ⌘ cmd.md>)`\|$in: *` 

    ---
    <br/>


1. **What's a [`PUT`](<⬇️ PUT ⌘ cmd.md>) example with static values?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ The A holder has 3.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Holder B also has 3.

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # First message.
    - PUT|3 >> $A:

    - INFO|The A holder has {$A}.

    # Second message.
    - PUT >> $B:
        Holder B also has {$A} 
    - INFO|$B
    ```
    Uses: [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>



1. **What's an PUT example with [Pair 🧠 holders](<../../../📃 Holders 🧠/🧠 Holder types/Pair holders.md>)?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Welcome to Any Business! <br/> - We are a 3.6 M£ business  <br/> &nbsp;&nbsp; based out of London, UK.
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Run code to get the revenue
    - EVAL|Get-Revenue >> $revenue

    # Prepare the data into an object.
    - PUT >> $data:
        Input:
            Name: Any Business
            Revenue: {$revenue}
            Address: 
                City: London
                Country: UK

    # Render the intro into a string.
    - PUT >> $intro:
        Input:
            Welcome to {$data.Name}! \n
            We are a {$data.Revenue} M£ 
            business based out of 
            {$data.Address.City}, 
            {$data.Address.Country}

    # Show the intro.
    - INFO|$intro
    ```

    Uses: [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>



1. **How to merge objects in an PUT?**

    With a mix of dictionary values and [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) surrounded with `:`.
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # $partB: {B:2}
    - PUT >> $partB:
        B: 2

    # $partC: {C:3}
    - PUT >> $partC:
        C: 3

    # $output: {A:1, B:2, C:3, D:4}
    - PUT >> $output:
        A: 1
        :{$partB}:
        :{$partC}:
        D: 4
    ```
    
    In the example above, `$output` has `{A:1,B:2,C:3,D:4}`.


    ---
    <br/>
