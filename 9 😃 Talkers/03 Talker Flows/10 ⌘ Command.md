# 😃 Talker `<Command>`

> Part of [Talker 😃](<../01 😃 Talker.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../3 Prompts/10 Prompt definitions/01 🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../3 Prompts/10 Prompt definitions/01 🤔 Prompt.md>).

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
    | ℹ️ [`INFO`](<../3 Prompts/20 ⚠️🤔 Status prompts/21 ℹ️ INFO prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../3 Prompts/20 ⚠️🤔 Status prompts/25 ⏳ TEMP prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../3 Prompts/20 ⚠️🤔 Status prompts/23 ✅ SUCCESS prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../3 Prompts/20 ⚠️🤔 Status prompts/24 ❌ FAILURE prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../3 Prompts/30 ✏️ Input prompts/32 🔠 TEXT prompt.md>) | Bla | Unstructured text | 
    | 🔄 [`QUANTITY`](<../3 Prompts/30 ✏️ Input prompts/42 🔄 QUANTITY prompt.md>) | 123| Numbers with ⬆️ ⬇️ arrows |
    | 🔢 [`DIGITS`](<../3 Prompts/30 ✏️ Input prompts/44 🔢 DIGITS prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../3 Prompts/30 ✏️ Input prompts/43 💰 AMOUNT prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../3 Prompts/30 ✏️ Input prompts/46 ⭐ RATE prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../3 Prompts/30 ✏️ Input prompts/57 🔑 OTP prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../3 Prompts/30 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../3 Prompts/30 ✏️ Input prompts/54 🔠 MANY prompt.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../3 Prompts/30 ✏️ Input prompts/53 1️⃣ ONE prompt.md>) | A |
    | 📆 [`DATE`](<../3 Prompts/30 ✏️ Input prompts/61 📆 DATE prompt.md>)
    | 🕓 [`TIME`](<../3 Prompts/30 ✏️ Input prompts/62 🕓 TIME prompt.md>)
    | 👤 [`IDENTITY`](<../3 Prompts/30 ✏️ Input prompts/71 👤 IDENTIFY prompt.md>)
    | 🔆 [`SCAN`](<../3 Prompts/30 ✏️ Input prompts/72 🔆 SCAN prompt.md>)
    | 🦋 [`TOUCH`](<../3 Prompts/30 ✏️ Input prompts/73 🦋 TOUCH prompt.md>)
    | 🛒 [`EAN`](<../3 Prompts/30 ✏️ Input prompts/74 🛒 EAN prompt.md>)
    | ⬆️ [`UPLOAD`](<../3 Prompts/30 ✏️ Input prompts/81 ⬆️ UPLOAD prompt.md>)
    | 📍 [`LOCATION`](<../3 Prompts/30 ✏️ Input prompts/91 📍 LOCATION prompt.md>)
    | 🗺️ [`TRACK`](<../3 Prompts/30 ✏️ Input prompts/92 🗺️ TRACK prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<../5 Messages/44 🔗 BIND msg.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>) flow.
    | 🎫 [`OFFER`](<../5 Messages/49 🎫 OFFER msg.md>) | Calls the [Save Token @ Wallet ⏩](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.
    | 👋 [`GOODBYE`](<../5 Messages/50 👋 GOODBYE.md>) | Calls the [Goodbye @ Host](<../../5 ⏩ Flows/50 🤗⏩ Hosts/07 🤗⏩🧑‍🦰 Goodbye 👋.md>) ⏩ flow.
    | 📜 [`FLOW`](<../5 Messages/41 📝 FORM msg.md>)
    | 💳 [`CHARGE`](<../5 Messages/47 💳 CHARGE msg.md>)
    | 💼 [`SHARE`](<../5 Messages/45 💼 SHARE msg.md>)
    | 🛰️ [`RELAY`](<../5 Messages/51 🛰️ RELAY msg.md>)
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
    | 🫥 [`EMOJI`](<../16 😶 EMOJI flow.md>) | Changes the [default emoji 😃](<../3 Prompts/25 ✏️ Input defintions/14 ✏️😶 Input emojis.md>) for [input prompts ✏️](<../3 Prompts/10 Prompt definitions/09 ✏️ as Input.md>).
    | ⬇️ [`EVAL`](<../2 Data/20 ⬇️ EVAL flow.md>) | Evaluates a [{Function}](<../2 Data/12 🐍 {Function}.md>) into a placeholder.
    | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) based on a [{Function}](<Functi../Functions/12 🐍 {Function}.md
    | 🪵 [`LOG`](<../2 Data/15 🪵 LOG flow.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | Repeats the current [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a confirmation.
    | ↩️ [`RETURN`](<25 ↩️ RETURN flow.md>) | Returns from a [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a result.
    | ▶️ [`RUN`](<24 ▶️ RUN flow.md>) | Runs a [Procedure ⚙️](<11 ⚙️ Procedure.md>) and puts the result in a placeholder.
    | ⏸️ [`WAIT`](<28 ⏸️ WAIT flow.md>) | Waits for a period of time or until signaled.

    ---
    <br/>
