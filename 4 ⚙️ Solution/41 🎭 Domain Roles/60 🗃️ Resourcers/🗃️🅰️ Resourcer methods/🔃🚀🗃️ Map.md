# 🔃🚀🗃️ Map @ Resourcer

> Part of the [🔃⏩🗃️ Sync](<../../../90 👷 Build/01 🛠️ Syncers/🔃⏩ Syncer flows/20 🔃⏩🗃️ Sync.md>) flow:
> <br/> • Succeeded by [`Upload@Resourcer`](<🔃🚀🗃️ Upload.md>)

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
    Subject: Map@Resourcer

Body:
    Files: 
        /any-folder/any-file.yaml: 
            Hash: 8ab686eafeb1f44702738c8b0f24f2567c36da6d
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<🔃🚀🗃️ Clone.md>) 
|           | `To`          | string    | [Resourcer 🗃️](<../🗃️🎭 Resourcer role.md>) from [`Clone@`](<🔃🚀🗃️ Clone.md>) 
|           | `Subject`     | string    | `Map@Resourcer`
| Body      | `Files`       | dict | Dictionary of local files
| File      | `Hash`        | string | Hashed with [`Clone@`](<🔃🚀🗃️ Clone.md>) hash
|

<br/>

## Successful Response ✅

```yaml
# HTTP 200
Map: <map-uuid>
Files: 
    /any-folder/any-file.yaml: 
        Action: UPLOAD
```


|Object| Property | Type | Description
|-|-|-|-
|Top| `Map`         | uuid      | ID for [`Upload@`](<🔃🚀🗃️ Upload.md>) and [`Uploaded@`](<🔃🚀🗃️ Uploaded.md>)
|| `Files` | dict | List of files required to change
|File| `Action` | string | `UPLOAD` `REMOVE`
|