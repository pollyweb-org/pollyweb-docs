# 😃📃 Host.Talkers 🪣 table

> About
* Maps a [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * to [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) internally by the [`TALK`](<../../../🤗⌘ Host cmds/TALK 😃/😃 TALK ⌘ cmd.md>) command
    * upon the [`Hello@Host` 🐌 msg](<../../../🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) 
    * depending on the [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key.

<br/>

## Data access

* [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by a [Hoster ☁️ helper domain](<../../../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️🤲 Hoster helper.md>)
* [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by the [`REGISTER`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/REGISTER 🔆/🔆 REGISTER ⌘ cmd.md>) command
* [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) by the [`TALK` command](<../../../🤗⌘ Host cmds/TALK 😃/😃 TALK ⌘ cmd.md>)

<br/>

## Schema

Here's the [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema

```yaml
Prefix: Host
Table: Talkers
Item: Talker
Key: Domain, Key
```

<br/>

## Example

Here's the [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) output.

```yaml
Key: ANY-KEY
Language: en-us
Script: Any-Script
```

Property | Type | Details | Origin | Purpose
|-|-|-|-|-
| `Domain` | text | [domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name  || [`Hello@`](<../../../🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| `Key`| text | [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key || [`Hello@`](<../../../🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| `Script` | text | [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to [`RUN`](<../../../🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| `Language`| text | [`.Translate`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) language || [`Prompt@`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|

