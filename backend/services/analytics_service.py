from services.data_loader import data_loader


class AnalyticsService:

    def summary(self):

        df = data_loader.df

        return {

            "total_tickets": len(df),

            "open_tickets":
            len(df[df["status"]=="Open"]),

            "resolved_tickets":
            len(df[df["status"]=="Resolved"]),

            "escalated_tickets":
            len(df[df["status"]=="Escalated"]),

            "avg_rating":
            round(
                df["customer_rating"]
                .fillna(0)
                .mean(),
                2
            )
        }


analytics_service = AnalyticsService()