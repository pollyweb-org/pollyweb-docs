# 👥⏩👥 Sync Request 🚀

> Part of [Domain 👥](<../../👥 Domain/👥 Domain.md>)


> Implements [🚀📨 Synchronous request messages](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Calls 🚀.md>)

> Requires [👥⏩🌐 DNS config](<../DNS config 👥🌐/👥 DNS config ⏩ flow.md>)

<br/>

## Flow diagram ⏩

![alt text](<👥 Sync Request ⚙️ uml.png>)


<br/>

## HTTP Codes

| Code | Reason
|-|-
| 401 | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)  with invalid [domain Signature 🔏](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) 
| 422 | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) not matching its [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
| 200 | [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) with repeated [correlation ID ✉️](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Envelope ✉️.md>)
| 200 | Valid [Sync Request 🚀](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Sync Calls 🚀.md>) with immediate response
|