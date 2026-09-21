# Healthcare Analytics Project — Interview & Stakeholder Q&A

## 1. Give me a brief introduction to your project.

**Answer:**
"I developed a healthcare analytics project in Python to analyze patient, visit, admission, billing, laboratory, prescription and workforce data. My goal was to clean and integrate multiple datasets, perform exploratory analysis, identify important KPIs and convert the results into business-friendly insights."

---

## 2. What was the business objective?

**Answer:**
"The objective was to understand healthcare operations from multiple angles: patient demographics, visit patterns, diagnoses, admissions, revenue, laboratory testing, prescriptions and staffing. I wanted to move from raw operational data to information that a stakeholder could use for monitoring and decision-making."

---

## 3. How many datasets did you use?

**Answer:**
"I worked with seven datasets: patients, visits, admissions, doctors, lab tests, prescriptions and staff."

---

## 4. What was the size of the data?

**Answer:**
"The main datasets included 50,000 patients, 180,000 visits, 50,000 admissions, 5,000 doctors, 250,000 lab tests, 220,000 prescriptions and 10,000 staff records."

---

## 5. Which tools did you use?

**Answer:**
"I used Python with Pandas and NumPy for data manipulation and calculations, and Matplotlib and Seaborn for visualization. I used Jupyter Notebook as the development environment."

---

## 6. What was your first step?

**Answer:**
"My first step was data understanding. I loaded each CSV separately and checked shape, columns, data types, missing values, duplicates, unique categorical values and descriptive statistics."

---

## 7. What data-quality problems did you find?

**Answer:**
"I found missing values and inconsistent categorical formatting. For example, the Gender column contained values such as 'Female', 'FEMALE', 'Female ' and similar variations. Visit Type and Diagnosis also contained differences in capitalization and spaces."

---

## 8. How did you solve inconsistent categorical values?

**Answer:**
"I used Pandas string operations such as `.str.strip()` to remove extra spaces and `.str.title()` to standardize capitalization."

Example:

```python
patients["Gender"] = (
    patients["Gender"]
    .str.strip()
    .str.title()
)
```

---

## 9. How did you handle missing values?

**Answer:**
"I first measured the number and percentage of missing values. For fields where a business-readable placeholder was appropriate, I used values such as 'Unknown' or 'Not available'. For numerical fields that needed to remain numeric for analysis, I converted them appropriately and considered the analytical impact before using them."

---

## 10. Why did you use `pd.to_datetime()`?

**Answer:**
"The source dates were stored as strings in day-first format. I converted them to datetime so I could perform time-based analysis such as monthly visits and monthly revenue."

Example:

```python
visits["Visit_Date"] = pd.to_datetime(
    visits["Visit_Date"],
    dayfirst=True
)
```

---

## 11. Why did you create Age_Group?

**Answer:**
"Age is a continuous variable, but age groups make stakeholder reporting easier. I created groups such as 0–18, 19–35, 36–50, 51–65 and 65+ using `pd.cut()`."

---

## 12. Why did you merge datasets?

**Answer:**
"The information was distributed across different tables. For example, visits contained patient and doctor IDs, while patient details were in the patients table and doctor information was in the doctors table. Merging allowed me to analyze these dimensions together."

---

## 13. What keys did you use?

**Answer:**
"I used `Patient_ID` to connect patients with visits, `Doctor_ID` to connect visits with doctors, and `Visit_ID` to connect visit-level information with lab and prescription summaries."

---

## 14. Why did you standardize ID data types before merging?

**Answer:**
"Because join keys need compatible data types. I found that Patient_ID had different types in different DataFrames, so I standardized the IDs before merging to avoid incorrect or missing matches."

---

## 15. Why did you create a lab summary?

**Answer:**
"There can be multiple laboratory tests for one visit. I grouped lab tests by Visit_ID and calculated the number of tests, number of abnormal tests and average result. This converted test-level data into useful visit-level metrics."

---

## 16. How did you calculate laboratory result status?

**Answer:**
"I compared Result_Value with Reference_Low and Reference_High. Values below the lower reference were classified as Low, values above the upper reference as High, and the remaining values as Normal."

---

## 17. What was the total revenue/billing?

**Answer:**
"The total visit billing in the notebook was approximately ₹1.89 billion."

---

## 18. What was the average bill?

**Answer:**
"The average bill was approximately ₹10,515."

---

## 19. What was the average length of stay?

**Answer:**
"The average length of stay was approximately 7.49 days."

---

## 20. Which visit type had the highest total billing?

**Answer:**
"In the analyzed data, Inpatient visits had the highest total billing, followed closely by Emergency, Outpatient and Follow-Up."

---

## 21. Which diagnosis had the highest number of visits?

**Answer:**
"Routine Check had the highest visit count, with 22,912 visits."

---

## 22. What did you learn from the length-of-stay analysis?

**Answer:**
"The average length of stay was about 7.49 days, with values ranging from 0 to 15 days. I also visualized bill amount against length of stay instead of assuming that a longer stay automatically produces higher billing."

---

## 23. Did you find a strong correlation between bill amount and length of stay?

**Answer:**
"The notebook calculated a correlation of approximately -0.0049 between Bill_Amount and Length_of_Stay. That is very close to zero, so the analysis does not show a meaningful linear relationship between those two variables in this dataset."

---

## 24. Why did you use a scatter plot?

**Answer:**
"A scatter plot helps me visually examine the relationship between two numerical variables. I used it for Bill Amount versus Length of Stay."

---

## 25. Why did you use a box plot?

**Answer:**
"A box plot helps identify the distribution, median, spread and potential outliers. I used it for Bill Amount and Length of Stay."

---

## 26. Did you analyze outliers?

**Answer:**
"Yes. I used the IQR method for Bill Amount to identify potential outliers. The notebook identified 4,569 rows as potential bill-amount outliers using the IQR rule."

---

## 27. How many laboratory tests were there?

**Answer:**
"There were 250,000 laboratory test records across nine test types."

---

## 28. What was the abnormal test rate?

**Answer:**
"The notebook reports an abnormal test rate of 22.094%, based on the Abnormal_Flag field."

---

## 29. How many prescriptions were there?

**Answer:**
"There were 220,000 prescription records."

---

## 30. What was the total medication cost?

**Answer:**
"The notebook reports total medication cost of approximately ₹4.018 billion."

---

## 31. What were the admission types?

**Answer:**
"The admission types were Elective, Transfer and Emergency."

---

## 32. What wards did you analyze?

**Answer:**
"I analyzed Private, General, Semi Private, Emergency and ICU wards."

---

## 33. What discharge statuses did you analyze?

**Answer:**
"The dataset included Home, Referred, Transfer and Expired discharge statuses."

---

## 34. What was the biggest technical challenge?

**Answer:**
"One challenge was data consistency across multiple datasets. IDs had to be standardized before joins, categorical values had inconsistent capitalization and spaces, and dates needed conversion before time-series analysis."

---

## 35. What was the most important lesson from the project?

**Answer:**
"I learned that data cleaning is as important as analysis. If categories, IDs and dates are inconsistent, the final KPIs can be misleading. So I focused on data quality before building insights."

---

## 36. If you had more time, what would you improve?

**Answer:**
"I would build a Streamlit dashboard with filters for city, age group, insurance, diagnosis and visit type. I would also add automated data-quality checks, more advanced statistical analysis and role-specific KPI pages for operations and finance."

---

## 37. How would this help a stakeholder?

**Answer:**
"It gives stakeholders a consolidated view of patient volume, visit activity, billing, admissions, diagnostics and prescriptions. Instead of reviewing several raw files, they can focus on KPIs, trends and areas that need further investigation."

---

## 38. What is the difference between an insight and a KPI?

**Answer:**
"A KPI is a measurable performance indicator, such as total visits or average bill. An insight explains what the data is showing and why it may matter. For example, total visits is a KPI, while a change in monthly visit volume is an analytical insight."

---

## 39. What would you present first to a senior stakeholder?

**Answer:**
"I would start with a small KPI section: total patients, visits, admissions, total billing, average bill, average length of stay and laboratory activity. Then I would move to trends, diagnosis patterns and operational breakdowns."

---

## 40. What if the stakeholder asks, 'So what?' after showing a chart?

**Answer:**
"I would connect the chart to a business question. Instead of only saying what the chart contains, I would explain the observed pattern, its possible operational meaning, and what additional analysis would be needed before taking action."

---

# ⭐ 60-Second Project Presentation

"I worked on a healthcare analytics project using Python. I used seven datasets covering patients, visits, admissions, doctors, lab tests, prescriptions and staff.

I started by understanding the data and checking missing values, duplicates, data types and inconsistent categories. I cleaned the data by standardizing text, converting dates, handling missing values and aligning ID types.

Then I integrated the datasets using Patient_ID, Doctor_ID and Visit_ID. After that, I performed exploratory analysis on patient demographics, visit types, diagnoses, admissions, billing, laboratory results, prescriptions and staff.

The project contains 50,000 patients, 180,000 visits, 50,000 admissions and 250,000 lab tests. Total visit billing was about ₹1.89 billion, with an average bill of around ₹10,515 and average length of stay of about 7.49 days.

Finally, I created visualizations for trends, distributions, revenue, diagnoses, laboratory activity and outliers. The main objective was to transform raw healthcare data into clear KPIs and business insights that stakeholders can use for monitoring and further decision-making."

---

# 🎤 If You Get Stuck During Presentation

Use this structure:

**Problem → Data → Cleaning → Analysis → Insight → Business Value**

Example:

"I first identified the business question. Then I understood the relevant datasets. After that I cleaned and standardized the data, performed the analysis, identified the key pattern, and finally explained how that pattern could help a stakeholder."

