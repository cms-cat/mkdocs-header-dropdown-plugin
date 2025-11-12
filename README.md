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

### Quick Start with Presets

The easiest way to get started is using a preset:

```yaml
plugins:
  - search
  - header-dropdown:
      preset: "cms-pog"
```

This automatically adds the CMS POG documentation dropdown with all standard links and the CMS logo.

### Custom Configuration

You can also define your own dropdowns:

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
```

**That's it!** The plugin automatically provides the necessary templates. No manual template overrides required.

## Configuration Options

### Plugin Configuration

The plugin supports three ways to configure dropdowns, which can be combined:

1. **`preset`** (string, optional): Load a predefined dropdown configuration
   - Available presets: `"cms-pog"`

2. **`config_file`** (string, optional): Load dropdown configuration from a YAML file
   - Path is relative to the repository root
   - Useful for sharing configuration across multiple repositories via git submodules

3. **`dropdowns`** (list, optional): Define dropdowns directly in mkdocs.yml

All three sources are merged together, allowing you to extend presets or shared configs.

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

## Example: Extending Presets

You can extend a preset with additional dropdowns:

```yaml
plugins:
  - header-dropdown:
      preset: "cms-pog"  # Load CMS POG links
      dropdowns:
        - title: "External Resources"  # Add custom dropdown
          links:
            - text: "GitHub"
              url: "https://github.com/cms-cat"
              target: "_blank"
            - text: "GitLab"
              url: "https://gitlab.cern.ch/cms-analysis"
              target: "_blank"
```

## Example: Using Shared Config File

For multiple repositories that share the same dropdown configuration:

```yaml
# In shared-config/header-links.yml (e.g., via git submodule)
dropdowns:
  - title: "My Shared Dropdown"
    links:
      - text: "Link 1"
        url: "https://example.com"

# In mkdocs.yml
plugins:
  - header-dropdown:
      config_file: "shared-config/header-links.yml"
```

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

- **Preset configurations**: Zero-config setup for common documentation sites
- **Shared configuration**: Load dropdown config from external YAML files (great for git submodules)
- **Flexible configuration**: Mix presets, shared configs, and custom dropdowns
- **Built-in assets**: Plugin includes CMS logo and other assets
- **Multiple dropdown menus**: Support for any number of dropdowns
- **Configurable icons and titles**: Customize appearance
- **Hover and click interactions**: User-friendly interactions
- **Responsive design**: Works on all screen sizes
- **Theme integration**: Works with Material theme's light and dark modes
- **Accessible**: Keyboard-friendly navigation

## Requirements

- MkDocs >= 1.4.0
- Material for MkDocs theme

## License

MIT License

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
