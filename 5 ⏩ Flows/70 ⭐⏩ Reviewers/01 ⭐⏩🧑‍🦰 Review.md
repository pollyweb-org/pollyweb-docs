# ⭐⏩🧑‍🦰 Review chat @ [Reviewer](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>)



## Flow diagram

![Review](<.📎 Assets/⚙️ Review.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌⭐ `Rate@Reviewer`](<../../6 🅰️ APIs/80 ⭐🅰️ Reviewer/02 🤵🐌⭐ Rate.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) ask [Reviewers ⭐](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) to review
| 2 | [👥🚀🕸 `Service@Graph`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/09 👥🚀🕸 Offer.md>) | [Reviewers ⭐](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) pull specific service questions 
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Reviewers ⭐](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) ask [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) for feedback
| 4 | [⭐🐌🤗 `Rated@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/09 ⭐🐌🤗 Rated.md>) | Later, [Reviewers ⭐](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) may report to [Hosts 🤗](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)
| 5 | [🌬️⏩💼 Ingest @ Consumer](<../76  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) | Later, [Reviewers ⭐](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) alert subscriber [Finders 🔎](<../../4 ⚙️ Solution/50 🫥 Agents/40 🔎 Finders/$ 🔎🫥 Finder agent.md>)
||


<br/>

## FAQ

1. **How is privacy protected?**
   
    [Reviewer ⭐ domains](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>) collect user feedback after every [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) goodbye:
    - it is shared with hosts anonymously, after a period o time, to avoid time mapping;
    - users may ask contacted for follow-up, still anonymized by [Reviewer ⭐ domains](<../../4 ⚙️ Solution/50 🫥 Agents/73 ⭐ Reviewers/$ ⭐🫥 Reviewer agent.md>).

    ---
    <br/>