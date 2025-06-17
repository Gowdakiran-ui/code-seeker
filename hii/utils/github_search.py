from flask import Flask, request, render_template
import requests
from github_search import search_github_repos  # assuming filename is github_search.py

app = Flask(__name__)

WEBHOOK_URL = "http://localhost:5678/webhook-test/github"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        if keyword:
            result = search_github_repos(keyword)
            payload = {"results": result, "query": keyword}
            
            try:
                response = requests.post(WEBHOOK_URL, json=payload)
                status = "✅ Sent to n8n successfully" if response.status_code == 200 else f"❌ Failed to send: {response.status_code}"
            except Exception as e:
                status = f"❌ Error: {str(e)}"

            return render_template("index.html", keyword=keyword, result=result, status=status)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
