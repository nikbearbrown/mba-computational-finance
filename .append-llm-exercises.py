#!/usr/bin/env python3
"""Insert LLM Exercise blocks at the bottom of each of the 13 content chapters
of computational-finance-with-ai. The Wayback Machine block already sits at EOF;
the LLM Exercise must precede it (LLM Exercise → Wayback, not the reverse).
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# Each entry: (filename, chapter_n, chapter_title, what_youre_building, tool, prompt, produces, how_code, how_project, connection, preview)
EXERCISES = [
    (
        "01-introduction-the-three-beat-method.md", "1", "The Three-Beat Method",
        "The position you will analyze across the next twelve chapters, plus a one-paragraph brief and an explicit three-beat plan for the work ahead.",
        "Claude Project",
        """I'm starting a project that will run across the next twelve chapters of *Computational Finance with AI* by Nik Bear Brown. The book teaches the **three-beat method** — *idea, execute, verify* — as the discipline for producing analytical work with an AI tool that does not collapse into plausible-but-wrong output.

Across the chapters I am going to build one complete investment memo on a single real position. Help me set up Chapter 1's deliverable. Paste the position below; if I haven't yet, ask.

Produce four things, in order:

1. **The position, named precisely.** One paragraph. The actor (me / a hypothetical fund / Sara's small business buyer / etc.); the instrument (specific ticker, specific fund, specific bond, specific small business); the action under consideration (buy / size up / hedge / refuse); the time horizon; the constraint (capital available, mandate, personal liquidity).

2. **The three-beat plan.** Three sentences:
   - **Idea**: what is the question this memo has to answer?
   - **Execute**: what analytical tools will I bring to bear (preview the chapters that will produce them)?
   - **Verify**: what would a hostile reader ask, and what would I want in writing to defend the recommendation?

3. **The five layers.** The capstone (Ch 13) integrates five layers: return measurement, valuation, portfolio fit, capital allocation, financial-statement quality. For my specific position, write one sentence per layer naming what *this* layer must answer.

4. **The "what would change my mind" sentence.** One sentence. The specific evidence that would move my recommendation from buy to hold, or hold to sell. This is the verify-step's anchor.

Format the output as a markdown document I can save as `01-position-brief.md`. Be honest about uncertainty in the time horizon and the constraint — pick numbers I'd defend in a meeting, not numbers that sound impressive.""",
        "A markdown document `01-position-brief.md` containing the precise position, the three-beat plan, the five-layer outline, and the what-would-change-my-mind sentence. This document is the seed for every subsequent chapter's exercise.",
        "Not the right tool yet. Save this as plain markdown.",
        "Create a Claude Project named *Maya's Memo — [position ticker / name]*. Put the three-beat method definition in the system prompt plus the rule: *every output is a section that fits into a final 6–10 page memo*. Each subsequent chapter's exercise becomes a new conversation in this project.",
        "First chapter — no prior exercise to build on. The position chosen here governs every subsequent exercise; pick something real you actually want a defensible answer on.",
        "Chapter 2 takes your position and produces the *return and risk profile* section of the memo — arithmetic vs. geometric returns, volatility, and the Sharpe ratio with the period and frequency stated.",
    ),

    (
        "02-returns-and-risk-measurement.md", "2", "Returns and Risk Measurement",
        "The Return-and-Risk-Profile section of the memo: arithmetic and geometric returns, volatility, and a Sharpe ratio reported with the period and frequency stated.",
        "Claude Project",
        """I'm working on Maya's Memo for the position named in `01-position-brief.md` (paste the position if not in the project context).

Chapter 2 introduced:
- **Arithmetic vs. geometric (CAGR) returns** — and the magic-trick result that 50% up then 50% down is not 0%
- **Volatility** as standard deviation of returns
- **The Sharpe ratio** as $(\\text{return} - \\text{risk-free rate}) / \\text{volatility}$, *always* with the period and frequency stated

Produce `02-return-risk.md`, the second section of the memo, containing:

1. **The lookback window.** State the window you'll use to characterize returns and why (e.g., "10-year monthly returns, Jan 2015 – Dec 2024, capturing one full cycle plus the 2020 dislocation"). Defend the choice in two sentences against two alternative windows.

2. **Arithmetic and geometric returns.** Compute both for the position over your window. State the gap between them and what it tells you about volatility. *If the position is a private business or a bond, adapt: arithmetic = average annual cash yield, geometric = CAGR of intrinsic value.*

3. **Volatility.** Report the standard deviation of monthly returns, annualized by $\\sqrt{12}$. Compare to the S&P 500 (or to the relevant benchmark for fixed income / private business — say which you used and why).

4. **The Sharpe ratio.** Compute it. State the period (annualized), the frequency the inputs were sampled at (monthly), and the risk-free rate you used (3-month T-bill, dated). State the convention you used for the excess-return calculation (subtracting the matching-period T-bill).

5. **What the numbers say about the position.** Two paragraphs. Not the numbers — what they *mean* for the recommendation. A high Sharpe ratio relative to the benchmark is one signal; a high Sharpe with low volatility is a different signal from a high Sharpe with high volatility paired with a high return.

Save as a section that will eventually go in the full memo. Be specific about the period and frequency throughout — *that* is the discipline this chapter teaches.""",
        "A markdown document `02-return-risk.md` containing the lookback window, arithmetic and geometric returns, volatility, a fully-annotated Sharpe ratio, and a two-paragraph reading of what the numbers say.",
        "Optional — if you want the computations as a runnable script, ask Claude Code to scaffold `analysis/02-return-risk.py` that pulls the data via `yfinance` (for public equities) and produces the Sharpe ratio with the conventions stated.",
        "Append to the project. The Sharpe ratio computed here becomes the headline number that Chapter 9's portfolio analysis and Chapter 10's allocation decision will consume.",
        "Chapter 1 set up the position; Chapter 2 produces its empirical return-and-risk profile.",
        "Chapter 3 produces the *equity-vs-debt framing* section: how does your position's claim structure (equity, debt, hybrid) shape the analysis?",
    ),

    (
        "03-equity-and-fixed-income.md", "3", "Equity and Fixed Income",
        "The Equity-vs-Debt Framing section of the memo: what kind of claim is this position, and how does that claim structure shape the rest of the analysis?",
        "Claude Project",
        """I'm working on Maya's Memo for the position in `01-position-brief.md`. The Chapter 2 return profile is in `02-return-risk.md`.

Chapter 3 distinguished:
- **Equity claim** — residual after all obligations; uncapped upside, full downside, voting / discretion over distributions
- **Debt claim** — fixed contractual cash flows; capped upside (par + coupon), prior claim in liquidation, priced from coupon, par, YTM, and maturity
- **Three different bond yields**: coupon rate, current yield, yield-to-maturity — and why they are not the same number

Produce `03-claim-framing.md` containing:

1. **What kind of claim is this?** Equity / debt / hybrid (preferred, convertible, mezzanine, MLP)? One paragraph naming the claim and listing the specific obligations and rights it carries (dividend, voting, conversion, seniority, callability).

2. **The bond / debt analysis (skip if pure equity).** If the position is debt or has a debt component: compute coupon rate, current yield, YTM. If you only have one of the three, work back to the others. State which yield is the right number for your decision and why. *For private business: substitute the implied yield on the seller-financing terms or the leveraged-buyout debt.*

3. **The equity analysis (skip if pure debt).** If the position is equity: name the equity story in two sentences. The story has a who-pays (operating cash) and a who-receives (residual after every other claim). What conditions would have to break for the residual to disappear? *For private business: identify the dominant operating-cash driver and the obligations senior to the equity holder.*

4. **The substitution test.** If your position is equity, name the bond a rational investor in the *same* company would prefer if the equity story breaks (the company's senior bonds, if any). If your position is debt, name the equity case a rational investor would prefer if the debt story is too cautious. The substitution test is what disciplines the framing.

5. **Implications for the rest of the memo.** Two sentences. Equity vs. debt structurally changes Chapter 6's leverage decision and Chapter 7's option overlay; name how.""",
        "A markdown document `03-claim-framing.md` containing the claim type, the relevant yield calculation (or equity story), the substitution test, and the implications for downstream chapters.",
        "Not needed for this section.",
        "Append to the project. The claim type drives several downstream decisions — surface it in the project's running notes so each subsequent chapter inherits the framing.",
        "Chapter 2 measured the position's empirical risk and return; Chapter 3 names the claim structure that produces that profile.",
        "Chapter 4 produces the *fund-vs-direct decision* section: would an ETF or fund dominate the case for direct ownership of this specific position?",
    ),

    (
        "04-funds-and-etfs.md", "4", "Funds and ETFs",
        "The Fund-vs-Direct decision section of the memo: would an ETF or fund dominate direct ownership of this position, and on what evidence?",
        "Claude Project",
        """I'm working on Maya's Memo for the position in `01-position-brief.md`. The framing so far: `02-return-risk.md`, `03-claim-framing.md`.

Chapter 4 introduced:
- **The law-of-large-numbers argument**: a 100-coin bet at +60% / -40% has the same expected value as a 1-coin bet, with massively lower variance
- **Mutual funds vs. ETFs**: NAV pricing, expense ratios, tracking error, in-kind creation
- **The indexing case**: why most active managers underperform their benchmark net of fees over a decade

Produce `04-fund-vs-direct.md` containing:

1. **Name the closest fund / ETF.** What is the fund or ETF that owns either *this exact position* or a basket of close substitutes? (For NVDA: SMH semiconductor ETF, QQQ, VOO. For a corporate bond: a credit ETF like LQD or a maturity-matched bond fund. For a small private business: not applicable — say so and skip the rest.) Name the fund, its expense ratio, and the position's weight in it.

2. **The single-position vs. fund comparison.** A two-column table: rows = expected return, volatility, Sharpe, idiosyncratic risk exposure, fees, liquidity. Columns = direct position vs. closest fund. Be honest about what you *can* know and what you can't.

3. **The argument for direct.** Two sentences. What about *this* position justifies single-name exposure when a fund containing it is available? Either you have a thesis the fund-weight does not reflect, or you accept that the variance reduction is worth the expected-return concentration.

4. **The argument for the fund.** Two sentences. The default case. Lower variance at the same expected return; the law-of-large-numbers bet from the chapter.

5. **The recommendation.** One sentence. Which one and why — and what specific evidence would flip the recommendation.""",
        "A markdown document `04-fund-vs-direct.md` containing the closest fund, the comparison table, the arguments on both sides, and a recommendation with the flipping condition named.",
        "Not needed.",
        "Append to the project. The fund-vs-direct call interacts with Chapter 8's diversification analysis and Chapter 10's allocation decision — flag the linkage.",
        "Chapter 3 framed the claim type; Chapter 4 asks whether direct ownership of that claim type is dominated by a fund version.",
        "Chapter 5 produces the *DCF section* of the memo — the present-value valuation that the recommendation must defend.",
    ),

    (
        "05-time-value-of-money-and-discounted-cash-flows.md", "5", "Time Value and DCF",
        "The DCF Valuation section of the memo: a present-value model of the position, with the discount rate defended and a clean sensitivity table.",
        "Claude Project",
        """I'm working on Maya's Memo for the position in `01-position-brief.md`. Sections so far: `02-return-risk.md`, `03-claim-framing.md`, `04-fund-vs-direct.md`.

Chapter 5 taught:
- **Present value** as the discounted sum of future cash flows
- **Discount rate** selection and why it matters more than any other assumption
- **Terminal value** via Gordon growth and why it usually dominates the answer
- **Payback-period intuition** (Sara's catering case) and why it systematically over-pays

Produce `05-dcf.md` containing:

1. **The cash-flow forecast.** A 5–10 year projection of the cash flow that accrues to your position. For an equity: free cash flow to equity (or dividends, if a stable payer). For a bond: the contractual coupon and principal stream. For a private business: forecast operating cash flow with explicit assumptions about growth, margin, and reinvestment. Show the full table.

2. **The discount rate, defended.** State the rate you're using and why. For a public equity: the cost of equity from CAPM (β × market risk premium + r_f) — even though Chapter 11 will refine β, do a rough cut now. For a bond: the YTM on a comparable-credit instrument. For a private business: the hurdle rate the buyer would accept, defended against alternative uses of the capital.

3. **The present value.** Compute the PV of the explicit forecast. Compute the terminal value (Gordon growth: $TV = CF_n \\times (1+g) / (r - g)$, with $g$ defended). Discount the terminal value back. Sum to get the total present value.

4. **The sensitivity table.** A 5×5 table: discount rate on one axis (5 values around your central estimate), terminal growth on the other (5 values). Each cell is the resulting PV. *This is the most important table in the memo* — most disagreements about a DCF are disagreements about the corner values, not the math.

5. **Compare PV to current price.** State the implied margin of safety (or shortfall). One sentence: at this PV, the position is *attractive / fairly valued / expensive*. Name the corner of the sensitivity table that flips your recommendation.""",
        "A markdown document `05-dcf.md` containing the cash-flow forecast, the discount-rate defense, the PV computation, the 5×5 sensitivity table, and the recommendation framing relative to the current price.",
        "Optional but useful — ask Claude Code to scaffold `analysis/05-dcf.py` so the sensitivity table re-runs with one command when you update assumptions.",
        "Append to the project. The DCF's central PV and the sensitivity-table corners become the *valuation* layer the capstone integrates.",
        "Chapters 2–4 measured the position empirically and structurally; Chapter 5 produces the first defensible price for it.",
        "Chapter 6 asks whether a leveraged version of this position dominates the unleveraged one — and at what cost.",
    ),

    (
        "06-margin-and-short-selling.md", "6", "Margin and Short Selling",
        "The Leverage Decision section of the memo: should this position be levered, and what does the margin-call price say about the size that survives a 30% drawdown?",
        "Claude Project",
        """I'm working on Maya's Memo. Sections so far: `02-return-risk.md`, `03-claim-framing.md`, `04-fund-vs-direct.md`, `05-dcf.md`.

Chapter 6 taught the four margin numbers:
- **Position value** = cash + broker's loan
- **Equity** = position value − loan
- **Margin %** = equity / position value
- **Margin-call price** = loan / (shares × (1 − maintenance margin))

And the discipline: leverage amplifies both directions; the difference between useful and ruinous is whether you understood the mechanism before you used it.

Produce `06-leverage.md` containing:

1. **The unleveraged base case.** State the position size you would take with no margin. Reference Chapter 5's DCF and Chapter 4's fund-vs-direct call to defend the size.

2. **The leveraged variant.** Compute, at a chosen leverage ratio (1.5×, 2×, or 3×): position value, equity, margin %, margin-call price, the stock-price drawdown that triggers the margin call. *For a private business: substitute "the LBO debt covenant breach price" or the lender's call provision.*

3. **The 30% adverse-move test.** Suppose the position drops 30% from entry. For each candidate leverage ratio (1.5×, 2×, 3×), state whether the margin call fires. Report the size you can take at each leverage and survive the 30% move with margin to spare.

4. **The expected return on equity at each leverage.** Multiply the unleveraged expected return by the leverage ratio, subtract the broker's interest (state the rate). Compare the levered expected return to the unleveraged.

5. **The recommendation.** One paragraph. Lever / don't lever, at what ratio, with what stop-loss, against what specific risk. Reference the worked-out margin-call price as the binding constraint. The case against leverage is the LTCM/Archegos/GameStop sentence — name which scenario most closely resembles the failure mode this position is exposed to.""",
        "A markdown document `06-leverage.md` containing the leverage decision, the four margin numbers at each candidate ratio, the 30% drawdown test, and a recommendation that names the binding constraint.",
        "Optional — Claude Code can scaffold `analysis/06-margin.py` that takes leverage, maintenance margin, and entry price and returns the margin-call price and the survivable drawdown.",
        "Append to the project. The leverage decision interacts with the diversification analysis (Ch 8) and the y* recommendation (Ch 10) — flag the linkage.",
        "Chapter 5's DCF produced the price; Chapter 6 asks whether a leveraged version of the same position dominates the unleveraged one and at what risk.",
        "Chapter 7 asks whether an option overlay (a put hedge, a call substitute, a covered-call income trade) dominates the linear leverage move.",
    ),

    (
        "07-options-and-derivatives.md", "7", "Options and Derivatives",
        "The Option Overlay section of the memo: would an option-based position dominate the linear long or levered long, and what does the kinked payoff buy you?",
        "Claude Project",
        """I'm working on Maya's Memo. Sections so far through Chapter 6 are in the project.

Chapter 7 taught:
- **The kinked payoff** — calls and puts as asymmetric claims
- **Intrinsic vs. time value**
- **The price barely depends on your forecast** — it depends on volatility, time to expiration, and rates
- **The Greeks** as the partial-derivative summary of how the option price changes

Produce `07-option-overlay.md` containing:

1. **Three candidate option overlays for this position.** Pick the three most defensible:
   - **Protective put**: long the stock, long an at-the-money put — capped downside, full upside, paid for in time premium
   - **Covered call**: long the stock, short an out-of-the-money call — collect premium, capped upside, full downside
   - **Long call as substitute**: long an at-the-money call instead of the stock — capped downside (the premium), uncapped upside, leveraged exposure to the stock's move

   For each, draw (in ASCII or markdown table) the payoff diagram at expiration.

2. **Pricing each.** For a public equity, look up the actual option chain. State the strike, the expiration, the bid-ask, the implied volatility. For a private business or a bond, simulate plausible parameters and label them as such.

3. **The expected-value comparison.** For each overlay vs. the linear long (Ch 6's unleveraged base case), compute the expected payoff under three scenarios: a base case, a 30% drawdown, a 30% rally. State which overlay dominates in which scenario.

4. **Volatility's role.** One paragraph. Why does the option price depend much more on volatility than on your forecast? What does this say about *when* an overlay is cheap vs. expensive — independent of your view on direction?

5. **The recommendation.** One paragraph. Which overlay (if any) belongs in the memo, against which scenario, with which expiration. The case for *no overlay* is also a defensible answer — name the volatility regime in which it is right.""",
        "A markdown document `07-option-overlay.md` containing payoff diagrams for three candidate overlays, pricing for each, an expected-value comparison, and a recommendation that names the volatility regime supporting it.",
        "Optional — Claude Code can scaffold `analysis/07-option-pricing.py` using `py_vollib` for Black-Scholes pricing and the Greeks.",
        "Append to the project. The option-overlay decision is independent of the leverage decision (Ch 6) but combines with it in the integrated capstone (Ch 13).",
        "Chapter 6 examined linear leverage; Chapter 7 examines whether the kinked payoff of an option dominates the linear case.",
        "Chapter 8 zooms out from the single position to the *diversification analysis* — how much of the risk in this position is idiosyncratic and how much is systematic?",
    ),

    (
        "08-the-diversification-miracle.md", "8", "The Diversification Miracle",
        "The Diversification Analysis section of the memo: how much of this position's variance is idiosyncratic and how much is systematic, and what does the covariance with the rest of your portfolio say?",
        "Claude Code",
        """I'm working on Maya's Memo for the position in `01-position-brief.md`. The single-position analysis is in `02-return-risk.md` through `07-option-overlay.md`.

Chapter 8 taught:
- **Variance of the average is less than the average of the variances** — and *correlation*, not just count, drives the gap
- **Idiosyncratic vs. systematic risk** — only the systematic part survives diversification
- **The Buffett objection** ("diversification is for people who don't know what they're doing") and why it is wrong about the specific question of *combining risks*

I want the math, not just the prose. Scaffold `analysis/08-diversification.py`:

1. **Load returns.** Pull monthly returns for the position and for 5–10 candidate portfolio peers (S&P sectors, factor ETFs, or a benchmark + 4 named diversifiers). Use `yfinance` for public, or a CSV for private.

2. **Compute the covariance matrix.** Annualized.

3. **Decompose the position's variance.** Run the position's returns against the market (R^2 from a univariate regression on SPY). Report:
   - Total variance
   - Systematic variance (R^2 × total)
   - Idiosyncratic variance (the residual)

4. **The Buffett-vs-LLN comparison.** Compute the variance of *just* the position vs. the variance of an equal-weight portfolio of the position plus its top-3 lowest-correlation peers. Report the variance reduction.

5. **Save `analysis/08-diversification.md`** with the numbers, the decomposition, and one paragraph: how does the idiosyncratic-vs-systematic split change my view on the position size? A high-idiosyncratic-variance position belongs at a smaller weight unless you have a specific edge; a high-systematic-variance position belongs at a smaller absolute weight in any case but for a different reason.

The script should run with `python analysis/08-diversification.py --ticker [TICKER] --benchmark SPY --peers [TICKER1,TICKER2,...]`.""",
        "A runnable script `analysis/08-diversification.py` plus the results file `analysis/08-diversification.md` containing the variance decomposition, the LLN comparison, and a one-paragraph reading of what the split implies for position size.",
        "This is the right tool — pulling data, computing the covariance matrix, running the regression, and saving the results is exactly the kind of multi-step computational work Claude Code is built for.",
        "Save the artifacts in the project. The systematic / idiosyncratic split feeds directly into Chapter 9's portfolio construction and Chapter 11's CAPM read.",
        "Chapters 2–7 analyzed the position alone; Chapter 8 begins the analysis of the position *as part of a portfolio*.",
        "Chapter 9 takes the covariance matrix and constructs the efficient frontier — and asks where the position sits on it.",
    ),

    (
        "09-portfolio-construction.md", "9", "Portfolio Construction",
        "The Portfolio Fit section of the memo: where does your position sit relative to the efficient frontier built from your candidate universe?",
        "Claude Code",
        """I'm working on Maya's Memo. The single-position analysis (Chs 2–7) and the diversification decomposition (Ch 8) are in the project.

Chapter 9 taught:
- **Markowitz's mean-variance frontier**
- **The tangency portfolio** that maximizes Sharpe
- **What the optimizer cannot see**: regime change, fat tails, parameter uncertainty
- The case for *and* against running the optimizer on real data

Scaffold `analysis/09-frontier.py`:

1. **Load returns and the covariance matrix.** Use the same universe as Chapter 8 (the position + 5–10 candidate peers + benchmark).

2. **Build the efficient frontier.** Compute the minimum-variance portfolio at each of 50 target expected returns. Plot the frontier. Mark:
   - The minimum-variance portfolio
   - The tangency portfolio (max Sharpe)
   - 100% in your position alone
   - The benchmark (SPY)

3. **Where is your position?** Is it on the frontier? Inside the frontier? Outside? Report its distance from the frontier in Sharpe-ratio terms.

4. **What weight does the optimizer give it?** Report the optimizer's weight on your position in the tangency portfolio. State the most likely reason if it's much higher or lower than your own intuition (the optimizer doesn't see what you see, or vice versa).

5. **The three failure modes.** For your specific universe, name the most plausible failure mode the optimizer cannot see:
   - **Regime change**: covariance matrix from the lookback window may not hold
   - **Fat tails**: the historical worst case underestimates the future worst case
   - **Parameter uncertainty**: small changes in expected returns produce wildly different optimal weights

6. **Save `analysis/09-frontier.md`** with the frontier plot, the optimizer's tangency weights, the position's location relative to the frontier, and a paragraph naming the failure mode that most threatens the result.

The script should run with `python analysis/09-frontier.py --ticker [TICKER] --peers [TICKER1,...]`.""",
        "A runnable script `analysis/09-frontier.py` plus `analysis/09-frontier.md` containing the efficient frontier plot, the optimizer's tangency weights, the position's location, and the failure-mode paragraph.",
        "Right tool — this is real numerical optimization. Claude Code can use `cvxpy` or `scipy.optimize` to build the frontier in 30–50 lines.",
        "Append to the project. The tangency portfolio's weight on your position becomes the input to Chapter 10's y* recommendation and Chapter 13's capstone.",
        "Chapter 8 decomposed the position's variance; Chapter 9 builds the universe-level frontier and locates the position on it.",
        "Chapter 10 takes the tangency portfolio and asks: how much of your wealth should sit in it?",
    ),

    (
        "10-capital-allocation-and-diversification.md", "10", "How Much Should You Risk?",
        "The y* Recommendation section of the memo: the fraction of the learner's wealth that belongs in the risky portfolio, defended.",
        "Claude Code",
        """I'm working on Maya's Memo. The tangency portfolio is in `analysis/09-frontier.md`.

Chapter 10 taught:
- **The Capital Allocation Line** (CAL) connecting the risk-free asset to the tangency portfolio
- **The y* formula**: $y^* = (E[r_p] - r_f) / (\\gamma \\sigma_p^2)$, where γ is the risk-aversion coefficient
- **The Kelly fraction** as the related-but-different limit case (γ = 1 in log utility)
- The gap between *math-right* and *right for a human life*

Scaffold `analysis/10-allocation.py`:

1. **Load the tangency portfolio's expected return and variance** from `analysis/09-frontier.md`.

2. **Compute y* for three risk-aversion coefficients**:
   - γ = 2 (aggressive, e.g., a 25-year-old with high human capital)
   - γ = 4 (moderate, the textbook default)
   - γ = 8 (conservative, e.g., near-retirement)

   Report y* for each, and the resulting expected return and volatility of the *combined* portfolio (y* in the tangency portfolio plus (1 − y*) in the risk-free asset).

3. **Compute the Kelly fraction** for the same tangency portfolio. Compare to the y* values above.

4. **Plot the Capital Allocation Line.** Mark the three y* points, the Kelly fraction, and 100% tangency.

5. **The human-life check.** One paragraph. The math gives a fraction. What is the *behavioral* check — what's the largest drawdown the learner can live through without selling? Apply that constraint and report the implied y*.

6. **Save `analysis/10-allocation.md`** with the y* values, the CAL plot, the human-life check, and a one-sentence recommendation: *given my risk aversion and my behavioral capacity, the fraction of my wealth in the risky portfolio should be approximately X%.*

The script runs with `python analysis/10-allocation.py --gamma [VALUE]`.""",
        "A runnable script `analysis/10-allocation.py` plus `analysis/10-allocation.md` containing y* for three risk-aversion levels, the Kelly fraction, the CAL plot, the behavioral check, and a final recommendation.",
        "Right tool — y* is a one-line formula but the comparison to Kelly and the behavioral check are easier to communicate from a script that produces the plot.",
        "Append to the project. The y* recommendation here is the *single most important number* for translating the analysis into action; the capstone (Ch 13) integrates it.",
        "Chapter 9 produced the tangency portfolio; Chapter 10 asks how much of the learner's wealth belongs in it.",
        "Chapter 11 asks whether the position's return profile is *exceptional* (alpha) or *lucky* (beta-driven) — using CAPM and factor models.",
    ),

    (
        "11-asset-pricing-models.md", "11", "Asset Pricing Models",
        "The CAPM and Factor Read section of the memo: was the position's return exceptional (alpha) or lucky (beta-driven)? Decompose into systematic factor exposures.",
        "Claude Code",
        """I'm working on Maya's Memo. The diversification decomposition (Ch 8) and the frontier (Ch 9) are in the project.

Chapter 11 taught:
- **CAPM**: $E[r] = r_f + \\beta (E[r_m] - r_f)$ — beta is the only systematic-risk number that should be priced
- **Alpha** as the residual: the part of the return CAPM cannot explain
- **Multi-factor extensions** — Fama-French 3-factor (market, size, value) and 5-factor (adds profitability and investment)
- The exceptional-vs-lucky question

Scaffold `analysis/11-asset-pricing.py`:

1. **Estimate β against the market.** Regress the position's monthly excess returns on the market's monthly excess returns. Report β, α, R^2, the standard error on β, and the p-value on α.

2. **The CAPM expected return.** Plug β into the CAPM formula. Compare to the position's *realized* return. The difference is α. State whether α is statistically distinguishable from zero.

3. **Three-factor decomposition.** Regress excess return on the three Fama-French factors (Market, SMB, HML). Report the loadings and the resulting α. Has the alpha shrunk relative to the CAPM single-factor regression? If yes, the position's return was partly explained by size and value factors that CAPM ignored.

4. **Five-factor decomposition.** Run again with profitability (RMW) and investment (CMA) added. Report and compare.

5. **The exceptional-vs-lucky verdict.** One paragraph. Was the realized return *exceptional* (statistically significant alpha after factor controls), *lucky* (alpha collapses once you control for factor exposure), or *systematic with a tilt* (significant factor loadings, no residual alpha)?

6. **Save `analysis/11-asset-pricing.md`** with the four regression results, the verdict paragraph, and the implication: a position with high alpha post-controls deserves single-name exposure; a position whose return is fully factor-explained should be replaced by the cheapest factor ETFs.

Run with `python analysis/11-asset-pricing.py --ticker [TICKER]`.""",
        "A runnable script `analysis/11-asset-pricing.py` plus `analysis/11-asset-pricing.md` containing CAPM β and α, the three- and five-factor decompositions, the verdict on exceptional-vs-lucky, and the implication for direct ownership.",
        "Right tool — Fama-French factor data is downloadable from Ken French's website; `pandas-datareader` handles it. Claude Code can scaffold the full pipeline.",
        "Append to the project. The verdict here either reinforces or undermines the case for direct ownership made in Chapter 4 — flag the contradiction if it appears.",
        "Chapter 9 placed the position on the frontier; Chapter 11 asks whether its historical return came from skill, luck, or factor tilts.",
        "Chapter 12 produces the *financial-statement diligence* section — pulling the actual numbers from the 10-K to test whether the position's case rests on facts or on hype.",
    ),

    (
        "12-financial-statement-analysis.md", "12", "Financial Statement Analysis",
        "The Financial-Statement Diligence section of the memo: does the company's accounting support the equity case, or contradict it?",
        "Cowork",
        """I'm working on Maya's Memo. All quantitative sections are now in the project.

Chapter 12 taught:
- **The three statements as one system**: net income → cash flow → balance-sheet retained earnings
- **Accrual quality**: net income vs. operating cash flow; growing gap = warning
- **The ratios that matter**: ROE, ROIC, current ratio, debt/equity, FCF margin
- Reading 10-Ks like a doctor reads a chart

For a public-equity position, do this in **Cowork**:

1. **Pull the latest 10-K and 10-Q** from SEC EDGAR for the company. Save them in `filings/`.

2. **Read for structure.** Extract:
   - Income statement: revenue, gross profit, operating income, net income (last 5 years)
   - Balance sheet: cash, total assets, total liabilities, equity (last 5 years)
   - Cash flow statement: operating cash flow, capex, FCF (last 5 years)

3. **Reconcile the system.** Confirm that:
   - Net income from the income statement matches the cash-flow statement's starting line
   - Ending cash balance from cash flow ties to the balance sheet's cash line
   - Retained earnings movement = net income − dividends

4. **Compute the ratios.** Five years for each:
   - **ROE** = net income / equity
   - **ROIC** = NOPAT / invested capital
   - **Current ratio** = current assets / current liabilities
   - **Debt/equity** = total debt / equity
   - **FCF margin** = FCF / revenue

5. **The accrual-quality check.** Plot net income vs. operating cash flow over the five years. A widening gap (net income growing faster than OCF) is a warning. State what the chart shows.

6. **The diligence verdict.** One paragraph. Does the accounting support the equity story — *the same story you used in `03-claim-framing.md` and `05-dcf.md`* — or contradict it? Name three specific line items that would change your recommendation if they moved.

7. **Save the analysis as `analysis/12-statements.md`** with the ratios table, the accrual-quality chart description, and the verdict.

For a private business or a bond, adapt: the bond's covenant compliance schedule + the issuer's credit metrics; the private business's tax returns + bank statements + AR/AP aging.""",
        "A markdown document `analysis/12-statements.md` containing the five-year ratios table, the accrual-quality finding, and a verdict that names specific line items whose movement would change the recommendation.",
        "Optional — `analysis/12-statements.py` can pull EDGAR filings via `sec-edgar-downloader` and compute ratios automatically. Cowork's file-handling makes this section easier to assemble than pure code.",
        "Cowork is the right tool — it can read PDFs from EDGAR, extract numbers, and assemble the ratios table in one session. Save the result to the project for the capstone.",
        "Chapters 5 and 11 produced the *price* and the *factor read*; Chapter 12 tests whether the company's actual accounting supports the case the prior chapters assumed.",
        "Chapter 13 — the capstone — assembles all twelve sections into one integrated 6–10 page memo with a defended recommendation.",
    ),

    (
        "13-putting-it-all-together-the-investment-decision-capstone.md", "13", "The Whole Thing at Once",
        "The full integrated investment memo — 6–10 pages — assembling every section from Chapters 1–12 into one coherent recommendation that survives senior-practitioner Q&A.",
        "Cowork",
        """I'm working on Maya's Memo. Every chapter section is in the project: `01-position-brief.md` through `analysis/12-statements.md`.

Chapter 13 taught:
- **All five layers held at once**: return measurement, valuation, portfolio fit, capital allocation, financial-statement quality
- The *Feynman moment* — the pieces snap into a structure
- The defensible recommendation that survives Q&A from a senior practitioner

In **Cowork**, assemble the final memo as `report/13-final-memo.md`:

**Structure** (6–10 pages):

1. **Executive summary** (½ page). The recommendation in one sentence — actor, action, magnitude, timing. The expected return with a confidence band. The single largest risk. The what-would-change-my-mind sentence from `01-position-brief.md`, refined.

2. **Position and brief** (½ page). Adapted from `01-position-brief.md`. Updated with what the analysis taught.

3. **Return and risk profile** (½ page). From `02-return-risk.md`. The Sharpe ratio with period and frequency stated.

4. **Claim framing** (½ page). From `03-claim-framing.md`. Equity / debt / hybrid + the substitution test.

5. **Fund-vs-direct** (½ page). From `04-fund-vs-direct.md`. The recommendation, with the flipping condition.

6. **DCF valuation** (1 page). From `05-dcf.md`. The PV with the 5×5 sensitivity table.

7. **Leverage and option overlay** (1 page). Combine `06-leverage.md` and `07-option-overlay.md`. The recommended overlay (or no overlay) with the volatility regime that supports it.

8. **Diversification and portfolio fit** (1 page). Combine `analysis/08-diversification.md` and `analysis/09-frontier.md`. The variance decomposition and the position's location relative to the frontier.

9. **Capital allocation** (½ page). From `analysis/10-allocation.md`. The y* recommendation and the behavioral check.

10. **Asset pricing read** (½ page). From `analysis/11-asset-pricing.md`. The exceptional-vs-lucky verdict.

11. **Financial-statement diligence** (1 page). From `analysis/12-statements.md`. The ratios, the accrual-quality finding, the verdict.

12. **The integrated recommendation** (1 page). The decision. The size. The hedge. The trigger conditions for closing the position. The audit record — pointers to each prior section that supports the recommendation.

13. **What would change my mind** (¼ page). The named-and-dated commitment to specific evidence that would reverse the recommendation.

**The Q&A audit.** After Cowork generates the draft, run a critique pass: a senior practitioner reads this memo and asks the three hardest questions they would ask. Rewrite any section that doesn't already answer those questions in writing.

**The named-owner block.** End with: *Recommendation owned by [name], dated [date]. Audit trail: every section in this memo references the analysis file that produced it. The recommendation will be reviewed against [specific trigger condition or date].*""",
        "A complete 6–10 page integrated investment memo as `report/13-final-memo.md`, plus a one-page Q&A audit, plus a named-owner block. This is the deliverable the entire course was building toward.",
        "Optional — Claude Code can render the memo to PDF via Pandoc as `report/13-final-memo.pdf` for distribution.",
        "Cowork is the right tool — it can read every chapter's output file, compose the integrated memo, and run the Q&A critique pass in one session. The Project's accumulated context is the input.",
        "Every prior chapter contributed one section; Chapter 13 assembles them into the artifact the entire course was building toward.",
        "This is the final chapter. Your deliverable is now a complete memo that a senior practitioner could read in fifteen minutes and either agree with or disagree with on specific named points — the closure of the three-beat method introduced in Chapter 1.",
    ),
]


BLOCK_TEMPLATE = """
---

###  LLM Exercise — Chapter {n}: {title}

**Project:** Maya's Memo, Built Across the Course
**What you're building this chapter:** {what}
**Tool:** {tool}

---

**The Prompt:**

```
{prompt}
```

---

**What this produces:** {produces}

**How to adapt this prompt:**

- *For your own project:* Replace any bracketed domain placeholder with your specific instrument, ticker, or context. The exercise structure is instrument-agnostic; the content is yours.
- *For ChatGPT / Gemini:* Works as-is. For ChatGPT, save the running memo to a Custom GPT instead of a Claude Project. For Gemini, paste the project's accumulated section files into the context window each session.
- *For Claude Code:* {how_code}
- *For a Claude Project:* {how_project}

**Connection to previous chapters:** {connection}

**Preview of next chapter:** {preview}
"""


def main():
    for entry in EXERCISES:
        (filename, n, title, what, tool, prompt, produces,
         how_code, how_project, connection, preview) = entry
        path = CH / filename
        text = path.read_text()
        if "###  LLM Exercise — Chapter" in text or "### LLM Exercise — Chapter" in text:
            print(f"  SKIP (already has LLM Exercise): {filename}")
            continue
        block = BLOCK_TEMPLATE.format(
            n=n, title=title, what=what, tool=tool, prompt=prompt,
            produces=produces, how_code=how_code, how_project=how_project,
            connection=connection, preview=preview,
        )
        # Insert BEFORE the existing Wayback Machine section so the order is
        # chapter content → LLM Exercise → Wayback Machine (per spec).
        wb_marker = "## AI Wayback Machine"
        if wb_marker in text:
            wb_idx = text.index(wb_marker)
            # Walk back to the preceding `---\n\n` separator if present
            before = text[:wb_idx].rstrip()
            after = text[wb_idx:]
            # The Wayback section was preceded by `\n\n---\n\n` when we authored it.
            # Strip the trailing `---` from `before` so we can re-insert it below.
            if before.endswith("---"):
                before = before[:-3].rstrip()
            new_text = before + "\n" + block + "\n---\n\n" + after
        else:
            new_text = text.rstrip() + "\n" + block + "\n"
        path.write_text(new_text)
        print(f"  appended LLM Exercise to {filename}")


if __name__ == "__main__":
    main()
