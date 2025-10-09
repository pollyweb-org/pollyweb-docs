# 😃⏩🤗 Forward @ Talker

> Implements a [Talker 😃 helper domain](<../../9 😃 Talkers/10 📘 Talker specs/02 😃🛠️ Talker helper.md>)

> Used in: 
> <br/>• [😃⏩🤗 Talk @ Talker](<40 😃⏩🤗 Talk.md>) flow
> <br/>• [😃⏩🤗 Handle @ Talker](<20 😃⏩🤗 Handle.md>)  flow
> <br/>• [😃⏩🤗 Wait @ Talker](<30 😃⏩🤗 Wait.md>)  flow

## Flow

![alt text](<../49 ☁️⏩Hosters/.📎 Assets/Forward.png>)

|#|Step|Purpose
|-|-|-
|1| [😃🐌🤗 `Forward@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/20 😃🐌🤗 Forward.md>) | [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/02 😃🛠️ Talker helper.md>) send [Messages 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) from [Commands ⌘](<../../9 😃 Talkers/20 🌊 Talker flows/10 ⌘ Command.md>)
|2| 🤗⏩🤵 Request 📨 | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) forward them to [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|3| [Receive](<../../6 🅰️ APIs/30 💼🅰️ Consumer/03 🧑‍🦰🐌💼 Receive.md>)
|3| [Consume](<../../6 🅰️ APIs/30 💼🅰️ Consumer/02 🗄️🐌💼 Consume.md>)
|4| [🤗🐌😃 `Returned@Host`](<../../6 🅰️ APIs/52 ☁️🅰️ Hoster/30 🤗🐌😃 Returned.md>) | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) send reply [Messages 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/02 😃🛠️ Talker helper.md>)
|