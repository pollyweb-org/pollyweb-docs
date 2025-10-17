
# [🧩](<../../Codes 🧩/🧩 Schema Code.md>) `.MSG`

> Schema of a [domain Message 📨](<../📨 Message.md>)

<br/>

## Definition

> [🤝:](<../../Codes 🧩/🧩 Schema Code.md>) [`.MANIFEST/CODE`](<../../Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /MSG

Schema: 
  Version: 1.0
  
  Properties: 
    - Header:     # Meta information.
      - From        # Domain that sent the message (except if sent by a wallet).
      - To          # Destination domain name.
      - Subject     # Method to be called at the destination, typically <method>@<role>.
      - Correlation # Unique request ID from the sender, for deduping.
      - Timestamp   # Date-time when the message was sent, in UTC.
      - Schema      # Optional schema of the header, e.g. any-domain.dom/any-request:1.0
    - Body        # Main content of the message.
    - Hash        # Hash of canonical representation of the header and body.
    - Signature   # Signature of the of canonical representation of the header and body.

  Format: 
    type: object
    required: [Header, Hash, Signature]
    properties:

      Header:
        type: object
        required: [From, To, Subject, Correlation, Timestamp]
        properties:

          From: 
            type: string
            format: hostname
            example: any-domain.dom
            description: >
              Typically, the domain that sent the message, except if sent by a wallet.
              Wallets either: 
                a) send their WalletID to brokers and notifiers, or
                b) sent their brokers domain to everyone else.

          To:
            type: string
            format: hostname
            example: any-domain.dom
            description: To destination domain.

          Subject:
            type: string
            example: CheckIn@Broker
            description: >
              Method to be called at the destination domain.
              Typically formatted as <method>@<role>.
              
          Correlation:
            type: string
            format: uuid
            example: 125a5c75-cb72-43d2-9695-37026dfcaa48
            description: Uniquely identifies the initial request.

          Timestamp:
            type: string
            format: utc.datetime
            example: 2023-09-17T09:56:32.381673+00:00Z
            description: Date and time when the request was sent, in UTC.

          Schema:
            type: string
            default: nlweb.dom/MSG:1.0
            description: >
              Code schema to validate the content of the body.
              Defined as <domain>/<code-path>:<schema-version>.

      Body:
        type: object
        description: > 
          Main content of the message.
          Its schema may be defined in the header.

      Hash:
        type: string
        description: >
          Hash of compacted content of the message:
            1. create an object with just {header,body} content;
            2. compact the content with JSON Canonicalization Scheme (JCS);
            3. read more at https://www.rfc-editor.org/rfc/rfc8785.

          To generate the hash with openssl, prepare the following file:
            - canonical.json: a canonical representation of {header,body};
          then run: 
            $ cat canonical.json | openssl dgst -sha256 > hash.txt 
            $ truncate -s -1 hash.txt
            $ cat hash.txt

      Signature:
        type: string
        description: >
          Signature of the header+body content, with sender's private key.
            - Purpose: validated with public key from the sender.
            - Validate domain messages with their public key published with DKIM.
            - Validate wallet messages with the their pre-shared public key.
            - More on DKIM: https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail

          To create a signature with openssl, prepare the following files:
            - canonical.json: a canonical representation of {header,body};
            - private.pem: the domain's private signature;
          then run the following commands on a terminal: 
            $ openssl dgst -sha256 -sign private.pem -out signature.sha1 canonical.json
            $ openssl base64 -A -in signature.sha1 -out signature.txt
            $ cat signature.txt

          To validate a signature with openssl, prepare the following files:
            - signature.txt: the signature received in a message from another domain;
            - canonical.json: a canonical representation of the received {header,body};
            - public.pem: the public key of the sender domain;
          then run the following commands on a terminal: 
            $ openssl enc -d -A -base64 -in signature.txt -out signature.sha1 
            $ openssl dgst -sha256 -verify public.pem -signature signature.sha1 canonical.json
