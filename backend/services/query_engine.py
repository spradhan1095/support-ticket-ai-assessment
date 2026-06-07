from services.data_loader import data_loader
from services.llm_service import llm_service


class QueryEngine:

    def answer_question(self, question):

        df = data_loader.df

        try:
            intent = llm_service.identify_intent(
                question
            )

            print(
                f"Question: {question}"
            )

            print(
                f"Detected Intent: {intent}"
            )

        except Exception as e:

            return (
                f"LLM Error: {str(e)}"
            )

        # ==========================
        # Total Tickets
        # ==========================
        if intent == "total_tickets":

            return (
                f"There are {len(df)} total tickets."
            )

        # ==========================
        # Open Tickets
        # ==========================
        elif intent == "open_tickets":

            count = len(
                df[
                    df["status"]
                    .str.lower()
                    == "open"
                ]
            )

            return (
                f"There are {count} open tickets."
            )

        # ==========================
        # Resolved Tickets
        # ==========================
        elif intent == "resolved_tickets":

            count = len(
                df[
                    df["status"]
                    .str.lower()
                    == "resolved"
                ]
            )

            return (
                f"There are {count} resolved tickets."
            )

        # ==========================
        # Escalated Tickets
        # ==========================
        elif intent == "escalated_tickets":

            count = len(
                df[
                    df["status"]
                    .str.lower()
                    == "escalated"
                ]
            )

            return (
                f"There are {count} escalated tickets."
            )

        # ==========================
        # Critical Tickets
        # ==========================
        elif intent == "critical_tickets":

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
        # Unresolved Critical
        # ==========================
        elif intent == "unresolved_critical":

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
        # Average Rating
        # ==========================
        elif intent == "average_rating":

            avg = round(
                df["customer_rating"].mean(),
                2
            )

            return (
                f"The average customer rating is {avg}."
            )

        # ==========================
        # Average Response Time
        # ==========================
        elif intent == "average_response_time":

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
        elif intent == "average_resolution_time":

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
        elif intent == "most_common_category":

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
        # Highest Rated Agent
        # ==========================
        elif intent == "highest_rated_agent":

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
        # Lowest Rated Agent
        # ==========================
        elif intent == "lowest_rated_agent":

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
        # Unknown Question
        # ==========================
        else:

            return (
                "I couldn't understand that question. "
                "Please ask about tickets, ratings, "
                "agents, categories, response times, "
                "or resolution times."
            )


query_engine = QueryEngine()