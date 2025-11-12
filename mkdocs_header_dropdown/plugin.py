"""
MkDocs Header Dropdown Plugin

A plugin to add configurable dropdown menus to the MkDocs Material theme header.
"""
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig
import re


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
        """
        if not config.extra:
            config.extra = {}

        # Add the dropdowns to extra so templates can access them
        config.extra['header_dropdowns'] = self.config.get('dropdowns', [])

        return config

    def on_page_context(self, context, page, config, nav):
        """
        Add dropdown data to the page context for template rendering.
        """
        context['header_dropdowns'] = self.config.get('dropdowns', [])
        return context

    def on_post_page(self, output, page, config):
        """
        Inject dropdown HTML into the page after rendering.
        This allows the plugin to work without requiring template overrides.
        """
        dropdowns = self.config.get('dropdowns', [])
        if not dropdowns:
            return output

        # Generate the dropdown HTML
        dropdown_html = self._generate_dropdown_html(dropdowns)

        # Find the insertion point in the header (after search, before repo info)
        # Look for the search partial or repo section
        search_pattern = r'(<!-- Search interface -->.*?</form>)'
        repo_pattern = r'(<!-- Repository information -->)'

        # Try to inject after search
        if re.search(search_pattern, output, re.DOTALL):
            output = re.sub(
                search_pattern,
                r'\1\n\n    <!-- Header dropdown menus from plugin -->\n' + dropdown_html,
                output,
                flags=re.DOTALL
            )
        # Otherwise inject before repo info
        elif re.search(repo_pattern, output):
            output = re.sub(
                repo_pattern,
                '    <!-- Header dropdown menus from plugin -->\n' + dropdown_html + '\n\n    \\1',
                output
            )

        return output

    def _generate_dropdown_html(self, dropdowns):
        """Generate the HTML for dropdown menus."""
        html_parts = []

        for dropdown in dropdowns:
            title = dropdown.get('title', '')
            icon = dropdown.get('icon', '')
            links = dropdown.get('links', [])

            dropdown_html = f'''    <div class="md-header__option" style="margin-right: 0.1rem;">
      <div class="md-header__dropdown"
           style="position: relative; display: inline-block;"
           onmouseenter="showHeaderDropdown(this)"
           onmouseleave="hideHeaderDropdown(this)">
        <button class="md-header__button"
                style="padding: 0.4rem; display: flex; align-items: center; gap: 0.3rem"
                onclick="toggleHeaderDropdown(event)">'''

            if icon:
                dropdown_html += f'\n          <img src="{icon}" alt="{title}" style="width: 35px; height: 35px;" />'

            dropdown_html += f'''
          <span style="font-size: 0.7rem;">{title}</span>
        </button>
        <div class="md-header__dropdown-content"
             style="display: none; position: absolute; left: 0; top: 100%; background: var(--md-default-bg-color); border: 1px solid var(--md-default-fg-color--lightest); border-radius: 0.1rem; box-shadow: var(--md-shadow-z2); min-width: 200px; z-index: 1000;">'''

            for link in links:
                link_text = link.get('text', '')
                link_url = link.get('url', '#')
                link_target = link.get('target', '')
                target_attr = f' target="{link_target}"' if link_target else ''

                dropdown_html += f'''
          <a href="{link_url}"{target_attr}
             style="display: block; padding: 0.5rem 1rem; color: var(--md-default-fg-color); text-decoration: none; font-size: 0.7rem"
             onmouseover="this.style.backgroundColor='var(--md-default-fg-color--lightest)'"
             onmouseout="this.style.backgroundColor='transparent'">
            {link_text}
          </a>'''

            dropdown_html += '''
        </div>
      </div>
    </div>'''

            html_parts.append(dropdown_html)

        # Add JavaScript (only once)
        js = '''
    <script>
      // Only define functions once
      if (typeof toggleHeaderDropdown === 'undefined') {
        function toggleHeaderDropdown(event) {
          event.stopPropagation();
          const dropdown = event.target.closest('.md-header__dropdown');
          const content = dropdown.querySelector('.md-header__dropdown-content');
          const isVisible = content.style.display === 'block';

          // Close all other dropdowns
          document.querySelectorAll('.md-header__dropdown-content').forEach(el => {
            el.style.display = 'none';
          });

          // Toggle current dropdown
          content.style.display = isVisible ? 'none' : 'block';
        }

        function showHeaderDropdown(dropdown) {
          const content = dropdown.querySelector('.md-header__dropdown-content');
          content.style.display = 'block';
        }

        function hideHeaderDropdown(dropdown) {
          // Add a small delay to prevent flickering when moving between elements
          setTimeout(() => {
            const content = dropdown.querySelector('.md-header__dropdown-content');
            if (!dropdown.matches(':hover')) {
              content.style.display = 'none';
            }
          }, 100);
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function() {
          document.querySelectorAll('.md-header__dropdown-content').forEach(el => {
            el.style.display = 'none';
          });
        });
      }
    </script>'''

        return '\n'.join(html_parts) + js
