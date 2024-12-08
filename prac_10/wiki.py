import wikipedia

while True:
    # Prompt the user for a page title or search phrase
    search_input = input("Enter a page title or search phrase (or leave blank to exit): ")
    if not search_input:
        break  # Exit the loop if the input is blank

    try:
        # Fetch the page summary
        page = wikipedia.page(search_input, auto_suggest=False)  # Disable auto-suggest
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error: The search phrase may refer to multiple pages. Please provide a more specific "
              "input.")
    except wikipedia.exceptions.PageError as e:
        print("Page Error: The page could not be found.")
