# 🔃🐌🌲 Chat @ Filer

* Part of the [🔃⏩🌲 Chat @ Syncer](<../../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/30 🔃⏩🌲 Chat.md>) flow

* This request 
    * is signed with the [Syncer's 🔃](<../../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) private-key pair 
    * matching the `PublicKey` 
    * sent on the [`Clone@Filer`](<🔃🚀🌲 Clone.md>) request.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <clone-uuid>
    To: any-filer.com
    Subject: Chat@Filer
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<🔃🚀🌲 Clone.md>) 
|           | `To`          | string    | [Filer 🌲](<../🌲🎭 Filer role.md>) from [`Clone@`](<🔃🚀🌲 Clone.md>) 
|           | `Subject`     | string    | `Chat@Filer`
|

