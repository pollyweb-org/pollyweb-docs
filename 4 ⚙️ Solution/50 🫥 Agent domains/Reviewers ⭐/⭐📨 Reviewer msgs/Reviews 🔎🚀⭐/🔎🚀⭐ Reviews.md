<!-- Docs: -->
<!-- Source: -->
<!-- Test: -->


# 🔎🚀⭐ Reviews@Reviewer

> About
* Implements the [Reviewer ⭐ agent](<../../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>)
* Part of the [`Present` ⏩ flow](<../../../Finders 🔎/🔎⏩ Finder flows/Present 🔎⏩🧑‍🦰/🔎 Present ⏩ flow.md>)

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-finder.dom
    To: any-reviewer.dom
    Subject: Reviews@Reviewer

Body:
    Domain: any-domain.dom
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header |`From`|text| [Finder 🔎](<../../../Finders 🔎/$/🔎 Finder 🫥 agent.md>) | [`Present@Finder`](<../../../Finders 🔎/🔎😃 Finder Talkers/Present/🔎 Present 🐌 msg.md>)
|        |`To`|text| [Reviewer ⭐](<../../⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | [`Present@Finder`](<../../../Finders 🔎/🔎😃 Finder Talkers/Present/🔎 Present 🐌 msg.md>)
|        | `Subject` |text| `Reviews@Reviewer`
| Body   | `Domain`  | domain | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`Present@Finder`](<../../../Finders 🔎/🔎😃 Finder Talkers/Present/🔎 Present 🐌 msg.md>)
|

<br/>

# Synchronous response

```yaml
Rating: 4.6
Description: |
    User feedback:
    - 4.7⭐ delivery by 357 users
    - 3.5⭐ support by 21 users
Options:
    - /List reviews § .HOST,any-reviewer.dom,domain
```