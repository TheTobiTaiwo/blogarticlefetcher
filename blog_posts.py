from langchain.text_splitter import TokenTextSplitter, CharacterTextSplitter
import prompts
import newspaper

def split_text_into_chunks(text, max_tokens):
    # Using TokenTextSplitter for token-based chunking
    token_splitter = TokenTextSplitter(chunk_size=max_tokens, chunk_overlap=0)
    token_chunks = token_splitter.split_text(text)
    
    # Using CharacterTextSplitter for character-based chunking
    char_splitter = CharacterTextSplitter(chunk_size=100)
    char_chunks = char_splitter.split_text(text)
    
    return token_chunks, char_chunks

def get_article_from_url(url):
    try:
        # Scrape the web page for content using newspaper
        article = newspaper.Article(url)
        # Download the article's content with a timeout of 10 seconds
        article.download()
        # Check if the download was successful before parsing the article
        if article.download_state == 2:
            article.parse()
            # Get the main text content of the article
            article_text = article.text
            print("Article Text:", article_text)  # Debugging output
            return article_text
        else:
            print("Error: Unable to download article from URL:", url)
            return None
    except Exception as e:
        print("An error occurred while processing the URL:", url)
        print(str(e))
        return None

def get_blog_summary_prompt(blog_url):
    # Example blog URL
    # https://www.bellanaija.com/2024/08/public-reactions-to-repeal-vapp-act/
    blog_article = get_article_from_url(blog_url)
    if blog_article:
        prompt = prompts.blog_bullet_summary_prompt.format(
            MaxPoints="10", MinPoints="5", InputText=blog_article
        )
        print("Generated Prompt:", prompt)  # Debugging output
        return prompt
    else:
        print("No article content to generate prompt.")
        return None

# Example usage
get_blog_summary_prompt("https://www.bellanaija.com/2024/08/public-reactions-to-repeal-vapp-act/")
