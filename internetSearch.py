# created by Nicholas Garrett

"""
    description:
"""

import search

def search(words):
    result = search.google("Python", max_results = 30, lang = "en")
    print("google search result:")
    print(result)
