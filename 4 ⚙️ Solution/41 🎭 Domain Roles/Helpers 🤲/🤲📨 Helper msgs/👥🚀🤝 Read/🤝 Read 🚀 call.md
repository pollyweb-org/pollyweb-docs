# 🤝 Read@Helper 🚀 call

> About
* Part of the [Helper 🤲 domain](<../../🤲 Helper/🤲👥 Helper domain.md>)
* Fails if the number of items is too high 
* For a large number of items, use the [`Export@Helper` 🐌 msg](<../👥🐌🤝 Export/🤝 Export 🐌 msg.md>) instead
 
<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-helper.dom
    Subject: Read@Helper

Body:

    Sets: Set1, Set3 

    Outputs:
        Set1: FieldA, FieldB
    
    Asserts: 
        Set1:
            FieldX.IsNot: ACTIVE
        Set3:
            FieldZ.IsAbove: 25
```
Uses: [`.IsNot`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsNot ⓕ.md>) [`.IsAbove`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAbove ⓕ.md>)

<br/>

|Object|Property|Type|Purpose|Default
|-|-|-|-|-
|Header|`From`|text| Client [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name|
||`To`|text| [Helper 🤲 domain](<../../🤲 Helper/🤲👥 Helper domain.md>) name |   
||`Subject`|text| `Read@Helper` |
|Body|`Sets`|[list](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)| Optional [set](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) names to export | All sets|
||`Asserts`|[map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)| Optional [`.Assert`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) filter to apply | No filter
||`Outputs`|[map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)| Optional output of [`.Format`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Format ⓕ.md>) per [set](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) | All fields


<br/>

## Synchronous Response

```yaml
Set1: # Exported set
  Item1Key: # Indexed sets are returned with keys
    FieldA: ValueA
    FieldB: ValueB

Set3: # Sets without indexes are returned as arrays
  - FieldX: ValueX
    FieldY: ValueY
```