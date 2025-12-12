# 🤵🔆 Broker locators

> About
* These are the [Scripts 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) invoked by [`Hello@Host` 🐌 msg](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
* This map is loaded into the [`Host.Talkers` 🪣 table](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Talkers 😃 table/Talkers 🪣/😃 Host.Talkers 🪣 table.md>) by [Hoster ☁️ helper domains](<../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️ Hoster 🤲 helper.md>)

<br/>

## Schemas

| [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [Talker 😃](<../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>) | Inputs | Purpose
|-|-|-|-
| `.HOST/WELCOME` | [`Welcome`](<../🤵😃 Broker talkers/Welcome 💬 talker/🤵 Welcome 😃 handler.md>) | `Chat` `Domain` | Introduces a [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

<br/>

## Locators

| [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) | [Talker 😃](<../../../35 💬 Chats/Talkers 😃/😃 Talker/😃🤲 Talker helper.md>) | Inputs | Purpose
|-|-|-|-
| `PopWallet` | [`PopWallet`](<../🤵😃 Broker talkers/PopWallet 🧑‍🦰 talker/Wallet/🤵 PopWallet 😃 handler.md>) | | Context menu for [Wallets 🧑‍🦰](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| `PopChat` | [`PopChat`](<../🤵😃 Broker talkers/PopChat 💬 talker/Chat/🤵 PopChat 😃 handler.md>) | `Chat` | Context menu for [Chats 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
| `PopBind`| [`PopBind`](<../🤵😃 Broker talkers/PopBind 🔗 talker/Bind/🤵 PopBind 😃 handler.md>) | `Vault` `Bind` | Context menu for [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| `PopToken` | [`PopToken`](<../🤵😃 Broker talkers/PopToken 🎫 talker/Token/🤵 PopToken 😃 handler.md>) | `Issuer` `Token` | Context menu for [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)