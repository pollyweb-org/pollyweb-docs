<!-- TODO: replace call links -->

# 😃 Talker FAQ
<!-- https://quip.com/J24GAMbu7HKF/-Talker -->

1. **What is a Talker?**

    [Talkers 😃](<03 😃 Talker.md>) are scripts to render dialogs in a [💬 Chat](<01 💬 Chat.md>).

    ---
    <br/>

1. **Why are Talkers important?**

    [Talkers 😃](<03 😃 Talker.md>) dramatically reduce the time to build a [Host 🤗 domain](<04 🤗🎭 Host role.md>) by simplifying the workflow orchestration of a [💬 Chat](<01 💬 Chat.md>).

    * They allow [Hoster 🧑‍💻 helper domains](<05 🧑‍💻🛠️ Hoster helper.md>) to manage the workflow state on behalf of [Host 🤗 domains](<04 🤗🎭 Host role.md>), removing the undifferentiated heavy-lifting of handling [Prompts 🤔](<02 🤔 Prompt.md>) communications, and invoking [Host 🤗 domains](<04 🤗🎭 Host role.md>) only when it's necessary to execute business-specific logic.
  
    ---
    <br/>

2. **What are examples of Talkers?**

    |Example
    |-
    | [🏪 Buy drinks at vending machines](<../../../3 🤝 Use Cases/02 🍽️ Eat & Drink/01 🏪 Drink at vendings/01 🏪 Index.md>)

    ---
    <br/>

3. **Coding commands**

    * `💬|<title>:`	
        * Top menu entry - i.e., the "what?"
    * `<procedure>:`   
        * Executable procedure.
    * `{function}`	
        * Calculates the value with a function.
  
    ---
    <br/>

    
4. **Flow commands**

    * `CASE|<eval>|<anchor>`	
        * Runs a procedure when the eval is matched 
    * `EVAL|{function}`	
        * Calculates something to be used in cases.
        * Without a function, uses the last answer.
        * Without cases, evaluates and discards.
    * `IF|{func}|<trueProc>`	
        * Runs a procedure based on a function
    * `IF|{func}|<trueProc>|<falseProc>`	
        * Runs procedures based on a function
    * `MENU|<message>`	
        * Calls 👍 CONFIRM [Prompt 🤔](<02 🤔 Prompt.md>)
        * If confirmed, repeats the top menu
        <!-- TODO: this should probably be automatic -->
    * `REPEAT|<message>`
        * Calls 👍 CONFIRM [Prompt 🤔](<02 🤔 Prompt.md>)
        * If confirmed, repeats the current anchor
        * Without a message, just repeats.  
    * `RUN|<procedure>`	
        * Executes a procedure

    ---
    <br/>

5. **Prompt commands**

   * `CONFIRM|<message>|<falseProc>`	
       * Calls the [CONFIRM 👍 Prompt](<02 🤔 Prompt.md>)
       * If not confirmed, execs `falseProc`.
       * If `falseProc` not given stops the current proc.
       * When stopping the current proc, pops stack.
   * `DOWNLOAD|<message>|<fileID>|<options>`	
       * Calls the [⬇️ DOWNLOAD Prompt](<02 🤔 Prompt.md>)
       * Options are optional, comma separated
       * Example: `Erase, Duplicate`
   * `EAN|<message>`	
       * Calls the [🛒 EAN Prompt](<02 🤔 Prompt.md>)
   * `INFO|<message>`	
       * Calls the [ℹ️ INFO Prompt 🤔](<02 🤔 Prompt.md>)
       * A second call overrides the previous
   * `TEMP|<message>`
       * Calls the [⏳ TEMP Prompt 🤔](<02 🤔 Prompt.md>)
       * Disappears any new [Prompt 🤔](<02 🤔 Prompt.md>)
   * `SUCCESS|<message>`
       * Calls the [✅ SUCCESS Prompt 🤔](<02 🤔 Prompt.md>)
   * `FAILURE|<message>`
       * Calls the [❌ FAILURE Prompt 🤔](<02 🤔 Prompt.md>)
   * `INT|<message>`	
       * Calls the [💯 INT Prompt 🤔](<02 🤔 Prompt.md>)
   * `LOCATION|<message>`	
       * Calls the [📍 LOCATION Prompt 🤔](<02 🤔 Prompt.md>)
   * `MANY|<message>|<options>`	
       * Calls the [🔢 MANY Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are comma separated
       * Example: `Milk, Sugar, Rice`
   * `MANY|<message>|<options>`	
       * Calls the [🔢 MANY Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are comma separated
       * Example: `Milk, Sugar, Rice`
   * `ONE|<message>|<options>`	
       * Calls the [1️⃣ ONE Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are comma separated
       * Example: `1:Milk, 2:Sugar, R:Rice`
   * `QUANTITY|<message>`	
       * Calls the [↕️ QUANTITY Prompt 🤔](<02 🤔 Prompt.md>)
   * `SCAN|<message>`	
       * Calls the [🔆 SCAN Prompt 🤔](<02 🤔 Prompt.md>)
   * `SELFIE|<message>`	
       * Calls the [👤 SELFIE Prompt 🤔](<02 🤔 Prompt.md>)
   * `TOUCH|<message>|<locator>`	
       * Calls the [🦋 TOUCH Prompt 🤔](<02 🤔 Prompt.md>)
   * `TRACK|<message>`	
       * Calls the [🗺️ TRACK Prompt 🤔](<02 🤔 Prompt.md>)
   * `UNTIL|<message>`	
       * Calls the [🗓️ UNTIL Prompt 🤔](<02 🤔 Prompt.md>)
   * `UPLOAD|<message>`	
       * Calls the the [⬆️ UPLOAD Prompt 🤔](<02 🤔 Prompt.md>)

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
   * `CHARGE|<amount>`	
       * Calls [💵🐌🤵 Charge @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/70 🤵🅰️ Pay/21 💵🐌🤵 Charge.md>)
   * `CRUD`	
       * Initiates the CRUD dialog
   * `GOODBYE|<message>`	
       * Calls 👉 Goodbye: 🤗 Host
   * `ISSUE|<code>|{credentialID}`	
       * Calls [🎴⏩🧑‍🦰 Offer token](<../../../5 ⏩ Flows/06 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>)
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