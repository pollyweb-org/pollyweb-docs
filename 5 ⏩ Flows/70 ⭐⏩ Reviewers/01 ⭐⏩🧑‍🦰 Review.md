# ⭐⏩🧑‍🦰 Review chat @ [Reviewer](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>)



## Flow diagram

![Review](<.📎 Assets/⚙️ Review.png>)


| # | Call | Notes
|-|-|-
| 1 | [🤵🐌⭐ `Rate@Reviewer`](<../../6 🅰️ APIs/80 ⭐🅰️ Reviewer/02 🤵🐌⭐ Rate.md>) | [Brokers 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) ask [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) to review
| 2 | [👥🚀🕸 `Service@Graph`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/09 👥🚀🕸 Offer.md>) | [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) pull specific service questions 
| 3 | [🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) | [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) ask [Wallets 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) for feedback
| 4 | [⭐🐌🤗 `Rated@Host`](<../../6 🅰️ APIs/50 🤗🅰️ Host/09 ⭐🐌🤗 Rated.md>) | Later, [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) may report to [Hosts 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
| 5 | [🌬️⏩💼 Ingest @ Consumer](<../78  🌬️⏩ Streamers/01 🌬️⏩🔔 Stream.md>) | Later, [Reviewers ⭐](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) alert subscriber [Finders 🔎](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)
||


<br/>

## FAQ

1. **How is privacy protected?**
   
    [Reviewer ⭐ domains](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>) collect user feedback after every [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) goodbye:
    - it is shared with hosts anonymously, after a period o time, to avoid time mapping;
    - users may ask contacted for follow-up, still anonymized by [Reviewer ⭐ domains](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/01 ⭐🫥 Reviewer vault.md>).

    ---
    <br/>