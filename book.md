# Computational Finance with AI

*Per-book metadata. Read by `/chapter`, `/bookmap`, `/mega`, `/essay` every run.*

---

## One-sentence description

A working introduction to MBA-level computational finance taught with conversational AI as the primary instrument — present value, securities valuation, portfolio construction, asset pricing, financial-statement analysis — explicitly without Excel, on the argument that the spreadsheet was a workaround for the absence of better tools and the workaround is no longer needed.

## Subtitle (working)

*Hands-On Finance for MBAs in the Age of AI*

The current subtitle reads as 2024-vintage trend-chasing and undersells the thesis. Candidates worth testing before launch: *Without Excel*; *The First MBA Finance Course Built for the Conversation*; *Why the Spreadsheet Is Over*. Decision deferred — flagged in the launch plan, not the architecture.

## Relationship to other books in this workspace

Sibling, not replacement, of `intro-finance`. The two books share subject matter (TVM, equities, bonds, portfolios, CAPM) and diverge on substrate. `intro-finance` is undergraduate, Python-and-Excel literate, treats LLMs as tools. `computational-finance-with-ai` is MBA, conversation-first, treats LLMs as the substrate. A reader who finishes one does not need the other.

## Audience

**Primary reader (Maya):** 28-year-old second-year MBA student at a mid-tier program. Came in from non-finance work — consulting or operations. Excel-comfortable, ChatGPT-casual, non-programmer. Targeting corporate finance or fintech post-graduation. Reading this book concurrently with or after her MBA finance core courses.

**Reader floor:** any 26+ adult who can use a web app with guided prompts. Account creation and conversation interface are normal adult digital literacy. No programming, no calculus, no prior finance assumed beyond what an MBA core course supplies.

**Faculty adopters:** professors teaching a 14–15 week MBA Investments or Corporate Finance course who want an AI-native primary text or a four-chapter supplement (Ch 1, 3, 5, 12).

## Scope

**In:** the three-beat method (idea → execute → verify); returns and risk measurement; equity and fixed income valuation; funds and ETFs; time value of money and DCF; margin and short selling; options and derivatives; the diversification reframe; portfolio construction; capital allocation; asset pricing models (CAPM, multifactor); financial statement analysis; integrated investment decision-making (capstone). Plus two extended Claude Code examples and two extended Claude Cowork examples in Parts 2 and 3.

**Out:** international finance, behavioral finance, real options, private equity / venture capital / alternatives, cryptocurrency and digital assets, jurisdiction-specific tax-aware portfolio construction, Excel as substrate.

## Prerequisites

- Adult digital literacy — comfort creating an account, holding a sustained chat conversation, uploading a file
- One MBA-level finance core course either completed or in progress (or equivalent self-study)
- No programming, no calculus, no statistics beyond what a finance core supplies

## Voice notes (book-specific)

- **The three-beat method** (idea → execute → verify) is the spine of every chapter. Every default project moves through it. Every worked example shows the verify step explicitly. Verification is not an appendix; it lives in the body of the chapter.
- **First-person Maya, third-person book.** The protagonist is Maya. The narrator is the book. The book never says "I, Maya"; it says "Maya" or "you" when inviting the reader to step into her seat. Maya is the worked example, not the narrator.
- **Maya-fatigue mitigation.** The architecture currently opens every chapter with someone in Maya's life bringing her a question. By Chapter 5 this pattern is going to feel formulaic. At least three chapters in Part 1 should break frame — open with the data, with a historical episode, or with Maya alone in front of a screen at midnight. Drafting will flag chapters where the pattern is wearing thin and propose alternatives.
- **Tool stance: Claude-centric, cross-LLM verified.** Default worked examples use Claude. Every chapter through Part 1 includes at least one cross-LLM verification move (ChatGPT, Gemini) to teach the verification reflex and to keep the book usable for readers who land in a different ecosystem. Parts 2 and 3 escalate to Claude Code and Claude Cowork respectively.
- **Excel rejection — handle with care.** The thesis is the marketing hook. It is also the most fragile claim, and the chapter openers are where it leaks into preachiness. The argument is made fully in Chapter 1 and demonstrated thereafter; subsequent chapters do not re-litigate it. A chapter that catches itself arguing the thesis instead of doing the work has drifted out of voice.
- **Math on the page when the analysis is quantitative.** Calculations run visibly. A Sharpe ratio of 0.5 becomes the decision the number should lead the reader toward, not a number reported in passing.
- **Verification as professional discipline, not methodology for its own sake.** Verification is taught because real outputs go to real audiences — boss, client, professor, investor. The discipline is framed as what a competent professional does, not as an academic exercise.
- **Dollar amounts:** `$X` notation. Never spelled out.

## Chapter cadence

Linear three-act build.

- **Act One — Establish (Ch 1–7):** Maya learns to analyze any single financial asset.
- **Act Two — Build (Ch 8–11):** Maya makes the conceptual leap from single-asset to portfolio thinking and builds the technical capability to act on it.
- **Act Three — Apply (Ch 12–13):** Maya integrates everything into a defensible investment decision artifact.

A reader can dip into a later chapter, but Chapter 8 is the conceptual hinge — readers who skip it will struggle from Chapter 9 forward. A "Where this chapter fits" line at the top of each chapter makes the dependencies explicit.

## Running examples

- **The boss's NVDA decision** — opens Chapter 1, returns as the integrated capstone in Chapter 13. The pebble that becomes the pond.
- **Maya's father's 401(k)** — Chapter 4 (funds), revisited in Chapter 8 (the diversification reframe).
- **Sara's catering acquisition** — Chapter 5 (TVM/DCF). Standalone case.
- **Jin's IPO concentration** — Chapter 7 (options, protective put). Standalone case.
- **Maya's recruiting target** — Chapter 12 (financial statement analysis).

Primary sources: NVDA price history (Yahoo Finance / Nasdaq); Vanguard ETF documentation (vanguard.com); FRED for macro data; SEC EDGAR for 10-K filings. Specific source URLs locked at the chapter level, not here.

## Hero image direction

Schematic, instrument-focused. Clean diagrams of decision flow, calculation lineage, verification chains. Conversational interface mockups when the chapter teaches a prompting move. Avoid stock photos of trading floors, AI faces, or generic spreadsheet imagery. The book's visual language should match its argument: the work is conceptual, the substrate is conversation, the artifact is a defensible decision.

## Voice ground truth

*Empty as of initial scaffold.* The first chapter drafted in this book will be flagged `voice-unanchored`. Maya's voice and the book's narrator-voice are both calibrated in the first chapter — review with that in mind.

## Architecture status

Architecture locked through Phase 3 (chapter architecture) of the design process. The full canonical reference is `architecture-toc.md` in this folder. Items still open per that document: specific Part 2 / Part 3 example topics; production timeline; companion site infrastructure; instructor materials; launch plan. None of these affect chapter drafting.

---

*Initial version: 2026-04-27.*

