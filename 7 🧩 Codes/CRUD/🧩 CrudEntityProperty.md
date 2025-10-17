
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): CrudEntityProperty

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /CRUD/ENTITY/PROPERTY

Schema:
  Properties:
    - Default   # Default value for the user prompt.
    - Details   # Additional user prompt message.
    - External  # Loads ONE|MANY options from an external domain.
    - Format    # Prompt format for the wallet user, e.g. TEXT.
    - If        # Show this property if another is True.
    - Internal  # Loads ONE|MANY options from an internal entity.
    - MaxLength # Maximum lenght for TEXT|EMAIL formats.
    - MinLength # Minimum lenght for TEXT|EMAIL formats.
    - Options   # Lodas ONE|MANY options with static values.
    - Send      # Array of properties to send to a Supplier.
    - Title     # Display override for the name of the property.
    - Unique    # Is there a unique index in the property? 

  Format:
    type: object
    required: [Details, Format]
    properties: 

      Default:
        type: string
        description: >
          Default value for the user prompt.
          - For [CONFIRM], highlights the YES or NO button.
          - For [ONE,MANY], moves the option to the top.
          - For [TEXT], pre-types the text.

      Details:
        type: string
        description: >
          Additional user prompt message.
          - Tipically, a description of the field.

      External:
        $ref: nlweb.dom/CRUD/ENTITY/PROPERTY/EXTERNAL

      Format: 
        enum: [AMOUNT, CONFIRM, EMAIL, DIGITS, MANY, ONE, OTP, PHONE, TEXT]
        default: TEXT
        description: >
          See details in https://quip.com/CDrjAxNKwLpI
          - If [ONE,MANY] requires Options or Lookup.
          - If [OTP] requires Data.

      If: 
        type: string
        example: HasDetails
        description: >
          Show this property if another is True.
          - The conditional property must have format CONFIRM.

      Internal:
        $ref: nlweb.dom/CRUD/ENTITY/PROPERTY/INTERNAL

      MaxLength:
        type: integer
        description: Maximum lenght for TEXT|EMAIL formats.

      MinLength:
        type: integer
        description: Minimum lenght for TEXT|EMAIL formats.

      Options:
        oneOf:

          - type: array
            items:
              - type: string
            example: [Portugal, United Kingdom]
            description: 
              A list of static strings.
              Used when what is being saved is the same that users see.

          - type: object
            additionalProperties: 
              type: string
            example: 
              PT: Portugal
              UK: United Kingdom
            description: > 
              A dictionary of <save>:<show>.
              Used when the value saved differs from what users see.

      Send:
        type: array
        items:
          type: string
        example: [Country, Number]
        description: >
          Array of properties to send to a Supplier.
          - OTP format for SMS requires [Country, Number].
          - OTP format for emails requires [Email].
          - OTP prompts only appear upon changes of properties to send.

      Title:
        type: string
        description: > 
          Display override for the name of the property.
          - If there is no title, the property name is used.
          - Used for single-word properties that need titles with 2+ words.

      Unique:
        type: boolean
        description: >
          Is there a unique index in the property? 
          - This will be validated after each input.
          - The workflow remains blocked while not unique.