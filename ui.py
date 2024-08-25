import newspaper
import streamlit as st

def get_article_from_url(url):
    try:
        # Scrape the web page for content using newspaper
        article = newspaper.Article(url)
        # Download the article's content with a timeout of 10 seconds
        article.download()
        # Check if the download was successful before parsing the article
        if article.download_state == 2:
            article.parse()
            return article.text
        else:
            return "Error: Unable to download article from URL."
    except Exception as e:
        return f"An error occurred while processing the URL: {str(e)}"

def main():
    st.title("Blog Article Fetcher")

    url = st.text_input("Enter the URL of the blog article:")

    if st.button("Fetch Article"):
        if url:
            st.write("Fetching article...")
            article_text = get_article_from_url(url)
            if article_text:
                st.write("**Article Text:**")
                st.write(article_text)
            else:
                st.write("Unable to fetch article. Please check the URL.")
        else:
            st.write("Please enter a URL to fetch the article.")

if __name__ == "__main__":
    main()
