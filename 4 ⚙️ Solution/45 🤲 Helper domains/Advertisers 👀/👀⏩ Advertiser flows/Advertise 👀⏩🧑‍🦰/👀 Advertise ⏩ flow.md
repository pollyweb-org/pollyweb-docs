# 👀⏩🧑‍🦰 Advertise @ [Advertiser](<../../👀🤲 Advertiser helper.md>)



<br/>

## Flow diagram 

![Advertise](<👀 Advertise ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌👀 Advertise @ Advertiser](<../../👀📨 Advertiser msgs/Advertise 🤵🐌👀/👀 Advertise 🐌 msg.md>) | [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) initiate the advertising with user context
| 2 | [🤵🐌🤗 Summarize @ Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Summarize 🤵🐌🤗/🤗 Summarize 🐌 msg.md>) | Then ask [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to summarize the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
| 3 | [🤗🐌👀 Summarized @ Advertiser](<../../👀📨 Advertiser msgs/Summarized 🤗🐌👀/👀 Summarized 🐌 msg.md>) | [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) notify [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) when summarized
| 4 | [🤗🐌🧚 Anonymize @ Curator](<../../../../50 🫥 Agent domains/Curators 🧚/🧚🅰️ Curator methods/🤗🐌🧚 Anonymize.md>) | Then ask [Curators 🧚](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) to anonymize the summary
| 5 | [🧚🐌👀 Anonymized @ Advertiser](<../../👀📨 Advertiser msgs/Anonymized 🧚🐌👀/👀 Anonymized 🐌 msg.md>) | [Curators 🧚](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) add anonymized summaries to context
| 6 | [👀🐌🧚 Sort @ Curator](<../../../../50 🫥 Agent domains/Curators 🧚/🧚🅰️ Curator methods/👀🐌🧚 Sort.md>) | [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) ask [Curators 🧚](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) to sort possible ads
| 7 | [🧚🐌👀 Sorted @ Advertiser](<../../👀📨 Advertiser msgs/Sorted 🧚🐌👀/👀 Sorted 🐌 msg.md>) | [Curators 🧚](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) return their view of user preferences
| 8 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) show  next best actions to [Wallets 🧑‍🦰](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| 9 | [👀🐌🤵 Promote @ Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Promote 👀🐌🤵/🤵 Promote 🐌 msg.md>) | Then ask [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to check-in into any selection
||

<br/>

## FAQ

1. **How is privacy protected?**

    [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) can't read [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) contents.
    - Instead, [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) and [Curators 🧚](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) summarize and anonymize [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    - [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) generate nest best actions with that anonymous summary.

    ---
    <br/>

1. **How resilient is the process?**

    [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) or [Curators 🧚](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) may fail to do their part.
    - If so, [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) generate based only on context given by [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>)

    ---
    <br/>

1. **How can users avoid ads?**

    [Brokers 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) may not contact [Advertisers 👀](<../../👀🤲 Advertiser helper.md>) at all.
    - For example, users may pay a subscription to avoid seeing generic ads.

    ---
    <br/>

1. **On the last step, why not open the link directly from the Wallet?**

    Effectively, 

    ---
    <br/>