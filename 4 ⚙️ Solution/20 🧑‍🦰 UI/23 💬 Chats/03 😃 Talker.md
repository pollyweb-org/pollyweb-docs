# 😃 Talker FAQ
<!-- https://quip.com/J24GAMbu7HKF/-Talker -->

1. **What is a Talker?**

    [Talkers 😃](<03 😃 Talker.md>) are scripts to render dialogs in a [💬 Chat](<01 💬 Chat.md>).

    ---
    <br/>

1. **Why are Talkers important?**

    [Talkers 😃](<03 😃 Talker.md>) dramatically reduce the time to build a [Host 🤗 domain](<04 🤗🎭 Host role.md>) by simplifying the workflow orchestration of a [💬 Chat](<01 💬 Chat.md>).

    ---
    <br/>

2. **Coding commands**

    * `💬|<title>:`	
        * Top menu entry - i.e., the "what?"
    * `<procedure>:`   
        * Executable procedure.
    * `{function}`	
        * Calculates the value with a function.
  
    ---
    <br/>

    
3. **Flow commands**

    * `CASE|<eval>|<anchor>`	
        * Runs a procedure when the eval is matched 
        * Use case: 👉 Wait for a table: 🧪🍛 Food @ Restaurant
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

4. **Prompt commands**

   * `CONFIRM|<message>|<falseProc>`	
       * Calls 👍 CONFIRM [Prompt 🤔](<02 🤔 Prompt.md>)
       * If not confirmed, execs falseProc.
       * If falseProc not given stops the current proc.
       * When stopping the current proc, pops stack.
   * `DOWNLOAD|<message>|<fileID>|<options>`	
       * Calls the ⬇️ DOWNLOAD [Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are optional, comma separated
       * Example: Erase, Duplicate
   * `EAN|<message>`	
       * Calls the 🛒 EAN [Prompt 🤔](<02 🤔 Prompt.md>)
   * `INFO|<message>`	
       * Calls the ℹ️ INFO [Prompt 🤔](<02 🤔 Prompt.md>)
       * A 2nd call overides the previous
   * `SUCCESS|<message>`
       * Calls the ✅ SUCCESS [Prompt 🤔](<02 🤔 Prompt.md>)
   * `INT|<message>`	
       * Calls the 💯 INT [Prompt 🤔](<02 🤔 Prompt.md>)
   * `LOCATION|<message>`	
       * Calls the 📍 LOCATION [Prompt 🤔](<02 🤔 Prompt.md>)
   * `MANY|<message>|<options>`	
       * Calls the 🔢 MANY [Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are comma separated
       * Example: Milk, Sugar, Rice
   * `MANY|<message>|<options>`	
       * Calls the 🔢 MANY [Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are comma separated
       * Example: Milk, Sugar, Rice
   * `ONE|<message>|<options>`	
       * Calls the 1️⃣ ONE [Prompt 🤔](<02 🤔 Prompt.md>)
       * Options are comma separated
       * Example: 1:Milk, 2:Sugar, R:Rice
   * `QUANTITY|<message>`	
       * Calls the ↕️ QUANTITY [Prompt 🤔](<02 🤔 Prompt.md>)
   * `SCAN|<message>`	
       * Calls the 🔆 SCAN [Prompt 🤔](<02 🤔 Prompt.md>)
   * `SELFIE|<message>`	
       * Calls the 👤 SELFIE [Prompt 🤔](<02 🤔 Prompt.md>)
       * The wallet opens an iFrame on dtfw.<domain>/selfie
       * The wallet closes on another prompt or user action.
   * `TOUCH|<message>|<locator>`	
       * Calls the 🦋 TOUCH [Prompt 🤔](<02 🤔 Prompt.md>)
   * `TRACK|<message>`	
       * Calls the 🗺️ TRACK [Prompt 🤔](<02 🤔 Prompt.md>)
   * `UNTIL|<message>`	
       * Calls the 🗓️ UNTIL [Prompt 🤔](<02 🤔 Prompt.md>)
   * `UPLOAD|<message>`	
       * Calls the the ⬆️ UPLOAD [Prompt 🤔](<02 🤔 Prompt.md>)

    ---
    <br/>

5. **Behavior commands**

   * `BINDABLE|<codes>`	
       * Calls 👉 Advertise bindable: 🗄️ Vault
       * Codes are comma separated
       * Example: iata.org/SSR/WCHR, iata.org/...
   * `CHARGE|<amount>`	
       * Calls 👉 Charge: 💸 Seller
   * `CRUD`	
       * Initiates the CRUD dialog
   * `GOODBYE|<message>`	
       * Calls 👉 Goodbye: 🤗 Host
   * `ISSUE|<code>|{credentialID}`	
       * Calls 👉 Issue token: 🃏 Issuer
       * The function waits for all shares
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With 🧩 /HOST: 🤝🤗 Host.DTFW.org
   * `RESUBSCRIBE|<amount>`	
       * Calls 🐌 Resubscribe: 🤵📎 Broker. Pay()
   * `REVOKE|{credentialID}`	
       * Calls 👉 Revoke token: 🃏 Issuer
   * `SHARE|<code>|<message>`	
       * Calls 👉 Query: 📡 Consumer
       * Groups sequencial shares in one call
   * `SUBSCRIBE|<amount>`	
       * Calls 🐌 Subscribe: 🤵📎 Broker. Pay()
