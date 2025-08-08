# 👥👉🌐 Config DNS @ [Domain](<../../4 ⏳ ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)

## About

- FAQ: [Domain communication 📨](<../../4 ⏳ ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)
- Components: [🚀 Outbox](<../../8 ⏳ 🧑‍💻 SDKs/20 ⏳ ☁️ AWS SDK/23 ⏳ 🚀 Outbox @ AWS.md>), [📥 Inbox](<../../8 ⏳ 🧑‍💻 SDKs/20 ⏳ ☁️ AWS SDK/22 ⏳ 📥 Inbox @ AWS.md>)


## Flow diagram ⏩

![DnsSetup](<📎 Assets/⚙️🌐 DnsSetup.png>)



## Sample DNS

| Record Name | Type | Value | Notes
|-|-|-|-|
| [any-domain.com]() | NS | {name servers} | 👉 Given by the DNS register
| nlweb.[any-domain.com]() | A | {API domain name} | 👉 Domain [📥 Inbox](<../../8 ⏳ 🧑‍💻 SDKs/20 ⏳ ☁️ AWS SDK/22 ⏳ 📥 Inbox @ AWS.md>) endpoint
| pk1._domainkey.[any-domain.com]() | TXT | "v=DKIM1;k=rsa;p=..." | 👉 Old issuer key for active [Tokens 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>)
| pk2._domainkey.[any-domain.com]() | TXT | "v=DKIM1;k=rsa;p=..." | 👉 Key for [🚀 Outbox](<../../8 ⏳ 🧑‍💻 SDKs/20 ⏳ ☁️ AWS SDK/23 ⏳ 🚀 Outbox @ AWS.md>) and [Tokens 🎫](<../../4 ⏳ ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>)
||
