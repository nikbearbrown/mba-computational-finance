# Computational Finance with AI — Detailed Table of Contents

*Canonical architecture reference. Locked through Phase 3 (chapter architecture). Items still open after Phase 3 are listed in the document status section at the bottom.*

*This document is the source of record for chapter purpose, opening scenes, learning outcomes, default projects, primary verification techniques, and bridges between chapters. `outline.md` is a slimmer planning view derived from this. `book.md` is the per-book metadata read by skills.*

---

## About this document

This is the compiled detailed Table of Contents for *Computational Finance with AI*. It pulls together architecture decisions made across multiple design phases into a single document scannable by faculty considering adoption, contributors considering involvement, and the author considering the whole.

**Format:** Kindle ebook, $1, self-published, continuous updates.
**Target reader:** MBA students taking required or elective finance courses.
**Length:** 13 chapters in Part 1; 4 extended examples across Parts 2 and 3.
**Status:** Architecture locked; drafting not yet begun.

---

## Book metadata

**Title:** Computational Finance with AI
**Subtitle (working):** Hands-On Finance for MBAs in the Age of AI
**Thesis:** AI tools have made it possible, and necessary, to teach computational finance without Excel. The Excel-based tradition was a workaround for the absence of better tools, never a feature. This book teaches MBA-level finance the way it should be taught now that the workaround is no longer needed.

**Reader profile:** Maya — 28-year-old MBA student, second-year, mid-tier program. Came in from non-finance work (consulting, ops). Excel-comfortable, ChatGPT-casual, non-programmer. Targeting corporate finance or fintech post-graduation. Reading this book concurrently with or after her MBA finance core courses.

**Reader floor:** 26+ adult who can use a web app with guided prompts. Account creation and conversation interface are normal adult digital literacy.

**Tool stance:** Claude-centric (book teaches Claude as primary tool), with cross-LLM verification (ChatGPT, Gemini) woven through Part 1, and Claude Code + Claude Cowork as escalation tiers in Parts 2 and 3.

**Pedagogical model:** Three-beat method (idea → execute → verify), applied to a default project per chapter, with reader's own substrate as encouraged alternative.

**Verification stance:** Verification as professional discipline — taught because real outputs go to real audiences (boss, client, professor, investor). Not as methodology for its own sake.

---

## The three-act learning arc

The book moves Maya from "I have access to AI tools but don't know how to use them for real finance work" to "I can produce a defensible investment decision artifact" through three acts.

**Act One — Establish (Chapters 1–7).** Maya learns to analyze any single financial asset. By the end of Act One, she has a complete and reusable workflow for taking a candidate asset and producing defensible analysis on it.

**Act Two — Build (Chapters 8–11).** Maya learns to think in portfolios rather than single assets. The conceptual reframe in Chapter 8 shifts her mental model; Chapters 9–11 build the technical capability to act on the new thinking.

**Act Three — Apply (Chapters 12–13).** Maya integrates everything into a defensible investment decision. The capstone synthesizes the entire course into a single artifact she could hand to her boss.

---

## Part 1: Computational Finance with Claude — Prompting Foundations

The 13 chapters that constitute the MBA finance curriculum, taught with conversational AI as the primary tool.

### Chapter 1 — Introduction: The Three-Beat Method

*Act One — Establish | Onboarding chapter | 35–50 pages | Highest writing priority*

**Opening scene:** Maya's hypothetical boss forwards an email at 4 PM Friday: "Should we invest the company's $2M reserve in NVDA for the next 18 months? Need your analysis Monday morning." Maya has finance education from her MBA but has never produced this kind of analysis under real conditions. The chapter opens here.

**Chapter promise:** By the end of this chapter, you will have set up Claude on your machine, learned the three-beat method (idea, execute, verify) that powers every chapter in this book, and produced a working analysis of NVDA that your boss could actually read on Monday morning — with verification documentation that proves you didn't just trust the AI.

**Learning outcomes:**
1. Explain why AI-native computational finance replaces the Excel-based tradition.
2. Set up Claude and complete a working financial calculation using the three-beat method.
3. Apply at least three verification techniques to a single AI-generated financial output.
4. Evaluate when to trust an AI-generated answer and when to dig deeper.

**Section plan:**
- The Pebble (the boss's email scenario)
- Why Excel Was Wrong (the thesis section)
- What You're Going to Learn (book-level promise)
- Setup (Claude account, conversation interface, file upload, sustained dialogue)
- The Three-Beat Method (idea, execute, verify in detail)
- The Verification Toolkit (survey of 11 techniques)
- The First Worked Example (the NVDA analysis)
- Choosing Your Substrate
- What's Next

**Default project:** The boss's NVDA decision — a real investment question with real data.
**Primary verification technique:** Multiple — the chapter introduces the toolkit. The worked example uses cross-LLM comparison and bounds-checking explicitly.
**Bridge to Chapter 2:** Returns and risk give us the language to talk about assets. Chapter 2 takes us into measuring them precisely.

### Chapter 2 — Returns and Risk Measurement

*Act One — Establish | Standard chapter | 25–35 pages*

**Opening scene:** Maya's boss sends a follow-up question: "Before we commit to NVDA, I need to understand the risk profile. How volatile has it been? How does it compare to the broader market? Make this defensible — I'll be sharing it with the audit committee."

**Chapter promise:** By the end of this chapter, you'll be able to take any publicly traded asset and produce a defensible return-and-risk analysis on it — annualized return, volatility, Sharpe ratio — with cross-LLM verification that would survive committee scrutiny.

**Learning outcomes:**
1. Distinguish simple returns, log returns, arithmetic averages, geometric averages.
2. Calculate annualized returns, volatility, Sharpe ratio for any publicly traded asset.
3. Diagnose risk-return profile of a candidate investment.
4. Evaluate a published return claim and identify which assumptions could change the conclusion.

**Default project:** NVDA — calculate annualized return, volatility, Sharpe ratio over the past 3 years.
**Primary verification technique:** Cross-LLM comparison.
**Bridge to Chapter 3:** Returns and risk give us measurement language. But what *are* these assets, structurally? Chapter 3 takes us into stocks and bonds.

### Chapter 3 — Equity and Fixed Income

*Act One — Establish | Standard chapter | 25–35 pages*

**Opening scene:** Maya's CFO mentions in passing: "We're considering taking on debt to fund the NVDA position. We could issue an Apple-style bond ourselves — investors would buy it. Should we?" Maya needs to understand the tradeoff: equity ownership versus debt issuance.

**Chapter promise:** By the end of this chapter, you'll understand the structural difference between owning equity and holding debt, you'll be able to value both a stock (using DDM and simplified DCF) and a bond (using yield-to-maturity), and you'll catch internal inconsistencies in AI-generated valuations.

**Learning outcomes:**
1. Explain structural differences between common stock, preferred stock, corporate bonds.
2. Value a publicly traded stock using DDM and simplified DCF; price a corporate bond.
3. Analyze relationship between yield, price, risk for fixed income.
4. Evaluate whether an AI-generated valuation is internally consistent.

**Default project:** AAPL stock and an Apple corporate bond — value both, compare.
**Primary verification technique:** Independent recalculation.
**Bridge to Chapter 4:** Individual stocks and bonds are the building blocks. But most MBAs hold securities through pooled vehicles — funds and ETFs.

### Chapter 4 — Funds and ETFs

*Act One — Establish | Standard chapter | 25–35 pages*

**Opening scene:** Maya's father, retiring in 5 years, asks her at Thanksgiving: "I have $400K in a 401(k) that's all in the company stock. Friends say I should diversify. What do I do?" Maya has the technical tools but needs to translate them into a clear, actionable recommendation using accessible vehicles.

**Chapter promise:** By the end of this chapter, you'll be able to construct a defensible fund-based portfolio for a real-world investor profile, understand how expense ratios drag returns over decades, and choose between active and passive vehicles based on cost-adjusted reasoning rather than belief.

**Learning outcomes:**
1. Distinguish open-end mutual funds, closed-end funds, ETFs in structure, fees, tax efficiency.
2. Calculate NAV, expense ratio drag, tracking error.
3. Compare two funds covering similar markets and identify which is appropriate for a given profile.
4. Construct an ETF-based asset allocation appropriate for a stated goal.

**Default project:** 60/40 retirement portfolio using only Vanguard ETFs for a 60-year-old retiring in 5 years.
**Primary verification technique:** Provider data cross-check.
**Bridge to Chapter 5:** Funds and ETFs let us hold portfolios of assets. But we've been valuing securities and computing returns — the foundational lens is time value of money.

### Chapter 5 — Time Value of Money and Discounted Cash Flows

*Act One — Establish | Standard chapter | 25–35 pages*

**Opening scene:** Maya's friend Sara is considering buying her family's small business — a regional catering company her parents want to sell. The asking price is $850K. The business generated $180K in net cash flow last year. Sara asks Maya: "Is this a good deal?" Maya realizes the question doesn't have a quick answer.

**Chapter promise:** By the end of this chapter, you'll be able to take any cash flow stream — a business acquisition, a real estate decision, a retirement plan, a project at work — and produce a defensible NPV/IRR analysis with sensitivity testing.

**Learning outcomes:**
1. Explain TVM in any managerial decision context.
2. Calculate PV, FV, NPV, IRR for any cash flow stream.
3. Diagnose which of two investment opportunities is more valuable given different cash flow timing.
4. Build a personalized financial model that produces a defensible recommendation.

**Default project:** NPV/IRR on a small business acquisition (catering company, $850K asking price).
**Primary verification technique:** Bounds-checking.
**Bridge to Chapter 6:** TVM is the universal valuation tool. We've been working with simple positions in single assets. Chapter 6 brings us to leveraged positions.

### Chapter 6 — Margin and Short Selling

*Act One — Establish | Standard chapter | 25–35 pages*

**Opening scene:** Maya's brother, who works at a hedge fund, mentions over dinner that his fund is short TSLA. Maya, a few months into her finance education, realizes she doesn't actually understand how short selling makes money — or how it can lose money catastrophically.

**Chapter promise:** By the end of this chapter, you'll understand exactly how margin accounts and short selling work, you'll be able to calculate the risk profile of leveraged positions under multiple scenarios, and you'll be equipped to evaluate whether a leveraged strategy is appropriate for any given investor.

**Learning outcomes:**
1. Explain margin amplification and conditions that trigger margin calls; explain short selling mechanics.
2. Calculate margin requirements, margin call prices, short-selling P&L.
3. Analyze risk-reward of leveraged vs unleveraged position under multiple scenarios.
4. Evaluate whether a margin or short strategy is appropriate given investor risk tolerance and constraints.

**Default project:** Margin and short-selling scenarios on TSLA — model the leveraged P&L under five price scenarios.
**Primary verification technique:** Scenario stress-testing.
**Bridge to Chapter 7:** Margin and short give us linear leverage. Options give us asymmetric leverage — the most powerful tool for shaping risk.

### Chapter 7 — Options and Derivatives

*Act One — Establish | Standard chapter | 25–35 pages*

**Opening scene:** Maya's classmate Jin works at a tech company that just IPO'd. He has $800K in employee stock that vests over 4 years. Concentrated, exposed, and worried about a downturn. He asks Maya: "Is there a way to protect this without selling?" The answer is yes — protective puts.

**Chapter promise:** By the end of this chapter, you'll understand how options create asymmetric payoffs, you'll be able to price European options using both binomial and Black-Scholes methods, and you'll be able to design and recommend option strategies that match a stated market view and risk tolerance.

**Learning outcomes:**
1. Explain how options create asymmetric payoffs and why that's foundational to hedging and speculation.
2. Price a European option using both binomial and Black-Scholes methods, verified against published quotes.
3. Analyze option strategies (covered call, protective put, collar, spread) and identify which fits a stated profile.
4. Evaluate option Greeks output and judge whether the position aligns with intended exposure.

**Default project:** Protective put on a concentrated AAPL position for an investor with $500K exposure.
**Primary verification technique:** Replication against published market quotes.
**Bridge to Chapter 8:** We've been thinking in single assets — even option strategies are about a single underlying. Chapter 8 makes the conceptual leap that powers the rest of the book: from single-asset thinking to portfolio thinking.

### Chapter 8 — The Diversification Miracle

*Act Two — Build | Conceptual chapter | 25–35 pages | Second-highest writing priority*

**Opening scene:** Maya tells her father about Chapter 4's portfolio recommendation. He pushes back: "You're saying I should hold less of my company stock and more of these funds. But I know my company. The funds are full of stuff I don't know. That feels riskier, not safer." Maya realizes his intuition is wrong — but she also realizes she can't prove it's wrong without doing the math. The chapter exists to bridge intuition and math.

**Chapter promise:** By the end of this chapter, you'll understand why diversification works at a level that lets you defend it to a skeptic — using the math of correlation rather than the slogan. You'll have built two-asset and three-asset toy portfolios that demonstrate counterintuitive results, and you'll have made the conceptual leap from "is this asset good?" to "does this asset help my portfolio?"

**Learning outcomes:**
1. Explain why diversification reduces portfolio risk through the math of correlation.
2. Construct two-asset and three-asset toy portfolios showing how correlation changes portfolio volatility.
3. Analyze a real-world claim about diversification and identify whether it survives the math.
4. Reframe an investment question from "is this asset good?" to "does this asset help my portfolio?"

**Section plan (conceptual anatomy variant):**
- The Counterintuitive Opening
- The Reframe
- The Math, Demystified
- The Toy Portfolio Workshop
- Verifying Your Intuition
- The Generalization
- Apply It Yourself

**Default project:** Two-asset toy portfolios using TSLA + AAPL, then AAPL + JNJ. Three-asset portfolio with one negatively correlated asset.
**Primary verification technique:** Two-asset case verification.
**Bridge to Chapter 9:** With the conceptual reframe in hand, Chapter 9 builds the math of full portfolio construction.

### Chapter 9 — Portfolio Construction

*Act Two — Build | Standard chapter | 25–35 pages*

**Opening scene:** Maya is asked to advise a colleague's parent: 65 years old, $1.2M to invest, 20-year horizon, moderate risk tolerance, wants 5% real returns. Maya has the conceptual reframe from Chapter 8. Now she needs the math.

**Chapter promise:** By the end of this chapter, you'll be able to construct an efficient frontier for any chosen asset universe, identify the minimum-variance and maximum-Sharpe portfolios, and document a portfolio construction process — including rebalancing rules — appropriate for a stated investor profile.

**Learning outcomes:**
1. Explain the Markowitz framework in plain language.
2. Calculate expected portfolio return, variance, full correlation matrix for 5–10 assets.
3. Construct an efficient frontier and identify minimum-variance and maximum-Sharpe portfolios.
4. Build and document a portfolio construction process for a stated investor profile.

**Default project:** Build an efficient frontier for a 6-asset retirement portfolio for a 65-year-old with $1.2M and 20-year horizon.
**Primary verification technique:** Sanity-checking.
**Bridge to Chapter 10:** We've built portfolios of risky assets. But the optimal portfolio mix usually includes a risk-free asset.

### Chapter 10 — Capital Allocation and Diversification

*Act Two — Build | Standard chapter | 25–35 pages*

**Opening scene:** Maya is reviewing her own retirement situation. She has $80K saved, 30 years to retirement, moderate risk tolerance. She has built efficient frontiers for risky-asset portfolios. But she also has cash and Treasury bills as options. The optimal mix of risky and risk-free assets — that's the missing piece.

**Chapter promise:** By the end of this chapter, you'll be able to solve for the optimal mix of risky and risk-free assets for any stated risk aversion, you'll understand how real-world constraints reshape the efficient frontier, and you'll be able to evaluate whether an investment manager is adding value relative to their fees.

**Learning outcomes:**
1. Explain the role of the risk-free asset and the Capital Allocation Line.
2. Solve for optimal mix of risky and risk-free given stated risk aversion.
3. Analyze how real-world constraints (no shorting, sector limits, ESG screens, liquidity) affect the efficient frontier.
4. Evaluate an investment manager against the efficient frontier and judge value added relative to fees.

**Default project:** Optimal mix of risky portfolio + Treasury bills for stated risk aversion (Maya's own retirement, or a hypothetical 35-year-old).
**Primary verification technique:** Constraint-imposed comparison.
**Bridge to Chapter 11:** We've built portfolios and allocated capital. But how do we know whether any given asset is fairly priced for its role in the portfolio?

### Chapter 11 — Asset Pricing Models

*Act Two — Build | Standard chapter | 25–35 pages*

**Opening scene:** Maya is asked: "NVDA returned 240% last year. The S&P returned 24%. Is that just luck, or is NVDA exceptional?" Her instinct says "exceptional," but she realizes she doesn't actually know how to answer the question rigorously. CAPM gives her the framework.

**Chapter promise:** By the end of this chapter, you'll be able to estimate beta for any publicly traded stock with a calculated confidence interval, diagnose why a stock's CAPM-predicted return differs from its actual return, and evaluate when CAPM is appropriate versus when a multifactor model is needed.

**Learning outcomes:**
1. Explain CAPM and beta in plain language; explain the model's limitations honestly.
2. Estimate beta via historical regression with confidence interval calculated and reported.
3. Diagnose why CAPM-predicted returns differ from actual returns; identify which factors might explain the gap.
4. Evaluate appropriateness of CAPM vs multifactor model for a specific valuation context.

**Default project:** Estimate beta for NVDA over multiple time windows. Diagnose the gap between CAPM-predicted and actual returns.
**Primary verification technique:** Confidence interval analysis.
**Bridge to Chapter 12:** We've been working with market data on assets. But what about the underlying companies — their financial health, their fundamentals?

### Chapter 12 — Financial Statement Analysis

*Act Three — Apply | Standard chapter | 25–35 pages*

**Opening scene:** Maya's recruiting target — a mid-stage growth tech company — sends her their financial statements before her on-site interview. She has 48 hours to evaluate the company. CAPM and portfolio analysis don't help her here; what she needs is to read a 10-K and produce a defensible view of the company's financial health.

**Chapter promise:** By the end of this chapter, you'll be able to take any public company's financial statements and produce a defensible analysis of its financial health using ratio analysis, DuPont decomposition, and trend analysis — with peer benchmarking that puts the numbers in context.

**Learning outcomes:**
1. Explain how the three financial statements connect; identify red flags in each.
2. Calculate and interpret key ratios (liquidity, profitability, leverage, efficiency) using real 10-K data.
3. Diagnose financial health using DuPont and trend analysis.
4. Evaluate a company against industry peers and identify red flags or signals of strength.

**Default project:** Financial statement analysis comparing MSFT, AAPL, GOOGL using 5-year ratio trends and DuPont decomposition.
**Primary verification technique:** Peer comparison.
**Bridge to Chapter 13:** We have all the tools — return analysis, valuation, portfolio thinking, asset pricing, financial statements. Chapter 13 puts it all together.

### Chapter 13 — Putting It All Together: The Investment Decision (Capstone)

*Act Three — Apply | Synthesis chapter | 35–50 pages | Third-highest writing priority*

**Opening scene:** Maya's hypothetical boss is back. Not with a single asset question this time. With the full thing: "We have a 60/40 portfolio of $5M for the company's reserve fund. Treasury yields are dropping; equity volatility is rising. NVDA looks expensive but transformative. Should we add it to the reserve fund? If yes, how much, and what should we sell? Memo by next Friday."

The pebble from Chapter 1 has grown into the pond. Now Maya integrates everything she's learned across 12 chapters into a defensible investment decision.

**Chapter promise:** By the end of this chapter, you will have produced a defensible investment decision artifact — a complete memo that integrates asset-level analysis, portfolio impact, capital allocation, valuation, risk assessment, and a clear recommendation. The artifact will survive professional scrutiny. The verification chain across the integrated decision will be documented. You will have done this on the default project, and you will have done it on your own substrate. You will have completed the book's promise.

**Learning outcomes:**
1. Explain how Chapters 1–12 tools integrate into a coherent investment decision process.
2. Analyze a real investment opportunity by integrating asset-level, portfolio, capital allocation, valuation, risk into a single argument.
3. Evaluate the verification chain across an integrated decision; identify which assumptions are most consequential.
4. Produce a defensible investment decision artifact.

**Section plan (synthesis anatomy variant):**
- The Investment Decision (the boss's full prompt)
- The Architecture of an Investment Decision
- The Worked Decision (stage-by-stage walkthrough)
- The Verification Chain (the unique synthesis content)
- Producing the Artifact
- Apply It Yourself

**Default project:** Full integrated decision — should we add NVDA to an existing 60/40 portfolio? If yes, how much, and what should we sell?
**Primary verification technique:** The verification chain — multi-stage discipline integrating all techniques from Chapters 2–12.
**Bridge to Part 2:** The book promised computational finance with AI; you've now done it. Part 2 introduces what becomes possible when conversational prompting isn't enough.

---

## Part 2: Beyond Prompting — Working with Claude Code

Two extended examples showing how Claude Code adds capability over conversational prompting: reproducibility, file artifacts, real data pipelines, scale.

**Format:** Each extended example is a sustained 40–60 page worked case. Not new finance content — same concepts, more powerful tooling.

**Specific topics for the two examples: TBD** (logged in Phase 2 as O-002).

Likely candidates:
- A portfolio analyzer with live data pipeline
- A DCF automation across multiple companies
- A financial statement parser at scale
- A reproducible Monte Carlo simulation

**Coupling to Mycroft:** Loose. Where Mycroft has a useful component (likely Research Agent, Verification Agent, Diversification Agent simplified for teaching), it's used. Where Mycroft doesn't fit cleanly, fresh examples are written.

---

## Part 3: Beyond Files — Workflow Orchestration with Claude Cowork

Two extended examples showing how Claude Cowork orchestrates multi-step workflows: integration across sources, automated reporting, professional-grade pipelines.

**Format:** Each extended example is a sustained 40–60 page worked case demonstrating multi-stage automation.

**Specific topics for the two examples: TBD** (logged in Phase 2 as O-003).

Likely candidates:
- A quarterly investment review pipeline (multi-source data → analysis → report)
- A risk dashboard for a multi-asset portfolio
- An NLP-based earnings call sentiment analysis pipeline
- An automated competitive analysis from financial filings

**Coupling to Mycroft:** Tight in this part. Mycroft's full workflow orchestration is the natural model for what Part 3 demonstrates — likely the most direct use of Mycroft components in the book.

---

## Out of Scope (acknowledged in the preface)

Topics the book deliberately excludes:

- **International finance** — covered in MBA international finance modules; could expand Part 1 well beyond course-adoptable length.
- **Behavioral finance** — its own field with its own pedagogy; brief treatment would caricature it.
- **Real options** — useful but rarely taught well; better to acknowledge the gap than do it badly.
- **Private equity, venture capital, alternatives** — natural fit for the planned advanced second book.
- **Cryptocurrency and digital assets** — too new and unstable for textbook treatment; the verification methods generalize but specific coverage is excluded.
- **Detailed tax-aware portfolio construction** — jurisdiction-specific; changes too frequently.
- **Excel** — actively rejected as substrate per the book's thesis.

---

## Top adoption risks

For faculty considering recommendation:

1. **The Excel-rejection thesis offends Excel-committed adopters** — mitigated by reasoned (not polemical) presentation; the book never disparages individual faculty.
2. **Tool-specific content ages** — mitigated by Kindle's continuous-update format and concentration of tool-specific content in revisable sections.
3. **Mainstream publishers' competing AI editions land first** — mitigated by speed-to-market; the more provocative thesis is differentiation.
4. **OpenStax launches an AI-finance text** — currently no signal this is happening; would be most serious competitor if it does.
5. **AI tools change capabilities mid-edition** — mitigated by methodology-over-features framing and continuous-update model.

---

## What each reader path yields

**Required-core MBA student reads Part 1 and stops:** Has a complete MBA finance education in AI-native form. Can produce defensible investment decisions on real opportunities. Has the verification discipline as professional reflex.

**Finance-focused MBA student reads everything:** Same as above, plus exposure to Claude Code workflows for reproducible analysis, plus exposure to Claude Cowork orchestration for multi-stage automated pipelines. Prepared for AI-fluent finance roles.

**Faculty member adopts Part 1 as Investments course primary text:** Has a 13-chapter sequence mapped to a 14–15 week semester, with default projects, verification rotation, exercises, discussion questions, and assessments. Faculty reading guide and instructor materials available separately on companion site.

**Faculty member assigns Ch 1, 3, 5, 12 as Corporate Finance supplementary:** Has four high-quality AI-native chapters covering method introduction, securities valuation, TVM/DCF, and financial statement analysis — at $1 per student.

**Self-directed reader picks up the book for $1:** Gets a structured AI-native finance education they can complete on their own schedule, with continuous updates pushed to their Kindle as the book improves.

---

## Document status

This TOC reflects architecture locked through Phase 3 of the design process (chapter architecture). Phase 4 (scope and market positioning) and Phase 5 (production and proposal) are partially complete.

**Items still open:**
- Specific topics for Part 2 and Part 3 extended examples
- Production timeline and launch date
- Companion site infrastructure and instructor materials specifics
- /m2 features list with priority tagging
- /m3 formal out-of-scope section
- /m4 risk register with mitigation
- /p1 launch plan (replacing the traditional publisher proposal)
- /p3 contributor coordination

These do not affect the book's content architecture, which is locked.

---

*Initial version: 2026-04-27. Source of record for chapter architecture. Revisions logged in workspace `CHANGELOG.md`.*

