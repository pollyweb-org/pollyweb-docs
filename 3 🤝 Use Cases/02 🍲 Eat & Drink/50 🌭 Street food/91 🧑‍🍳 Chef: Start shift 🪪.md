# 🌭 Serve food at a street market stall

> From [Eat street food 🌭](<01 🌭 Index.md>)

> Mentioned in [Verify Identity-bound Tokens 🆔](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

At the street market, vendors access the stall chat.
- the supporter prepares the trays with a name.
- the chef prepares the food and places it on the right tray.

## 💬 Chat


| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Stall (4.4 ⭐) [+]
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | ⓘ Staff [🪪 token](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) shared [+]
| 🎪 Stall  | 😃 Hi Daniel, what's up? <br/>- [ Serve ] customers  <br/>- [ Something else ] | > Serve 
| 🎪 Stall  | [� Share location?](<../../../9 😃 Talkers/Prompts/30 Input prompts/91 📍 LOCATION prompt.md>) | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
| 🎪 Stall  | ⏳ Waiting requests... <br/> - [ Bill ] <br/> - [ Pause  shift ] <br/> 
|...
||