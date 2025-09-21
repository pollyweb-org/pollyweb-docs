# 👥🚀🖨️ Grab @ Printer

> A [Printer 🖨️ domain](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) grabs a free QR code. 

> If already grabbed, then returns false.
<br/>

## Synchronous Request

```yaml
Header:
    From: any-domain.com
    To: any-printer.com
    Subject: Grab@Printer
Body: 
   QRID: MY-QR-CODE
   Code: dtfw.org/HOST
   Host: any-host.com
   Mapping: MY-LOCATOR-ID
   Matadata: Property1,Property2

```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) name
|| `Subject`| string | `Grab@Printer`
|Body|`QRID`| string | Unique ID of the QR on the [Printer 🖨️](<../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>)
|    | `Code`    | enum | [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)<br/>• [nlweb.org/HOST 🧩](<../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 Host.md>) <br/>• [nlweb.org/THING 🧩](<../../8 📜 Manifests/👥 nlweb.org/{codes}/STORAGE/🧩 Thing.md>)
|       | `Host`    | string | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) name
|       | `Mapping` | string | [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) in the [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>)
|       | `Metadata`| string | Metadata
|