# MkDocs Header Dropdown Plugin - Example

Welcome to the example site for the **mkdocs-header-dropdown-plugin**! This site demonstrates how the plugin works with the Material theme.

## What is this plugin?

This plugin adds configurable dropdown menus to your MkDocs Material theme header, making it easy to create cross-documentation navigation.

## Features

- 🎯 **Simple Configuration**: Define dropdowns in YAML
- 📦 **Shared Configs**: Load from external files (perfect for git submodules)
- 🎨 **Customizable**: Icons, titles, and links
- 🌙 **Theme Integration**: Works with light and dark modes
- ♿ **Accessible**: Keyboard-friendly navigation

## Check the Header!

Look at the header above - you'll see **three dropdown menus** demonstrating the plugin's capabilities:

1. **CMS POG Docs** - Loaded from a shared configuration file via git submodule (`cms-docs-common`)
2. **Examples** - Defined directly in `mkdocs.yml`
3. **Resources** - Also defined directly in `mkdocs.yml`, with a **nested submenu** under "Documentation"!

Try hovering over "Resources" → "Documentation" to see the nested dropdown in action!

This demonstrates:
- Configuration via shared git submodule
- Direct configuration in mkdocs.yml
- **Nested dropdowns** with submenu support

## Installation

```bash
pip install git+https://github.com/cms-cat/mkdocs-header-dropdown-plugin.git
```

## Quick Start

**For organizations with shared links (using git submodules):**

```bash
git submodule add https://github.com/your-org/docs-common.git
```

```yaml
# mkdocs.yml
plugins:
  - header-dropdown:
      config_file: "docs-common/header-dropdown.yml"
```

**For standalone projects:**

```yaml
# mkdocs.yml
plugins:
  - header-dropdown:
      dropdowns:
        - title: "Documentation"
          links:
            - text: "Getting Started"
              url: "/getting-started/"
            - text: "User Guide"
              url: "/guide/"
            - text: "API Reference"
              url: "/api/"
```

## Learn More

- [GitHub Repository](https://github.com/cms-cat/mkdocs-header-dropdown-plugin)
- [README](https://github.com/cms-cat/mkdocs-header-dropdown-plugin#readme)
- [Configuration Guide](https://github.com/cms-cat/mkdocs-header-dropdown-plugin#configuration-options)
