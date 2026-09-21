🚦 Smart City Traffic Forecasting

A machine learning project for forecasting traffic patterns across four smart-city junctions using historical traffic data, time-based features, and lag-based features.

📌 Project Overview

Traffic congestion is a major challenge in smart-city planning. Accurate traffic forecasting can help authorities understand traffic patterns, prepare for peak periods, and support traffic management and infrastructure planning.

This project develops a machine learning-based traffic forecasting system for four junctions. The model learns from historical hourly traffic observations and generates future traffic forecasts.

The project also includes an interactive Streamlit dashboard for exploring the predicted traffic patterns.

🎯 Objectives
Analyze historical traffic patterns across four junctions.
Identify hourly, weekday/weekend, and calendar-based traffic patterns.
Create time-series features such as lagged traffic values.
Train and evaluate machine learning models.
Generate future traffic forecasts.
Build an interactive traffic forecasting dashboard.
Deploy the application for online access.
📊 Dataset

The dataset contains hourly traffic observations with the following columns:

Column	Description
DateTime	Date and time of the traffic observation
Junction	Junction identifier
Vehicles	Number of vehicles observed
ID	Unique observation identifier
Dataset Period

Training data:

November 2015 – June 2017

Forecast period:

July 1, 2017 – October 31, 2017

The test dataset contains 11,808 observations across four junctions.

🔍 Exploratory Data Analysis

The project analyzes:

Traffic variation over time
Average hourly traffic
Weekday vs weekend traffic
Junction-wise traffic patterns
Unusual traffic spikes
Historical traffic trends

Example analysis includes identifying the average traffic level for each hour of the day and comparing weekday and weekend patterns.

⚙️ Feature Engineering

Several features were created to help the model understand traffic behavior.

Calendar Features
Hour
DayOfWeek
IsWeekend
Month
Day
IsMonthStart
IsMonthEnd
Lag Features

Historical traffic values were used as predictors:

Lag_1 → traffic one hour earlier
Lag_2 → traffic two hours earlier
Lag_3 → traffic three hours earlier
Lag_24 → traffic 24 hours earlier
Lag_48 → traffic 48 hours earlier
Lag_168 → traffic 168 hours earlier (one week)

Lag features were calculated separately for each junction to prevent information from one junction being used as another junction's history.

🤖 Machine Learning Models

The project experimented with:

Baseline

A previous-day traffic value (Lag_24) was used as a baseline.

Random Forest Regressor

Random Forest was trained using historical traffic and calendar features.

HistGradientBoostingRegressor

A histogram-based gradient boosting regression model was also trained.

The final model uses:

HistGradientBoostingRegressor

with:

max_iter = 300
learning_rate = 0.08
max_leaf_nodes = 31
📈 Model Evaluation

A chronological validation strategy was used because this is a time-series forecasting problem.

Randomly splitting the data was avoided so that future observations would not be used to predict the past.

One-Step Validation
Model / Approach	MAE	RMSE
Previous-day baseline	6.78	11.91
Random Forest	2.87	5.04
HistGradientBoosting	2.74	4.82
Recursive Validation

For realistic multi-step forecasting, predictions were fed back into the model as future lag values.

The recursive validation results were:

MAE  : 5.60
RMSE : 8.75

This demonstrates the difference between one-step prediction using known historical values and longer recursive forecasting where previous predictions become inputs.

🚦 Future Traffic Forecasting

The final model was trained using 47,448 usable historical observations.

It was then used to recursively forecast traffic for:

July 1, 2017 – October 31, 2017

A total of:

11,808 traffic predictions

were generated.

The predictions are stored in:

smart_city_traffic_predictions.csv
🌐 Interactive Dashboard

The project includes a Streamlit dashboard where users can:

Select a junction
Select a forecast date
View average predicted traffic
View peak predicted traffic
Identify the peak traffic hour
View traffic status
Explore hourly traffic forecasts
View the hourly prediction table
Dashboard

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Joblib
Streamlit
Google Colab
GitHub
📁 Project Structure
smart-city-traffic-forecasting/
│
├── app.py
├── requirements.txt
├── final_traffic_forecasting_model.pkl
└── smart_city_traffic_predictions.csv
▶️ Run the Project Locally
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/smart-city-traffic-forecasting.git
2. Navigate into the project
cd smart-city-traffic-forecasting
3. Install dependencies
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run app.py

The application will open in your browser.

🌐 Live Demo

Live Application:
👉https://smart-city-traffic-forecasting-fvshgxgwpovsqbr55hwy9v.streamlit.app/ 


📌 Key Results
Analyzed hourly traffic patterns across 4 junctions.
Created multiple time-based and lag-based features.
Improved validation error substantially over the previous-day baseline.
Final HistGradientBoosting model achieved MAE 2.74 and RMSE 4.82 in one-step chronological validation.
Recursive validation achieved MAE 5.60 and RMSE 8.75.
Generated 11,808 future traffic forecasts.
Developed and deployed an interactive Streamlit dashboard.
⚠️ Limitations

The provided dataset does not contain explicit information about:

Weather conditions
Accidents
Road closures
Events
Location-specific holiday information

Therefore, these external factors were not directly modeled.

The future test period does not contain actual vehicle counts, so the July–October forecasts cannot be directly evaluated within this project using the provided test data.

🚀 Future Improvements

Possible future improvements include:

Incorporating weather data
Adding verified holiday/event information for the relevant city
Incorporating accident and road-closure information
Testing advanced time-series models
Adding real-time traffic data
Adding traffic forecasting for user-selected future horizons
Developing automated model retraining
Adding real-time alerts for predicted traffic peaks
