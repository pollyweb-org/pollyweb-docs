# 🤗⏩🧑‍🦰 Goodbye @ Host

* [Host 🤗 domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
    * inform [Broker 🤵 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) of the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ending, 
    * for them to trigger the [Advertisement 👀 ](<../../4 ⚙️ Solution/45 🛠️ Helper domains/12 👀 Advertisers/$ 👀👥 Advertiser helper.md>) flow.
* Activated by:
    * [👋 Talker `GOODBYE` command](<../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>)

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) as an example.

| [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🏨 Hotel  | ✅ Booking confirmed! 
| [👀 Ads](<../../4 ⚙️ Solution/45 🛠️ Helper domains/12 👀 Advertisers/$ 👀👥 Advertiser helper.md>) | 🫥 Explore follow-up actions? [No] <br/>- [ Book a city tour 🚌 ]  <br/>- [ See a flamenco show 💃 ]
| ⭐ [Rate](<../../4 ⚙️ Solution/30 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer vault.md>) | 🫥 Experience feedback? | ⭐⭐⭐⭐
|

<br/>

## 😃 Talker 


The associated [Talker 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) would be the following.

```yaml
- SUCCESS|Booking confirmed! 
- GOODBYE
```


<br/>

## ⏩ Flow diagram

![Goodbye](<.📎 Assets/⚙️👋 Goodbye.png>)



| # | Call | Notes
|-|-|-
| 1 | [🤗🐌🤵 `Goodbye@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/05 🤗🐌🤵 Goodbye.md>) | [Hosts 🤗](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) tell [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) of [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) endings
| 2 | [👀⏩🧑‍🦰 Advertise 👀](<../../4 ⚙️ Solution/45 🛠️ Helper domains/12 👀 Advertisers/01 👀⏩🧑‍🦰 Advertise.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Advertisers 👀](<../../4 ⚙️ Solution/45 🛠️ Helper domains/12 👀 Advertisers/$ 👀👥 Advertiser helper.md>) to advertise
| 3 | [⭐⏩🧑‍🦰 Review ⭐](<../70 ⭐⏩ Reviewers/01 ⭐⏩🧑‍🦰 Review.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer vault.md>) to review
||
