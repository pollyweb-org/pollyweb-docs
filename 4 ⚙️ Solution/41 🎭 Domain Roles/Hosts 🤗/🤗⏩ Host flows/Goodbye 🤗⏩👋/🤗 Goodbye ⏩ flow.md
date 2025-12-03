# 🤗⏩🧑‍🦰 Goodbye @ Host

* [Host 🤗 domains](<../../🤗 Host role/🤗🎭 Host role.md>) 
    * inform [Broker 🤵 domains](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) of the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ending, 
    * for them to trigger the [Advertisement 👀 ](<../../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) flow.
* Activated by:
    * [👋 Talker `GOODBYE` command](<../../Host commands/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>)

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) as an example.

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - |
| 🏨 Hotel  | ✅ Booking confirmed! 
| [👀 Ads](<../../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ]
| ⭐ [Rate](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐
|

<br/>

## 😃 Talker 


The associated [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) would be the following.

```yaml
- DONE|Booking confirmed! 
- GOODBYE
```


<br/>

## ⏩ Flow diagram

![Goodbye](<🤗 Goodbye ⚙️ uml.png>)



| # | Call | Notes
|-|-|-
| 1 | [🤗🐌🤵 `Goodbye@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Goodbye 🤗🐌🤵/🤵 Goodbye 🐌 msg.md>) | [Hosts 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) tell [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) of [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) endings
| 2 | [👀⏩🧑‍🦰 Advertise 👀](<../../../../45 🤲 Helper domains/Advertisers 👀/👀⏩ Advertiser flows/Advertise 👀⏩🧑‍🦰/👀 Advertise ⏩ flow.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) ask [Advertisers 👀](<../../../../45 🤲 Helper domains/Advertisers 👀/👀🤲 Advertiser helper.md>) to advertise
| 3 | [⭐⏩🧑‍🦰 Review ⭐](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐⏩ Reviewer flows/01 ⭐⏩🧑‍🦰 Review.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) ask [Reviewers ⭐](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) to review
||
