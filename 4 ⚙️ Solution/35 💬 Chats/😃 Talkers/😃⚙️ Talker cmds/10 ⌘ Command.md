# 😃 Talker `<Command>`

> Part of [Talker 😃](<../😃 Talker.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../../🤔 Prompts/🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../../🤔 Prompts/🤔 Prompt.md>).

    ---
    <br/>

1. **What the restrictions in Prompt commands?**

    Messages in Prompt commands need to be escaped:
    * escape `|` with `\|` because these are command separators;
    * escape `>>` with `\>>` because these are for placeholders.

    ---
    <br/>
  
1. **What are the Status prompt commands?**

    Command | Purpose
    |-|-
    | ℹ️ [`INFO`](<../../🤔 Prompts/🤔📢 Prompt status/21 ℹ️ INFO prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../../🤔 Prompts/🤔📢 Prompt status/25 ⏳ TEMP prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../../🤔 Prompts/🤔📢 Prompt status/23 ✅ SUCCESS prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../../🤔 Prompts/🤔📢 Prompt status/24 ❌ FAILURE prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../../🤔 Prompts/🤔✏️ Prompt inputs/32 🔠 TEXT prompt.md>) | Bla | Unstructured text | 
    | ↕️ [`QUANTITY`](<../../🤔 Prompts/🤔✏️ Prompt inputs/42 ↕️ QUANTITY prompt.md>) | 123| Numbers with ⬆️ ⬇️ arrows |
    | 🔢 [`DIGITS`](<../../🤔 Prompts/🤔✏️ Prompt inputs/44 🔢 DIGITS prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../../🤔 Prompts/🤔✏️ Prompt inputs/43 💰 AMOUNT prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../../🤔 Prompts/🤔✏️ Prompt inputs/46 ⭐ RATE prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../../🤔 Prompts/🤔✏️ Prompt inputs/57 🔑 OTP prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../../🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../../🤔 Prompts/🤔✏️ Prompt inputs/54 🔠 MANY prompt.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../../🤔 Prompts/🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>) | A |
    | 📆 [`DATE`](<../../🤔 Prompts/🤔✏️ Prompt inputs/61 📆 DATE prompt.md>)
    | 🕓 [`TIME`](<../../🤔 Prompts/🤔✏️ Prompt inputs/62 🕓 TIME prompt.md>)
    | 👤 [`IDENTITY`](<../../🤔 Prompts/🤔✏️ Prompt inputs/71 👤 IDENTIFY prompt.md>)
    | 🔆 [`SCAN`](<../../🤔 Prompts/🤔✏️ Prompt inputs/72 🔆 SCAN prompt.md>)
    | 🦋 [`TOUCH`](<../../🤔 Prompts/🤔✏️ Prompt inputs/73 🦋 TOUCH prompt.md>)
    | 🛒 [`EAN`](<../../🤔 Prompts/🤔✏️ Prompt inputs/74 🛒 EAN prompt.md>)
    | ⬆️ [`UPLOAD`](<../../🤔 Prompts/🤔✏️ Prompt inputs/81 ⬆️ UPLOAD prompt.md>)
    | 📍 [`LOCATION`](<../../🤔 Prompts/🤔✏️ Prompt inputs/91 📍 LOCATION prompt.md>)
    | 🗺️ [`TRACK`](<../../🤔 Prompts/🤔✏️ Prompt inputs/92 🗺️ TRACK prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<../😃📨 Talker msgs/44 🔗 BIND msg.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>) flow.
    | 🎫 [`OFFER`](<../😃📨 Talker msgs/49 🎫 OFFER msg.md>) | Calls the [Save Token @ Wallet ⏩](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/🧑‍🦰👉🎴 Save token.md>) flow.
    | 👋 [`GOODBYE`](<../😃📨 Talker msgs/50 👋 GOODBYE.md>) | Calls the [Goodbye @ Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Goodbye 👋.md>) ⏩ flow.
    | 📜 [`FLOW`](<../😃📨 Talker msgs/41 📝 INFORM msg.md>)
    | 💳 [`CHARGE`](<../😃📨 Talker msgs/53 💳 CHARGE msg.md>)
    | 💼 [`SHARE`](<../😃📨 Talker msgs/45 💼 SHARE msg.md>)
    | 🛰️ [`RELAY`](<../😃📨 Talker msgs/51 🛰️ RELAY msg.md>)
    |
    
   
   * `CRUD`	
       * Initiates the CRUD dialog

   
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.org/HOST](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
   * `RESUBSCRIBE|<amount>`	
       * Calls 🐌 Resubscribe: 🤵📎 Broker. Pay()
   * `REVOKE|{credentialID}`	
       * Calls 👉 Revoke token: 🃏 Issuer

   * `SUBSCRIBE|<amount>`	
       * Calls 🐌 Subscribe: 🤵📎 Broker. Pay()

    ---
    <br/>


1. **What are Flow commands?**

    > Flow commands allow the creation of complex workflows.

    Command | Purpose
    |-|-
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) matching a [{Function}](<../😃💾 Talker data/12 🐍 {Function}.md>).
    | 🫥 [`EMOJI`](<../../🤔 Prompts/🤔✏️ Prompt input features/16 😶⌘ EMOJI cmd.md>) | Changes the [default emoji 😃](<../../🤔 Prompts/🤔✏️ Prompt input features/14 😶 Input emojis.md>) for [input prompts ✏️](<../../🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>).
    | ⬇️ [`EVAL`](<../😃💾 Talker data/20 ⬇️ EVAL flow.md>) | Evaluates a [{Function}](<../😃💾 Talker data/12 🐍 {Function}.md>) into a placeholder.
    | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) based on a [{Function}](<../😃💾 Talker data/12 🐍 {Function}.md>).
    | 🪵 [`LOG`](<../😃💾 Talker data/15 🪵 LOG flow.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | Repeats the current [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a confirmation.
    | ↩️ [`RETURN`](<25 ↩️ RETURN flow.md>) | Returns from a [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a result.
    | ▶️ [`RUN`](<24 ▶️ RUN flow.md>) | Runs a [Procedure ⚙️](<11 ⚙️ Procedure.md>) and puts the result in a placeholder.
    | ⏸️ [`WAIT`](<28 ⏸️ WAIT flow.md>) | Waits for a period of time or until signaled.

    ---
    <br/>
