# 😃 Talker `<Command>`

> Part of [Talker 😃](<../01 😃 Talker.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>).

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
    | ℹ️ [`INFO`](<../Prompts/21 ℹ️ INFO prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/25 ⏳ TEMP prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/23 ✅ SUCCESS prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/24 ❌ FAILURE prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/32 🔠 TEXT prompt.md>) | Bla | Unstructured text | 
    | 🔄 [`QUANTITY`](<../Prompts/42 🔄 QUANTITY prompt.md>) | 123| Numbers with ⬆️ ⬇️ arrows |
    | 🔢 [`DIGITS`](<../Prompts/44 🔢 DIGITS prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../Prompts/43 💰 AMOUNT prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/46 ⭐ RATE prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/57 🔑 OTP prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../Prompts/31 👍 CONFIRM prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../Prompts/54 🔠 MANY prompt.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../Prompts/53 1️⃣ ONE prompt.md>) | A |
    | 📆 [`DATE`](<../Prompts/61 📆 DATE prompt.md>)
    | 🕓 [`TIME`](<../Prompts/62 🕓 TIME prompt.md>)
    | 👤 [`IDENTITY`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/71 👤 IDENTIFY prompt.md>)
    | 🔆 [`SCAN`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/72 🔆 SCAN prompt.md>)
    | 🦋 [`TOUCH`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/73 🦋 TOUCH prompt.md>)
    | 🛒 [`EAN`](<../Prompts/74 🛒 EAN prompt.md>)
    | ⬆️ [`UPLOAD`](<../Prompts/81 ⬆️ UPLOAD prompt.md>)
    | 📍 [`LOCATION`](<../Prompts/91 📍 LOCATION prompt.md>)
    | 🗺️ [`TRACK`](<../Prompts/92 🗺️ TRACK prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<../Messages/44 🔗 BIND msg.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>) flow.
    | 🎫 [`OFFER`](<../Messages/49 🎫 OFFER msg.md>) | Calls the [Save Token @ Wallet ⏩](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.
    | 👋 [`GOODBYE`](<../Messages/50 👋 GOODBYE.md>) | Calls the [Goodbye @ Host](<../../5 ⏩ Flows/50 🤗⏩ Hosts/07 🤗⏩🧑‍🦰 Goodbye 👋.md>) ⏩ flow.
    | 📜 [`FLOW`](<../Messages/41 📝 FORM msg.md>)
    | 💳 [`CHARGE`](<../Messages/47 💳 CHARGE msg.md>)
    | 💼 [`SHARE`](<../Messages/45 💼 SHARE msg.md>)
    | 🛰️ [`RELAY`](<../Messages/51 🛰️ RELAY msg.md>)
    |
    
   
   * `CRUD`	
       * Initiates the CRUD dialog

   
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.org/HOST](<../../7 🧩 Schemas/HOST/🧩 Host.md>)
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
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) matching a [{Function}](<Functi../Functions/12 🐍 {Function}.md
    | 🫥 [`EMOJI`](<../16 😶 EMOJI flow.md>) | Changes the [default emoji 😃](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/14 ✏️😶 Input emojis.md>) for [input prompts ✏️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>).
    | ⬇️ [`EVAL`](<../Data/20 ⬇️ EVAL flow.md>) | Evaluates a [{Function}](<../Data/12 🐍 {Function}.md>) into a placeholder.
    | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) based on a [{Function}](<Functi../Functions/12 🐍 {Function}.md
    | 🪵 [`LOG`](<../Data/15 🪵 LOG flow.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | Repeats the current [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a confirmation.
    | ↩️ [`RETURN`](<25 ↩️ RETURN flow.md>) | Returns from a [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a result.
    | ▶️ [`RUN`](<24 ▶️ RUN flow.md>) | Runs a [Procedure ⚙️](<11 ⚙️ Procedure.md>) and puts the result in a placeholder.
    | ⏸️ [`WAIT`](<28 ⏸️ WAIT flow.md>) | Waits for a period of time or until signaled.

    ---
    <br/>
