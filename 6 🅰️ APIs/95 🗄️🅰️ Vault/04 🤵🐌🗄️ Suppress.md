<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZeda25d5a05a3470a994e6689d -->


# 🤵🐌🗄️ Suppress @ Vault

> Suppress [🖐️ Palm scans](<../../4 ⚙️ Solution/30 🫥 Agents/45 🆔 Identities/22 🆔🖐️ Palm scan.md>) on Palmist devices.

## Async Message 🐌


```yaml
Header:
    From: any-broker.com
    To: any-vault.com
    Subject: Suppress@Vault
    
Body:
    Consumer: any-consumer.com
    ChatID: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>)
|| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>)
|| `Subject` | string | `Suppress@Vault`
|Body| `Consumer` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>)
|| `ChatID`| uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID
|

<br/>


## Steps

* If the session is tracked, stop it - e.g.: 
    * GIVEN a vault that is a [Palmist 🖐️ supplier domain](<../../4 ⚙️ Solution/60 🧰 Edge/63 🖐️ Palmists/02 🖐️🏭 Palmist supplier.md>)
    * AND the palm reader is actively looking for the user of the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
    * WHEN suppressed 
    * THEN stop searching for it
    * AND stop sending findings to the [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>).
    
* Remove the session from 🪣 Disclosures
* If the session is not found on disclosures, just discard the message.

---