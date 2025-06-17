from utils.github_search import search_github_repos

# 🔍 Example keyword to search
keyword = "blood bank database"

# 🔁 Search GitHub for repos
results = search_github_repos(keyword)

# 🖨️ Print the first result
if results and "error" not in results[0]:
    repo = results[0]
    print("✅ Repository Found:")
    print("Name:", repo["name"])
    print("URL:", repo["url"])
    print("Description:", repo["description"])
else:
    print("❌ Error:", results[0].get("error", "Unknown error"))
