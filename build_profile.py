#!/usr/bin/env python3
"""Generate every SVG in assets/ (light + dark), README.md and use-cases/*.md. Stdlib only.

    python3 build_profile.py              # write + validate SVGs and markdown
    python3 build_profile.py --preview    # also render previews to _preview/ (PyMuPDF; Chrome if present)
    python3 build_profile.py --only hero  # build a subset of static panels (comma-separated)
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from panels_agents import AGENTS, agents
from panels_approach import STEPS, approach
from panels_awards import AWARDS, awards
from panels_build import relay
from panels_concepts import CONCEPTS, concepts
from panels_curve import curve
from panels_evolution import evolution
from panels_maturity import maturity
from panels_method import method, stack, writing
from panels_solution import solution
from panels_top import hero, metrics
from panels_usecase import accbtn, case_card, tabbar, tabbtn, teaser, workflow
from panels_world import constellation, statement
from readme import case_alt, wf_alt, write_all
from svgkit import doc
from theme import THEMES
from usecases import CASES, TABS, workflow_for

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
MAX_BYTES = 150 * 1024

# name, builder, accessible title, description (also the README alt text)
PANELS = [
    ("hero", hero, "Shivaji M D, AI Solutions Engineer, Bengaluru",
     "From connectors that sync to agents that act. Animated: ERP, CRM, ticketing, HR, commerce, logistics, voice "
     "and knowledge bubbles feed a glowing enterprise-context core; an agent below it fires actions: deflect, "
     "resolve, automate."),
    ("metrics", metrics, "Business outcomes",
     "Under 5 minutes per airline payments-desk case, down from 15-30 (target); 16+ systems unified into one governed context; +50% conversion to proposal stage "
     "at MoEngage; 70+ BFSI projects; 13+ years in SaaS across engineering, customer success, presales and AI solutions."),
    ("maturity", maturity, "The AI maturity journey",
     "AI-centric employees create AI-centric companies. Two dotted curves. The AI employee journey: AI blind, "
     "AI curious, daily AI, expanding AI, AI first, AI evangelist. The AI company journey, running behind it: AI desert, "
     "AI tools, AI initiatives, AI champions, AI platform, AI-centric business."),
    ("evolution", evolution, "How I evolved",
     "Latest first: 2024-now AI Solutions Engineer at DevRev (generative and agentic AI, L4, M3-M4; airline "
     "payments desk 15-30 to under 5 min per case, target), then 2021-2024 Presales Manager to Lead Solutions Consulting at MoEngage "
     "(predictive ML, L2; +50% conversion to proposal). A dotted line points ahead to "
     "Solutions Architect, governed enterprise AI."),
    ("awards", awards, "Recognition",
     "Awards, latest first: " + "; ".join(f"{a[1]}, {a[2]}, {a[3]}" for a in AWARDS) + "."),
    ("approach", approach, "My approach",
     "A seven-step problem-solving loop: " + "; ".join(f"{i + 1} {t}" for i, (t, _, _) in enumerate(STEPS))
     + ". Each industry tab is one run of the loop."),
    ("concepts", concepts, "How sync actually works",
     "Nine connector concepts, each with its business effect: " + "; ".join(c[1] for c in CONCEPTS) + "."),
    ("agents", agents, "How agents actually work",
     "Twelve agent-design concepts, each with its business effect: " + "; ".join(a[1] for a in AGENTS) + "."),
    ("stack", stack, "Stack", "Agents and AI, context and integration, languages, and solution craft."),
    ("writing", writing, "Writing",
     "LinkedIn article, April 2026: Your AI agent doesn't have a knowledge problem. It has a noise problem."),
    # kept for later use; not in the README
    ("solution", solution, "Where AI met the solution", "Earlier relay view of selected cases."),
    ("curve", curve, "The maturity curve of my career", "Five career milestones on a rising dotted curve."),
    ("relay", relay, "What I build", "Context layer, guarded agent orchestration and a connector delta engine."),
    ("constellation", constellation, "Industries", "Industries sized by depth of work."),
    ("statement", statement, "Why work with me?", "Your AI is only as good as the context it can govern."),
    ("method", method, "How I run an engagement", "Nine engagement blocks as a staircase."),
]
README_ORDER = ["hero", "metrics", "maturity", "evolution", "awards", "approach", "tabs-airlines", "uc-airlines-1",
                "wf-airlines-1", "concepts", "agents", "stack", "writing"]


def dynamic():
    """(name, builder(T), title, desc) for tab bars, use-case cards and workflows."""
    out = []
    for slug, label in TABS:
        out.append((f"tabs-{slug}", lambda T, s=slug: tabbar(T, s), f"Industry tabs: {label}",
                    f"Industry tabs with {label} selected."))
        for on in (True, False):
            out.append((f"tab-{slug}-{'on' if on else 'off'}", lambda T, l=label, on=on: tabbtn(T, l, on),
                        f"Tab: {label}", f"{label} tab{' (selected)' if on else ''}"))
        out.append((f"acc-{slug}", lambda T, l=label, n=len(CASES[slug]): accbtn(T, l, n), f"Open {label}",
                    f"{label}: click to open"))
        for n, c in enumerate(CASES[slug], 1):
            out.append((f"uc-{slug}-{n}", lambda T, l=label, c=c, n=n: case_card(T, l, c, n), c["use"],
                        case_alt(label, c)))
            out.append((f"tz-{slug}-{n}", lambda T, l=label, c=c: teaser(T, l, c), c["use"],
                        f"{label}: {c['use']}. Outcome: {c['outcome']}. Click to open."))
            wf = workflow_for(c["use"])
            if wf:
                out.append((f"wf-{slug}-{n}", lambda T, c=c, wf=wf: workflow(T, c["use"], wf),
                            f"Workflow: {c['use']}", wf_alt(c, wf)))
    return out


def build(only=None):
    files = {}
    entries = list(PANELS) + ([] if only else dynamic())
    for theme, T in THEMES.items():
        for name, fn, title, desc in entries:
            if only and name not in only:
                continue
            w, h, body = fn(T)
            files[(name, theme)] = (doc(w, h, body, title, desc), w, h)
    return files


def write(files):
    ASSETS.mkdir(exist_ok=True)
    problems = []
    for (name, theme), (svg, _, _) in files.items():
        try:
            ET.fromstring(svg)
        except ET.ParseError as e:
            problems.append(f"INVALID {name}-{theme}: {e}")
        size = len(svg.encode())
        if size > MAX_BYTES:
            problems.append(f"TOO BIG {name}-{theme}: {size // 1024} KB")
        (ASSETS / f"{name}-{theme}.svg").write_text(svg, encoding="utf-8")
    return problems


def main(argv):
    only = set(argv[argv.index("--only") + 1].split(",")) if "--only" in argv else None
    files = build(only)
    problems = write(files)
    if not only:
        write_all(ROOT, PANELS)
    for p in problems:
        print(p, file=sys.stderr)
    biggest = max(len(s.encode()) for s, _, _ in files.values()) // 1024
    print(f"wrote {len(files)} SVGs to {ASSETS} (largest {biggest} KB), problems: {len(problems)}")
    if "--preview" in argv:
        from preview import render_all
        names = sorted({n for n, _ in files})
        order = [n for n in README_ORDER if n in names] if not only else names
        render_all(files, names, order, ROOT / "_preview")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
