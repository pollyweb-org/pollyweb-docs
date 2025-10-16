# 🤗⏩🧑‍🦰 Goodbye @ Host

* [Host 🤗 domains](<../🤗🎭 Host role.md>) 
    * inform [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) of the [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) ending, 
    * for them to trigger the [Advertisement 👀 ](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀🤲 Advertiser helper.md>) flow.
* Activated by:
    * [👋 Talker `GOODBYE` command](<../../../90 👷 Build/😃 Talkers/😃📨 Talker msgs/50 👋 GOODBYE.md>)

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) as an example.

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🏨 Hotel  | ✅ Booking confirmed! 
| [👀 Ads](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀🤲 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ]
| ⭐ [Rate](<../../../50 🫥 Agent domains/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐
|

<br/>

## 😃 Talker 


The associated [Talker 😃](<../../../90 👷 Build/😃 Talkers/😃 Talker.md>) would be the following.

```yaml
- SUCCESS|Booking confirmed! 
- GOODBYE
```


<br/>

## ⏩ Flow diagram

![Goodbye](<../.📎 Assets/⚙️👋 Goodbye.png>)



| # | Call | Notes
|-|-|-
| 1 | [🤗🐌🤵 `Goodbye@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Goodbye.md>) | [Hosts 🤗](<../🤗🎭 Host role.md>) tell [Brokers 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) of [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) endings
| 2 | [👀⏩🧑‍🦰 Advertise 👀](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀⏩ Advertiser flows/👀⏩🧑‍🦰 Advertise.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) ask [Advertisers 👀](<../../../45 🤲 Helper domains/12 👀 Advertisers/👀🤲 Advertiser helper.md>) to advertise
| 3 | [⭐⏩🧑‍🦰 Review ⭐](<../../../50 🫥 Agent domains/73 ⭐ Reviewers/⏩ Reviewer flows/01 ⭐⏩🧑‍🦰 Review.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) ask [Reviewers ⭐](<../../../50 🫥 Agent domains/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) to review
||
