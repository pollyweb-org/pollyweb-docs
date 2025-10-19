# 🔃⏩🗂️ Sync @ Syncer

* Syncs the files in a [Filer 🗂️ domain](<../../../41 🎭 Domain Roles/Filer 🗂️/🗂️🎭 Filer role.md>), 
    * sending and receiving file changes in a local folder.

<br/>

## User interface 🧑

```yaml
# Run on the console
$ syncer sync
> ⏳ Syncing...
> ✅ Done.
```

<br/>

## Flow diagram ⏩

![alt text](<../.📎 Assets/sync.png>)

| # | Call | Notes
|-|-|-
|1|[🔃🚀🗂️ `Map@Filer`](<../../../41 🎭 Domain Roles/Filer 🗂️/🗂️🅰️ Filer methods/🔃🚀🗂️ Map.md>) | [Syncers](<../🔃🛠️ Syncer tool.md>) send a map current files
|2|[🔃🚀🗂️ `Upload@Filer`](<../../../41 🎭 Domain Roles/Filer 🗂️/🗂️🅰️ Filer methods/🔃🚀🗂️ Upload.md>) | Then upload each file individually
|3|[🔃🚀🗂️ `Uploaded@Filer`](<../../../41 🎭 Domain Roles/Filer 🗂️/🗂️🅰️ Filer methods/🔃🚀🗂️ Uploaded.md>) | [Filer 🗂️](<../../../41 🎭 Domain Roles/Filer 🗂️/🗂️🎭 Filer role.md>) calculate changes
|4|[🔃🚀🗂️ `Download@Filer`](<../../../41 🎭 Domain Roles/Filer 🗂️/🗂️🅰️ Filer methods/🔃🚀🗂️ Download.md>) | [Syncers](<../🔃🛠️ Syncer tool.md>) execute the changes
|