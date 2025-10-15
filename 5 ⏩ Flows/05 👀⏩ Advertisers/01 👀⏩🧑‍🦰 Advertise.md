# 👀⏩🧑‍🦰 Advertise @ [Advertiser](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>)



<br/>

## Flow diagram 

![Advertise](<.📎 Assets/⚙️ Advertise.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌👀 Advertise @ Advertiser](<../../6 🅰️ APIs/05 👀🅰️ Advertiser/01 🤵🐌👀 Advertise.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) initiate the advertising with user context
| 2 | [🤵🐌🤗 Summarize @ Host](<../../6 🅰️ APIs/50 🤗🅰️ Host/10 🤵🐌🤗 Summarize.md>) | Then ask [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to summarize the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
| 3 | [🤗🐌👀 Summarized @ Advertiser](<../../6 🅰️ APIs/05 👀🅰️ Advertiser/02 🤗🐌👀 Summarized.md>) | [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) notify [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) when summarized
| 4 | [🤗🐌🧚 Anonymize @ Curator](<../../6 🅰️ APIs/35 🧚🅰️ Curator/01 🤗🐌🧚 Anonymize.md>) | Then ask [Curators 🧚](<../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) to anonymize the summary
| 5 | [🧚🐌👀 Anonymized @ Advertiser](<../../6 🅰️ APIs/05 👀🅰️ Advertiser/03 🧚🐌👀 Anonymized.md>) | [Curators 🧚](<../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) add anonymized summaries to context
| 6 | [👀🐌🧚 Sort @ Curator](<../../6 🅰️ APIs/35 🧚🅰️ Curator/02 👀🐌🧚 Sort.md>) | [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) ask [Curators 🧚](<../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) to sort possible ads
| 7 | [🧚🐌👀 Sorted @ Advertiser](<../../6 🅰️ APIs/05 👀🅰️ Advertiser/04 🧚🐌👀 Sorted.md>) | [Curators 🧚](<../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) return their view of user preferences
| 8 | [🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) show  next best actions to [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| 9 | [👀🐌🤵 Promote @ Broker](<../../6 🅰️ APIs/15 🤵🅰️ Broker/20 🤵🅰️ Locators/06 👀🐌🤵 Promote.md>) | Then ask [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to check-in into any selection
||

<br/>

## FAQ

1. **How is privacy protected?**

    [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) can't read [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) contents.
    - Instead, [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) and [Curators 🧚](<../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) summarize and anonymize [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
    - [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) generate nest best actions with that anonymous summary.

    ---
    <br/>

1. **How resilient is the process?**

    [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) or [Curators 🧚](<../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) may fail to do their part.
    - If so, [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) generate based only on context given by [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)

    ---
    <br/>

1. **How can users avoid ads?**

    [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) may not contact [Advertisers 👀](<../../4 ⚙️ Solution/45 Helpers/12 👀 Advertisers/03 👀👥 Advertiser helper.md>) at all.
    - For example, users may pay a subscription to avoid seeing generic ads.

    ---
    <br/>

1. **On the last step, why not open the link directly from the Wallet?**

    Effectively, 

    ---
    <br/>