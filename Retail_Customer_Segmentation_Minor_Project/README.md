# Retail Customer Segmentation Using K-Means

## Minor Project

### Objective
Segment retail customers into meaningful groups based on purchasing behavior using K-Means clustering, PCA, and visualization.

### Dataset
`data/retail_customer_data.csv`

The dataset contains 600 synthetic customer records.

### Main Features
- AnnualIncome
- PurchaseFrequency
- AvgOrderValue
- TotalSpend
- RecencyDays
- DiscountUsagePct

### Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Power BI

### Workflow
1. Load dataset
2. Clean and inspect data
3. Perform EDA
4. Select customer behavior features
5. Standardize data
6. Determine suitable K using silhouette score
7. Apply K-Means
8. Use PCA for 2D visualization
9. Profile customer segments
10. Build Power BI dashboard
11. Present business recommendations

### Generated Files
- `data/retail_customer_data.csv` - original project dataset
- `data/customer_segments.csv` - clustering output
- `data/cluster_summary.csv` - segment-level summary
- `python/customer_segmentation.py` - complete Python starter script
- `python/requirements.txt` - required Python packages
- `visualizations/` - ready reference charts
- `report/minor_project_report.docx` - report draft
- `presentation/minor_project_presentation.pptx` - PPT draft
- `powerbi/powerbi_dashboard_plan.md` - dashboard design

### Current Model Result
Best K by silhouette score: 2
Best silhouette score: 0.5943

### Important
The dataset is synthetic and created for academic/project demonstration. If your faculty requires a public real-world dataset, replace the CSV while keeping the same workflow.
