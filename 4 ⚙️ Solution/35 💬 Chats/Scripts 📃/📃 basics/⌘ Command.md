# 😃⌘ Talker `<Command>`

> Part of [Talker 😃](<../../Talkers 😃/😃 Talker role.md>)

<br/>

1. **What is a Talker Command?**

    A `<Command>`
    * is a line starting with a dash `-`
    * that executes a [Prompt 🤔](<../../Prompts 🤔/🤔 Prompt.md>) or a workflow.

    ---
    <br/>


1. **What are Prompt commands?**

    These are Commands that execute [Prompts 🤔](<../../Prompts 🤔/🤔 Prompt.md>).

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
    | ℹ️ [`INFO`](<../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | Information message.
    | ⏳ [`TEMP`](<../../Prompts 🤔/🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>) |Temporary status message.
    | ✅ [`SUCCESS`](<../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) | Successful status message.
    | ❌ [`FAILURE`](<../../Prompts 🤔/🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>) | Unsuccessful status message.

    ---
    <br/>

1. **What are the Input prompt commands?**
    
    |Command |  Example | Purpose
    |-|-|-
    | 🔠 [`TEXT`](<../../Prompts 🤔/🤔✏️ Prompt inputs/TEXT 🔠/TEXT 🔠 prompt.md>) | Bla | Unstructured text | 
    | ↕️ [`QUANTITY`](<../../Prompts 🤔/🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) | 123| Numbers with ⬆️ ⬇️ arrows |
    | 🔢 [`DIGITS`](<../../Prompts 🤔/🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) |0123| Numerics with 0 prefix | 
    | 💰 [`AMOUNT`](<../../Prompts 🤔/🤔✏️ Prompt inputs/AMOUNT 💰/AMOUNT 💰 prompt.md>) |  1.23 | Decimals and currency
    | ⭐ [`RATE`](<../../Prompts 🤔/🤔✏️ Prompt inputs/RATE ⭐/RATE ⭐ prompt.md>) | 5 ⭐ | Integer from 1 to 5
    | 🔑 [`OTP`](<../../Prompts 🤔/🤔✏️ Prompt inputs/OTP 🔑/OTP 🔑 prompt.md>) | 0123 | SIM one time password
    | 👍 [`CONFIRM`](<../../Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Yes | `Yes` `No` `Cancel` answer
    | 🔠 [`MANY`](<../../Prompts 🤔/🤔✏️ Prompt inputs/MANY 🔠/🔠 MANY ⌘ cmd.md>) | [A,B] |
    | 1️⃣ [`ONE`](<../../Prompts 🤔/🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) | A |
    | 📆 [`DATE`](<../../Prompts 🤔/🤔✏️ Prompt inputs/DATE 📆/DATE 📆 prompt.md>)
    | 🕓 [`TIME`](<../../Prompts 🤔/🤔✏️ Prompt inputs/TIME 🕓/TIME 🕓 prompt.md>)
    | 👤 [`IDENTITY`](<../../Prompts 🤔/🤔✏️ Prompt inputs/IDENTIFY 👤/IDENTIFY 👤 prompt.md>)
    | 🔆 [`SCAN`](<../../Prompts 🤔/🤔✏️ Prompt inputs/SCAN 🔆/SCAN 🔆 prompt.md>)
    | 🦋 [`TOUCH`](<../../Prompts 🤔/🤔✏️ Prompt inputs/TOUCH 🦋/TOUCH 🦋 prompt.md>)
    | 🛒 [`EAN`](<../../Prompts 🤔/🤔✏️ Prompt inputs/EAN 🛒/EAN 🛒 prompt.md>)
    | ⬆️ [`UPLOAD`](<../../Prompts 🤔/🤔✏️ Prompt inputs/UPLOAD ⬆️/UPLOAD ⬆️ prompt.md>)
    | 📍 [`LOCATION`](<../../Prompts 🤔/🤔✏️ Prompt inputs/LOCATION 📍/LOCATION 📍 prompt.md>)
    | 🗺️ [`TRACK`](<../../Prompts 🤔/🤔✏️ Prompt inputs/TRACK 🗺️/TRACK 🗺️ prompt.md>)

    ---
    <br/>

1. **What are Message commands?**

    <!-- TODO: Finish the table -->

    |Command|Purpose
    |-|-
    | 🔗 [`BIND`](<../📃 methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | Calls the [Bind Vault @ Wallet ⏩](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>) flow.
    | 🎫 [`ISSUE`](<../📃 methods 🤵/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) | Calls the [Save Token @ Wallet ⏩](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>) flow.
    | 👋 [`GOODBYE`](<../📃 methods 🤵/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) | Calls the [Goodbye @ Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Goodbye 🤗⏩👋/🤗 Goodbye ⏩ flow.md>) ⏩ flow.
    | 📜 [`FLOW`](<../📃 methods 🤵/INFORM 📝/📝 INFORM ⌘ cmd.md>)
    | 💳 [`CHARGE`](<../📃 methods 🤵/CHARGE 💳/💳 CHARGE ⌘ cmd.md>)
    | 💼 [`SHARE`](<../📃 methods 🤵/SHARE 💼/💼 SHARE ⌘ cmd.md>)
    | 🛰️ [`RELAY`](<../📃 methods 🤵/RELAY 🛰️/🛰️ RELAY ⌘ cmd.md>)
    |
    
   
   * `CRUD`	
       * Initiates the CRUD dialog

   
   * `REDIRECT|{host}|{locator}`	
       * Calls 👉 Check-in: 👱📎 Wallet. Sessions
       * With [🧩 nlweb.dom/HOST](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
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
    | ⏯️️ [`CASE`](<../📃 control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) | Runs a [Command ⌘](<⌘ Command.md>) or [Script 📃](<../📃 functions 🐍/{Function} 🐍.md>).
    | 🫥 [`EMOJI`](<../../Prompts 🤔/🤔✏️ Prompt input features/😶⌘ EMOJI cmd.md>) | Changes the [default emoji 😃](<../../Prompts 🤔/🤔✏️ Prompt input features/😶 Input emojis.md>) for [input prompts ✏️](<../../Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>).
    | ⬇️ [`EVAL`](<../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) | Evaluates a [{Function}](<../📃 functions 🐍/{Function} 🐍.md>) into a holder.
    | ⤵️ [`IF`](<../📃 control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) | Runs a [Command ⌘](<⌘ Command.md>) or [Script 📃](<../📃 functions 🐍/{Function} 🐍.md>).
    | 🪵 [`LOG`](<../📃 control ▶️/LOG 🪵/🪵 LOG ⌘ cmd.md>) | Logs messages into the system handler.
    | 🔁 [`REPEAT`](<../📃 control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) | Repeats the current [Script 📃](<📃 Script.md>) with a confirmation.
    | ⤴️ [`RETURN`](<../📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) | Returns from a [Script 📃](<📃 Script.md>) with a result.
    | ▶️ [`RUN`](<../📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) | Runs a [Script 📃](<📃 Script.md>) and puts the result in a holder.
    | 🧘 [`WAIT`](<../📃 control ▶️/WAIT 🧘/🧘 WAIT ⌘ cmd.md>) | Waits for a period of time or until signaled.

    ---
    <br/>


1. **How to create custom commands?**

    |#|Step|Details
    |-|-|-
    |1| `Upload` | Upload the [Script 📃](<📃 Script.md>) for the [Command ⌘](<⌘ Command.md>)
    |2| `Parse` | Parse it at the [`Parse@Hosted` 🅰️ method](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 request.md>)
    |3| `Register`| Register it on the [`Commands.yaml` ⌘ file](<../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/📄⌘ Commands file.md>) 
    

    ---
    <br/>

1. **How to build a customer `ECHO` command?**

    Here's the [Chat 💬](<../../Chats 💬/💬 Chat.md>)

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Test ] my echo | > Test
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 💬 Say something | `Test`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Custom echo `Test`
    |

    <br/>

    Here's the [Script 📃](<📃 Script.md>) for the [`Hello@Host` 🅰️ method](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Goodbye 🤗⏩👋/🤗 Goodbye ⏩ flow.md>) 

    ```yaml
    💬 /Test my echo:
    - TEXT|Say something >> $something
    - ECHO|$something
    ```
    Commands: [`TEXT`](<../../Prompts 🤔/🤔✏️ Prompt inputs/TEXT 🔠/TEXT 🔠 prompt.md>)

    <br/>

    Here's the `ECHO` [Script 📃](<📃 Script.md>)

    ```yaml
    📃 .ECHO:
    - INFO|Custom echo `{$:UserInput}`
    ```
    Commands: [`INFO`](<../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    <br/>

    Here's the python handler for the [`Parse@Hosted` 🅰️ method](<../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 request.md>)

    ```python
    def talkerParser(args):
        match args['Command']:
            case 'ECHO':

                # Get the raw input
                #   ECHO|$something
                input_str = args['Input']             

                # Extract the holder
                #   $something
                parts = input_str.split("|", 1)       
                holder = parts[1] if len(parts) > 1 else ""

                # Instruct what to do next
                return {
                    'RUN|.ECHO': {
                        'UserInput': holder
                    }
                }
    ```
    Commands: [`RUN`](<../📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)

    ---
    <br/>