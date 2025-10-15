# ⭐⏩🧑‍🦰 Review chat @ [Reviewer](<../⭐🫥 Reviewer agent.md>)



## Flow diagram

![Review](<.📎 Assets/⚙️ Review.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌⭐ `Rate@Reviewer`](<../🅰️ Reviewer methods/02 🤵🐌⭐ Rate.md>) | [Brokers 🤵](<../../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Reviewers ⭐](<../⭐🫥 Reviewer agent.md>) to review
| 2 | [👥🚀🕸 `Service@Graph`](<../../../45 🛠️ Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Offer.md>) | [Reviewers ⭐](<../⭐🫥 Reviewer agent.md>) pull specific service questions 
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/30 🤗 Hosts/⏩ Host flows/31 🤗⏩🧑‍🦰 Prompt 🤔 flow.md>) | [Reviewers ⭐](<../⭐🫥 Reviewer agent.md>) ask [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) for feedback
| 4 | [⭐🐌🤗 `Rated@Host`](<../../../41 🎭 Domain Roles/30 🤗 Hosts/59 ⭐🐌🤗 Rated@Host.md>) | Later, [Reviewers ⭐](<../⭐🫥 Reviewer agent.md>) may report to [Hosts 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)
| 5 | [🌬️⏩💼 Ingest @ Consumer](<../../../41 🎭 Domain Roles/75 🌬️ Streamers/⏩ Streamer flows/🌬️⏩🔔 Stream.md>) | Later, [Reviewers ⭐](<../⭐🫥 Reviewer agent.md>) alert subscriber [Finders 🔎](<../../40 🔎 Finders/$ 🔎🫥 Finder agent.md>)
||


<br/>

## FAQ

1. **How is privacy protected?**
   
    [Reviewer ⭐ domains](<../⭐🫥 Reviewer agent.md>) collect user feedback after every [Host 🤗 domain](<../../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) goodbye:
    - it is shared with hosts anonymously, after a period o time, to avoid time mapping;
    - users may ask contacted for follow-up, still anonymized by [Reviewer ⭐ domains](<../⭐🫥 Reviewer agent.md>).

    ---
    <br/>