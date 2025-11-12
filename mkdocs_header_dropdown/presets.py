"""
Preset configurations for common documentation sites.
"""

# CMS POG (Physics Object Groups) Documentation Links
CMS_POG = {
    "title": "CMS POG Docs",
    "icon": "__plugin__/CMSlogo_white_nolabel_1024_May2014.png",
    "links": [
        {
            "text": "Analysis Corrections | CrossPOG",
            "url": "https://cms-analysis-corrections.docs.cern.ch/",
            "target": "_blank"
        },
        {
            "text": "BTV Docs",
            "url": "https://btv-wiki.docs.cern.ch/",
            "target": "_blank"
        },
        {
            "text": "JetMet TWiki",
            "url": "https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetMET#Quick_links_to_current_recommend",
            "target": "_blank"
        },
        {
            "text": "E/Gamma TWiki",
            "url": "https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaPOG",
            "target": "_blank"
        },
        {
            "text": "MUO Docs",
            "url": "https://muon-wiki.docs.cern.ch/guidelines/",
            "target": "_blank"
        },
        {
            "text": "TAU TWiki",
            "url": "https://twiki.cern.ch/twiki/bin/view/CMS/Tau#Instructions_Recommendations",
            "target": "_blank"
        },
        {
            "text": "PRO TWiki",
            "url": "https://twiki.cern.ch/twiki/bin/viewauth/CMS/TaggedProtonsPOGRecommendations",
            "target": "_blank"
        }
    ]
}

# Available presets
PRESETS = {
    "cms-pog": CMS_POG,
}


def get_preset(name):
    """
    Get a preset configuration by name.

    Args:
        name: Name of the preset (e.g., "cms-pog")

    Returns:
        Dictionary containing the preset configuration

    Raises:
        ValueError: If the preset name is not found
    """
    if name not in PRESETS:
        available = ", ".join(PRESETS.keys())
        raise ValueError(f"Unknown preset '{name}'. Available presets: {available}")

    return PRESETS[name].copy()
