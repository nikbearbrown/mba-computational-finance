#!/usr/bin/env python3
"""Pass 1 — render the 13 TABLE comments in computational-finance-with-ai/chapters/."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

TABLES = {}

TABLES["Five-element specification checklist"] = """| Element | What it forces you to decide | What goes wrong if omitted |
|---|---|---|
| **The Decision** | The specific action under consideration — buy, hold, sell, hedge, refuse | Without it, the analysis serves no one — every output sounds equally relevant |
| **The Alternative** | What you would do *instead* if the recommendation is *no* | Without it, the recommendation cannot be evaluated against opportunity cost |
| **The Data Window** | The exact period the analysis covers (e.g., monthly returns, Jan 2015 – Dec 2024) | Without it, comparable numbers across sources silently disagree about what they're comparing |
| **The Assumptions** | The premises the recommendation rests on — discount rate, growth rate, base rate, time horizon | Without them, the analysis cannot be stress-tested or audited |
| **The Output Shape** | The format of the deliverable — one-page memo, deck, table, executive summary | Without it, the work is sized wrong for the audience and gets re-done downstream |"""

TABLES["Cross-LLM comparison matrix for Maya"] = """| Metric | Claude | ChatGPT | Gemini | Spread |
|---|---|---|---|---|
| **Annualized return** | 78% | 76% | 81% | 5 pp |
| **Volatility** | 53% | 51% | 49% | 4 pp |
| **Max drawdown** | -56% | -54% | -58% | 4 pp |
| ***Sharpe ratio*** | **1.41** | **1.46** | **1.62** | **0.21** |

*The Sharpe-ratio row is the substantive disagreement. Returns and volatility differ cosmetically (3–5%, mostly rounding and window choice). The Sharpe ratio differs by 15% — large enough to flip a recommendation. Verifying which model used which risk-free rate, which lookback window, and which return frequency is the load-bearing work.*"""

TABLES["three-column comparison of simple, log, and total return"] = """| Return type | Formula | When to use it |
|---|---|---|
| **Simple (arithmetic) return** | $r_t = (P_t - P_{t-1}) / P_{t-1}$ | Single-period return for one position; what brokers report on a statement |
| **Log return** | $r_t = \\ln(P_t / P_{t-1})$ | When you need to add returns across time (log returns are time-additive); when modeling continuously compounded processes |
| **Total return (with dividends)** | $r_t = (P_t + D_t - P_{t-1}) / P_{t-1}$ | Comparing equity returns across companies with different dividend policies; computing realized investor return |"""

TABLES["summary results table — rows: NVDA"] = """| | Annualized return | Annualized volatility | Max drawdown | Sharpe ratio | Skewness | Kurtosis |
|---|---|---|---|---|---|---|
| **NVDA — 3-year window** | 96% | 54% | -56% | 1.71 | -0.12 | 4.8 |
| **NVDA — 5-year window** | 53% | 49% | -66% | 0.99 | -0.34 | 5.6 |
| **SPY — 3-year window** | 11% | 16% | -25% | 0.50 | -0.41 | 4.2 |
| **SPY — 5-year window** | 13% | 18% | -34% | 0.55 | -0.46 | 4.9 |

*Reading across the window-sensitivity story: the same security looks dramatically different depending on whether you measure over the post-2022 AI-infrastructure run (3-year) or include the 2022 drawdown (5-year). The Sharpe ratio drops by nearly half. Specify the window before quoting the number.*"""

TABLES["Three-structure comparison — rows: open-end mutual fund"] = """| Structure | Share supply | Pricing mechanism | Intraday trading | NAV tracking | Tax efficiency | Era introduced |
|---|---|---|---|---|---|---|
| **Open-end mutual fund** | Variable — shares created/redeemed at NAV | One price per day, set at 4 PM | No — orders fill at end-of-day NAV | Exact (you transact at NAV) | Lower — taxable distributions when other holders redeem | 1924 (MFS Massachusetts Investors Trust) |
| **Closed-end fund** | Fixed at IPO; shares trade on exchange | Market price, can diverge from NAV | Yes | Often trades at a discount or premium to NAV | Mid — can use leverage and capital-loss harvesting | 1893 (UK), 1929 (US peak) |
| **ETF** | Variable — shares created/redeemed *in-kind* by APs | Market price, kept tight to NAV via arbitrage | Yes | Tight tracking via creation/redemption mechanism | High — in-kind creation defers capital gains | 1993 (SPY) |

*Each structure solved the preceding era's main failure: closed-end funds added intraday trading; ETFs added in-kind tax efficiency on top of intraday liquidity.*"""

TABLES["four-row worked table for the $300/year contract"] = """| Year | Nominal cash flow | Discount factor $1/(1.08)^t$ | Present value |
|---|---|---|---|
| 1 | $300 | 0.9259 | $277.78 |
| 2 | $300 | 0.8573 | $257.20 |
| 3 | $300 | 0.7938 | $238.15 |
| 4 | $300 | 0.7350 | $220.51 |
| **Sum of PVs** | | | **$993.64** |
| **Cost** | | | **$1,000.00** |
| **NPV** | | | **−$6.36** |

*Nominal cash flows total $1,200 — the contract "looks" profitable at the $1,000 price. Discounted at 8%, the present value is $993.64 — narrowly negative NPV. The "profit" was eaten by the time value of money. The discount rate is where the entire decision lives.*"""

TABLES["two-dimensional sensitivity table — rows vary discount rate"] = """| | Year-1 CF: \\$120K | \\$150K | \\$180K | \\$210K |
|---|---|---|---|---|
| **Discount rate 10%** | -$95K | $42K | $179K | $316K |
| **Discount rate 12%** | -$143K | -$15K | $113K | $241K |
| **Discount rate 15%** | -$208K | -$93K | $22K | $137K |
| **Discount rate 18%** | -$262K | -$159K | -$56K | $47K |

*The break-even boundary runs from the upper-left toward the lower-right. The deal works in roughly the upper-right triangle (high CF, low discount rate). It does not work in the lower-left triangle. Most disagreements about a DCF are disagreements about which corner of this table the decision-maker is anchoring to.*"""

TABLES["Black-Scholes input summary"] = """| Symbol | Plain-English meaning | Observable or estimated | Where to find it |
|---|---|---|---|
| **$S$** — stock price | Current price of the underlying | **Observable** | Live quote from any broker or data feed |
| **$K$** — strike | Price at which the option holder can buy (call) or sell (put) | **Observable** | The option chain — the strike is contractual |
| **$r$** — risk-free rate | The continuously compounded risk-free rate over the life of the option | **Observable** | Treasury yield curve, matched to the option's maturity |
| **$T$** — time to expiration | Years remaining until the option expires | **Observable** | The expiration date, in calendar terms |
| ***$\\sigma$ — volatility*** | The expected annualized standard deviation of the underlying's returns over the option's life | ***Estimated*** | Historical volatility of returns, OR (more commonly) the implied volatility back-solved from current option prices |

*Four inputs are observable right now. One — $\\sigma$ — requires judgment. Notice what is missing: the expected return on the stock does not appear. The option's price does not depend on whether the stock is going up or down — only on how much it is going to move.*"""

TABLES["three-row comparison table — rows: TSLA/AAPL"] = """| Asset pair | Asset 1 vol | Asset 2 vol | Correlation | 50/50 portfolio vol | Portfolio return vs. weighted average |
|---|---|---|---|---|---|
| **TSLA / AAPL** | 58% | 28% | $\\rho = 0.62$ | 39% | Equal — diversification reduces risk modestly because correlation is positive and high |
| **AAPL / JNJ** | 28% | 16% | $\\rho = 0.30$ | 18% | Equal — substantial volatility reduction because correlation is moderate |
| **AAPL / Aggregate Bonds** | 28% | 5% | $\\rho = 0.10$ | 14% | Equal — large volatility reduction because correlation is near zero and the second asset is much less volatile |

*The portfolio volatility falls below both components as correlation decreases. Expected return is the weighted average of the components — diversification does not change return; it only reduces variance. The lower the correlation, the larger the variance reduction at zero return cost.*"""

TABLES["calm-period vs. crisis-period correlations"] = """| Asset pair | Calm-period correlation | Crisis-period correlation (2008) | Direction of change |
|---|---|---|---|
| **US equity / International equity** | 0.65 | 0.92 | ↑ — diversification benefit collapses just when needed |
| **US equity / Aggregate bonds** | -0.10 | +0.30 | ↑ — sign flips; the diversifier becomes a co-mover |
| **US equity / Long Treasuries** | -0.30 | -0.45 | ↓ (more negative) — Treasuries deliver in crisis as expected |
| **Aggregate bonds / TIPS** | 0.85 | 0.45 | ↓ — credit-bond correlations break in crisis |

*Equity-equity correlations converge toward 1 in crisis. Equity-bond correlations can shift sign. The optimizer trained on calm-period covariances cannot see this — and the portfolio it builds is exactly wrong about which assets diversify when diversification is most needed.*"""

TABLES["factor premium summary"] = """| Factor | What it captures | Approximate historical premium (annualized) | Data source / citation |
|---|---|---|---|
| **Market (CAPM)** | Excess return of the market portfolio over the risk-free rate | ~6–7% (1928–2024) | Damodaran NYU dataset; CRSP; *Sharpe (1964)*, *Lintner (1965)* |
| **SMB — size** | Small-cap excess return over large-cap | ~2–3% | Ken French Data Library; *Fama-French (1993)* |
| **HML — value** | High book-to-market (value) excess return over low (growth) | ~4–5% | Ken French Data Library; *Fama-French (1993)* |
| **UMD — momentum** | Past-year winners excess return over past-year losers | ~8–10% (with high turnover) | Ken French Data Library; *Carhart (1997)* |
| **RMW — profitability** | High operating profitability excess return over low | ~3% | Ken French Data Library; *Fama-French (2015)* |

*CAPM is one row in a family of compensated risk factors. A position whose return is fully explained by market + size + value + momentum + profitability has no alpha — the return came from factor exposure, which is available cheaply via factor ETFs.*"""

TABLES["DuPont decomposition for MSFT, AAPL, and GOOGL"] = """| Company | Net margin | Asset turnover | Leverage multiplier | Computed ROE | Reported ROE |
|---|---|---|---|---|---|
| **MSFT** | 36% | 0.51 | **1.8×** | 33% | 33% |
| **AAPL** | 25% | 1.04 | **6.6×** | 172% | 172% |
| **GOOGL** | 22% | 0.62 | **1.6×** | 22% | 22% |

*Same headline ROE story (high), three completely different decompositions. Apple's 6.6× leverage multiplier — driven by its capital-return program (large buybacks shrinking equity) — produces a 172% ROE that has almost nothing in common with MSFT's 33% from operating performance. Reading ROE without the DuPont decomposition is reading a single number that is doing three different jobs.*"""


def apply():
    pat = re.compile(r'<!--\s*→\s*\[TABLE:([^]]*?)(?:\]\s*-->|-->)', re.DOTALL)
    files = sorted(CH.glob('*.md'))
    total = 0
    miss = []
    for f in files:
        text = f.read_text()
        def replace(m):
            nonlocal total
            comment = m.group(0)
            for key, table in TABLES.items():
                if key in comment:
                    total += 1
                    return table
            miss.append((f.name, comment[:80]))
            return comment
        new_text = pat.sub(replace, text)
        if new_text != text:
            f.write_text(new_text)
    print(f"replaced: {total} tables")
    if miss:
        print("MISSED:")
        for fn, c in miss: print(f"  {fn}: {c}")


if __name__ == "__main__":
    apply()
