# 😃⌘ Talker `<Command>`

> Part of [Script 📃](<Script 📃.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../Chats 💬/🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../Chats 💬/🤔 Prompt.md>).

    ---
    <br/>

1. **What the restrictions in Prompt commands?**

    Messages in [Prompt 🤔](<../Chats 💬/🤔 Prompt.md>) commands need to be escaped:
    * escape `|` with `\|` because these are [Command ⌘](<Command ⌘.md>) separators;
    * escape `>>` with `\>>` because these are for [Holders 🧠](<Holder 🧠.md>).

    ---
    <br/>
  
1. **What are the Status prompt commands?**

    Command | Purpose
    |-|-
    | ℹ️ [`INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) |Temporary status message.
    | ✅ [`DONE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) | Successful status message.
    | ❌ [`FAIL`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) | Bla | Unstructured text | 
    | ↕️ [`QUANTITY`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) | 123| Numbers with ⬆️ ⬇️ arrows |
    | 🔢 [`DIGITS`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/DIGITS 🔢 prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/AMOUNT 💰/AMOUNT 💰 prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/RATE ⭐/RATE ⭐ prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/OTP 🔑/OTP 🔑 prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) | A |
    | 📆 [`DATE`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DATE 📆/DATE 📆 prompt.md>)
    | 🕓 [`TIME`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TIME 🕓/TIME 🕓 prompt.md>)
    | 👤 [`IDENTITY`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/IDENTIFY 👤/IDENTIFY 👤 prompt.md>)
    | 🔆 [`SCAN`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/SCAN 🔆/SCAN 🔆 prompt.md>)
    | 🦋 [`TOUCH`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TOUCH 🦋/TOUCH 🦋 prompt.md>)
    | 🛒 [`EAN`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/EAN 🛒/EAN 🛒 prompt.md>)
    | ⬆️ [`UPLOAD`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/UPLOAD ⬆️/UPLOAD ⬆️ prompt.md>)
    | 📍 [`LOCATION`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/LOCATION 📍/LOCATION 📍 prompt.md>)
    | 🗺️ [`TRACK`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TRACK 🗺️/TRACK 🗺️ prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    <!-- TODO: Finish the table -->

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | Calls the [`Bind Vault` ⏩ flow](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind Vault ⏩ flow.md>) 
    | 🎫 [`ISSUE`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) | Calls the [`Save Token` ⏩ flow](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) 
    | 👋 [`GOODBYE`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) | Calls the [`Goodbye` ⏩ flow](<../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Goodbye 🤗⏩👋/🤗 Goodbye ⏩ flow.md>).
    | 📜 [`FLOW`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/INFORM 📝/📝 INFORM ⌘ cmd.md>)
    | 💳 [`CHARGE`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/CHARGE 💳/💳 CHARGE ⌘ cmd.md>)
    | 💼 [`SHARE`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/SHARE 💼/💼 SHARE ⌘ cmd.md>)
    | 🛰️ [`RELAY`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/RELAY 🛰️/🛰️ RELAY ⌘ cmd.md>)
    

    ---
    <br/>

<!--TODO:Review-->

<!--
   * `CRUD`	| Initiates the CRUD dialog
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.dom/HOST](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
   * `RESUBSCRIBE|<amount>`	
       * Calls 🐌 Resubscribe: 🤵📎 Broker. Pay()
   * `REVOKE|{credentialID}`	
       * Calls 👉 Revoke token: 🃏 Issuer

   * `SUBSCRIBE|<amount>`	
       * Calls 🐌 Subscribe: 🤵📎 Broker. Pay()
-->

   


1. **What are Flow commands?**

    > Flow commands allow the creation of complex workflows.

    Command | Purpose
    |-|-
    | ⏯️️ [`CASE`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) | Runs a [Command ⌘](<Command ⌘.md>) or [Script 📃](<Function 🐍.md>).
    | 🫥 [`EMOJI`](<../Prompts 🤔/🤔✏️ Prompt inputs/😶⌘ EMOJI cmd.md>) | Changes the [default emoji 😃](<../Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>) for [input prompts ✏️](<../Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>).
    | 🧮 [`CALL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) | Evaluates a [{Function}](<Function 🐍.md>) into a holder.
    | ⤵️ [`IF`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) | Runs a [Command ⌘](<Command ⌘.md>) or [Script 📃](<Function 🐍.md>).
    | 🪵 [`LOG`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/LOG 🪵/🪵 LOG ⌘ cmd.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) | Repeats the current [Script 📃](<Script 📃.md>) with a confirmation.
    | ⤴️ [`RETURN`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) | Returns from a [Script 📃](<Script 📃.md>) with a result.
    | ▶️ [`RUN`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) | Runs a [Script 📃](<Script 📃.md>) and puts the result in a holder.
    | 🧘 [`WAIT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>) | Waits for a period of time or until signaled.

    ---
    <br/>



1. **How to pass YAML objects to a [Command ⌘](<Command ⌘.md>)?**

    [Commands ⌘](<Command ⌘.md>) parse inputs with the [`.Evaluate`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) function.

    ```yaml
    # in multiple lines as a YAML object
    - <CMD> >> $out:
        <pro-1>: <val-1>    # objects
        <pro-2>: <val-2>    #   with a property dict
        $holder-1:          # holders with ":" suffix
    ```

    ```yaml
    # in a single line as a YAML object
    - <CMD> >> $out:
        {P1:V1, Pn:Vn, $h1, $h2}
    ```

    ```yaml
    # in multiple lines as a YAML list
    - <CMD> >> $out:
        - <pro-1>: <val-1>    # objects
        - <pro-2>: <val-2>    #   with a property dict
        - $holder-1           # holders
        - $holder-2           #   with just the holder
    ```

    ```yaml
    # in a single line as a YAML list
    - <CMD> >> $out:
        [p1:v1, p2:v2, $h1, $h2]
    ```

    ```yaml
    # in a single line as a comma-separated string
    - <CMD> >> $out:
        p1:v1, p2:v2, $h1, $h2
    ```

    ```yaml
    # in a single line as a space-separated string
    - <CMD> >> $out:
        p1:v1 p2:v2 $h1 $h2
    ```

    Inputs | Purpose | Example
    |-|-|-
    | `<CMD>` | [Command ⌘](<Command ⌘.md>) | `TEXT`
    | `$out`| Output [Holder 🧠](<Holder 🧠.md>) | `$reply`
    | `<prop-n>` | Property of an object |`Details`
    | `<val-n>` | Value of a property   | `Hi!`
    | `$holder-n` | [Holder 🧠](<Holder 🧠.md>)    | [`$.Inputs`](<../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)

    ---
    <br/>

1. **How to pass [Holders 🧠](<Holder 🧠.md>) to a [Command ⌘](<Command ⌘.md>)?**

    [Commands ⌘](<Command ⌘.md>) also parse [Holder 🧠](<Holder 🧠.md>) inputs with the [`.Evaluate`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) function.

    ```yaml
    - <CMD> >> $out:    # single value
        $in
    ```

    ```yaml
    - <CMD> >> $out:    # multiple values
        $in-1 $in-n     # in a line with spaces
    ```

    ```yaml
    - <CMD> >> $out:    # multiple values 
        $in-1, $in-n    # in a line with commas
    ```

    ```yaml
    - <CMD> >> $out:    # multiple values 
        [$in-1, $in-n]    # in a line as an array
    ```

    ```yaml
    - <CMD> >> $out:    # multiple values 
        $in-1           # in multiple lines
        $in-n
    ```

    ```yaml
    - <CMD> >> $out:    # multiple values 
        $in-1,          # in multiple lines
        $in-n           # with commas
    ```
   
    ```yaml
    - <CMD> >> $out:    # multiple values 
        - $in-1         # in multiple lines
        - $in-n         # as an array
    ```

    Inputs | Purpose | Example
    |-|-|-
    | `<CMD>` | [Command ⌘](<Command ⌘.md>) | `TEXT`
    | `$out`| Output [Holder 🧠](<Holder 🧠.md>) | `$reply`
    | `$in-n` | Input [Holder 🧠](<Holder 🧠.md>) or value   | `$A` `123` `{A:1}` `[1,2]`

    ---
    <br/>