<!-- #TODO -->

<!-- https://quip.com/U97qAoGmSPAn#temp:C:HKUfb3022130c644b3faa5b9cce8 -->

# 👥🚀🖨️ Details @ [Printer](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>)

> A [Printer 🖨️ domain](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) returns the storage of a QR code, if any.

> No storage means that it’s free for grabs.

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.com
    To: any-printer.com
    Subject: Details@Printer
Body: 
    QRID: MY-QR-CODE
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) name
|| `Subject`| string | `Details@Printer`
|Body|`QRID`| string | Unique ID of the QR on the [Printer 🖨️](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>)
|


<br/>

## Synchronous Response

```yaml
Code: nlweb.org/HOST
Host: any-host.com
Mapping: MY-LOCATOR-ID
Matadata: Property1,Property2
```

|Object|Property|Type|Description
|-|-|-|-
|Top    | `Code`    | enum | [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)<br/>• [nlweb.org/HOST 🧩](<../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 Host.md>) <br/>• [nlweb.org/THING 🧩](<../../8 📜 Manifests/👥 nlweb.org/{codes}/STORAGE/🧩 Thing.md>)
|       | `Host`    | string | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) name
|       | `Mapping` | string | [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) in the [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>)
|       | `Metadata`| string | Metadata
|