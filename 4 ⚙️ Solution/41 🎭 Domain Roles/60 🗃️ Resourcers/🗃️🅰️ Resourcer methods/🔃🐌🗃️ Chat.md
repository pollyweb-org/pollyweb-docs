# 🔃🐌🗃️ Chat @ Resourcer

> Part of the [🔃⏩🗃️ Chat @ Syncer](<../../../../5 ⏩ Flows/77 🔃⏩ Syncer/30 🔃⏩🗃️ Chat.md>) flow

* This request 
    * is signed with the [Syncer's 🔃](<../../../90 👷 Build/01 🛠️ Syncers/01 🔃🛠️ Syncer tool.md>) private-key pair 
    * matching the `PublicKey` 
    * sent on the [`Clone@Resourcer`](<🔃🚀🗃️ Clone.md>) request.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <clone-uuid>
    To: any-resourcer.com
    Subject: Chat@Resourcer
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<🔃🚀🗃️ Clone.md>) 
|           | `To`          | string    | [Resourcer 🗃️](<../🗃️🎭 Resourcer role.md>) from [`Clone@`](<🔃🚀🗃️ Clone.md>) 
|           | `Subject`     | string    | `Chat@Resourcer`
|

