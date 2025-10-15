# 🔃🚀🗃️ Clone @ Resourcer

> Part of the [🔃⏩🗃️ Clone @ Syncer](<../../5 ⏩ Flows/77 🔃⏩ Syncer/10 🔃⏩🗃️ Clone.md>) flow.

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
|           | `To`          | string    | [Resourcer 🗃️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>) name
|           | `Subject`     | string    | `Clone@Resourcer`
| Body      | `WalletPin`  | string | Pin displayed on the [Wallet 🧑‍🦰](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
|           | `SyncerPin`   | string | Pin displayed on the [Syncer 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>)
|           | `PublicKey`   | string | [Syncer 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) public key
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
|| `Resourcer`   | string    | [Resourcer 🗃️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>) for parameter-less [Sync ⏩](<../../5 ⏩ Flows/77 🔃⏩ Syncer/20 🔃⏩🗃️ Sync.md>)
|| `Clone`       | uuid      | ID for future calls, e.g. [`Map@Resourcer`](<20 🔃🚀🗃️ Map.md>)
|| `Hash`        | enum | Algorithm for [`Map@`](<20 🔃🚀🗃️ Map.md>): `SHA-256`
|