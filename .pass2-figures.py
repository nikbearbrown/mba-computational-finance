#!/usr/bin/env python3
"""Pass 2 — generate 9 SVG+PNG figures for computational-finance-with-ai."""
import re
from pathlib import Path
import cairosvg

ROOT = Path(__file__).parent
CH = ROOT / "chapters"
IMG = ROOT / "images"
IMG.mkdir(exist_ok=True)

INK = "#1a1714"
GRAY_DARK = "#4a4540"
GRAY_MID = "#8a8480"
GRAY_LIGHT = "#c8c4c0"
CREAM = "#f5f2ee"
WHITE = "#fdfcfb"
SERIF = "Georgia, 'Times New Roman', serif"

DEFS = """<defs>
  <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#1a1714"/>
  </marker>
</defs>"""


def open_svg(w, h):
    return [
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">',
        DEFS,
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>',
    ]


# --- Ch 2 — NVDA monthly returns histogram with normal overlay -------------
def fig_ch2():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">NVDA monthly returns vs. fitted normal</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Fat tails on both ends; bulk shifted slightly right of zero. The normal underfits the extremes.</text>')

    # Axes
    chart_left, chart_right = 80, 620
    base_y, top_y = 340, 100
    out.append(f'<line x1="{chart_left}" y1="{base_y}" x2="{chart_right}" y2="{base_y}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<line x1="{chart_left}" y1="{base_y}" x2="{chart_left}" y2="{top_y}" stroke="{INK}" stroke-width="1"/>')

    # X-axis: monthly return -30% to +40%, with 0 marked
    bins = [
        (-30, 1), (-25, 0), (-20, 2), (-15, 3), (-10, 5), (-5, 8),
        (0, 12), (5, 14), (10, 11), (15, 7), (20, 4), (25, 3), (30, 1), (35, 1), (40, 1),
    ]
    bin_w = (chart_right - chart_left) / len(bins)
    max_count = max(b[1] for b in bins)
    for i, (xpct, count) in enumerate(bins):
        x = chart_left + i * bin_w
        bh = (count / max_count) * (base_y - top_y) * 0.92
        out.append(f'<rect x="{x+2}" y="{base_y - bh}" width="{bin_w-4}" height="{bh}" fill="{CREAM}" stroke="{INK}" stroke-width="0.5"/>')
        if xpct % 10 == 0:
            out.append(f'<text x="{x + bin_w/2}" y="{base_y + 16}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{xpct}%</text>')

    # Normal-curve overlay (fitted approximate: mean ~+5%, sd ~12%)
    import math
    mean_idx = bins.index((5, 14))
    sd_idx = 2.5  # ~12% / 5% per bin
    points = []
    for i in range(0, len(bins) * 8 + 1):
        idx = i / 8
        x = chart_left + idx * bin_w
        z = (idx - mean_idx) / sd_idx
        density = math.exp(-z*z/2) / (sd_idx * math.sqrt(2 * math.pi))
        # normalize so peak ~ max_count
        density_norm = density * max_count * sd_idx * math.sqrt(2 * math.pi)
        bh = (density_norm / max_count) * (base_y - top_y) * 0.92
        y = base_y - bh
        points.append(f"{x},{y}")
    out.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{INK}" stroke-width="1.5"/>')

    # Annotations
    out.append(f'<text x="180" y="280" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">left tail —</text>')
    out.append(f'<text x="180" y="294" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">extreme losses</text>')
    out.append(f'<text x="180" y="308" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">above normal</text>')
    out.append(f'<text x="540" y="280" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">right tail —</text>')
    out.append(f'<text x="540" y="294" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">extreme gains</text>')
    out.append(f'<text x="540" y="308" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}">above normal</text>')

    # Y axis label
    out.append(f'<text x="40" y="{(base_y+top_y)/2}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle" transform="rotate(-90 40 {(base_y+top_y)/2})">Frequency (months)</text>')
    # X axis label
    out.append(f'<text x="{(chart_left+chart_right)/2}" y="380" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">Monthly return</text>')

    # Legend
    out.append(f'<rect x="490" y="110" width="14" height="10" fill="{CREAM}" stroke="{INK}" stroke-width="0.5"/>')
    out.append(f'<text x="510" y="120" font-family="{SERIF}" font-size="10" fill="{INK}">observed</text>')
    out.append(f'<line x1="490" y1="138" x2="504" y2="138" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<text x="510" y="142" font-family="{SERIF}" font-size="10" fill="{INK}">fitted normal</text>')

    out.append('</svg>')
    return "\n".join(out)


# --- Ch 4 — AP arbitrage loop, two panels ---------------------------------
def fig_ch4():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The Authorized Participant arbitrage loop</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Why ETF prices stay tight to NAV — the AP makes risk-free profit by closing any gap.</text>')

    panels = [
        ("ETF ABOVE NAV", 56,  ["AP buys basket at $99", "AP delivers basket → fund", "Fund issues new ETF shares", "AP sells ETF on exchange at $100", "$1 risk-free profit"]),
        ("ETF BELOW NAV", 372, ["AP buys ETF cheap on exchange at $99", "AP redeems ETF → fund", "Fund delivers basket worth $100", "AP sells basket at $100", "$1 risk-free profit"]),
    ]
    for title, px, steps in panels:
        out.append(f'<rect x="{px}" y="80" width="272" height="300" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{px+16}" y="100" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.2">{title}</text>')
        out.append(f'<line x1="{px+16}" y1="108" x2="{px+256}" y2="108" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        for i, step in enumerate(steps):
            iy = 138 + i * 42
            # step number circle
            out.append(f'<circle cx="{px+30}" cy="{iy-5}" r="11" fill="{INK}"/>')
            out.append(f'<text x="{px+30}" y="{iy-1}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">{i+1}</text>')
            out.append(f'<text x="{px+50}" y="{iy}" font-family="{SERIF}" font-size="11" fill="{INK}">{step}</text>')

    out.append(f'<text x="{w/2}" y="408" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Each gap is closed by the AP&#8217;s arbitrage — the ETF tracks NAV almost perfectly, regardless of whether anyone is paying attention.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 5 — compounding / discounting timeline ----------------------------
def fig_ch5():
    w, h = 700, 360
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Compounding and discounting are one operation, run in opposite directions</text>')

    cy = 200
    out.append(f'<line x1="80" y1="{cy}" x2="620" y2="{cy}" stroke="{INK}" stroke-width="2"/>')

    # Today node
    out.append(f'<circle cx="120" cy="{cy}" r="10" fill="{INK}"/>')
    out.append(f'<text x="120" y="{cy+34}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Today</text>')
    out.append(f'<text x="120" y="{cy+52}" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">PV</text>')

    # Year n node
    out.append(f'<circle cx="580" cy="{cy}" r="10" fill="{INK}"/>')
    out.append(f'<text x="580" y="{cy+34}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Year n</text>')
    out.append(f'<text x="580" y="{cy+52}" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">FV</text>')

    # Compounding arrow (right)
    out.append(f'<path d="M150 {cy-30} Q350 {cy-90} 550 {cy-30}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="350" y="{cy-92}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Compounding</text>')
    out.append(f'<text x="350" y="{cy-74}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">multiply by $(1+r)^n$</text>')

    # Discounting arrow (left)
    out.append(f'<path d="M550 {cy+30} Q350 {cy+90} 150 {cy+30}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="350" y="{cy+98}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Discounting</text>')
    out.append(f'<text x="350" y="{cy+116}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">divide by $(1+r)^n$</text>')

    out.append(f'<text x="{w/2}" y="328" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The same factor in two directions. The discount rate is where the entire decision lives.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 6 fig 1 — balance sheets before and after a 28.6% drop -----------
def fig_ch6_a():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">A 28.6% drop wipes out 57% of equity</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The loan does not move. The equity absorbs the entire loss.</text>')

    panels = [
        ("AT ENTRY", 56, [("Position value", "$10,000"), ("− Loan", "$5,000"), ("Equity", "$5,000"), ("Margin %", "50%")]),
        ("AFTER −28.6% DROP", 372, [("Position value", "$7,143"), ("− Loan (unchanged)", "$5,000"), ("Equity", "$2,143"), ("Margin %", "30%")]),
    ]
    for title, px, rows in panels:
        out.append(f'<rect x="{px}" y="80" width="272" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{px+16}" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">{title}</text>')
        out.append(f'<line x1="{px+16}" y1="112" x2="{px+256}" y2="112" stroke="{GRAY_MID}" stroke-width="0.75"/>')
        for i, (label, val) in enumerate(rows):
            iy = 144 + i * 48
            emph = (i == len(rows) - 1) or "Loan" in label and "unchanged" in label
            weight = "bold" if i in (2, 3) else "normal"
            out.append(f'<text x="{px+16}" y="{iy}" font-family="{SERIF}" font-size="12" fill="{INK}">{label}</text>')
            out.append(f'<text x="{px+256}" y="{iy}" font-family="{SERIF}" font-size="13" font-weight="{weight}" fill="{INK}" text-anchor="end">{val}</text>')
            if i < len(rows) - 1:
                out.append(f'<line x1="{px+16}" y1="{iy+8}" x2="{px+256}" y2="{iy+8}" stroke="{GRAY_LIGHT}" stroke-width="0.75" stroke-dasharray="3 3"/>')

    out.append(f'<text x="{w/2}" y="396" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A 28.6% move in the underlying produces a 57% drop in your equity. That is leverage in one number.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 6 fig 2 — short sale flow ----------------------------------------
def fig_ch6_b():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Short-sale mechanics — four parties, two flows</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Shares move one way; cash and borrow fees move the other. The short seller owes the broker the shares back.</text>')

    nodes = [
        ("LENDER", "Original shareholder",  100, 200),
        ("BROKER", "Intermediary",          280, 200),
        ("SHORT SELLER", "Borrows + sells", 460, 200),
        ("BUYER", "Pays cash for shares",   620, 200),
    ]
    for label, sub, cx, cy in nodes:
        out.append(f'<rect x="{cx-56}" y="{cy-28}" width="112" height="56" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{cx}" y="{cy-6}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        out.append(f'<text x="{cx}" y="{cy+12}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{sub}</text>')

    # Shares-flow arrows (above)
    for i in range(3):
        x1 = nodes[i][2] + 56
        x2 = nodes[i+1][2] - 56
        ay = 180
        out.append(f'<path d="M{x1} {ay} L{x2} {ay}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
        out.append(f'<text x="{(x1+x2)/2}" y="{ay-6}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">shares</text>')

    # Cash-and-collateral flows (below)
    out.append(f'<path d="M{nodes[3][2]-56} 240 L{nodes[2][2]+56} 240" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)" stroke-dasharray="5 3"/>')
    out.append(f'<text x="{(nodes[2][2]+nodes[3][2])/2}" y="256" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">cash from sale</text>')
    out.append(f'<path d="M{nodes[2][2]-56} 280 L{nodes[1][2]+56} 280" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)" stroke-dasharray="5 3"/>')
    out.append(f'<text x="{(nodes[1][2]+nodes[2][2])/2}" y="296" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">collateral held</text>')

    # Borrow fee
    out.append(f'<path d="M{nodes[2][2]} 314 Q{nodes[2][2]} 360 {nodes[1][2]} 314" stroke="{INK}" stroke-width="1" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="{(nodes[1][2]+nodes[2][2])/2}" y="368" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">borrow fee (pays per day until covered)</text>')

    out.append(f'<text x="{w/2}" y="400" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The shares are owed back. The mechanism is a loan in shares, not a sale of cash.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 7 — binomial tree + replicating portfolio -----------------------
def fig_ch7():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">One-step binomial tree and the replicating portfolio</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">A long call equals 0.5 shares plus borrowing $38.10 — same payoffs in both states. No probability appears.</text>')

    # Left panel: tree
    out.append(f'<rect x="56" y="80" width="296" height="300" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="72" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.2">CALL OPTION TREE</text>')
    # root
    out.append(f'<circle cx="120" cy="220" r="20" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="120" y="217" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">$100</text>')
    out.append(f'<text x="120" y="232" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">today</text>')
    # up node
    out.append(f'<circle cx="280" cy="160" r="20" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="280" y="157" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">$120</text>')
    out.append(f'<text x="280" y="172" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">call: $20</text>')
    # down node
    out.append(f'<circle cx="280" cy="280" r="20" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="280" y="277" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">$80</text>')
    out.append(f'<text x="280" y="292" font-family="{SERIF}" font-size="9" fill="{GRAY_DARK}" text-anchor="middle">call: $0</text>')
    # branches
    out.append(f'<path d="M140 210 L260 168" stroke="{INK}" stroke-width="1.5" fill="none"/>')
    out.append(f'<path d="M140 230 L260 272" stroke="{INK}" stroke-width="1.5" fill="none"/>')
    out.append(f'<text x="200" y="190" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">up state</text>')
    out.append(f'<text x="200" y="262" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">down state</text>')

    # Right panel: replicating portfolio
    out.append(f'<rect x="404" y="80" width="252" height="300" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="420" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.2">REPLICATING PORTFOLIO</text>')
    out.append(f'<text x="420" y="140" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}">$\\Delta = 0.5$ shares</text>')
    out.append(f'<text x="420" y="166" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}">$B = -\\$38.10$ (borrow)</text>')
    out.append(f'<line x1="420" y1="180" x2="640" y2="180" stroke="{GRAY_LIGHT}" stroke-width="0.75" stroke-dasharray="3 3"/>')
    out.append(f'<text x="420" y="206" font-family="{SERIF}" font-size="11" fill="{INK}">In up state:</text>')
    out.append(f'<text x="420" y="222" font-family="{SERIF}" font-size="11" fill="{INK}">$0.5 \\times 120 - 38.10 \\times 1.05 = 20$</text>')
    out.append(f'<text x="420" y="248" font-family="{SERIF}" font-size="11" fill="{INK}">In down state:</text>')
    out.append(f'<text x="420" y="264" font-family="{SERIF}" font-size="11" fill="{INK}">$0.5 \\times 80 - 38.10 \\times 1.05 = 0$</text>')
    out.append(f'<line x1="420" y1="288" x2="640" y2="288" stroke="{INK}" stroke-width="1"/>')
    out.append(f'<text x="420" y="312" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}">Cost today:</text>')
    out.append(f'<text x="420" y="332" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}">$0.5 \\times 100 - 38.10 = \\$11.90$</text>')

    out.append(f'<text x="{w/2}" y="404" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">No probability of up vs. down appears in the calculation. The price comes from the replicating portfolio, not the forecast.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 11 — single stock vs. portfolio idiosyncratic cancellation ------
def fig_ch11():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Idiosyncratic risk cancels in a portfolio; market risk does not</text>')

    panels = [
        ("ONE STOCK", 56,  ["Market component", "+ Idiosyncratic component", "= Total return"]),
        ("500-STOCK PORTFOLIO", 372, ["Market component (sums)", "Idiosyncratic components (cancel)", "= Market return only"]),
    ]
    for title, px, lines in panels:
        out.append(f'<rect x="{px}" y="80" width="272" height="280" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{px+16}" y="104" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">{title}</text>')
        out.append(f'<line x1="{px+16}" y1="112" x2="{px+256}" y2="112" stroke="{GRAY_MID}" stroke-width="0.75"/>')

    # Single-stock arrows
    px = 56
    cy = 220
    out.append(f'<path d="M{px+40} {cy} L{px+220} {cy-50}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="{px+135}" y="{cy-58}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">market $\\beta r_m$</text>')
    out.append(f'<path d="M{px+40} {cy} L{px+220} {cy+50}" stroke="{GRAY_DARK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{px+135}" y="{cy+72}" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">idiosyncratic $\\epsilon_i$</text>')
    out.append(f'<text x="{px+135}" y="{cy+24}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{INK}" text-anchor="middle">total = $\\beta r_m + \\epsilon_i$</text>')

    # Portfolio arrows — many small idiosyncratic arrows that cancel
    px = 372
    out.append(f'<path d="M{px+40} {cy} L{px+220} {cy-50}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="{px+135}" y="{cy-58}" font-family="{SERIF}" font-size="11" fill="{INK}" text-anchor="middle">market $\\bar\\beta r_m$ (survives)</text>')
    # Many tiny idiosyncratic arrows pointing in different directions
    import math
    for k in range(7):
        angle = -0.6 + (k - 3) * 0.18
        x1 = px + 50
        y1 = cy + 12
        x2 = x1 + 22 * math.cos(angle)
        y2 = y1 + 22 * math.sin(angle)
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRAY_DARK}" stroke-width="0.75"/>')
    out.append(f'<text x="{px+135}" y="{cy+30}" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">idiosyncratic vectors</text>')
    out.append(f'<text x="{px+135}" y="{cy+46}" font-family="{SERIF}" font-size="11" fill="{GRAY_DARK}" text-anchor="middle">cancel ($\\sum \\epsilon_i \\to 0$)</text>')
    out.append(f'<text x="{px+135}" y="{cy+72}" font-family="{SERIF}" font-size="11" font-style="italic" fill="{INK}" text-anchor="middle">total = $\\bar\\beta r_m$ alone</text>')

    out.append(f'<text x="{w/2}" y="396" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Only systematic risk earns a return premium. CAPM prices that part — the idiosyncratic part is diversifiable, therefore unpriced.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 12 — three statements as one system ------------------------------
def fig_ch12():
    w, h = 700, 420
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Three statements, one system</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Pull one thread and the others move. Net income → cash flow → balance sheet retained earnings.</text>')

    boxes = [
        ("INCOME STATEMENT", "Revenue → Net Income\nover the period", 56,  220),
        ("CASH FLOW STATEMENT", "Net Income → adjustments\n→ ending cash", 280, 220),
        ("BALANCE SHEET", "Assets, liabilities, equity\nat a moment in time", 504, 220),
    ]
    for label, body, cx, cy in boxes:
        out.append(f'<rect x="{cx-80}" y="{cy-60}" width="160" height="120" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="{cx}" y="{cy-38}" font-family="{SERIF}" font-size="11" font-weight="bold" fill="{INK}" text-anchor="middle">{label}</text>')
        for i, line in enumerate(body.split("\n")):
            out.append(f'<text x="{cx}" y="{cy-12 + i*16}" font-family="{SERIF}" font-size="10" fill="{GRAY_DARK}" text-anchor="middle">{line}</text>')

    # Arrows
    # Income statement -> Cash flow (net income line)
    out.append(f'<path d="M{56+80} 200 L{280-80} 200" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="{(56+80+280-80)/2}" y="194" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">net income</text>')
    # Cash flow -> Balance sheet (ending cash)
    out.append(f'<path d="M{280+80} 200 L{504-80} 200" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')
    out.append(f'<text x="{(280+80+504-80)/2}" y="194" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">ending cash</text>')
    # Income statement -> Balance sheet (retained earnings) — curved arrow above
    out.append(f'<path d="M{56} 160 Q{280} 80 {504} 160" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)" stroke-dasharray="4 3"/>')
    out.append(f'<text x="280" y="100" font-family="{SERIF}" font-size="10" font-style="italic" fill="{INK}" text-anchor="middle">retained earnings = prior + net income − dividends</text>')

    out.append(f'<text x="{w/2}" y="380" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The three statements answer three different questions, but they share line items by construction. Reading any one alone misses the system.</text>')
    out.append('</svg>')
    return "\n".join(out)


# --- Ch 13 — five-layer dependency stack ---------------------------------
def fig_ch13():
    w, h = 700, 480
    out = open_svg(w, h)
    out.append(f'<text x="{w/2}" y="36" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">The five layers of an integrated investment decision</text>')
    out.append(f'<text x="{w/2}" y="54" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">Errors compound upward — a mistake in Layer 1 propagates through every layer above it.</text>')

    layers = [
        ("LAYER 5", "Capital allocation",        "y* — fraction of wealth at risk", 92),
        ("LAYER 4", "Portfolio fit",             "Where does this position sit on the frontier?", 168),
        ("LAYER 3", "Valuation",                 "DCF / option overlay / leverage decision", 244),
        ("LAYER 2", "Asset pricing read",        "CAPM / factor decomposition — alpha or beta?", 320),
        ("LAYER 1", "Return measurement",        "Returns, volatility, Sharpe with conventions stated", 396),
    ]
    for label, name, sub, y in layers:
        out.append(f'<rect x="120" y="{y}" width="460" height="60" fill="{CREAM}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<text x="140" y="{y+22}" font-family="{SERIF}" font-size="10" font-weight="bold" fill="{GRAY_DARK}" letter-spacing="1.5">{label}</text>')
        out.append(f'<text x="140" y="{y+42}" font-family="{SERIF}" font-size="13" font-weight="bold" fill="{INK}">{name}</text>')
        out.append(f'<text x="350" y="{y+42}" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}">{sub}</text>')

    # Downward arrows (errors propagate upward, drawn as upward arrows annotating that)
    for y in [156, 232, 308, 384]:
        out.append(f'<path d="M350 {y+8} L350 {y-8}" stroke="{INK}" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>')

    out.append(f'<text x="{w/2}" y="468" font-family="{SERIF}" font-size="10" font-style="italic" fill="{GRAY_DARK}" text-anchor="middle">The capstone holds all five layers at once — a recommendation that survives Q&amp;A is one that defends each layer separately.</text>')
    out.append('</svg>')
    return "\n".join(out)


FIGURES = [
    ("02-returns-and-risk-measurement-fig-01",                                   fig_ch2(),
     "Histogram of NVDA monthly returns with a fitted normal distribution overlay; both tails sit above the normal and the bulk shifts slightly right of zero",
     "Figure 2.1 — NVDA monthly returns vs. fitted normal",
     "02-returns-and-risk-measurement.md", "histogram of NVDA monthly returns"),
    ("04-funds-and-etfs-fig-01",                                                 fig_ch4(),
     "Two-panel diagram of the AP arbitrage loop — the steps an Authorized Participant takes to close a gap when an ETF trades above NAV (left) and below NAV (right)",
     "Figure 4.1 — The AP arbitrage loop",
     "04-funds-and-etfs.md", "AP arbitrage loop"),
    ("05-time-value-of-money-and-discounted-cash-flows-fig-01",                  fig_ch5(),
     "Two-arrow timeline showing compounding (today → year n) and discounting (year n → today) as the same factor in opposite directions",
     "Figure 5.1 — Compounding and discounting are one operation, run two ways",
     "05-time-value-of-money-and-discounted-cash-flows.md", "two-arrow timeline diagram"),
    ("06-margin-and-short-selling-fig-01",                                       fig_ch6_a(),
     "Two side-by-side balance sheets for a margin account at entry vs. after a 28.6% drop in the underlying — equity falls 57%, the loan does not move",
     "Figure 6.1 — A 28.6% drop wipes out 57% of equity",
     "06-margin-and-short-selling.md", 'Two side-by-side "balance sheets" for the margin account'),
    ("06-margin-and-short-selling-fig-02",                                       fig_ch6_b(),
     "Flow diagram of a short sale across four parties (Lender, Broker, Short Seller, Buyer), showing share flow, cash collateral, and the borrow fee",
     "Figure 6.2 — Short-sale mechanics",
     "06-margin-and-short-selling.md", "Flow diagram of the short sale mechanics"),
    ("07-options-and-derivatives-fig-01",                                        fig_ch7(),
     "One-step binomial tree for a call option ($100 → $120 or $80) alongside the replicating portfolio (0.5 shares − $38.10 borrowed) producing identical payoffs at $11.90",
     "Figure 7.1 — Binomial tree and the replicating portfolio",
     "07-options-and-derivatives.md", "One-step binomial tree"),
    ("11-asset-pricing-models-fig-01",                                           fig_ch11(),
     "Two-panel diagram showing one stock decomposed into market plus idiosyncratic components, and a 500-stock portfolio where the idiosyncratic vectors cancel and only the market component remains",
     "Figure 11.1 — Idiosyncratic risk cancels in a portfolio; market risk does not",
     "11-asset-pricing-models.md", "two-panel diagram"),
    ("12-financial-statement-analysis-fig-01",                                   fig_ch12(),
     "Three-box diagram showing the income statement, cash flow statement, and balance sheet linked by net income, ending cash, and retained earnings — one accounting system viewed from three angles",
     "Figure 12.1 — Three statements, one system",
     "12-financial-statement-analysis.md", "Diagram showing the three statements as an interconnected system"),
    ("13-putting-it-all-together-the-investment-decision-capstone-fig-01",       fig_ch13(),
     "Five-layer dependency stack — return measurement at the bottom, capital allocation at the top, with arrows showing that errors at any layer propagate upward through every layer above it",
     "Figure 13.1 — The five-layer dependency stack",
     "13-putting-it-all-together-the-investment-decision-capstone.md", "Five-layer dependency stack"),
]


def write_pair(slug, svg_str):
    svg_path = IMG / f"{slug}.svg"
    png_path = IMG / f"{slug}.png"
    svg_path.write_text(svg_str)
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_str)
    vw, vh = int(m.group(1)), int(m.group(2))
    cairosvg.svg2png(bytestring=svg_str.encode('utf-8'),
                      output_width=vw*2, output_height=vh*2,
                      write_to=str(png_path))


def replace_in_chapter(ch_file, comment_key, slug, alt, title):
    path = CH / ch_file
    text = path.read_text()
    pat = re.compile(
        r'<!--\s*→\s*\[(?:IMAGE|FIGURE|DIAGRAM):[^\n]*?'
        + re.escape(comment_key)
        + r'[^\n]*?-->'
    )
    m = pat.search(text)
    if not m:
        # Try multiline match
        pat = re.compile(
            r'<!--\s*→\s*\[(?:IMAGE|FIGURE|DIAGRAM):.*?'
            + re.escape(comment_key)
            + r'.*?-->',
            re.DOTALL,
        )
        m = pat.search(text)
        if not m:
            print(f"!!! NO MATCH: {ch_file} | {comment_key!r}")
            return
    new_md = f"![{alt}](images/{slug}.png)\n*{title}*"
    new_text = text[:m.start()] + new_md + text[m.end():]
    path.write_text(new_text)
    print(f"  [{ch_file}] {comment_key[:40]} → {slug}.png")


def main():
    print("=== generating SVG/PNG ===")
    for slug, svg, *_ in FIGURES:
        write_pair(slug, svg)
    print("\n=== replacing in chapter files ===")
    for slug, _, alt, title, ch_file, comment_key in FIGURES:
        replace_in_chapter(ch_file, comment_key, slug, alt, title)


if __name__ == "__main__":
    main()
