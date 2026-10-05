"""
Package the legal-templates skill as a zip for upload to Claude
(claude.ai / Claude desktop: Settings > Capabilities > Skills).

Bundles skills/legal-templates/SKILL.md together with every
templates/<slug>/ directory (README.md and template.md) into
dist/legal-templates.zip, with a single top-level legal-templates/
folder as the Skills uploader expects.

Usage:
    python3 scripts/build_skill.py

No third-party dependencies.
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "legal-templates"
TEMPLATES_DIR = ROOT / "templates"
OUT = ROOT / "dist" / "legal-templates.zip"

# Name of the folder at the top of the zip; must match the SKILL.md name.
TOP = "legal-templates"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    files = [(SKILL_DIR / "SKILL.md", f"{TOP}/SKILL.md")]
    # Read templates/ directly rather than through the skills/ symlink so
    # the build also works on checkouts where symlinks are disabled.
    for path in sorted(TEMPLATES_DIR.rglob("*.md")):
        rel = path.relative_to(TEMPLATES_DIR).as_posix()
        files.append((path, f"{TOP}/templates/{rel}"))

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arcname in files:
            zf.write(src, arcname)

    print(f"Wrote {OUT.relative_to(ROOT)} ({len(files)} files)")


if __name__ == "__main__":
    main()
