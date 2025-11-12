"""
MkDocs Header Dropdown Plugin

A plugin to add configurable dropdown menus to the MkDocs Material theme header.
"""
import os
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig


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
        ('dropdowns', config_options.Type(list, default=[])),
    )

    def on_config(self, config: MkDocsConfig, **kwargs) -> MkDocsConfig:
        """
        Add dropdown configuration to the MkDocs config's extra section.
        This makes it available in templates via config.extra.header_dropdowns
        Also adds plugin's template directory to the theme's search path.
        """
        if not config.extra:
            config.extra = {}

        # Add the dropdowns to extra so templates can access them
        config.extra['header_dropdowns'] = self.config.get('dropdowns', [])

        # Add plugin's template directory to theme's template search path
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(os.path.dirname(plugin_dir), 'templates')

        if os.path.exists(templates_dir):
            if not hasattr(config.theme, 'dirs'):
                config.theme.dirs = []
            # Insert at the beginning so it has priority
            config.theme.dirs.insert(0, templates_dir)

        return config

    def on_page_context(self, context, page, config, nav):
        """
        Add dropdown data to the page context for template rendering.
        """
        context['header_dropdowns'] = self.config.get('dropdowns', [])
        return context
