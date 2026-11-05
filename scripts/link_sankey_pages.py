"""Point the packaged Sankey's labels at the published Zensical pages."""

from html import escape, unescape
from pathlib import Path
from urllib.parse import urljoin
from zipfile import ZipFile
import json
import re
import tomllib


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "artefacts/DAMA_FAIR_Sankey_v1.2.0.zip"
DESTINATION = ROOT / "docs/fair-alignment/sankey-v1.1.0.html"
FAIR_PAGE = ROOT / "site/dama/fair-principles/index.html"


def main() -> None:
    site_url = tomllib.loads((ROOT / "zensical.toml").read_text())["project"]["site_url"]
    if not site_url.startswith("https://") or not site_url.endswith("/"):
        raise ValueError("site_url must be a canonical HTTPS directory URL")

    with ZipFile(PACKAGE) as archive:
        prefix = "dama-fair-sankey-v1.2.0/"
        html = archive.read(prefix + "index.html").decode("utf-8")
        original_anchors = json.loads(archive.read(prefix + "section-links.json"))
        data = json.loads(archive.read(prefix + "data.json"))

    areas = data["areas"]
    principles = [item["id"] for item in data["principles"]]
    if len(areas) != 11 or len(principles) != 15:
        raise ValueError("Unexpected Sankey label count")
    if set(original_anchors) != set(areas) | set(principles):
        raise ValueError("Sankey labels differ from section-links.json")

    urls = {}
    for label in areas:
        number_match = re.match(r"^(\d+)-", original_anchors[label])
        if number_match is None:
            raise ValueError(f"No segment number for {label}")
        number = int(number_match.group(1))
        candidates = list((ROOT / "docs/dama/segments").glob(f"{number:02d}-*.md"))
        if len(candidates) != 1:
            raise ValueError(f"Expected one segment page for {label}: {candidates}")
        stem = candidates[0].stem
        if not (ROOT / "site/dama/segments" / stem / "index.html").is_file():
            raise FileNotFoundError(f"Build the segment page before mapping {label}")
        urls[label] = urljoin(site_url, f"dama/segments/{stem}/")

    rendered = FAIR_PAGE.read_text(encoding="utf-8")
    fair_anchors = {}
    for anchor, heading in re.findall(r'<h2 id="([^"]+)">([^<]+)', rendered):
        principle_id = unescape(heading).split(" — ", 1)[0]
        if principle_id in principles:
            if principle_id in fair_anchors:
                raise ValueError(f"Duplicate FAIR heading: {principle_id}")
            fair_anchors[principle_id] = anchor
    if set(fair_anchors) != set(principles):
        raise ValueError(f"Missing FAIR headings: {set(principles) - set(fair_anchors)}")
    for principle_id in principles:
        urls[principle_id] = urljoin(
            site_url, f"dama/fair-principles/#{fair_anchors[principle_id]}"
        )

    start_marker = "    const sectionAnchors="
    end_marker = "    const chart="
    if html.count(start_marker) != 1 or html.count(end_marker) != 1:
        raise ValueError("Packaged Sankey script layout has changed")
    start = html.index(start_marker)
    end = html.index(end_marker, start)
    script = (
        "    // Published Zensical destinations for all 26 diagram labels.\n"
        f"    const pageUrls={json.dumps(urls, ensure_ascii=False)};\n"
        "    function sectionHref(id){\n"
        "      if(!Object.hasOwn(pageUrls,id)) throw new Error(`Missing page for ${id}`);\n"
        "      return pageUrls[id];\n"
        "    }\n"
    )
    line_ending = "\r\n" if "\r\n" in html else "\n"
    encoded = escape(script, quote=True).replace("\n", line_ending)
    html = html[:start] + encoded + html[end:]

    outer_start_marker = "  const requestedDocument ="
    outer_end_marker = (
        '  frame.dataset.srcdoc = frame.dataset.srcdoc.replace('
        '"__DAMA_DOCUMENT_URL__", encodedDocument);'
    )
    if html.count(outer_start_marker) != 1 or html.count(outer_end_marker) != 1:
        raise ValueError("Packaged document URL bootstrap has changed")
    outer_start = html.index(outer_start_marker)
    outer_end = html.index(outer_end_marker, outer_start) + len(outer_end_marker)
    html = (
        html[:outer_start]
        + "  // Diagram labels use the generated Zensical page map."
        + html[outer_end:]
    )
    if "DAMA_Segments_High_Level_v1.17.0.html" in html:
        raise ValueError("Old reading-copy target remains in the diagram")
    DESTINATION.write_bytes(html.encode("utf-8"))
    print(f"Mapped {len(areas)} DAMA and {len(principles)} FAIR labels to {site_url}")


if __name__ == "__main__":
    main()
