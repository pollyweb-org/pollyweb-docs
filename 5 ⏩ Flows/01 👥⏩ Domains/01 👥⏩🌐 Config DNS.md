# 👥👉🌐 Config DNS @ [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)

## About
#TODO add link to inbox

- FAQ: [Domain communication 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)
- Components: [🚀 Outbox](<02 👥⏩🚀 Sender outbox.md>), [📥 Inbox]()


## Flow diagram ⏩

![DnsSetup](<📎 Assets/⚙️🌐 DnsSetup.png>)


## Sample DNS
#TODO add link to inbox and outbox

| Record Name | Type | Value | Notes
|-|-|-|-|
| [any-domain.com]() | NS | {name servers} | 👉 Given by the DNS register
| nlweb.[any-domain.com]() | A | {API domain name} | 👉 Domain [📥 Inbox]() endpoint
| pk1._domainkey.[any-domain.com]() | TXT | "v=DKIM1;k=rsa;p=..." | 👉 Old issuer key for active [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>)
| pk2._domainkey.[any-domain.com]() | TXT | "v=DKIM1;k=rsa;p=..." | 👉 Key for [🚀 Outbox]() and [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 🎫 Tokens/01 🎫 Token.md>)
||
