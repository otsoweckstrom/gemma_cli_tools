import ollama
import argparse
from bs4 import BeautifulSoup
import re

def read_html_file(file_path):
    """Reads an HTML file and returns its content."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_page_structure(html_content):
    """Extracts the overall structure of the HTML document."""
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract sample element structures
    elements = soup.find_all(True)
    sample_structure = "\n".join(
        [str(el) for el in elements[:10]]  
    )

    return sample_structure

def get_css_selector(html_content, target_description):
    """Uses Gemma to determine the best CSS selector for a given target element."""
    sample_structure = extract_page_structure(html_content)

    prompt = f"""
    You are an expert in web scraping and CSS selectors. Analyze the following HTML structure and determine the best CSS selector for the target element.

    **HTML Sample (First 10 Elements):**
    {sample_structure}

    **Task:**
    Identify the best CSS selector to extract: "{target_description}".  
    - Prefer specific and unique selectors over generic ones.
    - If possible, suggest the most reliable way to select this element.
    - Do NOT include explanations—only return the exact CSS selector.
    """

    try:
        response = ollama.chat(model='gemma3:1b', messages=[{"role": "user", "content": prompt}])
        return response['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Extract the best CSS selector from an HTML file using AI.")
    parser.add_argument("html_file", type=str, help="Path to the HTML file.")
    parser.add_argument("--target", type=str, required=True, help="Description of the element to extract (e.g., 'product name').")

    args = parser.parse_args()

    html_content = read_html_file(args.html_file)
    if not html_content:
        return

    selector = get_css_selector(html_content, args.target)
    
    print(f"\nBest CSS Selector: {selector}")

if __name__ == "__main__":
    main()
