{% docs pricing_summary_report %}

# 📊 TPC-H Query 1: Pricing Summary Report
## 🧾 Summary

This model implements the **TPC-H Query 1**, also known as the **"Pricing Summary Report Query"**, which calculates aggregate metrics for line items that have been shipped before a specific reference date.

It summarizes revenue, discount, tax, and quantity metrics by `return_flag` and `line_status`, providing insights into the pricing and shipping status of line items. The query is often used to benchmark the performance of SQL engines and to demonstrate best practices in analytics engineering with dbt.

## 🛠️ Query Logic

The query:
- Filters line items that were shipped **on or before 90 days prior to December 1, 1998**.
- Groups the data by **return flag** and **line status**.
- Calculates:
  - Total quantity and price
  - Discounted price
  - Final charge (after tax)
  - Averages per group
  - Total count of line items

## 📥 Source

This model uses data from the **`stg_tpch__lineitem`** staging model, which cleans and prepares the `lineitem` table from the raw TPCH dataset.

## 🧮 Metrics Calculated

| Metric | Description |
|--------|-------------|
| `sum_qty` | Total quantity of items |
| `sum_base_price` | Total extended price before discounts |
| `sum_disc_price` | Total price after discounts |
| `sum_charge` | Final charge after discount and tax |
| `avg_qty` | Average quantity per line |
| `avg_price` | Average base price per line |
| `avg_disc` | Average discount per line |
| `count_order` | Number of line items in each group |

## 📅 Filter Condition

The `WHERE` clause ensures that only line items shipped **before September 2, 1998** are included:

```sql
ship_date <= dateadd(day, -90, date '1998-12-01')
```

This condition helps simulate an aged dataset for a business reporting snapshot.

## 📦 Grouping Columns

- **`return_flag`**: Indicator of return status (e.g., 'R' for returned).
- **`line_status`**: Status of the line item (e.g., 'F' for filled, 'O' for open).

## 📌 Use Cases

This model is useful for:
- Building a pricing or revenue summary dashboard.
- Benchmarking query performance across data engines.
- Validating the quality and completeness of `lineitem` data in your pipeline.
- Teaching or learning SQL transformations with realistic, structured datasets.

{% enddocs %}
