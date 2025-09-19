<!--# 🏳️🏥 https://quip.com/jneKAp8Lbg7M/-NHSuk-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: health.any-nation.org
  Name: Any Nation's Health Services


Trusts:


  # Share SSR of citizens with anyone trusted by the nation.
  - Role: CONSUMER
    Query: airlines.any-igo.org/SSR/*
    Domains: [ any-nation.org ]


  # Share COVID of citizens with airlines.
  - Role: CONSUMER
    Query: health.any-igo.org/COVID/DOSE
    Domains: [ airline.any-business.org ]


  # Blocks whoever Any Nation blocks.
  - Action: INHERIT
    Domains: [ any-nation.org ]
      
                      
# Issues SSR tokens for UK citizens.
Issuer:

  - From: 2022/01/09
    To: 9999/12/31
    Algorithm: RSA
    PublicKey: >-
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgS3bFZz2L6SnZSldCyaQc7BN3/JeDsfeDBXipvd/hZnqUeTo2OwIM2rUHlddqBn35WlP9H1fEDPzvQ9ZA4AxfLefZfEJsAwRkBgGNcqBXsqmDf8Liwu7gDYYuEeC6YRciTAf2G1s9Kv35NCjNwNTZ5wOXzQ1gCAxw8xbhW7hsWf4jFmkWt1sSRiZZpH8cWUUU2btP8cXmYvkbFHej6jmrgan/3gI2030R94vAAToSzHQyMHWW9YY+ybj0lrcSL+CaraBQd5bbXZrG8TuAj6IiaYveB+4L86M56CxEQaAAIzdzynFUGiSE0kyBg4MkZqtMKuNnUXy6NrPF65uXmgsqQIDAQAB
