# 🔃🚀🗂️ Download @ Filer

* Part of the [🔃⏩🗂️ Sync](<../../../55 👷 Build domains/Syncers 🔃/🔃⏩ Syncer flows/20 🔃⏩🗂️ Sync.md>) flow:
    * preceded by [`Uploaded@Filer`](<🔃🚀🗂️ Uploaded.md>)

* This request 
    * is signed with the [Syncer's 🔃](<../../../55 👷 Build domains/Syncers 🔃/🔃🛠️ Syncer tool.md>) private-key pair 
    * matching the `PublicKey` 
    * sent on the [`Clone@Filer`](<🔃🚀🗂️ Clone.md>) request.


<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: <clone-uuid>
    To: any-filer.dom
    Subject: Download@Filer
    
Body:
    Map: <map-uuid>
    File: /folder-C/folder-C1/file-C12.yaml
    Part: 1         # 1 by default, if missing
```

| Object| Property | Type | Description
|-|-|-|-
| Header    |`From`| uuid | `Clone` from [`Clone@`](<🔃🚀🗂️ Clone.md>) 
|           |`To`|string| [Filer 🗂️](<../🗂️🎭 Filer role.md>) from [`Clone@`](<🔃🚀🗂️ Clone.md>) 
|           | `Subject`     | string    | `Upload@Filer`
| Body      | `Map`         | uuid    | ID from [`Map@Filer`](<🔃🚀🗂️ Map.md>)
|           | `File`        | string | Path like `/dir/file.ext`
|           | `Part`        | int    | File part do download
|

<br/>

## Successful Response ✅

```yaml
# HTTP 200
Content: <content>
```

|| Property | Type | Description
|-|-|-|-
|| `Content`     | string | Content in text
|


<br/>

## Failure Response ❌

```yaml
# HTTP 409
Errors:
- There's a more recent Map.
- File not in Map > /path/file-1.yaml
- Map already done.
```

|| Property | Type | Description
|-|-|-|-
|| `Errors`    | string[]  | List of errors on failure
|