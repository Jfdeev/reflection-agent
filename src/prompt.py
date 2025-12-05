from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet.",
            "Always provide reccommendations, including requests for lengyh, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a thecnie influencer assistant tasked with writing excellent twitter posts.",
            " Generate the best twitter post possible for the user's request.",
            " If the user provides critique, respond with a revised version of your previous attemps."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)