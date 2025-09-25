# 💼🐌 Feedback

> Referenced by [domain Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>)

 > The feedback is sent via a [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) defined by the sender's domain. 

<br/> 

## Async Message 🐌

```yaml
🤝: nlweb.org/MSG:1.0
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
|Header|`From` | UUID | the receiver domain name
||`To`| string | the [Buffer ⏳ helper domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) name
||`Subject`| string | `Feedback@Buffer`
|Body|`Correlation`| UUID | the original correlation ID of the affected message.
||`Status`| string | Status code of the feedback.
||`Reason`| string | Reason for the status code.
|