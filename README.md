# Interactive Commercial Sales Performance Dashboard

## 📊 Project Overview
This repository features an interactive, end-to-end data analytics project built in Microsoft Excel. The project transforms raw, unstructured sales transaction data into a functional, one-page business intelligence dashboard designed to track regional performance, product catalog movement, and multi-year chronological timelines.

## 🗃️ Dataset Profile & Columns
The analysis is driven by a comprehensive transaction database containing the following parameters:
* **JE Code / Store / Region / Country:** Multi-layered geographic identifiers.
* **Date:** Timeline data tracking seasonal transaction flows.
* **Item:** Commercial product catalog tracking appliances (Refrigerators, Air Conditioners, etc.).
* **Salesperson:** Individual agent tracking identifiers.
* **List Price / Actual Price / Discounts (%):** Raw financial pricing and baseline reduction metrics.

## 🧼 Phase 1: Data Cleansing & Quality Control
Before running analytical scripts or formulas, the raw dataset underwent formatting adjustments to ensure structural integrity:
* Removed structural blank rows and duplicate records to ensure absolute metric normalization.
* Fixed corrupted text-based date fields into standardized system-recognized serial date values to support accurate historical data sorting.

## 🧪 Phase 2: Data Enrichment & Formula Metrics
To uncover deeper commercial profitability patterns, custom mathematical logic layers were added directly to the core data schema using specific Excel functions:
* **Discount Amount Calculation:** `=Actual Price * Discounts(%)` to isolate the total monetary value deducted per transaction.
* **Net Revenue Optimization:** `=Actual Price - Discount Amount` to compute true net financial income generated.
* **Dynamic Time Bucket Extraction:** Real Date structural parameters aggregated into chronological intervals for long-term trend analysis.

## 📊 Phase 3: Dashboard Architecture & Interactive Visualizations
The visual layer separates the raw database from actionable insights by deploying independent Pivot Tables and matching chart archetypes:
1. **Product Volume Distribution:** Utilizes an optimized Column/Bar layout to cleanly rank inventory catalog revenue.
2. **Chronological Revenue Trendline:** A dedicated Line Chart tracking month-over-month and year-over-year performance curves cleanly.
3. **Dynamic Control Interface (Slicers):** Implemented interactive **Region**, **Store**, and **Item** Slicer panels connected globally to all Pivot Tables via structural report connections.

