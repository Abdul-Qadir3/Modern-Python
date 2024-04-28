import webbrowser

def google_search(query):
    # Construct the Google search URL with the query
    search_url = f"https://www.google.com/search?q={query}"

    # Open the web browser and navigate to the Google search page
    webbrowser.open(search_url)

# Specify the word or phrase you want to search for
search_query = "deep learning"

# Perform the Google search
google_search(search_query)
