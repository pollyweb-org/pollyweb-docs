# 👥🐌⏳ Feedback @ Buffer

> The feedback is sent via a [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>) defined by the sender's domain. 

> Implements a [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>)

> Mentioned in [domain Message 📨](<../../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>)


<br/> 

## Async Message 🐌

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
|Header|`From` | uuid | [Domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) name of the [Message 📨](<../../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) receiver 
||`To`| string | Sender's [Buffer ⏳ helper domain](<../⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Feedback@Buffer`
|Body| `Sender`| string | [Domain 👥](<../../../40 👥 Domains/$ 👥 Domains/👥 Domain.md>) name of the [Message 📨](<../../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) sender
||`Correlation`| uuid | Correlation ID of the affected [Message 📨](<../../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>)
||`Status`| string | `Discarded`
||`Reason`| string | Reason for the status code
|