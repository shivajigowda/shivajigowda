"""Write README.md and use-cases/<slug>.md from the panel registry and the use-case data."""
from pathlib import Path
from urllib.parse import quote

from panels_agents import AGENTS
from panels_approach import STEPS
from panels_concepts import CONCEPTS
from panels_evolution import ERAS
from panels_usecase import loop_step
from usecases import CASES, TABS, workflow_for

LINKEDIN = "https://www.linkedin.com/in/shivaji-md-ab983a65"
ARTICLES = "https://www.linkedin.com/in/shivaji-md-ab983a65/recent-activity/articles/"
EMAIL = "shiv.shivaji090@gmail.com"


def pic(base, alt, prefix="assets/"):
    return (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{prefix}{base}-dark.svg">\n'
            f'  <img alt="{alt}" src="{prefix}{base}-light.svg" width="100%">\n</picture>\n')


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
            f"{c['solution']}. Business outcome: {c['outcome']}. Maturity {c['tag']}; KPI: {c['kpi']}. "
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
        out.append(f"**{c['use']}** · {c['tag']} · {c['outcome']}\n\n- Problem: {c['problem']}\n- AI did: {c['ai']}\n"
                   f"- Solution did: {c['solution']}\n- Architecture: {' → '.join(c['arch'])}\n")
    return "\n".join(out)


def industry_page(slug, label):
    parts = [f"# {label}: AI use cases I've solutioned\n", "[← back to profile](../README.md)\n",
             pic(f"tabs-{slug}", f"Industry tabs, {label} selected", "../assets/"), tab_links(slug, "") + "\n"]
    for n, c in enumerate(CASES[slug], 1):
        parts.append(case_block(slug, label, n, c, "../assets/"))
    parts.append("<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, "
                 "achieved, proposal or pilot exactly as the source work states them.</sub>\n")
    return "\n".join(parts)


def concept_text(items):
    return "\n".join(f"{i + 1}. **{c[1]}**: {c[2]} *Business:* {c[6]}. *Used in:* {c[3]}." for i, c in enumerate(items))


def evolution_text():
    out = []
    for years, role, company, (wave, _), level, nodes, outcome, rows, learned in ERAS:
        chips = "; ".join(f"{lab}: {', '.join(c)}" for lab, c in rows)
        out.append(f"- **{years} · {role}, {company}** ({wave}, {level}). Pipeline: "
                   f"{' → '.join(t for t, _ in nodes)} → {outcome}. {chips}. Learned: {learned}")
    return "\n".join(out) + (
        "\n\nExplainers I used with customers (general techniques, not vendor claims): propensity models are "
        "typically gradient-boosted trees; behavioral clustering, e.g. k-means; a multi-armed bandit shifts traffic "
        "to the winning variant while still exploring; RFM scores recency, frequency and monetary value; "
        "aggregations turn event streams into features (counts, recency, rolling windows).")


def readme(panels):
    alt = {name: desc for name, _, _, desc in panels}
    a_slug, a_label = TABS[0]
    others = "\n".join(
        f"<details>\n<summary><b>{label}</b>: {len(CASES[slug])} use case{'s' if len(CASES[slug]) > 1 else ''}"
        f"</summary>\n\n"
        + "\n".join(case_block(slug, label, n, c, "assets/") for n, c in enumerate(CASES[slug], 1))
        + f"\n[Open the {label} page](use-cases/{slug}.md)\n\n</details>\n" for slug, label in TABS[1:])
    badges = (f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-shivaji--md-6E22FE?style=for-the-badge&logo=linkedin"
              f"&logoColor=white&labelColor=151515)]({LINKEDIN}) "
              f"[![Email](https://img.shields.io/badge/Email-{quote(EMAIL.replace('-', '--'))}-FDF049?style=for-the-badge"
              f"&logo=gmail&logoColor=151515&labelColor=151515)](mailto:{EMAIL})")
    loop = "\n".join(f"{i + 1}. **{t}**: {d}" for i, (t, d, _) in enumerate(STEPS))
    return f"""{pic('hero', alt['hero'])}
{badges}

{pic('metrics', alt['metrics'])}
{pic('maturity', alt['maturity'])}
{pic('evolution', alt['evolution'])}
<details>
<summary><b>Text version: how I evolved</b></summary>

{evolution_text()}

</details>

{pic('approach', alt['approach'])}
<details>
<summary><b>Text version: my approach</b></summary>

{loop}

</details>

## AI use cases I've solutioned

{pic(f'tabs-{a_slug}', f'Industry tabs, {a_label} selected')}
{tab_links(a_slug, 'use-cases/')}

{case_block(a_slug, a_label, 1, CASES[a_slug][0], 'assets/')}
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


def write_all(root, panels):
    (root / "README.md").write_text(readme(panels), encoding="utf-8")
    pages = root / "use-cases"
    pages.mkdir(exist_ok=True)
    for slug, label in TABS:
        (pages / f"{slug}.md").write_text(industry_page(slug, label), encoding="utf-8")
