# 🌭 Serve food at a street market stall

> From [Eat street food 🌭](<01 🌭 Index.md>)

> Mentioned in [Verify Identity-bound Tokens 🆔](<../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

At the street market, vendors access the stall chat.
- the supporter prepares the trays with a name.
- the chef prepares the food and places it on the right tray.

## 💬 Chat


| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Stall (4.4 ⭐) [+]
| 🤵 [Broker](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | ⓘ Staff [🪪 token](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) shared [+]
| 🎪 Stall  | 😃 Hi Daniel, what's up? <br/>- [ Serve ] customers  <br/>- [ Something else ] | > Serve 
| 🎪 Stall  | [� Share location?](<../../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/91 📍 LOCATION prompt.md>) | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.  | [📸 selfie](<../../../4 ⚙️ Solution/50 🫥 Agents/45 🆔 Identities/21 🆔😶 Face scan.md>)
| 🎪 Stall  | ⏳ Waiting requests... <br/> - [ Bill ] <br/> - [ Pause  shift ] <br/> 
|...
||