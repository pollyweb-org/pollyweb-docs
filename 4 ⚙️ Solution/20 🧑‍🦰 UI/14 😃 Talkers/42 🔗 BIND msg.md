# 🔗 Talker BIND message

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a BIND message command?**

    A `BIND`
    * is a message [Command](<10 Command.md>) 
    * that invokes the [Bind@Vault ⏩ flow](<../../../5 ⏩ Flows/80 🗄️⏩ Vaults/01 🗄️⏩🧑‍🦰 Bind.md>).

    ---
    <br/>


2. **What's the BIND syntax?**

   ```yaml
   BIND >> <binds>:
       - <code-1>
       - <code-n>
   ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>` | Array of bindable [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>)
    | `<binds>`  |

    ---
    <br/>

3. **What does a Chat look like?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | ...
    | 🗄️ [Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ℹ️ [Let's bind you.](<../13 🤔 Prompts/11 ℹ️ INFO prompt.md>)
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Bind to Any Vault?](<42 🔗 BIND msg.md>) [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
    | 🗄️ [Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | ✅ [Done! Your wallet is bound.](<../13 🤔 Prompts/13 ✅ SUCCESS prompt.md>)


       * Calls [🗄️🐌🤵 Bindable @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/42 🗄️🐌🤵 Bindable.md>) 
       * Codes are comma separated
       * Example: `iata.org/SSR/WCHR`, `iata.org/...`



       | Command | Purpose
       |-|-
       | ℹ️ [INFO](<../13 🤔 Prompts/11 ℹ️ INFO prompt.md>) | To show the first message.
       |  | 
       | ⤵️ [IF](<21 ⤵️ IF flow.md>) | To verify the result.
       | ✅ [SUCCESS](<../13 🤔 Prompts/13 ✅ SUCCESS prompt.md>) | To report success.
       | ❌ [FAILURE](<../13 🤔 Prompts/14 ❌ FAILURE prompt.md>) | To report nothing was bound.    