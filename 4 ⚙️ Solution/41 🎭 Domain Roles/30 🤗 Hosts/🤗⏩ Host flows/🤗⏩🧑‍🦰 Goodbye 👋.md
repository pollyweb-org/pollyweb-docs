# 🤗⏩🧑‍🦰 Goodbye @ Host

* [Host 🤗 domains](<../🤗🎭 Host role.md>) 
    * inform [Broker 🤵 domains](<../../../45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) of the [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ending, 
    * for them to trigger the [Advertisement 👀 ](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀🛠️ Advertiser helper.md>) flow.
* Activated by:
    * [👋 Talker `GOODBYE` command](<../../../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>)

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) as an example.

| [Domain](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🏨 Hotel  | ✅ Booking confirmed! 
| [👀 Ads](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀🛠️ Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ]
| ⭐ [Rate](<../../../50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐
|

<br/>

## 😃 Talker 


The associated [Talker 😃](<../../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) would be the following.

```yaml
- SUCCESS|Booking confirmed! 
- GOODBYE
```


<br/>

## ⏩ Flow diagram

![Goodbye](<../.📎 Assets/⚙️👋 Goodbye.png>)



| # | Call | Notes
|-|-|-
| 1 | [🤗🐌🤵 `Goodbye@Broker`](<../../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/05 🤗🐌🤵 Goodbye.md>) | [Hosts 🤗](<../🤗🎭 Host role.md>) tell [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) of [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) endings
| 2 | [👀⏩🧑‍🦰 Advertise 👀](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀⏩ Advertiser flows/👀⏩🧑‍🦰 Advertise.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Advertisers 👀](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀🛠️ Advertiser helper.md>) to advertise
| 3 | [⭐⏩🧑‍🦰 Review ⭐](<../../../50 🫥 Agents/73 ⭐ Reviewers/⏩ Reviewer flows/01 ⭐⏩🧑‍🦰 Review.md>) | [Brokers 🤵](<../../../45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Reviewers ⭐](<../../../50 🫥 Agents/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) to review
||
