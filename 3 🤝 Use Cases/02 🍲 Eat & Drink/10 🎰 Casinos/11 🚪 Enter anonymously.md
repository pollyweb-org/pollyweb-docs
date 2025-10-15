# 🎰 Enter anonymously in a casino

> From [Entering casinos 🎰](<01 🎰 Index.md>)

> Mentioned in [Verify Identity-bound Tokens 🆔](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>)

Users can ask their [Identity 🆔 vault](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) for an age-related [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
 (e.g., over 16 years old). 
* At the casino, if users only have the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)
 printed QR or in an NFC card, 
  * the casino then takes a picture of the user with a fixed camera, 
  * and ask the token's [Identity 🆔 vault](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to match the picture. 

* If users have their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) device, 
  * users tap/scan the gate,
  * the casino then opens a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
 on the user's [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>), 
  * asks to share the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>),
  *  then takes a picture to send to the token's [Identity 🆔 vault](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to match it.

<br/>

## 💬 Chat

| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | ⓘ Any Casino (4.4 ⭐) [+]
| 🎰 Casino   | ℹ️ Request for minimum age. [+]
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Share over 21? [Yes, No]      | > Yes
| 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you.   | [📸 selfie](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
| 🎰 Casino   | ✅ Welcome, please enter!
||