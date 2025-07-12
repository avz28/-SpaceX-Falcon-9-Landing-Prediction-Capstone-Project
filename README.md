# -SpaceX-Falcon-9-Landing-Prediction-Capstone-Project
This repository contains my data science capstone project completed as part of the IBM Data Science specialization on Coursera. The project focuses on collecting, cleaning, exploring, and modeling SpaceX Falcon 9 launch data to predict the success of first-stage landings, and building an interactive dashboard to visualize insights.
📂 Project Structure
File / Notebook	Description
jupyter-labs-spacex-data-collection-api.ipynb	Data collection: Extracted launch data from the SpaceX REST API.
jupyter-labs-webscraping (2).ipynb	Collected additional data by scraping Wikipedia for launch payload and booster information.
jupyter-labs-eda-sql-coursera_sqllite (1).ipynb	Performed SQL-based data exploration and analysis on the collected dataset.
edadataviz (1).ipynb	Data visualization and exploratory data analysis (EDA) using matplotlib and seaborn.
lab_jupyter_launch_site_location (1).ipynb	Visualized launch site locations on an interactive map using Folium.
SpaceX_Machine Learning Prediction_Part_5 (2).ipynb	Built and evaluated machine learning models to predict landing success.
Dash/Plotly dashboard notebook	Developed an interactive dashboard to visualize success launches by site and payload correlation plots (with screenshot included).

📊 Goal
Predict whether the first stage of a SpaceX Falcon 9 rocket will successfully land, and build interactive visualizations to explore launch data.

⚙️ Tools & Libraries
Python

Jupyter Notebook

pandas, NumPy

matplotlib, seaborn, Folium

scikit-learn

Dash & Plotly

SQLite

Web scraping (BeautifulSoup, requests)

REST API (SpaceX)

📈 Key Steps
✅ Data Collection:

Used SpaceX API and web scraping to collect historical launch data.

✅ Data Cleaning & Exploration:

Handled missing values and inconsistent formats.

Explored relationships between payload, orbit type, booster version, and landing outcome.

✅ Visualization:

Created bar plots, scatter plots, heatmaps, and an interactive dashboard with Dash & Plotly.

✅ Machine Learning:

Tested classifiers like Decision Tree, SVM, and Logistic Regression.

Optimized hyperparameters and evaluated model accuracy.

📊 Dashboard Example
Interactive dashboard built with Dash & Plotly:


📌 How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/spacex-landing-prediction.git
cd spacex-landing-prediction
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Open notebooks in Jupyter:

bash
Copy
Edit
jupyter notebook
📄 Dataset
Publicly available data from:

SpaceX API

Wikipedia Falcon 9 launches page

✏️ Author
Avani S Jayan

IBM Data Science Professional Certificate (Coursera)











