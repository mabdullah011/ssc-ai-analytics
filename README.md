# SSC AI Analytics – AI-powered Study Intelligence for Bangladesh

> Data-driven insights, predictive analytics, and business intelligence for SSC (Class 9–10) students, teachers, and EdTech platforms in Bangladesh.

# Problem & Why It Matters

- Learning gaps are invisible**: Teachers and parents lack data to see which topics students struggle with.
- One-size-fits-all study plans**: Most SSC prep materials ignore individual performance patterns.
- EdTech platforms lack predictive BI**: Few tools forecast exam performance or recommend personalized study paths using AI.

This project turns raw study and mock-exam data into **actionable insights**—helping students study smarter, teachers teach better, and platforms build smarter products.

# Target Users  👥 

- SSC students (Class 9–10) in Bangladesh
- EdTech startups & online coaching platforms
- Teachers & school administrators
- Parents seeking data-driven study guidance

# Key Features✨

- Performance Prediction**: Forecast SSC exam scores using XGBoost + feature engineering.
- Topic-wise Weakness Detection**: Identify weak chapters using rule-based + ML hybrid approach.
- Personalized Study Plan**: Generate weekly study schedules based on predicted gaps.
- Interactive Dashboard**: Power BI / Streamlit dashboard for students & teachers.
- Explainable AI: SHAP-based feature importance for transparent recommendations.

# 📊 Data & Methodology

- Data sources :  
  - Mock exam results (collected via partner EdTech platforms)
  - Public SSC question banks (open datasets)
  - Simulated student activity logs (for prototyping)
- Preprocessing : 
  - Missing value imputation, outlier handling
  - Feature engineering: study_time, attempt_rate, topic_difficulty, past_performance
- Models used: 
  - XGBoost Regressor (score prediction)
  - Logistic Regression (pass/fail classification)
  - SHAP for explainability
- Evaluation metrics : 
  - RMSE, MAE (regression)
  - Accuracy, F1-score, AUC (classification)

## 📁 Repository Structure
.
├── data/  Raw & processed datasets (or links to external storage)
├── notebooks/ EDA, modeling, and experimentation notebooks
├── src/ Modular Python scripts (clean architecture)
│ ├── _init_.py
│ ├── data_loader.py
│ ├── features.py
│ ├── models.py
│ └── utils.py
├── models/ # Trained model artifacts (.pkl, .h5)
├── dashboard/ # Streamlit / Power BI dashboard files
│ └── app.py
├── tests/ # Unit & integration tests
│ └── test_features.py
├── requirements.txt # Python dependencies
├── README.md # This file
├── LICENSE # MIT License
└── .gitignore # Python gitignore


# 🛠️ Installation & Usage

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ssc-ai-analytics.git
cd ssc-ai-analytics

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run dashboard (Streamlit)
streamlit run dashboard/app.py

# Or run the main analysis script
python src/main.py
```

# 📈 Results & Visuals

- Score Prediction : RMSE ≈ 4.2 (on held-out mock exam data)
- Pass/Fail Classification : Accuracy ≈ 87%, AUC ≈ 0.91
- Key Insights :
  - Study consistency > total hours for score improvement
  - Topic-wise attempt rate is the strongest predictor of weak areas

> 📊 Dashboard screenshots and SHAP plots will be added soon.

# 🌍 Business & Startup Potential

- Market gap: Bangladesh EdTech lacks predictive BI for SSC prep; most tools are content-only.
- Revenue model:
  - B2B SaaS for coaching platforms (per-student/month)
  - B2C freemium app (basic insights free, premium plans for advanced analytics)
- Scalability :
  - Cloud deployment (AWS/Azure/GCP)
  - API for integration with existing LMS/EdTech platforms
  - Multi-language support (Bangla + English)

# 🤝 Contributing

Contributions welcome! Please open an issue or PR for:
- New feature suggestions
- Bug fixes
- Dataset contributions
- Dashboard improvements

# 📄 License

This project is licensed under the [MIT License](LICENSE).

# 📬 Contact & Portfolio

- LinkedIn : https://www.linkedin.com/in/mohammad-abdullah2109011?utm_source=share_via&utm_content=profile&utm_medium=member_android
- Email : Abdullah.CUET.11@proton.me


---

> 💡 Try it out: Clone the repo, run the dashboard, and star ⭐ if you find it useful for SSC prep!
