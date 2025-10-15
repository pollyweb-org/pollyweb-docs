<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDDf29b75b2d0214f9a87224b338 -->

# 🤵🐌🤗 Hello @ Host

> Starts a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with a [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>).

> Used by:
> <br/>• [🧑‍🦰👉🤗 Scan host QR @ Wallet](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR @ Wallet](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)

<br/> 

## Async Message 🐌


```yaml
Header:
    From: any-broker.com
    To: any-host.com
    Subject: Hello@Host

Body:
    Language: en-us
    ChatID: <chat-uuid>
    PublicKey: <public-key>
    Code: nlweb.org/THING
    Locator: MY-THING-ID
    Binds: 
        - <bind-#1-uuid>
        - <bind-#2-uuid>
    Tokens:
        - <token-#1-uuid>
        - <token-#2-uuid>
    Parameters: 
        Param1: Value1
        Param2: Value2
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`    | string    | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) name
|           | `To`      | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) name
|           | `Subject` | string    | `Hello@Host`
| Body      | `Language`| enum    | ISO language code
|           | `ChatID`  | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID in the [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>)
|           | `PublicKey`| string | For [`Prompted@`](<04 🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<05 🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<06 🧑‍🦰🚀🤗 Download.md>)
|           | `Locator` | string    | [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) in the [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)
|           | `Code`    | string    | [Schema Code 🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) of the Locator
|           | `Binds`   | uuid[] | List of [Binds 🔗](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/01 🔗 Bind.md>) for a [Vault 🗄️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) host
|           | `Tokens`  | uuid[] | List of [Tokens 🎫](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) for an [Issuer 🎴](<../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) host
|| `Parameters`| object | Custom parameters
|
