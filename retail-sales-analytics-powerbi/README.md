# Retail Sales Analytics – Power BI

End-to-end **Power BI** retail analytics solution: data model, KPIs, six analytical report pages, and interactive slicers for sales, customers, products, stores, inventory, and payments.

## Business questions answered

- Revenue, orders, customers, and quantity sold
- Top products, categories, and sales trends (daily and monthly)
- Store inventory and stock by location
- Payment methods and success / pending / failed status
- Customer, state, and city purchase behavior

## Data model

Tables include `fact_sales`, `daily_sales`, `monthly_sales`, `customer_sales_summary`, `product_performance`, `store_performance`, and `payment_analysis`.

## Report pages

1. **Executive Overview** — KPI cards, daily/monthly trends, category and date-range slicers  
2. **Sales Analysis** — Top products and category sales (Top-N, sorting)  
3. **Store & Payment Analysis** — Inventory vs stock; payment method and status  
4. **Customer Analysis** — Purchases by customer, state, and city  
5. **Product Analysis** — Sales, quantity, and orders by product/category  
6. **Payment Analysis** — Amount and count by method and status  

## Power BI techniques

KPI/card visuals, bar/column/line/donut charts, slicers, cross-filtering, Distinct Count, calculated columns (e.g. `MonthYear` sorted by `SalesMonth`), date-range filtering, and visual-level Top-N filters.

## Documentation

Full walkthrough: [Retail_Sales_Analytics_Power_BI_Project_Documentation.docx](./Retail_Sales_Analytics_Power_BI_Project_Documentation.docx)

## Deployment

Final PBIX can be published to **Power BI Service** for sharing, refresh, and portfolio demos.

## Use in proposals

> "I built a six-page Power BI retail dashboard with executive KPIs, time-series trends, product/store/customer/payment drill-down, and interactive category and date filters."
