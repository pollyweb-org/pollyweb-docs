# Contributing to PollyWeb Docs

Thank you for your interest in contributing. This repository holds the PollyWeb specification, research landscape, and use cases. Contributions that improve clarity, accuracy, or coverage are welcome.

## What you can contribute

- **Landscape research** — new articles or updates to existing ones under `2 🏔️ Landscape/`
- **Use cases** — new end-to-end flows under `3 🤝 Use Cases/`
- **Specification improvements** — corrections or clarifications under `4 ⚙️ Solution/`
- **Tooling** — improvements to the scripts under `.tools/`
- **Typos and broken links** — always welcome

## Getting started

1. Fork the repository and create a branch from `main`.
2. Make your changes following the conventions below.
3. Open a pull request with a clear description of what changed and why.

## VS Code setup (recommended)

For day-to-day editing in this repository, use the following VS Code addons:

- **Open files in external apps (including `.pptx`)**: `yutengjing.open-in-external-app`
- **PlantUML image generation**: `goohan.plantumlautogenerator` (optional companion: `jebbs.plantuml`)
- **Markdown link linting**: built-in Markdown validation + `davidanson.vscode-markdownlint`
- **Update links when renaming/moving markdown files**: `mathiassoeholm.markdown-link-updater` (or built-in `markdown.updateLinksOnFileMove.enabled`)

Recommended workspace settings (`.vscode/settings.json`):

```jsonc
{
	"markdown.validate.enabled": true,
	"markdown.validate.fileLinks.enabled": "error",
	"markdown.validate.fragmentLinks.enabled": "warning",
	"markdown.updateLinksOnFileMove.enabled": "always"
}
```

Notes:

- To open a `.pptx`, right-click the file in Explorer and choose **Open in External App**.
- For PlantUML, save a `.puml`/`.plantuml` file to trigger auto-generation; if needed, run **Generate diagram image** from the Command Palette.
- If both link-updating mechanisms are enabled (built-in + extension), keep an eye on duplicate updates; if you notice this, keep one mechanism and disable the other.

## Conventions

**File naming** — follow the existing emoji-prefixed naming pattern (e.g., `01 📺 Article title.md`). Emoji prefixes carry meaning:
- `📺` — references an external article or news item
- `🖼️` — a visual/chart overview
- `📄` — a data or market-size summary
- `00 … Index.md` — index file for a section

**Markdown style** — keep files concise. Use tables for comparisons, blockquotes (`>`) for summaries, and relative links for cross-references between documents.

**Links** — internal links must use relative paths. Run the link checker before submitting:
```bash
cd .tools/links
pip install -r requirements.txt
python links.py
```

**Pre-push enforcement** — pushes are blocked by `.githooks/pre-push` when either:
- there are pending local changes (staged, unstaged, or untracked files), or
- `links.py` reports broken/malformed links.

If you fix issues after a failed push, commit those fixes first, then push again.

**Assets** — place images and PDFs in a `.📎 Assets/` subfolder alongside the markdown files that reference them.

**Tone** — neutral and factual for landscape research; precise and unambiguous for specification content.

## Licensing

By contributing, you agree that your contributions will be licensed under the same [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license that covers this repository.

## Questions

Open an issue or reach out via [LinkedIn](https://www.pollyweb.org/#linkedin).
