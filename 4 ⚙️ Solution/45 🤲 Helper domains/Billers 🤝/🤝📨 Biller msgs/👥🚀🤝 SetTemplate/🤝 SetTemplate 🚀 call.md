# 🤝 SetTemplate@Biller 🚀 call

> About
* Part of [Biller 🤝 domain](<../../🤝 Biller/🤝 Biller 🤲 helper.md>)

<br/>

## Synchronous Call 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-biller.dom
    Subject: SetTemplate@Biller

Body:
    Format: >
        #### My Invoice {Number}
        ---
        **Customer**: ´{Customer.Name}´ <br/>
        **Tax Number**: ´{Customer.TaxNumber}´
        
        |Item|Tax|Price
        |-|-:|-:|
        {Items|´{Name}´ | {Tax}% | $ {Price|AMOUNT|2}}

        |||
        |-|-:|
        **Total**| $ {Total|AMOUNT}
        **Taxes**| $ {Taxes|AMOUNT}
```

<br/>

## Synchronous Response

```yaml
Template: <template-uuid>
```