<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZeda25d5a05a3470a994e6689d -->


# 🤵🐌🗄️ Suppress @ Vault

> Suppress [🖐️ Palm scans](<../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/7 🆔⏩🖐️ Palm scan.md>) on Palmist devices.

## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-vault.dom
    Subject: Suppress@Vault
    
Body:
    Consumer: any-consumer.dom
    Chat: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|domain| [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>)
||`To`|domain| [Vault 🗄️ domain](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
|| `Subject` | string | `Suppress@Vault`
|Body| `Consumer` | string | [Consumer 💼 domain](<../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)
|| `Chat`| uuid | [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID
|

<br/>


## Steps

* If the session is tracked, stop it - e.g.: 
    * GIVEN a vault that is a [Palmist 🖐️ supplier domain](<02 🖐️🏭 Palmist supplier.md>)
    * AND the palm reader is actively looking for the user of the [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    * WHEN suppressed 
    * THEN stop searching for it
    * AND stop sending findings to the [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).
    
* Remove the session from 🪣 Disclosures
* If the session is not found on disclosures, just discard the message.

---