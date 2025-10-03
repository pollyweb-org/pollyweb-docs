# 😃 Talker `- <command>`

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a Command?**

    A Command 
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) or a Flow.

    ---
    <br/>


4. **Flow commands**

    * `EVAL|{function}`	
        * Calculates something to be used in cases.
        * Without a function, uses the last answer.
        * Without cases, evaluates and discards.
    * [`CASE`](<22 CASE flow.md>) Runs an action matching a function evaluation.
    * [`IF`](<21 IF flow.md>) Runs an action based on a function evaluation.
    * `MENU|<message>`	
        * Calls 👍 CONFIRM [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
        * If confirmed, repeats the top menu
        <!-- TODO: this should probably be automatic -->
    * `REPEAT|<message>`
        * Calls 👍 CONFIRM [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
        * If confirmed, repeats the current anchor
        * Without a message, just repeats.  
    * [`RUN`](<23 RUN flow.md>) Executes a procedure.

    ---
    <br/>

5. **Prompt commands**

   * `CONFIRM|<message>|<falseProc>`	
       * Calls the [CONFIRM 👍 Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>)
       * If not confirmed, execs `falseProc`.
       * If `falseProc` not given stops the current proc.
       * When stopping the current proc, pops stack.
   * `EAN|<message> >> <key>`	
       * Calls the [🛒 EAN Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>)
   * [`ℹ️ INFO`](<../13 🤔 Prompts/11 ℹ️ INFO prompt.md>) Information.
   * [`⏳ TEMP`](<../13 🤔 Prompts/12 ⏳ TEMP prompt.md>) Temporary message.
   * [`✅ SUCCESS`](<../13 🤔 Prompts/13 ✅ SUCCESS prompt.md>)
   * [`❌ FAILURE`](<../13 🤔 Prompts/14 ❌ FAILURE prompt.md>)
   * [`🔢 INT`](<../13 🤔 Prompts/21 🔢 INT prompt.md>)
   * [`🔄 QUANTITY`](<../13 🤔 Prompts/21 🔄 QUANTITY prompt.md>)
   * [`📍 LOCATION`](<../13 🤔 Prompts/61 📍 LOCATION prompt.md>)
   * `MANY|<message>|<options> >> <key>`	
       * Calls the [🔢 MANY Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
       * Options are comma separated (e.g., `Milk, Sugar, Rice`)
       * Example: `MANY|What items?|Milk,Sugar,Rice >> items`
   * `ONE|<message>|<options> >> <key>`	
       * Calls the [1️⃣ ONE Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
       * Options are comma separated (e.g., `1:Milk, 2:Sugar, R:Rice`)
       * Example: `ONE|What item?|Milk,Sugar,Rice >> item`
   * `SCAN|<message>`	
       * Calls the [🔆 SCAN Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
   * `SELFIE|<message>`	
       * Calls the [👤 SELFIE Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
   * `TOUCH|<message>|<locator>`	
       * Calls the [🦋 TOUCH Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
   * `TRACK|<message>`	
       * Calls the [🗺️ TRACK Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)
   * `UPLOAD|<message>`	
       * Calls the the [⬆️ UPLOAD Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>)

    ---
    <br/>

6. **Behavior commands**

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