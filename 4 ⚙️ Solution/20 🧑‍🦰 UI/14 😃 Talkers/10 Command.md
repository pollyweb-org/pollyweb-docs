# 😃 Talker `- <command>`

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a Command?**

    A Command 
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) or a Flow.

    ---
    <br/>


4. **What are Flow commands?**

    > Flow commands allow the creation of complex workflows.

    Command | Purpose
    |-|-
    | ⏏️ [EVAL](<20 ⏏️ EVAL flow.md>) | Evaluates a [{Function}](<11 {Function}.md>) into a placeholder.
    | ▶️ [RUN](<24 ▶️ RUN flow.md>) | Runs a [Procedure](<12 ⚙️ Procedure.md>) and puts the result in a placeholder.
    | ⤵️ [IF](<21 ⤵️ IF flow.md>) | Runs a [Command](<10 Command.md>) or [Procedure](<12 ⚙️ Procedure.md>) based on a [{Function}](<11 {Function}.md>).
    | 🔀 [CASE](<22 🔀 CASE flow.md>) | Runs a [Command](<10 Command.md>) or [Procedure](<12 ⚙️ Procedure.md>) matching a [{Function}](<11 {Function}.md>).
    | 🔁 [REPEAT](<23 🔁 REPEAT flow.md>) | Repeats the current [Procedure](<12 ⚙️ Procedure.md>) with a confirmation.
    | ↩️ [RETURN](<25 ↩️ RETURN flow.md>) | Returns from a [Procedure](<12 ⚙️ Procedure.md>) with a result.
    

    ---
    <br/>

5. **Prompt commands**

    Messages need to escape:
    * `|` with `\|` because these are command separators;
    * `>>` with `\>>` because these are for placeholders.

    ---
    <br/>
  
6. **What are the Status prompt commands?**

    Command | Purpose
    |-|-
    | [ℹ️ INFO](<../13 🤔 Prompts/11 ℹ️ INFO prompt.md>) | Information.
    | [⏳ TEMP](<../13 🤔 Prompts/12 ⏳ TEMP prompt.md>) |Temporary message.
    | [✅ SUCCESS](<../13 🤔 Prompts/13 ✅ SUCCESS prompt.md>) | Successful action.
    | [❌ FAILURE](<../13 🤔 Prompts/14 ❌ FAILURE prompt.md>) | Unsuccessful action.

    ---
    <br/>

7. **What are the Input prompt commands?**
    
    |Command | Purpose
    |-|-
    | 🔠 [TEXT](<../13 🤔 Prompts/20 🔠 TEXT prompt.md>)
    | 🔄 [QUANTITY](<../13 🤔 Prompts/21 🔄 QUANTITY prompt.md>)
    | 🔑 [OTP](<../13 🤔 Prompts/21 🔑 OTP prompt.md>)
    | 🔢 [INT](<../13 🤔 Prompts/21 🔢 INT prompt.md>)
    | 💰 [AMOUNT](<../13 🤔 Prompts/22 💰 AMOUNT prompt.md>)
    | 👍 [CONFIRM](<../13 🤔 Prompts/24 👍 CONFIRM prompt.md>)
    | 🔠 [MANY](<../13 🤔 Prompts/25 🔠 MANY prompt.md>)
    | 1️⃣ [ONE](<../13 🤔 Prompts/25 1️⃣ ONE prompt.md>)
    | ⭐ [RATE](<../13 🤔 Prompts/26 ⭐ RATE prompt.md>)
    | 📆 [DATE](<../13 🤔 Prompts/27 📆 DATE prompt.md>)
    | 🕓 [TIME](<../13 🤔 Prompts/27 🕓 TIME prompt.md>)
    | 👤 [IDENTITY](<../13 🤔 Prompts/41 👤 IDENTIFY prompt.md>)
    | 🔆 [SCAN](<../13 🤔 Prompts/42 🔆 SCAN prompt.md>)
    | 🦋 [TOUCH](<../13 🤔 Prompts/43 🦋 TOUCH prompt.md>)
    | 🛒 [EAN](<../13 🤔 Prompts/44 🛒 EAN prompt.md>)
    | ⬆️ [UPLOAD](<../13 🤔 Prompts/51 ⬆️ UPLOAD prompt.md>)
    | 📍 [LOCATION](<../13 🤔 Prompts/61 📍 LOCATION prompt.md>)
    | 🗺️ [TRACK](<../13 🤔 Prompts/62 🗺️ TRACK prompt.md>)

    ---
    <br/>

8. **Behavior commands**

   * `FLOW|<key>`
       * Informs a new workflow starting.
       * The flow key has to be on the [host's Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).
   * `BINDABLE|<codes>`	
       * Calls [🗄️🐌🤵 Bindable @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>) 
       * Codes are comma separated
       * Example: `iata.org/SSR/WCHR`, `iata.org/...`
   * `CHARGE|<amount>|<bill-id>`	
       * Calls [💵🐌🤵 Charge @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/70 🤵🅰️ Pay/21 💵🐌🤵 Charge.md>)
       * May have a [Biller 🤝](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) ID for multiple [Collectors 🏦](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).
   * `CRUD`	
       * Initiates the CRUD dialog
   * `GOODBYE|<message>`	
       * Calls 👉 Goodbye: 🤗 Host
   * `ISSUE|<code>|{credentialID}`	
       * Calls [🎴⏩🧑‍🦰 Offer token](<../../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>)
       * The function waits for all shares
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.org/HOST](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 Host.md>)
   * `RESUBSCRIBE|<amount>`	
       * Calls 🐌 Resubscribe: 🤵📎 Broker. Pay()
   * `REVOKE|{credentialID}`	
       * Calls 👉 Revoke token: 🃏 Issuer
   * `SHARE|<code>|<message>`	
       * Calls 👉 Query: 📡 Consumer
       * Groups sequencial shares in one call
   * `SUBSCRIBE|<amount>`	
       * Calls 🐌 Subscribe: 🤵📎 Broker. Pay()

    ---
    <br/>