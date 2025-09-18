<!-- #TODO -->

<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

> Lists the Binds of a Wallet app.

## Sync Request

|Property|Type|Description
|-|-|-
|

```yaml
Header:
  From: <wallet-uuid>
  To: any-broker.org
  Subject: Binds@Broker
Body: 
`````


## Sync Response

|Property|Type|Description
|-|-|-
|

```yaml
Binds:
  - ID: <bind-uuid>
    Vault: any-vault.org
    VaultTitle: AnyVault
    Code: any-authority.org/ANY-CODE
    CodeTitle: Any Code
```