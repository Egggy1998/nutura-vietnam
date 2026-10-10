# -*- coding: utf-8 -*-
"""
Full Site Generator for Nutura Organic Vietnam
Generates 19 pages with complete Vietnamese translations, rich styling, and full interactivity.
"""

import os
from build_site import render_head, render_topbar, render_navbar, render_footer

OUTPUT_DIR = "C:/Users/sanon/projects/nutura-vietnam"

def save_page(filename, content):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filename} ({len(content)} bytes)")

print("Ready to generate pages.")
