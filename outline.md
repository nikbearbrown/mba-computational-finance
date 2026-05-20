# Computational Finance with AI — Chapter Outline

*Each chapter: working title + one-sentence purpose. Architecture locked through Phase 3 — see `architecture-toc.md` for the full design document including opening scenes, learning outcomes, default projects, primary verification techniques, and bridges between chapters.*

---

## To write

### Part 2: Beyond Prompting — Working with Claude Code

- **Extended Example 2A — TBD** — *Specific topic deferred (logged in `architecture-toc.md` as O-002). Likely candidate: portfolio analyzer with live data pipeline, DCF automation across multiple companies, financial statement parser at scale, or reproducible Monte Carlo simulation.* (40–60 pp)
- **Extended Example 2B — TBD** — *Same status. Second example chosen to complement 2A by demonstrating a different Claude Code capability — reproducibility, file artifacts, or scale.* (40–60 pp)

### Part 3: Beyond Files — Workflow Orchestration with Claude Cowork

- **Extended Example 3A — TBD** — *Specific topic deferred (O-003). Likely candidate: quarterly investment review pipeline (multi-source data → analysis → report), risk dashboard for multi-asset portfolio, NLP-based earnings call sentiment pipeline, or automated competitive analysis from financial filings.* (40–60 pp)
- **Extended Example 3B — TBD** — *Second orchestration example, chosen for tighter coupling to the Mycroft workflow architecture.* (40–60 pp)

## Drafted

*Rough first drafts for all 13 Part 1 chapters drafted 2026-04-27, renamed to NN-kebab-case-title convention 2026-04-27. All `voice-unanchored` (style/ folder empty at drafting). All carry `[verify]` markers on factual claims that need primary-source confirmation before publication. Drafts adapt source material from the Excel-Python-LLMs trilateral pasted material to the AI-native, Claude-centric architecture defined in `architecture-toc.md`.*

### Part 1: Computational Finance with Claude — Prompting Foundations

**Act One — Establish (single-asset analysis)**

- **Chapter 1 — Introduction: The Three-Beat Method** — *The reader sets up Claude, learns the idea-execute-verify spine that powers every chapter, and produces a working NVDA analysis their boss could actually read on Monday morning.* — `01-introduction-the-three-beat-method.md`
- **Chapter 2 — Returns and Risk Measurement** — *The reader can take any publicly traded asset and produce a defensible return-and-risk analysis — annualized return, volatility, Sharpe — with cross-LLM verification that survives committee scrutiny.* — `02-returns-and-risk-measurement.md`
- **Chapter 3 — Equity and Fixed Income** — *The reader understands the structural difference between owning equity and holding debt, can value both a stock (DDM, simplified DCF) and a bond (yield-to-maturity), and catches internal inconsistencies in AI-generated valuations.* — `03-equity-and-fixed-income.md`
- **Chapter 4 — Funds and ETFs** — *The reader can construct a defensible fund-based portfolio for a real investor profile and choose between active and passive vehicles on cost-adjusted reasoning rather than belief.* — `04-funds-and-etfs.md`
- **Chapter 5 — Time Value of Money and Discounted Cash Flows** — *The reader can take any cash flow stream — acquisition, real estate, project, retirement — and produce a defensible NPV/IRR analysis with sensitivity testing.* — `05-time-value-of-money-and-discounted-cash-flows.md`
- **Chapter 6 — Margin and Short Selling** — *The reader understands exactly how margin and short selling work, can calculate leveraged risk under multiple scenarios, and can evaluate whether leverage is appropriate for a given investor.* — `06-margin-and-short-selling.md`
- **Chapter 7 — Options and Derivatives** — *The reader understands how options create asymmetric payoffs, can price European options via binomial and Black-Scholes, and can design option strategies that match a stated market view and risk tolerance.* — `07-options-and-derivatives.md`

**Act Two — Build (portfolio thinking)**

- **Chapter 8 — The Diversification Miracle** — *The reader makes the conceptual leap from single-asset thinking to portfolio thinking and can defend diversification to a skeptic using the math of correlation rather than the slogan.* — `08-the-diversification-miracle.md`
- **Chapter 9 — Portfolio Construction** — *The reader can construct an efficient frontier for any chosen asset universe, identify minimum-variance and maximum-Sharpe portfolios, and document a portfolio construction process for a stated investor.* — `09-portfolio-construction.md`
- **Chapter 10 — Capital Allocation and Diversification** — *The reader can solve for the optimal mix of risky and risk-free assets given stated risk aversion and can evaluate whether an investment manager is adding value relative to fees.* — `10-capital-allocation-and-diversification.md`
- **Chapter 11 — Asset Pricing Models** — *The reader can estimate beta with a calculated confidence interval, diagnose why CAPM-predicted return differs from actual return, and judge when CAPM is appropriate versus when a multifactor model is needed.* — `11-asset-pricing-models.md`

**Act Three — Apply (integrated decision)**

- **Chapter 12 — Financial Statement Analysis** — *The reader can take any public company's financial statements and produce a defensible analysis of financial health using ratio analysis, DuPont decomposition, and trend analysis with peer benchmarking.* — `12-financial-statement-analysis.md`
- **Chapter 13 — Putting It All Together: The Investment Decision (Capstone)** — *The reader integrates everything across Chapters 1–12 into a single defensible investment-decision artifact — a memo that integrates asset-level analysis, portfolio impact, capital allocation, valuation, and risk into one argument that survives professional scrutiny.* — `13-putting-it-all-together-the-investment-decision-capstone.md`

## Finalized

*None yet — all chapters are first drafts pending review.*

## Killed

*None yet.*

---

*The 13 Part 1 chapters map to a 14–15 week MBA semester (one chapter per week + one buffer). If course time forces cuts, the capstone (Ch 13) is the most consequential to preserve and the first that will get squeezed — worth checking actual page counts against semester math during drafting. Faculty adoption planning lives in `architecture-toc.md`, not here.*

*Drafted: 2026-04-27. Renamed to NN-kebab-case convention: 2026-04-27. All chapters in voice-unanchored state — `style/` empty at drafting. Voice calibration is the next step before second-pass editing.*

