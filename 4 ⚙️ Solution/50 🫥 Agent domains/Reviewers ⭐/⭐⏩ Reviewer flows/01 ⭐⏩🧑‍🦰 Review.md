# ⭐⏩🧑‍🦰 Review chat @ [Reviewer](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>)



## Flow diagram

![Review](<⚙️ Review.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌⭐ `Rate@Reviewer`](<../⭐🅰️ Reviewer methods/🤵🐌⭐ Rate.md>) | [Brokers 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) ask [Reviewers ⭐](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) to review
| 2 | [👥🚀🕸 `Service@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Offer.md>) | [Reviewers ⭐](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) pull specific service questions 
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Reviewers ⭐](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) ask [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) for feedback
| 4 | [⭐🐌🤗 `Rated@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Rated ⭐🐌🤗/🤗 Rated 🐌 msg.md>) | Later, [Reviewers ⭐](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) may report to [Hosts 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
| 5 | [🌬️⏩💼 Ingest @ Consumer](<../../../41 🎭 Domain Roles/Streamers 🌬️/🌬️⏩ Streamer flows/🌬️⏩🔔 Stream/🌬️⏩🔔 Stream.md>) | Later, [Reviewers ⭐](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) alert subscriber [Finders 🔎](<../../Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>)
||


<br/>

## FAQ

1. **How is privacy protected?**
   
    [Reviewer ⭐ domains](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) collect user feedback after every [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) goodbye:
    - it is shared with hosts anonymously, after a period o time, to avoid time mapping;
    - users may ask contacted for follow-up, still anonymized by [Reviewer ⭐ domains](<../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>).

    ---
    <br/>