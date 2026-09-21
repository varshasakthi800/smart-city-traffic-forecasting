import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Smart City Traffic Forecasting",
    page_icon="🚦",
    layout="wide"
)

# --------------------------------------------------
# Load model and prediction data
# --------------------------------------------------
model = joblib.load("final_traffic_forecasting_model.pkl")
df = pd.read_csv("smart_city_traffic_predictions.csv")

# --------------------------------------------------
# Prepare date and time information
# --------------------------------------------------
df["ID"] = df["ID"].astype(str)

df["Date"] = pd.to_datetime(
    df["ID"].str[:8],
    format="%Y%m%d"
)

df["Hour"] = df["ID"].str[8:10].astype(int)
df["Junction"] = df["ID"].str[10].astype(int)

df["DateTime"] = (
    df["Date"] +
    pd.to_timedelta(df["Hour"], unit="h")
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🚦 Smart City Traffic Forecasting Dashboard")

st.write(
    "Machine-learning based forecasting of traffic patterns "
    "across four smart-city junctions."
)

st.markdown("---")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("🔎 Traffic Controls")

junction = st.sidebar.selectbox(
    "Select Junction",
    sorted(df["Junction"].unique())
)

selected_date = st.sidebar.date_input(
    "Select Date",
    value=df["Date"].min(),
    min_value=df["Date"].min(),
    max_value=df["Date"].max()
)

# --------------------------------------------------
# Filter selected junction and date
# --------------------------------------------------
filtered = df[
    (df["Junction"] == junction) &
    (df["Date"].dt.date == selected_date)
].copy()

# --------------------------------------------------
# Dashboard
# --------------------------------------------------
if len(filtered) > 0:

    average_traffic = filtered["Vehicles"].mean()
    maximum_traffic = filtered["Vehicles"].max()
    minimum_traffic = filtered["Vehicles"].min()

    peak_index = filtered["Vehicles"].idxmax()

    peak_hour = filtered.loc[
        peak_index, "Hour"
    ]

    # --------------------------------------------------
    # Determine traffic level
    # --------------------------------------------------
    if average_traffic < 15:
        traffic_status = "🟢 Low"
    elif average_traffic < 30:
        traffic_status = "🟡 Moderate"
    else:
        traffic_status = "🔴 High"

    # --------------------------------------------------
    # Metrics
    # --------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Traffic",
            f"{average_traffic:.1f}"
        )

    with col2:
        st.metric(
            "Peak Traffic",
            f"{maximum_traffic:.1f}"
        )

    with col3:
        st.metric(
            "Peak Hour",
            f"{peak_hour:02d}:00"
        )

    with col4:
        st.metric(
            "Traffic Status",
            traffic_status
        )

    st.markdown("---")

    # --------------------------------------------------
    # Hourly forecast chart
    # --------------------------------------------------
    st.subheader(
        f"📈 Hourly Traffic Forecast — Junction {junction}"
    )

    chart_data = filtered[
        ["DateTime", "Vehicles"]
    ].set_index("DateTime")

    st.line_chart(chart_data)

    # --------------------------------------------------
    # Hourly forecast table
    # --------------------------------------------------
    st.subheader("📋 Hourly Forecast")

    display_data = filtered[
        ["DateTime", "Junction", "Vehicles"]
    ].copy()

    display_data["Vehicles"] = (
        display_data["Vehicles"].round(2)
    )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No forecast data is available for this date."
    )

# --------------------------------------------------
# Model information
# --------------------------------------------------
st.markdown("---")

st.subheader("🤖 About This Project")

st.write(
    "This project uses a HistGradientBoostingRegressor "
    "to forecast traffic using historical traffic patterns "
    "and calendar-based features such as hour, day of week, "
    "month and lagged traffic values."
)

st.write(
    "The forecasting dataset contains four junctions "
    "and covers July 1, 2017 to October 31, 2017."
)

st.info(
    "The displayed values are model-generated traffic forecasts."
)

st.caption(
    "Smart City Traffic Forecasting | Machine Learning Project"
)