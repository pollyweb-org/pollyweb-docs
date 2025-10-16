# 👀⏩🧑‍🦰 Advertise @ [Advertiser](<../👀🛠️ Advertiser helper.md>)



<br/>

## Flow diagram 

![Advertise](<../.📎 Assets/⚙️ Advertise.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌👀 Advertise @ Advertiser](<../👀🅰️ Advertiser methods/🤵🐌👀 Advertise.md>) | [Brokers 🤵](<../../24 🤵 Brokers/$ 🤵 Broker domain.md>) initiate the advertising with user context
| 2 | [🤵🐌🤗 Summarize @ Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Summarize.md>) | Then ask [Hosts 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to summarize the [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
| 3 | [🤗🐌👀 Summarized @ Advertiser](<../👀🅰️ Advertiser methods/🤗🐌👀 Summarized.md>) | [Hosts 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) notify [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) when summarized
| 4 | [🤗🐌🧚 Anonymize @ Curator](<../../../50 🫥 Agents/30 🧚 Curators/🧚🅰️ Curator methods/🤗🐌🧚 Anonymize.md>) | Then ask [Curators 🧚](<../../../50 🫥 Agents/30 🧚 Curators/🧚🫥 Curator agent.md>) to anonymize the summary
| 5 | [🧚🐌👀 Anonymized @ Advertiser](<../👀🅰️ Advertiser methods/🧚🐌👀 Anonymized.md>) | [Curators 🧚](<../../../50 🫥 Agents/30 🧚 Curators/🧚🫥 Curator agent.md>) add anonymized summaries to context
| 6 | [👀🐌🧚 Sort @ Curator](<../../../50 🫥 Agents/30 🧚 Curators/🧚🅰️ Curator methods/👀🐌🧚 Sort.md>) | [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) ask [Curators 🧚](<../../../50 🫥 Agents/30 🧚 Curators/🧚🫥 Curator agent.md>) to sort possible ads
| 7 | [🧚🐌👀 Sorted @ Advertiser](<../👀🅰️ Advertiser methods/🧚🐌👀 Sorted.md>) | [Curators 🧚](<../../../50 🫥 Agents/30 🧚 Curators/🧚🫥 Curator agent.md>) return their view of user preferences
| 8 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) show  next best actions to [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| 9 | [👀🐌🤵 Promote @ Broker](<../../../../6 🅰️ APIs/15 🤵🅰️ Broker/20 🤵🅰️ Locators/06 👀🐌🤵 Promote.md>) | Then ask [Brokers 🤵](<../../24 🤵 Brokers/$ 🤵 Broker domain.md>) to check-in into any selection
||

<br/>

## FAQ

1. **How is privacy protected?**

    [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) can't read [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) contents.
    - Instead, [Hosts 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) and [Curators 🧚](<../../../50 🫥 Agents/30 🧚 Curators/🧚🫥 Curator agent.md>) summarize and anonymize [Chats 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
    - [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) generate nest best actions with that anonymous summary.

    ---
    <br/>

1. **How resilient is the process?**

    [Hosts 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) or [Curators 🧚](<../../../50 🫥 Agents/30 🧚 Curators/🧚🫥 Curator agent.md>) may fail to do their part.
    - If so, [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) generate based only on context given by [Brokers 🤵](<../../24 🤵 Brokers/$ 🤵 Broker domain.md>)

    ---
    <br/>

1. **How can users avoid ads?**

    [Brokers 🤵](<../../24 🤵 Brokers/$ 🤵 Broker domain.md>) may not contact [Advertisers 👀](<../👀🛠️ Advertiser helper.md>) at all.
    - For example, users may pay a subscription to avoid seeing generic ads.

    ---
    <br/>

1. **On the last step, why not open the link directly from the Wallet?**

    Effectively, 

    ---
    <br/>