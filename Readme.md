# Titanic Data Cleaning and Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on Data Cleaning and Exploratory Data Analysis (EDA) using the Titanic Dataset. The objective is to preprocess the data, identify patterns, handle missing values, detect outliers, and generate meaningful visualizations to gain insights into passenger survival trends.

---

## 🎯 Objectives

* Understand the structure of the dataset
* Handle missing values effectively
* Check for duplicate records
* Detect outliers using visualization techniques
* Perform Exploratory Data Analysis (EDA)
* Generate insights from data visualizations

---

## 📂 Dataset Information

The dataset contains passenger information from the Titanic disaster, including:

* Passenger ID
* Survival Status
* Passenger Class
* Name
* Gender
* Age
* Number of Siblings/Spouses
* Number of Parents/Children
* Ticket Information
* Fare
* Cabin
* Embarked Port

Dataset Source: Kaggle Titanic Dataset

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* VS Code

---

## 🧹 Data Cleaning Process

### Missing Value Treatment

| Column   | Missing Values | Method Used             |
| -------- | -------------- | ----------------------- |
| Age      | 177            | Median Imputation       |
| Cabin    | 687            | Replaced with "Unknown" |
| Embarked | 2              | Mode Imputation         |

### Duplicate Records

* Checked for duplicate entries
* No duplicate records found

### Outlier Detection

* Box Plot used for identifying outliers
* Fare column showed several extreme values

---

## 📊 Exploratory Data Analysis

The following visualizations were created:

### 1. Survival Count

* Comparison of survived vs non-survived passengers

### 2. Gender vs Survival

* Analysis of survival based on gender

### 3. Passenger Class vs Survival

* Survival trends across different passenger classes

### 4. Age Distribution

* Distribution of passenger ages

### 5. Correlation Heatmap

* Relationship between numerical features

### 6. Fare Box Plot

* Identification of fare outliers

---

## 📈 Key Insights

* Female passengers had a significantly higher survival rate than males.
* First-class passengers had better survival chances.
* Most passengers were between 20 and 40 years old.
* Fare values contained multiple outliers.
* Passenger class and fare showed relationships with survival outcomes.

---

## 📁 Project Structure

```text
Titanic-Data-Cleaning-and-Visualization
│
├── analysis.py
├── README.md
├── train.csv
images
├── survival_count.png
├── gender_vs_survival.png
├── class_vs_survival.png
├── age_distribution.png
└── heatmap.png
```

---

## 🚀 How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/svasidhar/Titanic-Data-Cleaning-and-Visualization.git
```

2. Navigate to the project folder

```bash
cd Titanic-Data-Cleaning-and-Visualization
```

3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

4. Run the analysis

```bash
python analysis.py
```

---

## 👨‍💻 Author

**Somanaboina Vasidhar**

GitHub: https://github.com/svasidhar

---

## ⭐ Project Status

✅ Completed

This project was completed as part of a Machine Learning Internship task focusing on Data Cleaning and Visualization using Python.
