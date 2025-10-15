# 🔃🚀🗃️ Map @ Resourcer

> Part of the [🔃⏩🗃️ Sync](<../../5 ⏩ Flows/77 🔃⏩ Syncer/20 🔃⏩🗃️ Sync.md>) flow:
> <br/> • Succeeded by [`Upload@Resourcer`](<30 🔃🚀🗃️ Upload.md>)

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
    Subject: Map@Resourcer

Body:
    Files: 
        /any-folder/any-file.yaml: 
            Hash: 8ab686eafeb1f44702738c8b0f24f2567c36da6d
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<10 🔃🚀🗃️ Clone.md>) 
|           | `To`          | string    | [Resourcer 🗃️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/02 🗃️🎭 Resourcer role.md>) from [`Clone@`](<10 🔃🚀🗃️ Clone.md>) 
|           | `Subject`     | string    | `Map@Resourcer`
| Body      | `Files`       | dict | Dictionary of local files
| File      | `Hash`        | string | Hashed with [`Clone@`](<10 🔃🚀🗃️ Clone.md>) hash
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
|Top| `Map`         | uuid      | ID for [`Upload@`](<30 🔃🚀🗃️ Upload.md>) and [`Uploaded@`](<50 🔃🚀🗃️ Uploaded.md>)
|| `Files` | dict | List of files required to change
|File| `Action` | string | `UPLOAD` `REMOVE`
|