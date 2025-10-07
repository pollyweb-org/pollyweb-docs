# 😃 Talker `<Command>`

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../31 🤔 Prompts/01 🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../31 🤔 Prompts/01 🤔 Prompt.md>).

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
    | ℹ️ [`INFO`](<../31 🤔 Prompts/11 ℹ️ INFO prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../31 🤔 Prompts/12 ⏳ TEMP prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../31 🤔 Prompts/13 ✅ SUCCESS prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../31 🤔 Prompts/14 ❌ FAILURE prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../31 🤔 Prompts/20 🔠 TEXT prompt.md>) | Bla | Unstructured text | 
    | 🔄 [`QUANTITY`](<../31 🤔 Prompts/21 🔄 QUANTITY prompt.md>) | 123| Integers with ⬆️ ⬇️ arrows |
    | 🔢 [`INT`](<../31 🤔 Prompts/21 🔢 INT prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../31 🤔 Prompts/22 💰 AMOUNT prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../31 🤔 Prompts/26 ⭐ RATE prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../31 🤔 Prompts/21 🔑 OTP prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../31 🤔 Prompts/19 👍 CONFIRM prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../31 🤔 Prompts/25 🔠 MANY prompt.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../31 🤔 Prompts/25 1️⃣ ONE prompt.md>) | A |
    | 📆 [`DATE`](<../31 🤔 Prompts/27 📆 DATE prompt.md>)
    | 🕓 [`TIME`](<../31 🤔 Prompts/27 🕓 TIME prompt.md>)
    | 👤 [`IDENTITY`](<../31 🤔 Prompts/41 👤 IDENTIFY prompt.md>)
    | 🔆 [`SCAN`](<../31 🤔 Prompts/42 🔆 SCAN prompt.md>)
    | 🦋 [`TOUCH`](<../31 🤔 Prompts/43 🦋 TOUCH prompt.md>)
    | 🛒 [`EAN`](<../31 🤔 Prompts/44 🛒 EAN prompt.md>)
    | ⬆️ [`UPLOAD`](<../31 🤔 Prompts/51 ⬆️ UPLOAD prompt.md>)
    | 📍 [`LOCATION`](<../31 🤔 Prompts/61 📍 LOCATION prompt.md>)
    | 🗺️ [`TRACK`](<../31 🤔 Prompts/62 🗺️ TRACK prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<44 🔗 BIND msg.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>) flow.
    | 🎫 [`OFFER`](<49 🎫 OFFER msg.md>) | Calls the [Save Token @ Wallet ⏩](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.
    | 👋 [`GOODBYE`](<50 👋 GOODBYE.md>) | Calls the [Goodbye @ Host](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/07 🤗⏩🧑‍🦰 Goodbye 👋.md>) ⏩ flow.
    | 📜 [`FLOW`](<41 📝 FORM msg.md>)
    | 💳 [`CHARGE`](<47 💳 CHARGE msg.md>)
    | 💼 [`SHARE`](<45 💼 SHARE msg.md>)
    | 🛰️ [`RELAY`](<51 🛰️ RELAY msg.md>)
    |
    
   
   * `CRUD`	
       * Initiates the CRUD dialog

   
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.org/HOST](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 Host.md>)
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
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) matching a [{Function}](<12 🐍 {Function}.md>).
    | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | Evaluates a [{Function}](<12 🐍 {Function}.md>) into a placeholder.
    | ⏏️ [`EXIT`](<26 ⏏️ EXIT flow.md>) | Leaves a [Procedure ⚙️](<11 ⚙️ Procedure.md>) to another permanently.
    | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | Runs a [Command ⌘](<10 ⌘ Command.md>) or [Procedure ⚙️](<11 ⚙️ Procedure.md>) based on a [{Function}](<12 🐍 {Function}.md>).
    | 🪵 [`LOG`](<15 🪵 LOG flow.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | Repeats the current [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a confirmation.
    | ↩️ [`RETURN`](<25 ↩️ RETURN flow.md>) | Returns from a [Procedure ⚙️](<11 ⚙️ Procedure.md>) with a result.
    | ▶️ [`RUN`](<24 ▶️ RUN flow.md>) | Runs a [Procedure ⚙️](<11 ⚙️ Procedure.md>) and puts the result in a placeholder.
    | ⏸️ [`WAIT`](<27 ⏸️ WAIT flow.md>) | Waits for a period of time or until signaled.

    ---
    <br/>
