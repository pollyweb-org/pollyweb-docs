After boarding, how to know if its the right train?
--

When inside a train, users tap/scan an NFC/QR tag in chair or train wall.

- a chat opens confirming that they are in the right train, 
- and the direction they must go to find their carriage and seat. 


| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/$ 🔎🫥 Finder agent.md>) | ⓘ Any Navigator (4.3 ⭐) [+]
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ✅ Train "Nouevos Ministerios" [+]
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ℹ️ Exit at MAD T2. <br/>- exit the train in 2 stops <br/>- it says "Terminals T1/T2/T3" <br/>- you're at a busy wagon <br/>- 1st is empty, 2 wagons back
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ⏳ ETA 9:28, ignore the next stop
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ⏳ ETA 9:28, your stop is next...
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | 📣 Arrived, exit the train.
||