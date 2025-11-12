# Getting Started

This page demonstrates additional content in the example site.

## Installation

Install the plugin from GitHub:

```bash
pip install git+https://github.com/cms-cat/mkdocs-header-dropdown-plugin.git
```

## Basic Configuration

The minimal configuration requires just the plugin and at least one dropdown:

```yaml
plugins:
  - header-dropdown:
      dropdowns:
        - title: "Links"
          links:
            - text: "Home"
              url: "/"
```

## Adding Icons

You can add icons to your dropdowns:

```yaml
plugins:
  - header-dropdown:
      dropdowns:
        - title: "Documentation"
          icon: "/assets/logo.png"
          links:
            - text: "Getting Started"
              url: "/getting-started/"
```

## Multiple Dropdowns

Add as many dropdowns as you need:

```yaml
plugins:
  - header-dropdown:
      dropdowns:
        - title: "Docs"
          links:
            - text: "Guide"
              url: "/guide/"
        - title: "External"
          links:
            - text: "GitHub"
              url: "https://github.com"
              target: "_blank"
```

## Using Shared Configuration

For multiple documentation sites sharing the same navigation:

1. Create a shared config repository
2. Add as git submodule
3. Reference in `mkdocs.yml`:

```yaml
plugins:
  - header-dropdown:
      config_file: "shared-config/dropdowns.yml"
```
