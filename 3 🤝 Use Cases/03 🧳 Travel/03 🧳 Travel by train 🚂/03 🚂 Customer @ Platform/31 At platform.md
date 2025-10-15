At the platform, how to know which train to board?
--

When at the platform, users tap/scan the NFC/QR tags in the platform's walls.

| [Domain](<../../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| | | 🔆 [tap](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
| 🔎 [Finder](<../../../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/$ 🔎🫥 Finder agent.md>) | ⓘ Any Navigator (4.3 ⭐) [+]
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ✅ Sign PA: platform A 🐜 [+] <br/> - MAD T4 train station
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ℹ️ Board the 3rd train. <br/>- your train is at 9:15 <br/>- it says "Nouevos Ministerios"
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ⏳ ETA 9:15, ignore the next 2 trains...
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ⏳ ETA 9:17, ignore the next train...
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | ⏳ ETA 9:17, your train is next...
| 🧭 [Navigator](<../../../../4 ⚙️ Solution/50 🫥 Agents/55 🧭 Navigators/$ 🧭🫥 Navigator agent.md>) | 📣 Arrived, board the train.
||