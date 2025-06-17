from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary_output = None

    if request.method == "POST":
        user_prompt = request.form.get("user_prompt")

        # 🔧 Simulated AI agent response (replace this with actual AI call)
        summary_output = f"🧠 AI Summary for Prompt:\n\n'{user_prompt}'\n\n👉 This project is a full-stack blood donation management system built using MERN stack. It allows users to register as donors, view available blood types, and manage blood banks effectively."

    return render_template("index.html", summary=summary_output)

if __name__ == "__main__":
    app.run(debug=True)
