# 👥⏩👥 Sync Request 🚀

> Part of [Domain 👥](<../👥 Domain.md>)


> Implements [🚀📨 Synchronous request messages](<../../📨 Messages/📨⏩ Message flows/Request Sync 🚀.md>)

> Requires [👥⏩🌐 DNS config](<👥⏩🌐 DNS config.md>)

<br/>

## Flow diagram ⏩

![alt text](<.📎 Assets/⚙️🚀 SyncRequest.png>)


<br/>

## HTTP Codes

| Code | Reason
|-|-
| 401 | [Message 📨](<../../📨 Messages/📨 Message.md>)  with invalid [domain Signature 🔏](<../../📨 Messages/📨⏩ Message flows/Signatures 🔏.md>) 
| 422 | [Message 📨](<../../📨 Messages/📨 Message.md>) not matching its [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| 200 | [Message 📨](<../../📨 Messages/📨 Message.md>) with repeated [correlation ID ✉️](<../../📨 Messages/📨⏩ Message flows/Envelope ✉️.md>)
| 200 | Valid [Sync Request 🚀](<../../📨 Messages/📨⏩ Message flows/Request Sync 🚀.md>) with immediate response
|