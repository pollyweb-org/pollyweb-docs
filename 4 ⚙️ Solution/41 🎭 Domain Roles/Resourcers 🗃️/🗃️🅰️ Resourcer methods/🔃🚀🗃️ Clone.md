# 🔃🚀🗃️ Clone @ Resourcer

> Part of the [🔃⏩🗃️ Clone @ Syncer](<../../../55 👷 Build domains/🛠️ Syncers/🔃⏩ Syncer flows/10 🔃⏩🗃️ Clone.md>) flow.

> ⚠️ This request is not signed.


<br/>

## Synchronous Request 🚀


```yaml
Header:
    From: Anonymous
    To: any-resourcer.com
    Subject: Clone@Resourcer
    
Body:
    WalletPin: 12345
    SyncerPin: 67890
    PublicKey: <public-key>
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | string | `Anonymous`
|           | `To`          | string    | [Resourcer 🗃️ domain](<../🗃️🎭 Resourcer role.md>) name
|           | `Subject`     | string    | `Clone@Resourcer`
| Body      | `WalletPin`  | string | Pin displayed on the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
|           | `SyncerPin`   | string | Pin displayed on the [Syncer 🔃](<../../../55 👷 Build domains/🛠️ Syncers/🔃🛠️ Syncer tool.md>)
|           | `PublicKey`   | string | [Syncer 🔃](<../../../55 👷 Build domains/🛠️ Syncers/🔃🛠️ Syncer tool.md>) public key
|

<br/>

## Synchronous Response

```yaml
Resourcer: any-resourcer.com
Clone: <clone-uuid>
Hash: SHA-256
```

|| Property | Type | Description
|-|-|-|-
|| `Resourcer`   | string    | [Resourcer 🗃️](<../🗃️🎭 Resourcer role.md>) for parameter-less [Sync ⏩](<../../../55 👷 Build domains/🛠️ Syncers/🔃⏩ Syncer flows/20 🔃⏩🗃️ Sync.md>)
|| `Clone`       | uuid      | ID for future calls, e.g. [`Map@Resourcer`](<🔃🚀🗃️ Map.md>)
|| `Hash`        | enum | Algorithm for [`Map@`](<🔃🚀🗃️ Map.md>): `SHA-256`
|