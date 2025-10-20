# 😃 Talker `<Command>`

> Part of [Talker 😃](<../../😃 Talker.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../../../🤔 Prompts/🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../../../🤔 Prompts/🤔 Prompt.md>).

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
    | ℹ️ [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../../../🤔 Prompts/🤔📢 Prompt status/TEMP ⏳ prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../../../🤔 Prompts/🤔📢 Prompt status/FAILURE ❌ prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/32 🔠 TEXT prompt.md>) | Bla | Unstructured text | 
    | ↕️ [`QUANTITY`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/42 ↕️ QUANTITY prompt.md>) | 123| Numbers with ⬆️ ⬇️ arrows |
    | 🔢 [`DIGITS`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/44 🔢 DIGITS prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/43 💰 AMOUNT prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/46 ⭐ RATE prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/57 🔑 OTP prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/54 🔠 MANY prompt.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>) | A |
    | 📆 [`DATE`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/61 📆 DATE prompt.md>)
    | 🕓 [`TIME`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/62 🕓 TIME prompt.md>)
    | 👤 [`IDENTITY`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/71 👤 IDENTIFY prompt.md>)
    | 🔆 [`SCAN`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/72 🔆 SCAN prompt.md>)
    | 🦋 [`TOUCH`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/73 🦋 TOUCH prompt.md>)
    | 🛒 [`EAN`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/74 🛒 EAN prompt.md>)
    | ⬆️ [`UPLOAD`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/81 ⬆️ UPLOAD prompt.md>)
    | 📍 [`LOCATION`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/91 📍 LOCATION prompt.md>)
    | 🗺️ [`TRACK`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/92 🗺️ TRACK prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<../for flows/BIND 🔗 msg.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉🗄️ Bind 🔗.md>) flow.
    | 🎫 [`ISSUE`](<../for flows/ISSUE 🎫 msg.md>) | Calls the [Save Token @ Wallet ⏩](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉🎴 Save token.md>) flow.
    | 👋 [`GOODBYE`](<../for flows/GOODBYE 👋 msg.md>) | Calls the [Goodbye @ Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Goodbye 👋.md>) ⏩ flow.
    | 📜 [`FLOW`](<../for flows/INFORM 📝 msg.md>)
    | 💳 [`CHARGE`](<../for flows/CHARGE 💳 msg.md>)
    | 💼 [`SHARE`](<../for flows/SHARE 💼 msg.md>)
    | 🛰️ [`RELAY`](<../for flows/RELAY 🛰️ msg.md>)
    |
    
   
   * `CRUD`	
       * Initiates the CRUD dialog

   
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.dom/HOST](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
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
    | ⏯️️ [`CASE`](<CASE ⏯️.md>) | Runs a [Command ⌘](<⌘ Command.md>) or [Script 📃](<📃 Script.md>) matching a [{Function}](<../for data/{Function} 🐍.md>).
    | 🫥 [`EMOJI`](<../../../🤔 Prompts/🤔✏️ Prompt input features/16 😶⌘ EMOJI cmd.md>) | Changes the [default emoji 😃](<../../../🤔 Prompts/🤔✏️ Prompt input features/14 😶 Input emojis.md>) for [input prompts ✏️](<../../../🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>).
    | ⬇️ [`EVAL`](<../for data/EVAL ⬇️ flow.md>) | Evaluates a [{Function}](<../for data/{Function} 🐍.md>) into a placeholder.
    | ⤵️ [`IF`](<IF ⤵️.md>) | Runs a [Command ⌘](<⌘ Command.md>) or [Script 📃](<📃 Script.md>) based on a [{Function}](<../for data/{Function} 🐍.md>).
    | 🪵 [`LOG`](<../for data/LOG 🪵 flow.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<REPEAT 🔁.md>) | Repeats the current [Script 📃](<📃 Script.md>) with a confirmation.
    | ⤴️ [`RETURN`](<RETURN ⤴️.md>) | Returns from a [Script 📃](<📃 Script.md>) with a result.
    | ▶️ [`RUN`](<RUN ▶️.md>) | Runs a [Script 📃](<📃 Script.md>) and puts the result in a placeholder.
    | ⏸️ [`WAIT`](<WAIT ⏸️.md>) | Waits for a period of time or until signaled.

    ---
    <br/>
