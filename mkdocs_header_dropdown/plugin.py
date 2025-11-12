"""
MkDocs Header Dropdown Plugin

A plugin to add configurable dropdown menus to the MkDocs Material theme header.
"""
import os
import shutil
import yaml
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig
from . import presets


class HeaderDropdownPlugin(BasePlugin):
    """
    Plugin that adds configurable dropdown menus to the header.

    Configuration in mkdocs.yml:

    plugins:
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
    """

    config_scheme = (
        ('preset', config_options.Type(str, default=None)),
        ('config_file', config_options.Type(str, default=None)),
        ('dropdowns', config_options.Type(list, default=[])),
    )

    def on_config(self, config: MkDocsConfig, **kwargs) -> MkDocsConfig:
        """
        Add dropdown configuration to the MkDocs config's extra section.
        This makes it available in templates via config.extra.header_dropdowns
        """
        if not config.extra:
            config.extra = {}

        # Collect dropdowns from various sources
        dropdowns = []

        # 1. Load from preset if specified
        preset_name = self.config.get('preset')
        if preset_name:
            try:
                preset_dropdown = presets.get_preset(preset_name)
                dropdowns.append(preset_dropdown)
            except ValueError as e:
                raise ValueError(f"Error loading preset: {e}")

        # 2. Load from config file if specified
        config_file = self.config.get('config_file')
        if config_file:
            config_file_path = os.path.join(config.docs_dir, '..', config_file)
            if os.path.exists(config_file_path):
                with open(config_file_path, 'r') as f:
                    file_config = yaml.safe_load(f)
                    if 'dropdowns' in file_config:
                        dropdowns.extend(file_config['dropdowns'])
            else:
                raise FileNotFoundError(f"Config file not found: {config_file_path}")

        # 3. Add dropdowns from mkdocs.yml
        dropdowns.extend(self.config.get('dropdowns', []))

        # Process icon paths - replace __plugin__ prefix with actual path
        for dropdown in dropdowns:
            if 'icon' in dropdown and dropdown['icon'].startswith('__plugin__/'):
                # Will be served at /header-dropdown-assets/...
                dropdown['icon'] = dropdown['icon'].replace('__plugin__/', '/header-dropdown-assets/')

        # Add the dropdowns to extra so templates can access them
        config.extra['header_dropdowns'] = dropdowns

        return config

    def on_env(self, env, config, files):
        """
        Add plugin's template directory to the Jinja2 environment's search path.
        This runs after the theme environment is set up.
        """
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(os.path.dirname(plugin_dir), 'templates')

        if os.path.exists(templates_dir):
            # Add to the beginning of the loader search path
            env.loader.searchpath.insert(0, templates_dir)

        return env

    def on_page_context(self, context, page, config, nav):
        """
        Add dropdown data to the page context for template rendering.
        """
        context['header_dropdowns'] = config.extra.get('header_dropdowns', [])
        return context

    def on_post_build(self, config):
        """
        Copy plugin assets to the site directory after build.
        """
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        assets_src = os.path.join(plugin_dir, 'assets')
        assets_dest = os.path.join(config.site_dir, 'header-dropdown-assets')

        if os.path.exists(assets_src):
            # Create destination directory if it doesn't exist
            os.makedirs(assets_dest, exist_ok=True)

            # Copy all files from assets directory
            for item in os.listdir(assets_src):
                src_path = os.path.join(assets_src, item)
                dest_path = os.path.join(assets_dest, item)

                if os.path.isfile(src_path):
                    shutil.copy2(src_path, dest_path)
