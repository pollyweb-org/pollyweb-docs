# 👥⏩👥 Sync Request 🚀

> Part of [Domain 👥](<../👥 Domain.md>)


> Implements [🚀📨 Synchronous request messages](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)

> Requires [👥⏩🌐 DNS config](<👥⏩🌐 DNS config.md>)

<br/>

## Flow diagram ⏩

![alt text](<.📎 Assets/⚙️🚀 SyncRequest.png>)


<br/>

## HTTP Codes

| Code | Reason
|-|-
| 401 | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)  with invalid [domain Signature 🔏](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) 
| 422 | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) not matching its [Schema Code 🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>)
| 200 | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) with repeated [correlation ID ✉️](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Envelope ✉️.md>)
| 200 | Valid [Sync Request 🚀](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>) with immediate response
|