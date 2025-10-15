# Pay at  kiosk to eat in  🍔

> From [Eat fast food 🍔](<01 🍔 Index.md>)


> The user leverages the kiosk's screen to chose what to eat. <br/>When done, they tap the kiosk's locator to see a personalized menu on their phone.

<br/>

## 💬 Chat


| [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/🔎🫥 Finder agent.md>) | ⓘ Any Fast Food (4.3 ⭐)  [+]
| 🍔 Fast Food | ℹ️ Order (£4.00) [+] <br/>- 1 house burger 🍔 (£3.00) <br/> - 1 still water (25 cl) 💧 (£1.00) <br/>  - to deliver at sign 014
| 💖 [Vitalogist](<../../../4 ⚙️ Solution/50 🫥 Agents/95 💖 Vitalogists/$ 💖🫥 Vitalogist agent.md>) | 🫥 Confirm? [Yes, No] <br/> - burger is outside your diet  | > Yes
| 💳 [Payer](<../../../4 ⚙️ Solution/50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Pay £4.00 bill? 🧾 [No] <br/>- [ Card ABC ] + $0.10 <br/>- [ Card DEF ] (free) | > Card ABC |
| 🍔 Fast Food | ✅ Eat-in submitted [+]
| 🍔 Fast Food | ⏳ Order in queue... [+] 
| 🍔 Fast Food | ⏳ Preparing your order... [+] 
| 🍔 Fast Food | ℹ️ Order ready [+]
| 🍔 Fast Food | ⏳ Taking it to sign 014... 
| 🍔 Fast Food | ✅ Eat-in delivered to 014.
| ⭐ [Rate](<../../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐ 5 |
||
