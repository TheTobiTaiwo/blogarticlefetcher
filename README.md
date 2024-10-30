Here's a README file for your project using chain of thought prompting:

---

# Blog Summary Generator

This project provides a utility to fetch and process text from a given URL and generate a blog summary prompt using LangChain's `TokenTextSplitter` and `CharacterTextSplitter`, as well as the `newspaper` library for web scraping.

## Features
1. **Text Splitting**: 
    - **Token-based chunking**: Splits text based on token count to manage prompt size and structure.
    - **Character-based chunking**: Splits text into chunks by a fixed number of characters for easier readability.

2. **Article Fetching**: 
    - Fetches articles from URLs using the `newspaper` library.
    - Downloads and parses the article text with error handling and timeouts to ensure reliability.

3. **Prompt Generation**:
    - Generates a summary prompt using a pre-defined template with the extracted article text.

## Code Overview

### `split_text_into_chunks(text, max_tokens)`
- **Purpose**: Splits text into two formats: token-based and character-based.
- **Parameters**:
    - `text`: The input text to be chunked.
    - `max_tokens`: Maximum number of tokens per chunk.
- **Returns**: Two sets of chunks – token-based and character-based.

### `get_article_from_url(url)`
- **Purpose**: Fetches and downloads the article content from the provided URL.
- **Parameters**:
    - `url`: The URL of the article.
- **Returns**: The raw text of the article or `None` if an error occurs.

### `get_blog_summary_prompt(blog_url)`
- **Purpose**: Generates a blog summary prompt from the article content fetched from the URL.
- **Parameters**:
    - `blog_url`: The URL of the blog or article.
- **Returns**: A formatted prompt for summarizing the blog or `None` if the article is not found.

## Example Usage

To generate a blog summary prompt from a URL:

```python
get_blog_summary_prompt("https://www.bellanaija.com/2024/08/public-reactions-to-repeal-vapp-act/")
```

This will download the article, split it into chunks, and generate a summary prompt using a predefined template.

## Installation

1. Install the required libraries:
    ```bash
    pip install langchain newspaper3k
    ```

2. Ensure you have a working internet connection to fetch articles.

## Error Handling

- The project includes basic error handling to manage issues during article download (e.g., network errors or timeouts).
- If the download fails, an error message is displayed, and `None` is returned.

## Notes

- The `prompts` module contains the template for the summary prompt, which should be customized as needed.
- The chunking strategy can be adjusted by modifying the `chunk_size` for both token and character-based splitting.

---

