# 👥⏩👥 Sync Request 🚀

> Part of [Domain 👥](<../👥 Domain.md>)


> Implements [🚀📨 Synchronous request messages](<../../👥📨 Domain Messages/📨⏩ Message flows/Request Sync 🚀.md>)

> Requires [👥⏩🌐 DNS config](<👥⏩🌐 DNS config.md>)

<br/>

## Flow diagram ⏩

![alt text](<.📎 Assets/⚙️🚀 SyncRequest.png>)


<br/>

## HTTP Codes

| Code | Reason
|-|-
| 401 | [Message 📨](<../../👥📨 Domain Messages/📨 Message.md>)  with invalid [domain Signature 🔏](<../../👥📨 Domain Messages/📨⏩ Message flows/Signatures 🔏.md>) 
| 422 | [Message 📨](<../../👥📨 Domain Messages/📨 Message.md>) not matching its [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| 200 | [Message 📨](<../../👥📨 Domain Messages/📨 Message.md>) with repeated [correlation ID ✉️](<../../👥📨 Domain Messages/📨⏩ Message flows/Envelope ✉️.md>)
| 200 | Valid [Sync Request 🚀](<../../👥📨 Domain Messages/📨⏩ Message flows/Request Sync 🚀.md>) with immediate response
|