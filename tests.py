from search_index import SearchIndex


catalog = [
    "catalog",
    "catch",
    "catdog",
    "catalog",
    "catdog"
]

index = SearchIndex()
index.build_index(catalog)

print("TEST 1")
result = index.search("cat", "og")

if result:
    print(result)
else:
    print("No Match")

print("\nTEST 2")
result = index.search("ca", "ch")

if result:
    print(result)
else:
    print("No Match")

print("\nTEST 3")
result = index.search("abc", "xyz")

if result:
    print(result)
else:
    print("No Match")