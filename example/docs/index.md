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

Look at the header above - you'll see example dropdown menus demonstrating the plugin's capabilities.

## Installation

```bash
pip install git+https://github.com/cms-cat/mkdocs-header-dropdown-plugin.git
```

## Quick Start

Add to your `mkdocs.yml`:

```yaml
plugins:
  - header-dropdown:
      dropdowns:
        - title: "Documentation"
          links:
            - text: "User Guide"
              url: "/user-guide/"
            - text: "API Reference"
              url: "/api/"
```

## Learn More

- [GitHub Repository](https://github.com/cms-cat/mkdocs-header-dropdown-plugin)
- [README](https://github.com/cms-cat/mkdocs-header-dropdown-plugin#readme)
- [Configuration Guide](https://github.com/cms-cat/mkdocs-header-dropdown-plugin#configuration-options)
