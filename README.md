# VaxTrack India: COVID-19 Vaccination Analytics Dashboard

An exploratory data analysis (EDA) and interactive dashboard project analyzing the progression, statewise distribution, and gender demographics of the COVID-19 vaccination drive in India.

This project is designed to be **sweet, simple, and self-contained**, making it extremely easy to read, review, and explain in technical interviews.

---

## 📂 Project Directory Structure

```
covid_vaccine_analysis/
├── Data/
│   └── covid_vaccine_statewise.csv      # Source vaccination dataset
├── analyze_vaccination.py                # Python/Pandas analysis script (~45 lines)
├── index.html                            # Self-contained web dashboard (HTML/CSS/Chart.js)
└── README.md                             # Project documentation
```

---

## 📊 Problem Statements Addressed

The project performs analytics to answer the following requirements:

* **a. Describe the dataset**: Shape, columns list, and basic description metrics (mean, min, max, count).
* **b. First Dose Statewise**: Regional progression showing the total first doses administered across individual states and UTs.
* **c. Second Dose Statewise**: Regional progression showing the total second doses administered (fully vaccinated individuals) statewise.
* **d & e. Gender Breakdown**: Total national counts and percentage splits of Males and Females vaccinated.

---

## 🛠️ Technology Stack

* **Data Processing**: Python 3 & Pandas
* **Frontend Interface**: Semantic HTML5 & Vanilla CSS3
* **Data Visualization**: Chart.js (via CDN for dynamic bar and donut charts)
* **Icons**: FontAwesome

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have Python installed and the `pandas` library. If you don't have Pandas, install it via:
```bash
pip install pandas
```

### Step 1: Run the Python Analysis
This script processes the CSV dataset and prints the results directly to your console:
```bash
python analyze_vaccination.py
```

### Step 2: Open the Dashboard
Since the frontend is completely self-contained in a single HTML file, you can view the visual dashboard in two ways:

#### Option A: Direct Open (Simplest)
Simply navigate to the project directory and **double-click the `index.html` file**. It will open instantly in your web browser.

#### Option B: Local Web Server
If you prefer to serve the files through a local server:
1. Start the Python built-in server from the project directory:
   ```bash
   python -m http.server 8000
   ```
2. Open your browser and navigate to: **[http://localhost:8000](http://localhost:8000)**
