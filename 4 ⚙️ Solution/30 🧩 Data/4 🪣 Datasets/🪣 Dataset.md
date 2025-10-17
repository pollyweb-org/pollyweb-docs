<!-- TODO -->

# 🪣 Datasets

> Relates to [🪣📂 Tables folder](<../../55 👷 Build domains/📦 Hosteds/📦📄 Hosted files/🪣📂 Tables folder.md>)

> Relates to [🪣🎭 Datasetter role](<../../41 🎭 Domain Roles/Datasetters 🪣/🪣🎭 Datasetter role.md>)

> Relates to [🛢🤲 Databaser helper](<../../45 🤲 Helper domains/Databasers 🛢/🛢🤲 Databaser helper.md>)

<br/>

1. **How to define a Dataset?**

    Resource Pools are defined in four ways in the [🪣 Pools file](<../../../55 👷 Build domains/📦 Hosteds/📦📄 Hosted files/🗺️📄 Tables file.mdd>) of [Hoster ☁️ domains](<../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>).

    |Format| Details
    |-|-
    | `Markdown` | This is an upload `.md` file.
    | `YAML` | This is also an uploaded `.yaml` file.
    | `HTTP`| This is an endpoint defined in the settings.
    | `Folder` | This is a folder with `.pdf` and `.png` files
    |

    <br/>

1. **How is a static Markdown dataset?**

    Here's a Markdown dataset called `Items.md`

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
