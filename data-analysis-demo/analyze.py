"""
Sales Data Analysis — Portfolio Demo
Run: python analyze.py
Output: output/report.txt, output/summary_chart.png
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "sales.csv"
OUTPUT_DIR = Path(__file__).parent / "output"


def load_sales(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def analyze(rows: list[dict]) -> dict:
    total_revenue = 0.0
    by_region: dict[str, float] = defaultdict(float)
    by_product: dict[str, float] = defaultdict(float)
    by_month: dict[str, float] = defaultdict(float)

    for row in rows:
        amount = float(row["amount"])
        total_revenue += amount
        by_region[row["region"]] += amount
        by_product[row["product"]] += amount
        by_month[row["month"]] += amount

    top_region = max(by_region, key=by_region.get)
    top_product = max(by_product, key=by_product.get)
    avg_order = total_revenue / len(rows) if rows else 0

    return {
        "total_orders": len(rows),
        "total_revenue": round(total_revenue, 2),
        "avg_order_value": round(avg_order, 2),
        "top_region": top_region,
        "top_region_revenue": round(by_region[top_region], 2),
        "top_product": top_product,
        "top_product_revenue": round(by_product[top_product], 2),
        "by_region": dict(sorted(by_region.items(), key=lambda x: -x[1])),
        "by_product": dict(sorted(by_product.items(), key=lambda x: -x[1])),
        "by_month": dict(sorted(by_month.items())),
    }


def write_report(stats: dict, path: Path) -> None:
    lines = [
        "SALES ANALYSIS REPORT",
        "=" * 40,
        f"Total orders:      {stats['total_orders']}",
        f"Total revenue:     ${stats['total_revenue']:,.2f}",
        f"Avg order value:   ${stats['avg_order_value']:,.2f}",
        f"Top region:        {stats['top_region']} (${stats['top_region_revenue']:,.2f})",
        f"Top product:       {stats['top_product']} (${stats['top_product_revenue']:,.2f})",
        "",
        "Revenue by region:",
    ]
    for region, val in stats["by_region"].items():
        lines.append(f"  {region:12} ${val:,.2f}")

    lines.extend(["", "Revenue by month:"])
    for month, val in stats["by_month"].items():
        lines.append(f"  {month:12} ${val:,.2f}")

    path.write_text("\n".join(lines), encoding="utf-8")


def write_chart(stats: dict, path: Path) -> bool:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        regions = list(stats["by_region"].keys())
        values = list(stats["by_region"].values())

        plt.figure(figsize=(8, 4))
        plt.bar(regions, values, color=["#2563eb", "#16a34a", "#dc2626", "#ca8a04"])
        plt.title("Revenue by Region")
        plt.ylabel("Revenue ($)")
        plt.tight_layout()
        plt.savefig(path, dpi=120)
        plt.close()
        return True
    except Exception:
        return False


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    rows = load_sales(DATA_FILE)
    stats = analyze(rows)
    write_report(stats, OUTPUT_DIR / "report.txt")
    chart_ok = write_chart(stats, OUTPUT_DIR / "summary_chart.png")
    print(stats)
    print(f"\nReport saved: {OUTPUT_DIR / 'report.txt'}")
    if chart_ok:
        print(f"Chart saved: {OUTPUT_DIR / 'summary_chart.png'}")
    else:
        print("Chart skipped (matplotlib not available on this PC — report still works)")


if __name__ == "__main__":
    main()
