# 👥🚀🖨️ Grab @ Printer

> A [Printer 🖨️ domain](<../../🖨️🤲 Printer helper.md>) grabs an available alias. 

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-printer.dom
    Subject: Grab@Printer

Body: 
    Alias: ANY-ALIAS
    Locator: .HOST,any-host.dom,any-key
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../../🖨️🤲 Printer helper.md>) name
|| `Subject`| string | `Grab@Printer`
|Body|`Alias`| string | Unique alias on the [Printer 🖨️](<../../🖨️🤲 Printer helper.md>)
|| `Locator` | string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
|

<br/>

## Synchronous Response

| HTTP | Details
|-|-
| 200   | Success.
| 409   | Alias already occupied - use another alias.
| 400   | Locator not supported - only [`.HOST 🧩`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) is supported.
|

<br/>
