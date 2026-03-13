# Repository Agent Instructions

## Editing Markdown Files

- When writing in md files, consider the magic links .tools/links/links.yaml 
    - e.g. "\{\{Wallet\}\}" will automatically link to the Wallet App page.
    - these are case insensitive, so "\{\{wallet\}\}" should also work.
    - other examples in the links.yaml file include token, tokens, chat, bind.
    - this also applies to prose inside tables, including description cells; replace generic nouns like chat, wallet, token, prompt, notifier, broker, host, and vault with magic-link-backed terms when available.
- Note that the magic links are only replace when running ".tools/links/links.py";
    - thus, you'll need to run it after editing to see the results.
- When working with tables, you may simplify names to make them shorter - e.g.:
    - remove "msg" from "🐌 msg", 
    - remove "call" from "🚀 call", 
    - remove the domain name like "Notifier" from "Updated@Notifier",
    - remove "domain" from "Notifier 📣 domain.",
    - remove "apps" from "Wallet 🧑‍🦰 apps"
    - remove "app" from "Wallet 🧑‍🦰 app"
- when listing domain methods in a table:
    - use the 3-icon group of the parent folder (e.g. 🧑‍🦰🚀📣), except for the domain emoji;
    - move the icons to the left;
    - don't make the link bold with ``;
    - e.g. the method "📣 Onboard 🚀 call.md" is in a parent folder "Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣", so the method link label should be "🧑‍🦰🚀 Onboard"
- When adding links to md files, make sure the target exists and it's not a folder.
