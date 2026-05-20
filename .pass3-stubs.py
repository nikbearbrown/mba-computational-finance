#!/usr/bin/env python3
"""Insert portrait stubs into all 13 Wayback Machine sections.
Pacioli (1447-1517) is pre-1850s -> painting + portrait
All others are post-1850s -> photograph + portrait
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

SUBJECTS = [
    ("01-introduction-the-three-beat-method.md",                       "Lillian Gilbreth",            "c. 1920s",  "photograph", "portrait", "lillian-gilbreth.jpg"),
    ("02-returns-and-risk-measurement.md",                             "Louis Bachelier",             "c. 1900",   "photograph", "portrait", "louis-bachelier.jpg"),
    ("03-equity-and-fixed-income.md",                                  "Frederick Macaulay",          "c. 1930s",  "photograph", "portrait", "frederick-macaulay.jpg"),
    ("04-funds-and-etfs.md",                                           "Sylvia Porter",               "c. 1950s",  "photograph", "portrait", "sylvia-porter.jpg"),
    ("05-time-value-of-money-and-discounted-cash-flows.md",            "John Burr Williams",          "c. 1940s",  "photograph", "portrait", "john-burr-williams.jpg"),
    ("06-margin-and-short-selling.md",                                 "Hyman Minsky",                "c. 1980s",  "photograph", "portrait", "hyman-minsky.jpg"),
    ("07-options-and-derivatives.md",                                  "Vinzenz Bronzin",             "c. 1900",   "photograph", "portrait", "vinzenz-bronzin.jpg"),
    ("08-the-diversification-miracle.md",                              "A. D. Roy",                   "c. 1950s",  "photograph", "portrait", "a-d-roy.jpg"),
    ("09-portfolio-construction.md",                                   "James Tobin",                 "c. 1970s",  "photograph", "portrait", "james-tobin.jpg"),
    ("10-capital-allocation-and-diversification.md",                   "John Larry Kelly Jr.",        "c. 1960s",  "photograph", "portrait", "john-larry-kelly-jr.jpg"),
    ("11-asset-pricing-models.md",                                     "John Lintner",                "c. 1960s",  "photograph", "portrait", "john-lintner.jpg"),
    ("12-financial-statement-analysis.md",                             "Luca Pacioli",                "c. 1495",   "painting",   "portrait", "luca-pacioli.jpg"),
    ("13-putting-it-all-together-the-investment-decision-capstone.md", "Hetty Green",                 "c. 1900",   "photograph", "portrait", "hetty-green.jpg"),
]


def insert_stub(filename, name, era, src_type, img_type, jpg_filename):
    path = CH / filename
    text = path.read_text()
    header_idx = text.find("## AI Wayback Machine")
    if header_idx == -1:
        print(f"!!! no Wayback section in {filename}")
        return False
    run_idx = text.find("**Run this:**", header_idx)
    if run_idx == -1:
        print(f"!!! no Run-this block in {filename}")
        return False
    section_text = text[header_idx:run_idx]
    if re.search(r'!\[' + re.escape(name), section_text):
        print(f"  SKIP (stub already): {filename}")
        return False
    stub = (
        f"![{name}, {era}. AI-generated {img_type} based on a public domain {src_type} (Wikimedia Commons).]"
        f"(images/{jpg_filename})\n"
        f"*{name}, {era}. AI-generated {img_type} based on a public domain {src_type}.*\n\n"
    )
    before = text[:run_idx].rstrip() + "\n\n" + stub
    after = text[run_idx:]
    path.write_text(before + after)
    print(f"  inserted stub for {name} in {filename}")
    return True


def main():
    n = 0
    for entry in SUBJECTS:
        if insert_stub(*entry): n += 1
    print(f"\ntotal stubs inserted: {n}")


if __name__ == "__main__":
    main()
