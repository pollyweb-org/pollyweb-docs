# 🤝 SavePlan 🚀 call

```yaml
Header:
    From: any-domain.dom
    To: any-biller.dom
    Subject: SavePlan@Biller

Body:
    Name: FreePlan
    Period: MONTH
    Currency: USD
    
    Pricing:

      - Metric: Requests
        Price: 8.00
        Quantity: 1M        
        Type: TRANSACTION

      - Metric: DataWritten
        Price: 0.25
        Quantity: 1GB
        Type: TRANSACTION

      - Metric: DataRetained
        Price: 0.15
        Quantity: 1GB
        Type: STORAGE

    Quotas:

      - Quota: RequestsPerSecond
        Limit: 5
        Period: SECOND

      - Quota: RequestsPerMinute
        Limit: 100
        Period: MINUTE

      - Quota: RequestSize
        Limit: 256KB
```

<br/>

## FAQ

1. **Why not an async message?**

    Using a synchronous call allows for immediate confirmation of success, ensuring that the client domain can proceed with its operations without delay.

    ---
    <br/>

1. **What's the difference between Transaction and Storage?**

    | Type | Definition
    |-|-
    | `TRANSACTION` | Metrics charged based on usage <br/> e.g. number of requests, data written |
    | `STORAGE` | Metrics charged based on data stored over time <br/> e.g. data retained in storage |

    ---
    <br/>

1. **What's the difference between Pricing and Quotas?**

    | Type | Definition | Example |
    |-|-|-
    | `Pricing` | Billing metrics for usage | 8.00 USD per 1M requests |
    | `Quotas` | Usage limits for resources | 5 requests per second |

  
    ---
    <br/>


1. **What are real examples of Pricing metrics?**

    AWS Lambda Durable Functions are charged as follows.

    | Metric | Price | Quantity | Type |
    |-|-:|-:|-
    | `Requests` | 8.00 | 1 M | TRANSACTION |
    | `Data Written` | 0.25 | 1 GB | TRANSACTION |
    | `Data Retained` | 0.15 | 1 GB | STORAGE |

    ---
    <br/>

