# Power BI Dashboard Plan

## Page 1 - Customer Segmentation Overview

### KPI Cards
1. Total Customers
2. Average Annual Income
3. Average Total Spend
4. Average Purchase Frequency
5. Number of Segments

### Charts
- Donut/Bar: Customers by Segment
- Column: Average Total Spend by Segment
- Column: Average Income by Segment
- Scatter: Annual Income vs Total Spend
- Bar: Average Purchase Frequency by Segment

### Slicers
- Segment
- Gender
- City
- Preferred Category

## Page 2 - Customer Behavior

- Spending by Preferred Category
- Online vs Store Purchases
- Recency by Segment
- Discount Usage by Segment
- Age distribution by Segment

## Page 3 - Business Recommendations

Example recommendations:
- High-Value Customers: loyalty rewards and premium offers
- Regular Customers: personalized offers and bundles
- Budget Customers: value packs and discounts
- Occasional Customers: re-engagement campaigns
- Low-Engagement Customers: targeted retention campaigns

## Import
Import `data/customer_segments.csv` into Power BI.

## Suggested calculated measures
```DAX
Total Customers = DISTINCTCOUNT(customer_segments[CustomerID])

Average Spend = AVERAGE(customer_segments[TotalSpend])

Average Income = AVERAGE(customer_segments[AnnualIncome])

Average Purchase Frequency = AVERAGE(customer_segments[PurchaseFrequency])

Segment Count = DISTINCTCOUNT(customer_segments[Segment])
```

## Suggested dashboard title
Retail Customer Segmentation Dashboard
