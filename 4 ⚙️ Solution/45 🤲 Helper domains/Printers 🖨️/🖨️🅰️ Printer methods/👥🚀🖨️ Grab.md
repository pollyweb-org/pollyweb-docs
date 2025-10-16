# 👥🚀🖨️ Grab @ Printer

> A [Printer 🖨️ domain](<../🖨️🤲 Printer helper.md>) grabs an available alias. 

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-printer.dom
    Subject: Grab@Printer
Body: 
    Alias: ANY-ALIAS
    Locator: .HOST,any-host.dom,ANY-RESOURCE,A=1,B=2
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../🖨️🤲 Printer helper.md>) name
|| `Subject`| string | `Grab@Printer`
|Body|`Alias`| string | Unique alias on the [Printer 🖨️](<../🖨️🤲 Printer helper.md>)
|       | `Locator`    | string | The [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) of a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
|

## Synchronous Response

| HTTP | Details
|-|-
| 200   | Success.
| 409   | Alias already occupied: <br/> - use another alias.
| 405   | Locator not supported: <br/> - only [`.HOST 🧩`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) is supported.
|