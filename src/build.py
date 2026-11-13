#!/usr/bin/env python3
"""Build the guide (English and French) with pandoc.

Reads the two Markdown sources and generates, with the IBM Redbooks look and feel:
  content/index.html      English (default)
  content/fr/index.html   French

Usage:  python3 src/build.py      (requires pandoc)
Output: content/ (published by MkDocs)
"""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "..", "content")
TEMPLATE = os.path.join(HERE, "redbook-template.html")
TMP_MD = os.path.join(HERE, ".build-tmp.md")

PAGES = [
    {
        "lang": "en",
        "md": "GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs.md",
        "html": os.path.join(CONTENT, "index.html"),
        "kicker": "IBM Bob Premium Package for Z | Practitioner's guide",
        "subtitle": "Features, modes, workflows, skills and hands-on labs for mainframe developers and architects",
        "nav_title": "Contents",
        "switch_label": "FR",
        "switch_title": "Lire en français",
        "switch_href": "fr/",
        "footer": "Made with IBM Bob",
    },
    {
        "lang": "fr",
        "md": "GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs-FR.md",
        "html": os.path.join(CONTENT, "fr", "index.html"),
        "kicker": "IBM Bob Premium Package for Z | Guide pratique",
        "subtitle": "Fonctionnalités, modes, workflows, skills et labs pratiques pour les développeurs et architectes mainframe",
        "nav_title": "Sommaire",
        "switch_label": "EN",
        "switch_title": "Read in English",
        "switch_href": "../",
        "footer": "Réalisé avec IBM Bob",
    },
]


def build(page):
    with open(os.path.join(HERE, page["md"]), encoding="utf-8") as f:
        text = f.read()

    # Take the document title from the first H1, then drop it from the body
    m = re.search(r"^# (.+)$", text, flags=re.M)
    title = m.group(1).strip()
    text = text.replace(m.group(0) + "\n", "", 1)
    # Drop the "Language: English · Français" line (replaced by the masthead switch)
    text = re.sub(r"^🌐.*\n+", "", text, flags=re.M)

    with open(TMP_MD, "w", encoding="utf-8") as f:
        f.write(text)

    os.makedirs(os.path.dirname(page["html"]), exist_ok=True)
    cmd = [
        "pandoc", TMP_MD, "-f", "gfm", "-t", "html5",
        "--template", TEMPLATE, "--toc", "--toc-depth=3",
        "-M", "lang=" + page["lang"],
        "-M", "pagetitle=" + title,
        "-M", "title=" + title,
        "-M", "kicker=" + page["kicker"],
        "-M", "subtitle=" + page["subtitle"],
        "-M", "nav_title=" + page["nav_title"],
        "-M", "switch_label=" + page["switch_label"],
        "-M", "switch_title=" + page["switch_title"],
        "-M", "switch_href=" + page["switch_href"],
        "-M", "footer=" + page["footer"],
        "-o", page["html"],
    ]
    try:
        subprocess.check_call(cmd)
    finally:
        os.remove(TMP_MD)

    # Post-process: wrap tables so they scroll on small screens
    with open(page["html"], encoding="utf-8") as f:
        h = f.read()
    h = h.replace("<table>", '<div class="table-wrap"><table>').replace(
        "</table>", "</table></div>"
    )
    with open(page["html"], "w", encoding="utf-8") as f:
        f.write(h)
    print("html written: " + os.path.normpath(page["html"]))


def main():
    for page in PAGES:
        build(page)


if __name__ == "__main__":
    main()
