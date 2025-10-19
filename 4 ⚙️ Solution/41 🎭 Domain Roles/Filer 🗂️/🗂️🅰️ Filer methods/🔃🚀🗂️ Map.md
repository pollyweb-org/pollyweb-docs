# 🔃🚀🗂️ Map @ Filer
  
* Part of the [🔃⏩🗂️ Sync](<../../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/20 🔃⏩🗂️ Sync.md>) flow:
    * succeeded by [`Upload@Filer`](<🔃🚀🗂️ Upload.md>)

* This request 
    * is signed with the [Syncer's 🔃](<../../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) private-key pair 
    * matching the `PublicKey` 
    * sent on the [`Clone@Filer`](<🔃🚀🗂️ Clone.md>) request.


<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <clone-uuid>
    To: any-filer.com
    Subject: Map@Filer

Body:
    Files: 
        /any-folder/any-file.yaml: 
            Hash: 8ab686eafeb1f44702738c8b0f24f2567c36da6d
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<🔃🚀🗂️ Clone.md>) 
|           | `To`          | string    | [Filer 🗂️](<../🗂️🎭 Filer role.md>) from [`Clone@`](<🔃🚀🗂️ Clone.md>) 
|           | `Subject`     | string    | `Map@Filer`
| Body      | `Files`       | dict | Dictionary of local files
| File      | `Hash`        | string | Hashed with [`Clone@`](<🔃🚀🗂️ Clone.md>) hash
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
|Top| `Map`         | uuid      | ID for [`Upload@`](<🔃🚀🗂️ Upload.md>) and [`Uploaded@`](<🔃🚀🗂️ Uploaded.md>)
|| `Files` | dict | List of files required to change
|File| `Action` | string | `UPLOAD` `REMOVE`
|