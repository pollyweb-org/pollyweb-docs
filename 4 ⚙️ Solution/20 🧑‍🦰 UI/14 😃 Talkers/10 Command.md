# 😃 Talker `<Command>`

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) or a workflow.

    ---
    <br/>


5. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>).

    ---
    <br/>

1. **What the restrictions in Prompt commands?**

    Messages in Prompt commands need to be escaped:
    * escape `|` with `\|` because these are command separators;
    * escape `>>` with `\>>` because these are for placeholders.

    ---
    <br/>
  
6. **What are the Status prompt commands?**

    Command | Purpose
    |-|-
    | ℹ️ [`INFO`](<../13 🤔 Prompts/11 ℹ️ INFO prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../13 🤔 Prompts/12 ⏳ TEMP prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../13 🤔 Prompts/13 ✅ SUCCESS prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../13 🤔 Prompts/14 ❌ FAILURE prompt.md>) | Unsuccessful status message.

    ---
    <br/>

7. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../13 🤔 Prompts/20 🔠 TEXT prompt.md>) | Bla | Unstructured text | 
    | 🔄 [`QUANTITY`](<../13 🤔 Prompts/21 🔄 QUANTITY prompt.md>) | 123| Integers with ⬆️ ⬇️ arrows |
    | 🔢 [`INT`](<../13 🤔 Prompts/21 🔢 INT prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../13 🤔 Prompts/22 💰 AMOUNT prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../13 🤔 Prompts/26 ⭐ RATE prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../13 🤔 Prompts/21 🔑 OTP prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../13 🤔 Prompts/24 👍 CONFIRM prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../13 🤔 Prompts/25 🔠 MANY prompt.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../13 🤔 Prompts/25 1️⃣ ONE prompt.md>) | A |
    | 📆 [`DATE`](<../13 🤔 Prompts/27 📆 DATE prompt.md>)
    | 🕓 [`TIME`](<../13 🤔 Prompts/27 🕓 TIME prompt.md>)
    | 👤 [`IDENTITY`](<../13 🤔 Prompts/41 👤 IDENTIFY prompt.md>)
    | 🔆 [`SCAN`](<../13 🤔 Prompts/42 🔆 SCAN prompt.md>)
    | 🦋 [`TOUCH`](<../13 🤔 Prompts/43 🦋 TOUCH prompt.md>)
    | 🛒 [`EAN`](<../13 🤔 Prompts/44 🛒 EAN prompt.md>)
    | ⬆️ [`UPLOAD`](<../13 🤔 Prompts/51 ⬆️ UPLOAD prompt.md>)
    | 📍 [`LOCATION`](<../13 🤔 Prompts/61 📍 LOCATION prompt.md>)
    | 🗺️ [`TRACK`](<../13 🤔 Prompts/62 🗺️ TRACK prompt.md>)

    ---
    <br/>

8. **What are Message commands?**

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<42 🔗 BIND msg.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>) flow.
    | 🎫 [`OFFER`](<45 🎫 OFFER msg.md>) | Calls the [Save Token @ Wallet ⏩](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow.
    | 👋 [`GOODBYE`](<44 👋 GOODBYE.md>) | Calls the [Goodbye @ Host](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/02 🤗⏩🧑‍🦰 Goodbye.md>) ⏩ flow.
    | 📜 [`FLOW`](<41 📝 FORM msg.md>)
    | 💳 [`CHARGE`](<43 💳 CHARGE msg.md>)
    | 💼 [`SHARE`](<46 💼 SHARE msg.md>)
    | 🛰️ [`RELAY`](<32 🛰️ RELAY msg.md>)
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


9. **What are Flow commands?**

    > Flow commands allow the creation of complex workflows.

    Command | Purpose
    |-|-
    | ⏏️ [`EVAL`](<20 ⏏️ EVAL flow.md>) | Evaluates a [{Function}](<11 {Function}.md>) into a placeholder.
    | ▶️ [`RUN`](<24 ▶️ RUN flow.md>) | Runs a [Procedure](<12 ⚙️ Procedure.md>) and puts the result in a placeholder.
    | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | Runs a [Command](<10 Command.md>) or [Procedure](<12 ⚙️ Procedure.md>) based on a [{Function}](<11 {Function}.md>).
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | Runs a [Command](<10 Command.md>) or [Procedure](<12 ⚙️ Procedure.md>) matching a [{Function}](<11 {Function}.md>).
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | Repeats the current [Procedure](<12 ⚙️ Procedure.md>) with a confirmation.
    | ↩️ [`RETURN`](<25 ↩️ RETURN flow.md>) | Returns from a [Procedure](<12 ⚙️ Procedure.md>) with a result.
    

    ---
    <br/>
