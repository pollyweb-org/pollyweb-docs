<!-- #TODO -->

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT7b35acc03fa342b9bc6e581e0 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L48 -->

# 🎴🐌🤵 Offer @ Broker

## Async Message 🐌

```yaml
Header:
    From: any-issuer.com
    To: any-broker.org
    Subject: Offer@Broker
  
Body:
    ChatID: <chat-uuid>
    Token:
        TokenID: <token-uuid>
        Code: any-authority/<offer>
        Version: 1.0.0
        Issued: 2018-12-10T13:45:00.000Z
        Starts: 2018-12-10T13:45:00.000Z
        Expires: 2018-12-10T13:45:00.000Z
        QR: <qr>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
||`To`|string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`Subject`|string|`Offer@Broker`
|Body  |`ChatID` |UUID  | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
|      |`Token`  |Token | [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) object
|Token |`TokenID` |UUID  | [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID
|      |`Code`   |string| [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) 
|      |`Version`|string| Schema version|      
|      |`Issued` |timestamp| When issued
|      |`Starts` |timestamp| valid from
|      |`Expires`|timestamp| valid until
|      |`QR`     |string| [QR Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>)
|