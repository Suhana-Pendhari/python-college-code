# Q5) URL Extraction: Write a Python program that reads a text file containing HTML 
# code and extracts all URLs (links) present in the document using regular expressions. 
# URLs should be validated against common URL patterns.

import re

def simple_url_extractor(html_text):
    """
    Simple URL extractor - one function version
    """
    # Find all URLs in the text
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(url_pattern, html_text)
    
    # Also find www URLs
    www_pattern = r'www\.[^\s<>"{}|\\^`\[\]]+'
    www_urls = re.findall(www_pattern, html_text)
    
    # Convert www URLs to full URLs
    full_urls = [f"https://{url}" for url in www_urls]
    
    all_urls = urls + full_urls
    return list(set(all_urls))  # Remove duplicates

sample_html = """
Check out these sites:
<a href="https://www.google.com">Google</a>
Visit www.github.com for code.
Also https://stackoverflow.com is great.
<img src="https://example.com/image.jpg">
"""

print("Simple URL Extractor:")
print("-" * 40)
print("HTML Content: ", sample_html)
print("-" * 40)
print("Extracted URL:")
urls = simple_url_extractor(sample_html)
for url in urls:
    print(f"🔗 {url}")
