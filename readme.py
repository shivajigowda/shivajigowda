"""Write README.md and use-cases/<slug>.md from the panel registry and the use-case data."""
from pathlib import Path
from urllib.parse import quote

from panels_agents import AGENTS
from panels_approach import STEPS
from panels_concepts import CONCEPTS
from panels_evolution import ERAS
from panels_usecase import loop_step
from usecases import CASES, TABS, workflow_for

LINKEDIN = "https://www.linkedin.com/in/shivaji-m-d-ab983a65"
ARTICLES = "https://www.linkedin.com/in/shivaji-m-d-ab983a65/recent-activity/articles/"
EMAIL = "shiv.shivaji090@gmail.com"


def pic(base, alt, prefix="assets/"):
    return (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{prefix}{base}-dark.svg">\n'
            f'  <img alt="{alt}" src="{prefix}{base}-light.svg" width="100%">\n</picture>\n')


def tab_buttons(active, link_prefix, asset_prefix):
    """Row of clickable tab images; each links to its industry page."""
    out = []
    for slug, label in TABS:
        state = "on" if slug == active else "off"
        base = f"{asset_prefix}tab-{slug}-{state}"
        out.append(f'<a href="{link_prefix}{slug}.md"><picture><source media="(prefers-color-scheme: dark)" '
                   f'srcset="{base}-dark.svg"><img alt="{label}" src="{base}-light.svg" height="40"></picture></a>')
    return "\n".join(out)


def teaser_grid(asset_prefix="assets/", link_prefix="use-cases/"):
    """3-across grid of teaser cards; each links to its industry page."""
    cells = []
    for slug, label in TABS:
        for n, c in enumerate(CASES[slug], 1):
            base = f"{asset_prefix}tz-{slug}-{n}"
            alt_ = f"{label}: {c['use']}. Outcome: {c['outcome']}. Click to open.".replace('"', "'")
            cells.append(f'<a href="{link_prefix}{slug}.md"><picture><source media="(prefers-color-scheme: dark)" '
                         f'srcset="{base}-dark.svg"><img alt="{alt_}" src="{base}-light.svg" width="32%"></picture></a>')
    return "<p align=\"center\">\n" + "\n".join(cells) + "\n</p>"


def acc_summary(slug, label, asset_prefix="assets/"):
    base = f"{asset_prefix}acc-{slug}"
    return (f'<summary><picture><source media="(prefers-color-scheme: dark)" srcset="{base}-dark.svg">'
            f'<img alt="{label}: click to open" src="{base}-light.svg" width="100%"></picture></summary>')


def tab_links(active, prefix):
    out = []
    for slug, label in TABS:
        colour = "6E22FE" if slug == active else "F2ECFE"
        text_c = "" if slug == active else "&labelColor=F2ECFE"
        badge = f"https://img.shields.io/badge/{quote(label.replace('-', '--'))}-{colour}?style=flat-square{text_c}"
        out.append(f'<a href="{prefix}{slug}.md"><img alt="{label}" src="{badge}"></a>')
    return " ".join(out)


def case_alt(industry, c):
    return (f"{industry} use case: {c['use']}. Problem: {c['problem']}. AI did: {c['ai']}. Solution did: "
            f"{c['solution']}. Business outcome: {c['outcome']}. KPI: {c['kpi']}. "
            f"Architecture: {' → '.join(c['arch'])}.").replace('"', "'")


def wf_alt(c, wf):
    steps = "; ".join(f"{i + 1} {a.lower()}: {t}" for i, (a, t) in enumerate(wf["steps"]))
    return f"Solution workflow ({wf['type']}) for {c['use']}: {steps}".replace('"', "'")


def wf_text(wf):
    rows = [f"{i + 1}. **{a.title()}** (loop step {loop_step(a.upper(), t)}): {t}" for i, (a, t) in enumerate(wf["steps"])]
    return "\n".join(rows)


def case_block(slug, label, n, c, prefix, with_text=True):
    base = f"{slug}-{n}"
    out = [pic(f"uc-{base}", case_alt(label, c), prefix)]
    wf = workflow_for(c["use"])
    if wf:
        out.append(pic(f"wf-{base}", wf_alt(c, wf), prefix))
        out.append(f"<details>\n<summary>Workflow steps as text: {c['use']}</summary>\n\n{wf_text(wf)}\n\n</details>\n")
    if with_text:
        out.append(f"**{c['use']}** · {c['outcome']}\n\n- Problem: {c['problem']}\n- AI did: {c['ai']}\n"
                   f"- Solution did: {c['solution']}\n- Architecture: {' → '.join(c['arch'])}\n")
    return "\n".join(out)


def industry_page(slug, label):
    parts = [f"# {label}: AI use cases I've solutioned\n", "[← back to profile](../README.md)\n",
             "<p align=\"center\">\n" + tab_buttons(slug, "", "../assets/") + "\n</p>\n"]
    for n, c in enumerate(CASES[slug], 1):
        parts.append(case_block(slug, label, n, c, "../assets/"))
    parts.append("<sub>Anonymized: industries and generic system types only.</sub>\n")
    return "\n".join(parts)


def concept_text(items):
    return "\n".join(f"{i + 1}. **{c[1]}**: {c[2]} *Business:* {c[6]}. *Used in:* {c[3]}." for i, c in enumerate(items))


def evolution_text():
    out = []
    for years, role, company, (wave, _), level, nodes, outcome, rows, learned in ERAS:
        chips = "; ".join(f"{lab}: {', '.join(c)}" for lab, c in rows)
        out.append(f"- **{years} · {role}, {company}** ({wave}, {level}). Pipeline: "
                   f"{' → '.join(t for t, _ in nodes)} → outcomes: {', '.join(f'{lab} {a}' for a, lab in outcome)}. {chips}. Learned: {learned}")
    return "\n".join(out) + (
        "\n\nExplainers I used with customers (general techniques, not vendor claims): propensity models are "
        "typically gradient-boosted trees; behavioral clustering, e.g. k-means; a multi-armed bandit shifts traffic "
        "to the winning variant while still exploring; RFM scores recency, frequency and monetary value; "
        "aggregations turn event streams into features (counts, recency, rolling windows).")


def readme(panels):
    alt = {name: desc for name, _, _, desc in panels}
    a_slug, a_label = TABS[0]
    others = "\n".join(
        f"<details>\n{acc_summary(slug, label)}\n\n"
        + "\n".join(case_block(slug, label, n, c, "assets/") for n, c in enumerate(CASES[slug], 1))
        + f"\n[Open the {label} page](use-cases/{slug}.md)\n\n</details>\n" for slug, label in TABS)
    HEADLINE = ["AI Solutions Engineer", "Context layer first, agents on top",
                "Agentic AI across complex enterprise systems", "Guardrails, evals and human gates built in",
                "13+ yrs SaaS · 5+ yrs AI · 3+ yrs GenAI", "APJ SE of the Year"]
    badges = (f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-shivaji--md-6E22FE?style=for-the-badge&logo=linkedin"
              f"&logoColor=white&labelColor=151515)]({LINKEDIN}) "
              f"[![Email](https://img.shields.io/badge/Email-{quote(EMAIL.replace('-', '--'))}-FDF049?style=for-the-badge"
              f"&logo=gmail&logoColor=151515&labelColor=151515)](mailto:{EMAIL})")
    loop = "\n".join(f"{i + 1}. **{t}**: {d}" for i, (t, d, _) in enumerate(STEPS))
    return f"""{pic('hero', alt['hero'])}

**{HEADLINE[0]}** | {" | ".join(HEADLINE[1:])}

{badges}

{pic('maturity', alt['maturity'])}
{pic('evolution', alt['evolution'])}
<details>
<summary><b>Text version: how I evolved</b></summary>

{evolution_text()}

</details>

{pic('awards', alt['awards'])}

{pic('approach', alt['approach'])}
<details>
<summary><b>Text version: my approach</b></summary>

{loop}

</details>

## AI use cases I've solutioned

Click any card to open its full page (architecture and step-by-step workflow), or expand an industry below.

{teaser_grid()}

### Full details by industry

{others}
## Concepts

<details>
<summary><b>How sync actually works: 9 concepts</b></summary>

{pic('concepts', alt['concepts'])}
{concept_text(CONCEPTS)}

</details>

<details>
<summary><b>How agents actually work: 12 concepts</b></summary>

{pic('agents', alt['agents'])}
{concept_text(AGENTS)}

</details>

{pic('stack', alt['stack'])}
<a href="{ARTICLES}">
{pic('writing', alt['writing'])}</a>

<sub>Every visual is generated by [build_profile.py](build_profile.py) (stdlib Python; `python3 build_profile.py --preview`
renders previews). Client names are left out on purpose: industries and generic system types only.</sub>
"""


def _versioned(md, base_dir):
    """Append ?v=<content hash> to every local .svg reference so GitHub and browsers never serve stale panels."""
    import hashlib
    import re

    def tag(m):
        ref = m.group(2)
        f = (base_dir / ref).resolve()
        if not f.exists():
            return m.group(0)
        v = hashlib.sha1(f.read_bytes()).hexdigest()[:8]
        return f'{m.group(1)}="{ref}?v={v}"'
    return re.sub(r'(src|srcset)="((?:\.\./)?assets/[^"?]+\.svg)"', tag, md)


def write_all(root, panels):
    (root / "README.md").write_text(_versioned(readme(panels), root), encoding="utf-8")
    pages = root / "use-cases"
    pages.mkdir(exist_ok=True)
    for slug, label in TABS:
        (pages / f"{slug}.md").write_text(_versioned(industry_page(slug, label), pages), encoding="utf-8")
