# 🔃🐌🗃️ Chat @ Resourcer

> Part of the [🔃⏩🗃️ Chat @ Syncer](<../../5 ⏩ Flows/77 🔃⏩ Syncer/30 🔃⏩🗃️ Chat.md>) flow

* This request 
    * is signed with the [Syncer's 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) private-key pair 
    * matching the `PublicKey` 
    * sent on the [`Clone@Resourcer`](<10 🔃🚀🗃️ Clone.md>) request.

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
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<10 🔃🚀🗃️ Clone.md>) 
|           | `To`          | string    | [Resourcer 🗃️](<../../9 😃 Talkers/90 ☁️ Hosters/02 🗃️🎭 Resourcer role.md>) from [`Clone@`](<10 🔃🚀🗃️ Clone.md>) 
|           | `Subject`     | string    | `Chat@Resourcer`
|

