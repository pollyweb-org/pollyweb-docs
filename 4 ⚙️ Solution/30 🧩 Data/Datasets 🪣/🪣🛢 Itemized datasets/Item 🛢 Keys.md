# Item 🛢 Keys

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ

1. **What's the simplest syntax for itemized schemas?**

    ```yaml
    # First column is the key.
    # No parents, children, or distincts.
    Table: <name>
    ```

    |Input|Details|Example
    |-|-|-
    | `<name>` | Dataset name | `ORDERS`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    ```

    ---
    <br/>

1. **Whats the syntax for complex keys?**

    ```yaml
    # Complex keys
    Table: <name>
    Key: <k1>[,<kN>]
    ```

    |Input|Details|Example
    |-|-|-
    |`<k1>[,<kN>]`  | Key combination | `ID` `COL1,COL2`
    |

    Here's an example.

    ```yaml
    # Example
    Table: ORDERS
    Key: ID
    ```


    ---
    <br/>    

