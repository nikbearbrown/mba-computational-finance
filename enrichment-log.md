# Enrichment + Cleanup Log

Run: 2026-05-05 — computational-finance-with-ai (pantry pass v1: anecdote enrichment)

## What changed (2026-05-05) — pantry pass v1 (anecdote enrichment)

User explicit instruction: "I'm particularly interested in adding some anecdotes and stories to what is currently a dry textbook." A 14-book pantry was provided. Audit of chapter narrative density showed Chs 4, 5, 6 had only 1–2 narrative-marker hits in ~5,000 words each — confirming the dryness diagnosis. Three targeted anecdote additions made; eleven pantry books skipped or held for later passes.

The pantry: *13 Bankers* (Johnson & Kwak), *Capital in the Twenty-First Century* (Piketty), *Crisis Economics* (Roubini), *Economic Gangsters*, *Extraordinary Popular Delusions and the Madness of Crowds* (Mackay), *Flash Boys* (Lewis), *Lombard Street* (Bagehot), *The Bankers' New Clothes* (Admati & Hellwig), *The Big Short* (Lewis), *The Black Swan* (Taleb), *The Intelligent Entrepreneur*, *The Physics of Wall Street* (Weatherall), *The Art of Statistics*, *The Book of Why* (Pearl).

### Three anecdote additions

| Ch | Source | Addition |
|---|---|---|
| 6 (Margin and Short Selling) | Lewis, *The Big Short* (2010) | New paragraph after the "fight the drift" passage, before the Tesla worked example. Tells the Michael Burry / Scion Capital subprime CDS story — Burry being right in 2005, his investors revolting in 2006 because they did not enjoy paying carry on a position the market disagreed with, his gating the fund to keep the position open, the lawsuit, the eventual 2007 vindication. The point is that being right and surviving the path to being proven right are different problems, in the structural geometry of a short. The chapter previously had only the GameStop 2021 case as a real-world anchor; the Burry story makes the carry-cost mechanism viscerally concrete. |
| 7 (Options and Derivatives) | Weatherall, *The Physics of Wall Street* (2013) | New paragraph immediately before the Black-Scholes formula introduction. Tells the seventy-three-year arc from Louis Bachelier's 1900 Sorbonne thesis (*Théorie de la spéculation*) — same continuous-random-motion mathematics physicists would borrow five years later for Brownian motion in water — through Henri Poincaré's polite second-tier grade, the half-century of disregard, Leonard Savage's 1950s rediscovery and postcard to Paul Samuelson, and the Black-Scholes-Merton finishing of the chain in 1973. Gives the formula on the next page a lineage; sets up why the constant-volatility assumption later becomes the contested seam (which the chapter already discusses). |
| 8 (Diversification Miracle) | Weatherall, *The Physics of Wall Street* (2013) | New section between the Buffett-on-concentration discussion and the closing summary. Tells the Markowitz / Friedman story — Markowitz's 1952 *Portfolio Selection* paper, the John Burr Williams reading-room insight, the Ph.D. defense at which Milton Friedman told Markowitz his work was not economics, the near-failure of the defense, the 1990 Nobel Prize for the same work. Lands the chapter's argument with a vivid demonstration that the variance-of-the-average move was, in living memory, a result strange enough that one of the most influential economists of the twentieth century could not place it. |

### Why these three and not more

The user asked for anecdotes — but the "don't force it" constraint still applies. The three additions chosen are the strongest pantry-to-chapter mappings in the entire 14-book pantry: each is a canonical financial story that maps directly onto an existing argument the chapter is making, and the story makes the argument viscerally concrete in a way the math alone does not.

### Pantry books not used (with brief reasoning)

- **Mackay, *Madness of Crowds*** — universally citable for bubble/crash anecdotes, but no specific chapter currently makes a bubble-mechanism argument that needs the South Sea / tulip / Mississippi cases. Held for a future pass if a chapter makes that argument explicitly.
- **Flash Boys** — HFT / market-microstructure stories don't fit Part 1 chapters, which are about prompting workflows and single-asset analysis. Likely stronger fit in Part 2/3 (Claude Code / Cowork chapters), still TBD per outline.
- **Lombard Street** (Bagehot) — classic banking anecdotes, but Part 1 doesn't have a chapter on banking systems specifically.
- **Pearl, *Book of Why*** — already heavily used in *Computational Skepticism for AI*; this finance book doesn't currently lean on Pearl's framework.
- **Black Swan** (Taleb) — already used in *Computational Skepticism for AI* Ch 14. Could add to CF-AI Ch 2 (returns/risk) or Ch 7 (options) but both are already well-grounded.
- **The Bankers' New Clothes**, **13 Bankers**, **Crisis Economics**, **Capital**, **Economic Gangsters**, **The Intelligent Entrepreneur**, **The Art of Statistics** — useful in their own right but not tightly mapped to the 13 drafted chapter arguments. Held.

**Citations to verify:**
- Lewis, M. (2010). *The Big Short: Inside the Doomsday Machine.* W. W. Norton.
- Weatherall, J. O. (2013). *The Physics of Wall Street: A Brief History of Predicting the Unpredictable.* Houghton Mifflin Harcourt.
- Bachelier, L. (1900). *Théorie de la spéculation.* Annales scientifiques de l'École Normale Supérieure.
- Markowitz, H. (1952). Portfolio Selection. *Journal of Finance* 7(1):77–91.
- Friedman's exact remark at Markowitz's defense — verify against Markowitz's Nobel lecture and subsequent interviews.

---

## What changed (earlier passes)

### Build infrastructure added

`bash build.sh` now produces `output/computational-finance-with-ai.epub` and `output/computational-finance-with-ai.html`. Build verified clean: 15 chapter splits (frontmatter + preface + 13 content chapters).

Files added: `metadata.yaml`, `styles/kindle.css`, `styles/kindle-book.css`, `build.sh` (executable), `images/` directory.

### Pass 3 — 13 portrait stubs inserted

Wayback Machine subjects were authored in a prior pass under the no-post-2000-alive rule. This pass added the spec-format portrait stubs.

| Ch | Subject | Era | Source type |
|---|---|---|---|
| 1 | Lillian Gilbreth (1878–1972) | c. 1920s | photograph |
| 2 | Louis Bachelier (1870–1946) | c. 1900 | photograph |
| 3 | Frederick Macaulay (1882–1970) | c. 1930s | photograph |
| 4 | Sylvia Porter (1913–1991) | c. 1950s | photograph |
| 5 | John Burr Williams (1900–1989) | c. 1940s | photograph |
| 6 | Hyman Minsky (1919–1996) | c. 1980s | photograph |
| 7 | Vinzenz Bronzin (1872–1970) | c. 1900 | photograph |
| 8 | A. D. Roy (1920–2003) | c. 1950s | photograph |
| 9 | James Tobin (1918–2002) | c. 1970s | photograph |
| 10 | John Larry Kelly Jr. (1923–1965) | c. 1960s | photograph |
| 11 | John Lintner (1916–1983) | c. 1960s | photograph |
| 12 | Luca Pacioli (1447–1517) | c. 1495 | **painting** (pre-1850s) |
| 13 | Hetty Green (1834–1916) | c. 1900 | photograph |

### Pass 1 — 13 tables rendered

Distribution: Ch 1 (2), Ch 2 (2), Ch 4 (1), Ch 5 (2), Ch 7 (1), Ch 8 (1), Ch 9 (1), Ch 11 (1), Ch 12 (1), Ch 13 (2). Highlights: the five-element specification checklist (Ch 1); the Cross-LLM comparison matrix on Maya's NVDA analysis showing where the substantive disagreement lives in the Sharpe row (Ch 1); the simple/log/total return reference card (Ch 2); the open-end / closed-end / ETF structural-comparison table with the 1924/1893/1993 introduction dates (Ch 4); the worked $300/year DCF table and the 4×4 NPV sensitivity grid (Ch 5); the Black-Scholes input summary highlighting σ as the only estimated input (Ch 7); the three-pair correlation comparison (Ch 8); the calm-vs-crisis correlation breakdown that explains why optimizer-built portfolios fail in 2008 (Ch 9); the factor premium summary across CAPM and the Fama-French extensions (Ch 11); the DuPont decomposition showing MSFT, AAPL, GOOGL with Apple's 6.6× leverage multiplier (Ch 12); the NVDA peer-comparison table for the capstone (Ch 13).

### Pass 2 — 9 SVG/PNG figures generated

All figures in editorial monochrome warm-grayscale, Georgia serif, 1px borders, no rounded corners or gradients. PNGs at 2× the SVG viewBox.

| Slug | Topic |
|---|---|
| 02-…-fig-01 | NVDA monthly-return histogram with fitted-normal overlay |
| 04-…-fig-01 | The Authorized Participant arbitrage loop (two panels: above-NAV / below-NAV) |
| 05-…-fig-01 | Compounding and discounting as one operation run two ways |
| 06-…-fig-01 | Margin-account balance sheets at entry vs. after a 28.6% drop |
| 06-…-fig-02 | Short-sale four-party flow diagram |
| 07-…-fig-01 | One-step binomial tree + replicating portfolio at $11.90 |
| 11-…-fig-01 | Idiosyncratic risk cancels in a 500-stock portfolio; market risk does not |
| 12-…-fig-01 | The three statements as one interconnected system |
| 13-…-fig-01 | The five-layer dependency stack from return measurement up to capital allocation |

## Per-chapter results

00-frontmatter.md — 0 tables, 0 figures, no Wayback (front matter)
00-preface-and-toc.md — 0 tables, 0 figures, no Wayback (preface)
01-introduction-the-three-beat-method.md — 2 tables, 0 figures, Wayback: stub inserted (Lillian Gilbreth)
02-returns-and-risk-measurement.md — 2 tables, 1 figure, Wayback: stub inserted (Louis Bachelier)
03-equity-and-fixed-income.md — 0 tables, 0 figures, Wayback: stub inserted (Frederick Macaulay)
04-funds-and-etfs.md — 1 table, 1 figure, Wayback: stub inserted (Sylvia Porter)
05-time-value-of-money-and-discounted-cash-flows.md — 2 tables, 1 figure, Wayback: stub inserted (John Burr Williams)
06-margin-and-short-selling.md — 0 tables, 2 figures, Wayback: stub inserted (Hyman Minsky)
07-options-and-derivatives.md — 1 table, 1 figure, Wayback: stub inserted (Vinzenz Bronzin)
08-the-diversification-miracle.md — 1 table, 0 figures, Wayback: stub inserted (A. D. Roy)
09-portfolio-construction.md — 1 table, 0 figures, Wayback: stub inserted (James Tobin)
10-capital-allocation-and-diversification.md — 0 tables, 0 figures, Wayback: stub inserted (John Larry Kelly Jr.)
11-asset-pricing-models.md — 1 table, 1 figure, Wayback: stub inserted (John Lintner)
12-financial-statement-analysis.md — 1 table, 1 figure, Wayback: stub inserted (Luca Pacioli)
13-putting-it-all-together-the-investment-decision-capstone.md — 2 tables, 1 figure, Wayback: stub inserted (Hetty Green)

## Summary

Total chapters processed: 15
Total tables rendered: 13
Total figures generated (SVG+PNG pairs): 9
Total Wayback Machine portrait stubs inserted: 13
Total Wayback Machine subject replacements: 0 (subjects were authored under the rule)

## Setup notes / spec interpretations

- **Pacioli (Ch 12) is pre-1850s.** Stub uses `painting` and `portrait` per the spec; the canonical reference is Jacopo de' Barbari's c. 1495 portrait of Pacioli.
- **`INFOGRAPHIC` / `CHART` comments left untouched.** The book has 7 INFOGRAPHIC and 19 CHART comments, all out of scope per the spec's literal Pass-2 token list. Concentration: Ch 8 (3), Ch 9 (2), Ch 10 (3), Ch 11 (2). If the intent was to render these too, expand the token list and re-run.
- **Preface H1 mismatch.** `chapters/00-preface-and-toc.md` opens with `# Causal Inference with Case Studies` — clearly a leftover heading from another book. Not in the spec's edit scope, but worth correcting before publish. The fix is a one-line change to the H1.

## Action items

### 1. Generate 13 Wayback portrait .jpg files

`lillian-gilbreth.jpg`, `louis-bachelier.jpg`, `frederick-macaulay.jpg`, `sylvia-porter.jpg`, `john-burr-williams.jpg`, `hyman-minsky.jpg`, `vinzenz-bronzin.jpg`, `a-d-roy.jpg`, `james-tobin.jpg`, `john-larry-kelly-jr.jpg`, `john-lintner.jpg`, `luca-pacioli.jpg`, `hetty-green.jpg`.

### 2. Add a cover image

`build.sh` looks for `cover.jpg` at the book root for KDP upload (1600×2560 JPEG).

### 3. Fix the preface H1

`chapters/00-preface-and-toc.md` line 1 currently reads `# Causal Inference with Case Studies`. Should be the actual book title (or a preface-specific heading) — the EPUB chapter list shows this as `ch002.xhtml: Causal Inference with Case Studies`, which would surprise a reader.

### 4. INFOGRAPHIC / CHART comments out of literal scope

7 INFOGRAPHIC + 19 CHART comments remain across the book. Expanding the Pass-2 token list to include these would generate ~26 additional figures.

## Build commands

```
cd books/computational-finance-with-ai
./build.sh
```

Outputs land in `output/`: `computational-finance-with-ai.epub`, `computational-finance-with-ai.html`, and `combined.md` (archival concatenated source).
