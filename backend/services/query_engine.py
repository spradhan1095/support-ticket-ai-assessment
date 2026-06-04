from services.data_loader import data_loader


class QueryEngine:

    def answer_question(self, question):

        df = data_loader.df

        q = question.lower().strip()

        # ==========================
        # Total Tickets
        # ==========================
        if "total" in q and "ticket" in q:
            return f"There are {len(df)} total tickets."

        # ==========================
        # Open Tickets
        # ==========================
        if "open" in q and "ticket" in q:
            count = len(
                df[df["status"].str.lower() == "open"]
            )

            return f"There are {count} open tickets."

        # ==========================
        # Resolved Tickets
        # ==========================
        if "resolved" in q and "ticket" in q:
            count = len(
                df[df["status"].str.lower() == "resolved"]
            )

            return f"There are {count} resolved tickets."

        # ==========================
        # Escalated Tickets
        # ==========================
        if "escalated" in q:
            count = len(
                df[df["status"].str.lower() == "escalated"]
            )

            return f"There are {count} escalated tickets."

        # ==========================
        # Critical Tickets
        # ==========================
        if "critical" in q and "unresolved" not in q:

            count = len(
                df[
                    df["priority"]
                    .str.lower()
                    == "critical"
                ]
            )

            return (
                f"There are {count} critical tickets."
            )

        # ==========================
        # High Priority Tickets
        # ==========================
        if "high priority" in q:

            count = len(
                df[
                    df["priority"]
                    .str.lower()
                    == "high"
                ]
            )

            return (
                f"There are {count} high-priority tickets."
            )

        # ==========================
        # Unresolved Critical Tickets
        # ==========================
        if "critical" in q and "unresolved" in q:

            count = len(
                df[
                    (df["priority"].str.lower() == "critical")
                    &
                    (df["status"].str.lower() != "resolved")
                ]
            )

            return (
                f"There are {count} unresolved critical tickets."
            )

        # ==========================
        # Average Customer Rating
        # ==========================
        if "average" in q and "rating" in q:

            rating = round(
                df["customer_rating"].mean(),
                2
            )

            return (
                f"The average customer rating is {rating}."
            )

        # ==========================
        # Average Response Time
        # ==========================
        if "response time" in q:

            avg = round(
                df["response_time_hrs"].mean(),
                2
            )

            return (
                f"The average response time is {avg} hours."
            )

        # ==========================
        # Average Resolution Time
        # ==========================
        if "resolution time" in q:

            avg = round(
                df["resolution_time_hrs"].mean(),
                2
            )

            return (
                f"The average resolution time is {avg} hours."
            )

        # ==========================
        # Most Common Category
        # ==========================
        if (
            "category" in q
            and (
                "most" in q
                or "highest" in q
                or "top" in q
            )
        ):

            category = (
                df["category"]
                .value_counts()
                .idxmax()
            )

            count = (
                df["category"]
                .value_counts()
                .max()
            )

            return (
                f"{category} has the most tickets "
                f"with {count} tickets."
            )

        # ==========================
        # Lowest Rated Agent
        # ==========================
        if "lowest" in q and "agent" in q:

            ratings = (
                df.groupby("agent_id")
                ["customer_rating"]
                .mean()
            )

            agent = ratings.idxmin()

            score = round(
                ratings.min(),
                2
            )

            return (
                f"{agent} has the lowest average "
                f"rating of {score}."
            )

        # ==========================
        # Highest Rated Agent
        # ==========================
        if (
            "highest" in q and "agent" in q
        ) or (
            "best agent" in q
        ):

            ratings = (
                df.groupby("agent_id")
                ["customer_rating"]
                .mean()
            )

            agent = ratings.idxmax()

            score = round(
                ratings.max(),
                2
            )

            return (
                f"{agent} has the highest average "
                f"rating of {score}."
            )

        # ==========================
        # Status Breakdown
        # ==========================
        if (
            "status distribution" in q
            or "status breakdown" in q
        ):

            status_counts = (
                df["status"]
                .value_counts()
                .to_dict()
            )

            return str(status_counts)

        # ==========================
        # Fallback
        # ==========================
        return (
            "I can answer questions about total tickets, "
            "open tickets, resolved tickets, escalated tickets, "
            "critical tickets, customer ratings, agents, "
            "categories, response times and resolution times."
        )


query_engine = QueryEngine()