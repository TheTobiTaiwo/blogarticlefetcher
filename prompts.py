# prompts.py

# Define the template for a blog summary in bullet points
blog_bullet_summary_prompt = (
    "Summarize the following text in bullet points, ensuring the number of bullet points "
    "is between [{MinPoints}] and [{MaxPoints}]. Write the summary in the same language as the input text."
)

# Define the template for refining text
text_refinement_prompt = (
    "Refine the following text by enhancing its originality, removing any plagiarism, and improving readability. "
    "Ensure it feels naturally written by a human while keeping the main idea and objective unchanged."
)




google_search_prompt = "I will provide you with summaries of multiple articles. Your task is to extract the key points from these summaries and synthesize them into a research paragraph of 7-10 sentences. input: {input}"
