# 👥🐌⏳ Feedback @ Buffer

> The feedback is sent via a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) defined by the sender's domain. 

> Implements a [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>)

> Mentioned in [domain Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)


<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-receiver.dom
    To: any-buffer.dom
    Subject: Feedback@Buffer
Body:
    Sender: any-domain.dom
    Correlation: <correlation-uuid>
    Status: Discarded
    Reason: Invalid DKIM signature.
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`| uuid | [Domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name of the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) receiver 
||`To`|domain| Sender's [Buffer ⏳ helper domain](<../⏳🤲 Buffer helper.md>) name
||`Subject`| string | `Feedback@Buffer`
|Body| `Sender`| string | [Domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name of the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) sender
||`Correlation`| uuid | Correlation ID of the affected [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
||`Status`| string | `Discarded`
||`Reason`| string | Reason for the status code
|