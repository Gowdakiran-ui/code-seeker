from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary_output = None

    if request.method == "POST":
        user_prompt = request.form.get("user_prompt", "")

        # ✅ Send POST to your n8n test webhook with JSON payload
        try:
            response = requests.post(
                "http://localhost:5678/webhook-test/github automation",
                json={"prompt": user_prompt}
            )
            response.raise_for_status()
            data = response.json()

            # ✅ Customize how you extract the response
            summary_output = data.get("summary") or str(data)
        except Exception as e:
            summary_output = f"❌ Error contacting agent: {e}"

    return render_template("index.html", summary=summary_output)


