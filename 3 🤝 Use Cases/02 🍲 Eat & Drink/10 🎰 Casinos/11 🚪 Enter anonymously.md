# 🎰 Enter anonymously in a casino

> From [Entering casinos 🎰](<01 🎰 Index.md>)

> Mentioned in [Verify Identity-bound Tokens 🆔](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

Users can ask their [Identity 🆔 vault](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) for an age-related [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>)
 (e.g., over 16 years old). 
* At the casino, if users only have the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>)
 printed QR or in an NFC card, 
  * the casino then takes a picture of the user with a fixed camera, 
  * and ask the token's [Identity 🆔 vault](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) to match the picture. 

* If users have their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) device, 
  * users tap/scan the gate,
  * the casino then opens a [Chat 💬](<../../../4 ⚙️ Solution/35 Chats/12 💬 Chats/💬 Chat.md>)
 on the user's [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>), 
  * asks to share the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>),
  *  then takes a picture to send to the token's [Identity 🆔 vault](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) to match it.

<br/>

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/25 Locators/15 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Casino (4.4 ⭐) [+]
| 🎰 Casino   | ℹ️ Request for minimum age. [+]
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]      | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/21 🆔😶 Face scan.md>)
| 🎰 Casino   | ✅ Welcome, please enter!
||