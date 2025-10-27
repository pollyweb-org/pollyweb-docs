# 🗄️🚀💼 Context @ Consumer

> Purpose

* Asks the [Consumer 💼 domain](<../../💼🎭 Consumer role.md>) for the context of a [`Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>), if the requested [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defines a context for requests.

> Example

* Consider a request to select the best date and time for a restaurant table reservation;
* it requires the context of the opening hours, working days, time slots still available, the building accessibility for the available slots, the menus available in each day of the week, and any other specificities related to the business.

<br>

## Synchronous Request 🚀

```yaml
Header:
    From: any-broker.dom
    To: any-consumer.dom
    Subject: Context@Consumer

Body:
    Hook: <hook-uuid>
```


## Synchronous Response

```yaml
Context: {...}
```