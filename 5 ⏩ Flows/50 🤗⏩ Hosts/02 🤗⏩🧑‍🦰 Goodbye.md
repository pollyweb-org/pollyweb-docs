# 🤗⏩🧑‍🦰 Goodbye @ Host

> [Host 🤗 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) inform [Broker 🤵 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) of the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ending, for them to trigger the [Advertisement 👀 ](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) flow.

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.

| Domain | [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) | User
| - | - | - |
| 🏨 Hotel  | ✅ Booking confirmed! 
| [👀 Ads](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ]
| ⭐ [Reviewer](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐
|

<br/>

## 😃 Talker 


The associated [Talker 😃](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/01 😃 Talker.md>) would be the following.

```yaml
- SUCCESS|Booking confirmed! 
- GOODBYE
```


<br/>

## ⏩ Flow diagram

![Goodbye](<.📎 Assets/⚙️👋 Goodbye.png>)



| # | Call | Notes
|-|-|-
| 1 | [🤗🐌🤵 Goodbye @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/05 🤗🐌🤵 Goodbye.md>) | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) inform [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) of the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ending
| 2 | [👀⏩🧑‍🦰 Advertise](<../05 👀⏩ Advertisers/01 👀⏩🧑‍🦰 Advertise.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask their [Advertisers 👀](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) to advertise
| 3 | [⭐⏩🧑‍🦰 Review @ Reviewer](<../70 ⭐⏩ Reviewers/01 ⭐⏩🧑‍🦰 Review.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to review
||
