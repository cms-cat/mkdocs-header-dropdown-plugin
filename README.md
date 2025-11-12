# MkDocs Header Dropdown Plugin

A MkDocs plugin that adds configurable dropdown menus to the Material theme header. This plugin allows you to create cross-documentation navigation menus that can be shared across multiple documentation sites.

## Installation

### From Source (Local Development)

```bash
pip install -e /path/to/mkdocs_header_dropdown
```

### From Git Repository

```bash
pip install git+https://github.com/cms-cat/mkdocs-header-dropdown.git
```

## Configuration

Add the plugin to your `mkdocs.yml` configuration file:

```yaml
plugins:
  - search
  - header-dropdown:
      dropdowns:
        - title: "CMS POG Docs"
          icon: "/assets/CMSlogo_white_nolabel_1024_May2014.png"
          links:
            - text: "Analysis Corrections | CrossPOG"
              url: "https://cms-analysis-corrections.docs.cern.ch/"
              target: "_blank"
            - text: "BTV Docs"
              url: "https://btv-wiki.docs.cern.ch/"
              target: "_blank"
            - text: "JetMet TWiki"
              url: "https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetMET"
              target: "_blank"
```

That's it! The plugin automatically injects the dropdown HTML into your Material theme header. No template overrides required.

## Configuration Options

### Plugin Configuration

- `dropdowns` (list): A list of dropdown menu configurations

### Dropdown Configuration

Each dropdown in the `dropdowns` list supports:

- `title` (string, required): The text displayed on the dropdown button
- `icon` (string, optional): Path to an icon image displayed next to the title
- `links` (list, required): List of links in the dropdown menu

### Link Configuration

Each link in the `links` list supports:

- `text` (string, required): The text displayed for the link
- `url` (string, required): The URL the link points to
- `target` (string, optional): The target attribute (e.g., `_blank` for new tab)

## Example: Multiple Dropdowns

```yaml
plugins:
  - header-dropdown:
      dropdowns:
        - title: "CMS POG Docs"
          icon: "/assets/cms-logo.png"
          links:
            - text: "BTV Docs"
              url: "https://btv-wiki.docs.cern.ch/"
              target: "_blank"
            - text: "JetMet TWiki"
              url: "https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetMET"
        - title: "External Resources"
          links:
            - text: "GitHub"
              url: "https://github.com/cms-cat"
              target: "_blank"
            - text: "GitLab"
              url: "https://gitlab.cern.ch/cms-analysis"
              target: "_blank"
```

## Features

- Multiple dropdown menus support
- Configurable icons and titles
- Hover and click interactions
- Responsive design
- Works with Material theme's light and dark modes
- Accessible and keyboard-friendly

## Requirements

- MkDocs >= 1.4.0
- Material for MkDocs theme

## License

MIT License

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
