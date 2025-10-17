# 🛢 Database helper

> Relates to [`MAP`](<../../35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🪣 item.md>), [`UPSERT`](<../../35 💬 Chats/😃 Talkers/😃💾 Talker data/UPSERT 🛢 item.md>), and
[`DELETE`](<../../35 💬 Chats/😃 Talkers/😃💾 Talker data/DELETE 🗑️ item.md>) commands.



<br/>

1. **How to define a Resource Pool?**

    Resource Pools are defined in four ways in the [🪣 Pools file](<../../../55 👷 Build domains/📦 Hosteds/📦📄 Hosted files/🗺️📄 Tables file.mdd>) of [Hoster ☁️ domains](<../Hosters ☁️/☁️🤲 Hoster helper.md>).

    |Format| Details
    |-|-
    | `Markdown` | This is an upload `.md` file.
    | `YAML` | This is also an uploaded `.yaml` file.
    | `HTTP`| This is an endpoint defined in the settings.
    | `Folder` | This is a folder with `.pdf` and `.png` files
    |

    <br/>

    Example of a Markdown resource pool called `Items.md`

    ```yaml
    # 🪣 Items
    | Code | Name          | Price  | 21+
    |------|---------------|--------|----
    | 123  | water bottle  |  1.50  |
    | ABC  | beer          |  4.50  | Yes
    ```

    <br/>

    Example of a YAML resource pool called `Items.yaml`

    ```yaml
    # 🪣 Items
    - 123: 
        Code: 123
        Name: water bottle
        Price: 1.50
    - ABC:
        Code: ABC
        Name: beer
        Price: 4.50
        21+: Yes
    ```

    <br/>

    Example of an HTTP endpoint.

    ```yaml
    Items:
        Endpoint: https://rest.any-domain.dom/Items/{key}
    ```

    ---
    <br/>


1. **What are use cases?**

    * [Vending machines 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>