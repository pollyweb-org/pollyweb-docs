<!-- #TODO -->

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTa9a1f10023324c448a569fa05 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS.py#L199 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L10 -->

# 🧑‍🦰🚀🤵 Tokens @ Broker

<br/>

## Sync Request

|Property|Type|Description
|-|-|-

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.org
    Subject: Tokens@Broker

Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| UUID  | [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID
|           | `To`  | string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|           | `Subject`| string|  `Tokens@Broker`
|

<br/>

## Sync Response

```yaml
Tokens:
  - TokenID: <token-uuid>
    Issuer: any-issuer.com
    IssuerTranslation: <translationOf(any-host.org)>
    Code: `any-authority.org/<code>
    CodeTranslation: `<translationOf(any-authority.org/<code>)>
    Schema: {...}
    Issued: 2018-12-10T13:45:00.000Z
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
    Version: 1.0.0
    QR: \U0001F91Dnlweb.org/...
    Path: /storage/tf/creds/<issuer>/<token-uuid>
    Status: REVOKED
```

|Object|Property|Type|Description|
|-|-|-|-
|Top   |Tokens   |Token[]|List of Token objects|
|Token |TokenID  |UUID   |[Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID|
|| `Issuer` | string 
|| `IssuerTranslation` | string
|| `Code` | string
|| `CodeTranslation` | string
|| `Schema` | object
|| `Issued`| timestamp
|| `Starts`| timestamp
|| `Expires`| timestamp
|| `Version`| timestamp
|| `QR`| string
|| `Path`| string
|| `Status`| enum
|