# 🤝 Render@Biller 🚀 call

> About
* Part of [Biller 🤝 domain](<../../🤝 Biller/🤝 Biller 🤲 helper.md>)
* Renders a [Biller 🤝 Template](<../../🤝 Biller/🤝📄 Biller templates.md>)

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-biller.dom
    Subject: Render@Biller

Body:
    Template: AnyName
    Sequence: AnySequence
    Input: {...}
```

<br/>

## Synchronous Response

```yaml
PDF: <based64-string>   # PDF generated content
Output: {...}           # Input after formulas and sequence
```