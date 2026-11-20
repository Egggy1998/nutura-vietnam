<div align="center">

# Nutura Việt Nam

**Brand & nutrition information site for Nutura Organic (Victoria, Australia) — 19 pages, Vietnamese market.**

[Live site](https://nutura-vietnam.pages.dev) · [WCAG 2.1 AA](#accessibility) · [AI-crawler ready](#seo--ai-discoverability)

</div>

---

## What this is

A complete Vietnamese-language information site for an imported organic infant formula brand: brand story, product stages 1–3, nutrition science, label lookup, FAQs and authorised retailer guidance.

**It is deliberately not a shop.** Vietnamese regulation (Nghị định 100/2014/NĐ-CP) restricts advertising and online sale of infant formula — so the site carries nutrition and label information only: no cart, no prices, no e-commerce.

This constraint shaped the whole build. Every page had to earn trust through information quality rather than conversion mechanics.

## Structure

| Path | Page |
|---|---|
| `index.html` | Brand overview, positioning |
| `product-stage1.html` | Nutura Organic Stage 1 (0–6 months) |
| `product-stage2.html` | Stage 2 (6–12 months) |
| `product-stage3.html` | Stage 3 (12–36 months) |
| `about-us.html` | Company, Australian origin, ACO certification |
| `fresh-milk-difference.html` | Farmgate fresh milk vs. powder-reconstituted |
| `certified-organic.html` | Australian Certified Organic chain of custody |
| `breast-is-best.html` | WHO / Vietnamese health-authority guidance |
| `faqs.html` | Parent questions |
| `contact.html` | Authorised retail points |

## Technical approach

The site is generated, not hand-maintained.

```
build_site.py      → assembles pages from Python templates
build_all.py       → full rebuild + sitemap
generate_site.py   → content generation helpers
pages_home.py      → shared layout / nav / footer
```

Static HTML out, deployed to **Cloudflare Pages**. No framework, no build step at runtime — pages load in under a second on 3G.

### Accessibility

- WCAG 2.1 AA contrast ratios on every colour pair
- Semantic landmarks, skip links, visible focus rings
- Full keyboard navigation, ARIA labels on interactive elements
- `prefers-reduced-motion` respected — Lenis smooth scroll disables itself

### SEO & AI discoverability

- `llms.txt` — structured summary so ChatGPT / Claude / Perplexity cite the brand accurately instead of guessing
- Per-page meta, canonical URLs, Open Graph, JSON-LD `Organization` + `Product`
- Sitemap generated at build time

## Notes for contributors

All nutrition figures are transcribed from the official Vietnamese label declarations (TCCS 01/2026, 02/2026, 03/2026). **Do not edit numbers without a source document.** This is regulated content.

---

<div align="center">
<sub>Built as a static generator because a CMS would have been 40× the cost and 10× the attack surface.</sub>
</div>
