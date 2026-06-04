import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API = "http://localhost:8000"

st.set_page_config(
    page_title="Support Ticket AI",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 AI Powered Support Ticket Analytics System")

tab1, tab2, tab3 = st.tabs(
    ["Dashboard", "Ask AI", "Anomalies"]
)

# ==================================
# Dashboard
# ==================================
with tab1:

    st.subheader("Support Ticket Dashboard")

    try:

        response = requests.get(
            f"{API}/dashboard"
        )

        data = response.json()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Tickets",
            data["total_tickets"]
        )

        c2.metric(
            "Open Tickets",
            data["open_tickets"]
        )

        c3.metric(
            "Resolved Tickets",
            data["resolved_tickets"]
        )

        c4.metric(
            "Escalated Tickets",
            data["escalated_tickets"]
        )

        st.metric(
            "Average Rating",
            data["avg_rating"]
        )

        st.markdown("---")

        df = pd.read_csv(
            "../backend/data/support_tickets.csv"
        )

        # Status Distribution
        st.subheader(
            "Ticket Status Distribution"
        )

        status_counts = (
            df["status"]
            .value_counts()
            .reset_index()
        )

        status_counts.columns = [
            "status",
            "count"
        ]

        fig1 = px.pie(
            status_counts,
            values="count",
            names="status",
            title="Ticket Status Distribution"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        # Priority Distribution
        st.subheader(
            "Priority Distribution"
        )

        priority_counts = (
            df["priority"]
            .value_counts()
            .reset_index()
        )

        priority_counts.columns = [
            "priority",
            "count"
        ]

        fig2 = px.bar(
            priority_counts,
            x="priority",
            y="count",
            title="Priority Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # Agent Performance
        st.subheader(
            "Agent Performance"
        )

        agent_df = (
            df.groupby("agent_id")
            ["customer_rating"]
            .mean()
            .reset_index()
        )

        fig3 = px.bar(
            agent_df,
            x="agent_id",
            y="customer_rating",
            title="Average Agent Rating"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Dashboard Error: {str(e)}"
        )

# ==================================
# Ask AI
# ==================================
with tab2:

    st.subheader("Ask Questions")

    question = st.text_input(
        "Ask anything about support tickets..."
    )

    if st.button("Submit"):

        try:

            result = requests.post(
                f"{API}/query",
                json={
                    "question": question
                }
            )

            if result.status_code == 200:

                st.success(
                    result.json()["answer"]
                )

            else:

                st.error(
                    result.text
                )

        except Exception as e:

            st.error(str(e))

# ==================================
# Anomalies
# ==================================
with tab3:

    st.subheader("Anomaly Detection")

    try:

        anomalies = requests.get(
            f"{API}/anomalies"
        ).json()

        st.metric(
            "Detected Anomalies",
            anomalies["count"]
        )

        anomaly_df = pd.DataFrame(
            anomalies["anomalies"]
        )

        if not anomaly_df.empty:

            st.dataframe(
                anomaly_df,
                use_container_width=True
            )

        else:

            st.success(
                "No anomalies detected."
            )

    except Exception as e:

        st.error(str(e))