# 🧩 .`REVIEWER`/`REVIEW`

```yaml
Path: REVIEWER/REVIEW
Title: Chat review

Fields:
    Rate: For replying
    Form: Last Inform@Broker, if any
    Stars: From 1 to 5
    Feedback: Free text

Asserts:
    AllOf: Rate, Stars
    UUIDs: Rate
    Texts: Feedback, Form
    Nums: Stars
    Stars.IsBetween(1,5):
```