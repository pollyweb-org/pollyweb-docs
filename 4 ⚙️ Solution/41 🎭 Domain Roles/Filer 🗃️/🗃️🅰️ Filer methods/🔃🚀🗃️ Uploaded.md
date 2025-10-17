# 🔃🚀🗃️ Uploaded @ Filer

* Part of the [🔃⏩🗃️ Sync](<../../../55 👷 Build domains/🔃 Syncers/🔃⏩ Syncer flows/20 🔃⏩🗃️ Sync.md>) flow:
    * preceded by [`Upload@Filer`](<🔃🚀🗃️ Upload.md>)
    * succeeded by [`Download@Filer`](<🔃🚀🗃️ Download.md>)

* This request 
    * is signed with the [Syncer's 🔃](<../../../55 👷 Build domains/🔃 Syncers/🔃🛠️ Syncer tool.md>) private-key pair 
    * matching the `PublicKey` 
    * sent on the [`Clone@Filer`](<🔃🚀🗃️ Clone.md>) request.



<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <clone-uuid>
    To: any-filer.com
    Subject: Uploaded@Filer

Body:
    Map: <map-uuid>
```

| Object| Property | Type | Description
|-|-|-|-
| Header    | `From`        | uuid | `Clone` from [`Clone@`](<🔃🚀🗃️ Clone.md>) 
|           | `To`          | string    | [Filer 🗃️](<../🗃️🎭 Filer role.md>) from [`Clone@`](<🔃🚀🗃️ Clone.md>) 
|           | `Subject`     | string    | `Uploaded@Filer`
| Body      | `Map`         | uuid    | ID from [`Map@Filer`](<🔃🚀🗃️ Map.md>)
|


<br/>

## Successful Response ✅

```yaml
# HTTP 200
Files: 
    /any-folder/any-file.yaml: 
        Hash: 8ab686eafeb1f44702738c8b0f24f2567c36da6d
        Parts: 1        # 1 by default, if missing
        Base46: False   # False by default, if missing
```

|Object| Property | Type | Description
|-|-|-|-
|Top| `Files` | dict | List of files required to download
|File| `Action` | string | `DOWNLOAD`
|    | `Hash`   | string | Hashed with [`Clone@`](<🔃🚀🗃️ Clone.md>) hash
|    | `Parts`  | int    | Number of file parts
|    | `Base64` | bool   | Convert Base46 to binary
|

<br/> 

## Failure Response ❌

```yaml
# HTTP 409
Errors:
- There's a more recent Map.
- Missing file > /path/file-1.yaml
- Missing part 2 of 6 > /path/file-2.yaml
- Map already done.
```


|| Property | Type | Description
|-|-|-|-
|| `Errors`    | string[]  | List of errors on failure
|