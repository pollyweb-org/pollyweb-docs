# 🔃🚀🗂️ Clone @ Filer

* Part of the [🔃⏩🗂️ Clone @ Syncer](<../../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/10 🔃⏩🗂️ Clone.md>) flow.

* ⚠️ This request is not signed.


<br/>

## Synchronous Request 🚀


```yaml
Header:
    From: Anonymous
    To: any-filer.com
    Subject: Clone@Filer
    
Body:
    WalletPin: 12345
    SyncerPin: 67890
    PublicKey: <public-key>
```

| Object| Property | Type | Description
|-|-|-|-
| Header    |`From`|domain| `Anonymous`
|           |`To`|domain| [Filer 🗂️ domain](<../🗂️🎭 Filer role.md>) name
|           | `Subject`     | string    | `Clone@Filer`
| Body      | `WalletPin`  | string | Pin displayed on the [Wallet 🧑‍🦰](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|           | `SyncerPin`   | string | Pin displayed on the [Syncer 🔃](<../../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>)
|           | `PublicKey`   | string | [Syncer 🔃](<../../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) public key
|

<br/>

## Synchronous Response

```yaml
Filer: any-filer.com
Clone: <clone-uuid>
Hash: SHA-256
```

|| Property | Type | Description
|-|-|-|-
|| `Filer`   | string    | [Filer 🗂️](<../🗂️🎭 Filer role.md>) for parameter-less [Sync ⏩](<../../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/20 🔃⏩🗂️ Sync.md>)
|| `Clone`       | uuid      | ID for future calls, e.g. [`Map@Filer`](<🔃🚀🗂️ Map.md>)
|| `Hash`        | enum | Algorithm for [`Map@`](<🔃🚀🗂️ Map.md>): `SHA-256`
|