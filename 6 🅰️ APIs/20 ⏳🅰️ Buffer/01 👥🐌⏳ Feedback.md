# 👥🐌⏳ Feedback @ Buffer

> The feedback is sent via a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) defined by the sender's domain. 

> Implements a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>)

> Mentioned in [domain Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)


<br/> 

## 🐌 Async Message

```yaml
Header:
    From: any-receiver.com
    To: any-buffer.com
    Subject: Feedback@Buffer
Body:
    Sender: any-domain.com
    Correlation: <correlation-uuid>
    Status: Discarded
    Reason: Invalid DKIM signature.
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From` | uuid | [Domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) name of the [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) receiver 
||`To`| string | Sender's [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Feedback@Buffer`
|Body| `Sender`| string | [Domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) name of the [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) sender
||`Correlation`| uuid | Correlation ID of the affected [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)
||`Status`| string | `Discarded`
||`Reason`| string | Reason for the status code
|