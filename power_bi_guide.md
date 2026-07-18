# Phase 5: Power BI Dashboard Step-by-Step Guide

This guide will walk you through creating the complete Data Analysis Dashboard in Power BI using your `sales_performance.csv` file, matching your requested KPIs, Charts, and Slicers.

## Step 1: Load Data into Power BI
1. Open **Power BI Desktop**.
2. Click on **Get Data** (or **Excel / Text/CSV** from the Home ribbon).
3. Select your `sales_performance.csv` file and click **Open**.
4. A preview window will appear. Click **Load**. (If your data needs cleaning, you would click **Transform Data**, but we'll assume it's ready for now).

---

## Step 2: Create KPIs (Cards)
We will create 5 KPIs using the **Card** visual.

1. **Total Sales**:
   * Click the **Card** icon in the **Visualizations** pane.
   * Drag the `Sales` field from the **Data** pane into the **Fields** section of the visual. Power BI will automatically sum it.
2. **Total Profit**:
   * Create a new **Card** visual.
   * Drag the `Profit` field into the **Fields** section.
3. **Total Orders**:
   * Create a new **Card**.
   * Drag `Order_ID` (or `Order Date`) into the **Fields** section. Click the dropdown arrow on the field in the Visualizations pane and select **Count (Distinct)**.
4. **Average Order Value (AOV)**:
   * First, let's create a Measure. Right-click your table name in the Data pane and select **New Measure**.
   * In the formula bar, type: `AOV = SUM(superstore[Sales]) / DISTINCTCOUNT(superstore[Order_ID])` (Adjust table name if it's not 'superstore').
   * Add a new **Card** and drag this `AOV` measure into it.
5. **Total Customers**:
   * Create a new **Card**.
   * Drag `Customer_Name` or `Customer_ID` into the **Fields** section, click the dropdown, and select **Count (Distinct)**.

*Tip: Arrange these 5 cards in a neat row at the top of your canvas.*

---

## Step 3: Create Charts
Now, let's build the visual charts.

1. **Monthly Sales Trend (Line Chart)**
   * Select the **Line Chart** visual.
   * **X-axis**: Drag `Order_Date` (make sure to use the Date Hierarchy and select Year and Month, or just Month).
   * **Y-axis**: Drag `Sales`.

2. **Sales by Category (Bar Chart)**
   * Select the **Clustered Column Chart** or **Clustered Bar Chart**.
   * **X-axis** (or Y-axis for horizontal): Drag `Category`.
   * **Y-axis** (or X-axis): Drag `Sales`.

3. **Sales by Region (Map/Bar Chart)**
   * Select the **Map** visual (ensure Map visuals are enabled in your Power BI Options > Security settings).
   * **Location**: Drag `Region`.
   * **Bubble size**: Drag `Sales`.
   * *(Alternative)*: Use a Clustered Bar chart with Region on Axis and Sales on Values.

4. **Profit by State (Filled Map or Bar Chart)**
   * Select the **Filled Map** visual.
   * **Location**: Drag `State`.
   * **Tooltips/Color saturation**: Drag `Profit`.

5. **Top 10 Customers (Bar Chart)**
   * Select **Clustered Bar Chart**.
   * **Y-axis**: Drag `Customer_Name`.
   * **X-axis**: Drag `Sales`.
   * **Filter to Top 10**: In the **Filters** pane on the right, under "Filter on this visual", expand `Customer_Name`, change Filter type to **Top N**, set Show items to **Top 10**, drag `Sales` into the "By value" box, and click **Apply filter**.

6. **Sales by Segment (Pie/Donut Chart)**
   * Select **Donut Chart**.
   * **Legend**: Drag `Segment`.
   * **Values**: Drag `Sales`.

7. **Top 10 Products (Bar Chart)**
   * Select **Clustered Bar Chart**.
   * **Y-axis**: Drag `Product_Name`.
   * **X-axis**: Drag `Sales` (or `Profit`).
   * Apply a **Top N (10)** filter on `Product_Name` using `Sales` as the value, exactly like the Top 10 Customers step.

8. **Loss-Making Products (Table)**
   * Select the **Table** visual.
   * Add `Product_Name` and `Profit` to the **Columns**.
   * In the **Filters** pane for this visual, expand `Profit`, choose **Advanced filtering**, select **is less than**, type `0`, and click **Apply filter**.

9. **Discount vs Profit (Scatter Plot)**
   * Select **Scatter Chart**.
   * **Values/Details**: Drag `Product_Name` or `Order_ID` (this defines the dots).
   * **X-axis**: Drag `Discount`.
   * **Y-axis**: Drag `Profit`.

---

## Step 4: Add Filters (Slicers)
Slicers allow users to interact with and filter the entire dashboard.

1. Click the empty canvas, then click the **Slicer** visual.
2. Drag `Order_Date` (select Year from hierarchy) into the Field.
3. Repeat steps 1 & 2 to create separate slicers for:
   * `Region`
   * `Category`
   * `Segment`
   * `State`

*Tip: You can format slicers as dropdowns to save space. Click the Slicer, go to the Format visual pane (the paintbrush icon), go to Slicer settings, and change Style to Dropdown.*

## Final Polish
* Use the **Format visual** pane to change colors, add data labels, and add descriptive titles to all your charts to make it look professional, similar to the "SALSE DATA ANALYSIS" screenshot you shared!
