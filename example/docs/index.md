# MkDocs Header Dropdown Plugin

Add configurable dropdown menus to your MkDocs Material theme header for easy cross-documentation navigation.

<div style="text-align: center; margin: 2rem 0;">
  <a href="/getting-started/" style="display: inline-block; padding: 0.75rem 2rem; background: var(--md-primary-fg-color); color: white; text-decoration: none; border-radius: 0.25rem; font-weight: bold; margin: 0.5rem;">Get Started</a>
  <a href="https://github.com/cms-cat/mkdocs-header-dropdown-plugin" target="_blank" style="display: inline-block; padding: 0.75rem 2rem; border: 2px solid var(--md-primary-fg-color); color: var(--md-primary-fg-color); text-decoration: none; border-radius: 0.25rem; font-weight: bold; margin: 0.5rem;">View on GitHub</a>
</div>

## ✨ Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div>
    <h3>🎯 Simple Configuration</h3>
    <p>Define dropdown menus in YAML - no template overrides needed</p>
  </div>
  <div>
    <h3>📦 Shared Configs</h3>
    <p>Load from external files via git submodules - perfect for organizations</p>
  </div>
  <div>
    <h3>🔄 Nested Menus</h3>
    <p>Create multi-level submenus with automatic arrow indicators</p>
  </div>
  <div>
    <h3>🎨 Customizable</h3>
    <p>Add icons, customize titles, and style to match your theme</p>
  </div>
  <div>
    <h3>🌙 Theme Integration</h3>
    <p>Works seamlessly with Material theme's light and dark modes</p>
  </div>
  <div>
    <h3>♿ Accessible</h3>
    <p>Keyboard-friendly navigation and screen reader support</p>
  </div>
</div>

## 🎪 Live Demo

**Look at the header above!** You'll see three dropdown menus demonstrating the plugin's capabilities:

| Dropdown | Description | Demonstrates |
|----------|-------------|--------------|
| **CMS POG Docs** | External links with icon | Shared config via git submodule |
| **Examples** | Internal site links | Direct mkdocs.yml configuration |
| **Resources** | Mixed with nested menu | Nested dropdowns (hover over "Documentation") |

Try interacting with them to see how the plugin works!

## 🚀 Quick Start

### For Organizations (Shared Links)

Perfect when multiple documentation sites need the same navigation:

```bash
# Add shared config as git submodule
git submodule add https://github.com/your-org/docs-common.git
```

```yaml
# mkdocs.yml
plugins:
  - header-dropdown:
      config_file: "docs-common/header-dropdown.yml"
```

### For Standalone Projects

Ideal for single projects with unique navigation:

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
        - title: "Resources"
          links:
            - text: "GitHub"
              url: "https://github.com/your-org/your-project"
              target: "_blank"
```

## 📦 Installation

```bash
pip install git+https://github.com/cms-cat/mkdocs-header-dropdown-plugin.git
```

## 📚 Documentation

- **[Getting Started](getting-started.md)** - Installation and basic setup
- **[Configuration Examples](examples.md)** - Real-world configuration patterns
- **[Nested Menus](nested-menus.md)** - Creating multi-level submenus
- **[GitHub Repository](https://github.com/cms-cat/mkdocs-header-dropdown-plugin)** - Source code and issues

## 💡 Use Cases

- **Organization-wide navigation**: Share common links across all documentation sites
- **Multi-project documentation**: Link between related projects
- **External resources**: Quick access to wikis, support portals, and tools
- **Contextual navigation**: Group related documentation by category
