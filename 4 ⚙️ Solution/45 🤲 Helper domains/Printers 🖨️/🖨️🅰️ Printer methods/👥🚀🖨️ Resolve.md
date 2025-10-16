<!-- https://quip.com/U97qAoGmSPAn#temp:C:HKUfb3022130c644b3faa5b9cce8 -->

# 👥🚀🖨️ Resolve @ Printer

> A [Printer 🖨️ domain](<../🖨️🤲 Printer helper.md>) returns the [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) of an alias, if any.

> Used in [🧑‍🦰👉🤗 Scan printer QR](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>).

> No locator means that it’s free for grabs.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.com
    To: any-printer.com
    Subject: Resolve@Printer

Body: 
    Alias: ANY-ALIAS
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../🖨️🤲 Printer helper.md>) name
|| `Subject`| string | `Resolve@Printer`
|Body|`Alias`| string | Unique [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) ID on the [Printer 🖨️ ](<../🖨️🤲 Printer helper.md>)
|


<br/>

## Synchronous Response

```yaml
Locator: .HOST,any-host.com,any-key
```

Property|Type|Description
|-|-|-
| Locator | string | [Locator 🔆](<../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) 
|