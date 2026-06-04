from services.data_loader import data_loader


class AnomalyDetector:

    def detect(self):

        df = data_loader.df.copy()

        anomalies = []

        # Resolution Time Outliers
        mean_time = df["resolution_time_hrs"].mean()
        std_time = df["resolution_time_hrs"].std()

        threshold = mean_time + (2 * std_time)

        outliers = df[
            df["resolution_time_hrs"] > threshold
        ]

        for _, row in outliers.iterrows():

            anomalies.append({
                "ticket_id": row["ticket_id"],
                "reason": "Long Resolution Time"
            })

        # Critical Unresolved
        critical_open = df[
            (df["priority"] == "Critical")
            &
            (df["status"] != "Resolved")
        ]

        for _, row in critical_open.iterrows():

            anomalies.append({
                "ticket_id": row["ticket_id"],
                "reason": "Critical Unresolved Ticket"
            })

        # Poor Ratings
        poor_ratings = df[
            df["customer_rating"] <= 2
        ]

        for _, row in poor_ratings.iterrows():

            anomalies.append({
                "ticket_id": row["ticket_id"],
                "reason": "Poor Customer Rating"
            })

        # NEW RULE
        # Slow Response Time
        slow_response = df[
            df["response_time_hrs"] > 24
        ]

        for _, row in slow_response.iterrows():

            anomalies.append({
                "ticket_id": row["ticket_id"],
                "reason": "Slow Response Time"
            })

        return anomalies


anomaly_detector = AnomalyDetector()