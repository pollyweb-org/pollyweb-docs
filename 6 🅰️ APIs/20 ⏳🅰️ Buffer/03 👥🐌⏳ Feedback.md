# 👥🐌⏳ Feedback @ Buffer

> The feedback is sent via a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) defined by the sender's domain. 

> Implements [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Mentioned in [domain Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)


<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-receiver.com
    To: any-buffer.com
    Subject: Feedback@Buffer
Body:
    Correlation: <correlation-uuid>
    Status: Discarded
    Reason: Invalid DKIM signature.
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | UUID | [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) receiver [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) name
||`To`| string | [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Feedback@Buffer`
|Body|`Correlation`| UUID | Correlation ID of the affected [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)
||`Status`| string | Status code of the feedback
||`Reason`| string | Reason for the status code
|