"""
Small data-engineering style demo for Git training

Run:
    python sales_pipeline_demo.py
"""

from collections import defaultdict

ENVIRONMENT = "dev"
REPORT_TITLE = "Sales Pipeline Demo DD"


def extract_raw_orders():
    return [
        {"order_id": 1001, "customer": "Acme", "country": "gr", "amount": 120.50, "status": "paid"},
        {"order_id": 1002, "customer": "Beta", "country": "gr", "amount": 80.00, "status": "paid"},
        {"order_id": 1003, "customer": "Acme", "country": "de", "amount": -15.00, "status": "paid"},
        {"order_id": 1004, "customer": "Delta", "country": "gr", "amount": 210.00, "status": "cancelled"},
        {"order_id": 1005, "customer": "Beta", "country": "de", "amount": 95.25, "status": "paid"},
        {"order_id": 1006, "customer": "Gamma", "country": "gr", "amount": 150.00, "status": "paid"},
    ]


def transform_orders(raw_orders):
    cleaned_orders = []

    for order in raw_orders:
        if order["status"] != "paid":
            continue

        if order["amount"] <= 0:
            continue

        cleaned_order = {
            "order_id": order["order_id"],
            "customer": order["customer"].strip().title(),
            "country": order["country"].strip().upper(),
            "amount": round(order["amount"], 2),
        }
        cleaned_orders.append(cleaned_order)

    return cleaned_orders


def aggregate_sales_by_country(cleaned_orders):
    totals = defaultdict(float)

    for order in cleaned_orders:
        totals[order["country"]] += order["amount"]

    return dict(sorted(totals.items()))


def print_report(country_totals):
    print(f"\n{REPORT_TITLE}")
    print(f"Environment: {ENVIRONMENT}")
    print("-" * 30)

    grand_total = 0.0
    for country, total in country_totals.items():
        print(f"{country}: {total:.2f}")
        grand_total += total

    print("-" * 30)
    print(f"Grand total: {grand_total:.2f}")


def main():
    raw_orders = extract_raw_orders()
    cleaned_orders = transform_orders(raw_orders)
    country_totals = aggregate_sales_by_country(cleaned_orders)
    print_report(country_totals)


if __name__ == "__main__":
    main()