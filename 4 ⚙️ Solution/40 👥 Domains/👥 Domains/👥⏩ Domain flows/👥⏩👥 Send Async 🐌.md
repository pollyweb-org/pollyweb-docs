<!-- TODO -->

# 👥⏩👥 Async Message 🐌

> Part of [Domain 👥](<../👥 Domain.md>)

> Implements [🐌📨 Async Messages](<../../👥📨 Domain Messages/📨⏩ Message flows/Send Async 🐌.md>)

> Requires [👥⏩🌐 DNS config](<👥⏩🌐 DNS config.md>)


## Flow diagram ⏩

![alt text](<.📎 Assets/⚙️🐌 AsyncMessage.png>)

<br/>

## HTTP Codes

| Code | Reason
|-|-
| 401 | [Message 📨](<../../👥📨 Domain Messages/📨 Message.md>)  with invalid [domain Signature 🔏](<../../👥📨 Domain Messages/📨⏩ Message flows/Signatures 🔏.md>) 
| 422 | [Message 📨](<../../👥📨 Domain Messages/📨 Message.md>) not matching its [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
| 200 | [Message 📨](<../../👥📨 Domain Messages/📨 Message.md>) with repeated [correlation ID ✉️](<../../👥📨 Domain Messages/📨⏩ Message flows/Envelope ✉️.md>)
| 200 | Valid [Async Message 🐌](<../../👥📨 Domain Messages/📨⏩ Message flows/Send Async 🐌.md>) to be processed later
|