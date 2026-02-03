---

# Innomatics Data Science Internship Tasks

This repository contains all my **Data Science internship assignments** completed during training at **Innomatics Research Labs**.  
The tasks are organized in a structured manner, covering Python programming, Exploratory Data Analysis (EDA), and a deployment project under **MLOps**.

---

## 📁 Project Structure

```
Innomatics-Data-Science-Tasks/
│
├── Task-1-Basic-Python/
│   ├── Problem_1.py
│   ├── Problem_2.py
│   ├── Problem_3.py
│   ├── Problem_4.py
│   ├── Problem_5.py
│   ├── Problem_6.py
│   └── Problem_7.py
│
├── Task-2-Advanced-Python/
│   ├── LeetCode_1480_RunningSum.py
│   ├── LeetCode_1470_ShuffleArray.py
│   └── LeetCode_1431_KidsWithCandies.py
│
├── Task-3-EDA-Basics/
│   └── EDA_Task_1.ipynb
│
├── Task-4-EDA-Advanced/
│   └── EDA_Task_2.ipynb
│
├── MLOps-Flipkart-Sentiment-Analysis/
│   ├── app.py
│   ├── requirements.txt
│   ├── svm_sentiment_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── flipkart-key.pem
│
└── README.md
```

---

## 📚 List of Tasks

### Task 1: Basic Python
Covers core Python fundamentals:
- Arithmetic operators  
- Python division  
- Print function  
- Loops  
- Leap year logic  
- Conditional statements  
- Input and output handling  

---

### Task 2: Advanced Python (LeetCode)
Algorithmic problem-solving using Python:
- Running Sum of 1D Array (1480)  
- Shuffle the Array (1470)  
- Kids With the Greatest Number of Candies (1431)  

---

### Task 3: Exploratory Data Analysis (EDA – Basics)
- Dataset loading and inspection  
- Understanding data types and structure  
- Handling missing values  
- Basic statistical analysis  
- Initial data insights  

---

### Task 4: Exploratory Data Analysis (EDA – Advanced)
- Data cleaning and preprocessing  
- Univariate and bivariate analysis  
- Correlation analysis  
- Data visualization  
- Insight extraction and conclusions  

---

### MLOps – Sentiment Analysis of Real-time Flipkart Product Reviews
This project demonstrates **sentiment analysis on Flipkart product reviews** using a **Support Vector Machine (SVM)** model with **TF-IDF vectorization**.  
The model is deployed using **Streamlit** and hosted on **AWS EC2**, showcasing practical **MLOps deployment skills**.

**Files Added**
- `app.py` → Streamlit application script  
- `requirements.txt` → Python dependencies  
- `svm_sentiment_model.pkl` → Trained SVM model  
- `tfidf_vectorizer.pkl` → TF-IDF vectorizer  
- `flipkart-key.pem` → AWS EC2 key (for server access, not required to run locally)  

**Technologies Used**
- Python (scikit-learn, pandas, numpy, nltk, joblib)  
- Streamlit (web app framework)  
- AWS EC2 (cloud deployment)  

**How to Run Locally**
```bash
pip install -r requirements.txt
streamlit run app.py
```
Open the link shown in terminal (usually `http://localhost:8501`).

**Live Deployment**
The app is hosted on AWS EC2 and accessible at:  
[http://13.235.75.228:8502](http://13.235.75.228:8502)

---

## 🧠 Skills Demonstrated
- Python programming  
- Loops and conditionals  
- Functions and modular coding  
- Algorithmic thinking  
- Problem solving  
- Exploratory Data Analysis (EDA)  
- Data cleaning and preprocessing  
- Statistical analysis  
- Data visualization  
- Model training and evaluation  
- Cloud deployment (AWS EC2 + Streamlit)  
- MLOps practices (real-time deployment, reproducibility)  
- Writing clean and readable code  

---

## 📌 Guidelines Followed
- Organized and consistent folder structure  
- All code written from scratch (no plagiarism)  
- Clean and readable code and notebooks  
- Tested in local Python environment, Google Colab, and AWS EC2  
- Followed Innomatics Research Labs task instructions  

---

## ▶️ How to Run the Code

### Run Python Files
```bash
python filename.py
```

### Run Jupyter Notebooks
Open `.ipynb` files using:
- Google Colab  
- Jupyter Notebook  
- VS Code  

### Run Streamlit App
```bash
streamlit run app.py
```

---
