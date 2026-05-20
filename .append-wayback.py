#!/usr/bin/env python3
"""Append `## AI Wayback Machine` blocks to each of the 13 content chapters
of computational-finance-with-ai. Spec says insert after the LLM Exercise block;
this book has none, so the natural anchor is end-of-file.

Figures: lesser-known where possible, pre-2001 dead OR foundational pre-2001 work,
no overlap with botspeak / branding-and-ai / computational-skepticism-for-ai /
living-models Wayback rosters.
"""
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

ENTRIES = [
    (
        "01-introduction-the-three-beat-method.md",
        "Lillian Gilbreth",
        "decomposing every white-collar task into a sequence of named, observable, repeatable motions",
        "the workflow discipline — idea, execute, verify",
        "Who was Lillian Gilbreth, and how does her industrial-engineering practice of breaking work into named, observable steps connect to the three-beat method (idea → execute → verify) the chapter teaches as the central discipline for analytical work with AI? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Lillian Moller Gilbreth",
        "Ask it to explain *therbligs* in plain language, as if you've never read a time-and-motion study",
        "Ask it to compare Gilbreth's hand-decomposition of a kitchen task to the three-beat decomposition of a financial analysis",
        'Add a constraint: "Answer as if you\'re writing the introduction to a chapter on workflow discipline for analytical AI work"',
    ),
    (
        "02-returns-and-risk-measurement.md",
        "Louis Bachelier",
        "deriving the mathematics of random walks for the Paris Bourse in 1900 — five years before Einstein used the same equations to describe Brownian motion",
        "returns, variance, and the formal measurement of risk",
        "Who was Louis Bachelier, and how does his 1900 thesis *Théorie de la Spéculation* — applying random-walk mathematics to securities prices — connect to the modern measurement of returns, volatility, and risk that the chapter teaches? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Louis Bachelier",
        "Ask it to explain a *random walk* in plain language, as if you've never seen a probability density",
        "Ask it to compare Bachelier's 1900 framing to the modern Sharpe-ratio + standard-deviation toolkit",
        'Add a constraint: "Answer as if you\'re writing the historical preface to a chapter on volatility"',
    ),
    (
        "03-equity-and-fixed-income.md",
        "Frederick Macaulay",
        "introducing the bond-duration concept in 1938 — the single number that makes interest-rate risk on a fixed-income security legible",
        "bond pricing, yield-to-maturity, and the structure of interest-rate risk",
        "Who was Frederick Macaulay, and how does his 1938 introduction of *duration* — the cash-flow-weighted average time to receipt — connect to the chapter's treatment of bond pricing and the way fixed income's risk is fundamentally different from equity's? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Frederick Macaulay",
        "Ask it to explain *Macaulay duration* in plain language, as if you've never seen a bond yield curve",
        "Ask it to compare Macaulay's duration to the modern *modified duration* and *convexity* concepts the chapter introduces",
        'Add a constraint: "Answer as if you\'re writing the rationale for why fixed-income risk needs its own metric"',
    ),
    (
        "04-funds-and-etfs.md",
        "Sylvia Porter",
        "writing personal-finance journalism for ordinary investors from 1935 onward — at a time when funds and indexed exposure to equities were treated as products for the wealthy alone",
        "mutual funds, ETFs, and how ordinary investors get diversified equity exposure",
        "Who was Sylvia Porter, and how does her decades of personal-finance journalism — translating institutional investing concepts into language ordinary households could act on — connect to the chapter's argument that funds and ETFs are the principal vehicles by which non-professional investors actually access markets? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Sylvia Porter",
        "Ask it to explain why *plain-language financial writing* was, in the 1940s, a contested project, in plain language",
        "Ask it to compare Porter's columns to a modern fund prospectus — what she would have wanted ordinary investors to be told",
        'Add a constraint: "Answer as if you\'re writing the consumer-facing explainer that should accompany an ETF launch"',
    ),
    (
        "05-time-value-of-money-and-discounted-cash-flows.md",
        "John Burr Williams",
        "publishing *The Theory of Investment Value* in 1938 — the foundational case that an asset's value is the present value of its future cash flows, formalized into the discount-rate apparatus the chapter teaches",
        "the time value of money and discounted-cash-flow valuation",
        "Who was John Burr Williams, and how does his 1938 dissertation *The Theory of Investment Value* — the foundational text on intrinsic value as the present value of future cash flows — connect to the chapter's apparatus of present value, discount rates, and discounted-cash-flow valuation? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "John Burr Williams",
        "Ask it to explain why *intrinsic value* required a formal definition before 1938, in plain language",
        "Ask it to compare Williams's dividend-discount-model framing to the modern free-cash-flow-to-equity DCF the chapter teaches",
        'Add a constraint: "Answer as if you\'re writing the historical foundation paragraph for a DCF chapter"',
    ),
    (
        "06-margin-and-short-selling.md",
        "Hyman Minsky",
        "developing the *financial instability hypothesis* — the argument that stable financial conditions actively produce the leverage cycles that destabilize them",
        "leverage, margin loans, and the mechanism by which short positions and borrowed money amplify both returns and ruin",
        "Who was Hyman Minsky, and how does his *financial instability hypothesis* — that stability breeds the leverage that breaks stability — connect to the chapter's mechanical treatment of margin accounts, short positions, and the way leverage moves from useful tool to existential risk? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Hyman Minsky",
        "Ask it to explain *the Minsky moment* in plain language, as if you've never read macrofinance",
        "Ask it to compare Minsky's three borrower types (hedge, speculative, Ponzi) to the margin-account stages in this chapter",
        'Add a constraint: "Answer as if you\'re writing the warning section of a margin-lending policy"',
    ),
    (
        "07-options-and-derivatives.md",
        "Vinzenz Bronzin",
        "deriving option-pricing formulas in 1908 — sixty-five years before Black, Scholes, and Merton — in a German-language textbook that was rediscovered in 2002 and re-evaluated as parallel to the Black-Scholes apparatus",
        "options pricing, the binomial model, and the Black-Scholes framework",
        "Who was Vinzenz Bronzin, and how does his 1908 *Theorie der Prämiengeschäfte* — derived parallel to and decades before Black-Scholes, but lost to history until 2002 — connect to the chapter's treatment of option pricing and the surprising stability of the underlying mathematics across rediscoveries? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Vinzenz Bronzin",
        "Ask it to explain why *option pricing kept getting reinvented* across the twentieth century, in plain language",
        "Ask it to compare Bronzin's 1908 derivation to the modern Black-Scholes formula the chapter introduces",
        'Add a constraint: "Answer as if you\'re writing a footnote in a chapter on option pricing"',
    ),
    (
        "08-the-diversification-miracle.md",
        "A. D. Roy",
        "publishing *Safety First and the Holding of Assets* in 1952 — the same year as Markowitz, with an alternative diversification framework built around minimizing the probability of a disastrous outcome rather than optimizing the variance trade-off",
        "diversification, covariance, and the way correlated risks combine in a portfolio",
        "Who was A. D. Roy, and how does his 1952 *safety-first* portfolio framework — published the same year as Markowitz but with a different organizing principle — connect to the chapter's argument that diversification is fundamentally about how risks combine, not how individual assets behave? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "A. D. Roy",
        "Ask it to explain *the safety-first criterion* in plain language, as if you've never seen Markowitz",
        "Ask it to compare Roy's safety-first framework to the mean-variance optimization the chapter teaches",
        'Add a constraint: "Answer as if you\'re writing the case for why diversification is two ideas, not one"',
    ),
    (
        "09-portfolio-construction.md",
        "James Tobin",
        "proving the *separation theorem* in 1958 — the result that any investor's optimal portfolio can be built from just two ingredients: the risk-free asset and the single tangency portfolio, regardless of risk preferences",
        "the efficient frontier and the construction of an optimal portfolio",
        "Who was James Tobin, and how does his 1958 *separation theorem* — that the choice of risky portfolio is independent of how much risk an investor wants to take — connect to the chapter's apparatus for constructing portfolios on the efficient frontier? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "James Tobin",
        "Ask it to explain *two-fund separation* in plain language, as if you've never seen an efficient frontier diagram",
        "Ask it to compare Tobin's separation theorem to the chapter's construction of the tangency portfolio",
        'Add a constraint: "Answer as if you\'re writing the rationale for offering only two products to an investor: the risk-free asset and the tangency portfolio"',
    ),
    (
        "10-capital-allocation-and-diversification.md",
        "John Larry Kelly Jr.",
        "deriving the *Kelly criterion* in 1956 at Bell Labs — the formal rule for what fraction of capital to bet given a known edge, applied first to information theory and signal processing before it reached finance",
        "capital allocation, the fraction of wealth at risk, and the math of *how much to bet*",
        "Who was John Larry Kelly Jr., and how does his 1956 derivation of the *Kelly criterion* — originating in Shannon's information theory rather than in finance — connect to the chapter's question of how much of one's wealth to put in the risky portfolio versus the risk-free asset? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "John Larry Kelly Jr.",
        "Ask it to explain *the Kelly criterion* in plain language, as if you've never seen utility theory",
        "Ask it to compare the Kelly fraction to the chapter's optimal $y^*$ — what's the same, what's different",
        'Add a constraint: "Answer as if you\'re writing the case for sizing positions by the Kelly fraction in a real portfolio"',
    ),
    (
        "11-asset-pricing-models.md",
        "John Lintner",
        "co-developing the Capital Asset Pricing Model in 1965 — independently of Sharpe, with a slightly different derivation that arrived at the same equilibrium result and shaped the way institutional investors would price risk for the next half-century",
        "the CAPM, beta, and the multi-factor extensions that followed",
        "Who was John Lintner, and how does his independent 1965 derivation of the CAPM — published in *The Review of Economics and Statistics* months before Sharpe's better-known paper appeared — connect to the chapter's treatment of beta, market risk premium, and multi-factor extensions? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "John Lintner",
        "Ask it to explain *systematic vs. idiosyncratic risk* in plain language, as if you've never seen beta",
        "Ask it to compare Lintner's 1965 derivation to Sharpe's 1964 paper — what was at stake in the difference",
        'Add a constraint: "Answer as if you\'re writing the historical preface to a CAPM chapter"',
    ),
    (
        "12-financial-statement-analysis.md",
        "Luca Pacioli",
        "publishing *Summa de Arithmetica* in 1494 — including the first complete printed treatment of double-entry bookkeeping, the structural ancestor of every income statement, balance sheet, and cash-flow statement the chapter teaches",
        "the three financial statements as one interconnected accounting system",
        "Who was Luca Pacioli, and how does his 1494 publication of double-entry bookkeeping in *Summa de Arithmetica* — over five centuries before any spreadsheet existed — connect to the chapter's argument that the three financial statements are one interconnected system, not three independent documents? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.",
        "Luca Pacioli",
        "Ask it to explain *double-entry bookkeeping* in plain language, as if you've never seen a balance sheet",
        "Ask it to compare Pacioli's 1494 ledger to the modern income-statement / balance-sheet / cash-flow-statement triad",
        'Add a constraint: "Answer as if you\'re writing the historical foundation paragraph for a chapter on financial-statement analysis"',
    ),
    (
        "13-putting-it-all-together-the-investment-decision-capstone.md",
        "Hetty Green",
        "running an integrated investment practice from the 1880s through the 1910s — moving across bonds, equities, distressed debt, and real estate with a discipline that anticipated modern integrated portfolio analysis by half a century",
        "integrated investment decision-making across all the chapter's tools",
        "Who was Hetty Green, and how does her late-nineteenth-century investment practice — moving deliberately across bond, equity, distressed-debt, and real-estate positions with explicit attention to risk, leverage, and time horizon — connect to the chapter's capstone argument that a real investment decision integrates every tool the book has taught? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.",
        "Hetty Green",
        "Ask it to explain *integrated capital allocation* in plain language, as if you've only seen each instrument analyzed alone",
        "Ask it to compare Green's positioning during the Panic of 1907 to a modern stress-tested portfolio decision",
        'Add a constraint: "Answer as if you\'re writing the case for why integrated decision-making is itself a discipline, not an aggregation of separate ones"',
    ),
]


BLOCK = """
---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **{name}** was {framing} decades before most people had heard of {concept}. Here's a prompt to find out more — and then make it better.

**Run this:**

```
{prompt}
```

→ Search **"{search}"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- {v1}
- {v2}
- {v3}

What changes? What gets better? What gets worse?
"""


def main():
    seen = set()
    for entry in ENTRIES:
        filename, name, framing, concept, prompt, search, v1, v2, v3 = entry
        if name in seen:
            print(f"!!! DUPLICATE figure: {name}")
        seen.add(name)
        path = CH / filename
        text = path.read_text()
        if "## AI Wayback Machine" in text:
            print(f"  SKIP (Wayback already present): {filename}")
            continue
        block = BLOCK.format(
            name=name, framing=framing, concept=concept,
            prompt=prompt, search=search, v1=v1, v2=v2, v3=v3,
        )
        new_text = text.rstrip() + "\n" + block + "\n"
        path.write_text(new_text)
        print(f"  appended Wayback ({name}) to {filename}")
    print(f"\nfigures included: {len(seen)} unique")


if __name__ == "__main__":
    main()
