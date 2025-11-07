from flask import Flask, render_template, request, redirect, url_for
import json, os
from datetime import date
from collections import defaultdict

app = Flask(__name__)

DATA_FILE = "meals.json"
users = ["پارسا", "ابوالفضل", "محمدحسین", "سپهر"]

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            for entry in data:
                if "date" not in entry: entry["date"] = date.today().isoformat()
                if "bringers" not in entry: entry["bringers"] = []
                if "eaters" not in entry: entry["eaters"] = []
            return data
    except Exception:
        return []

def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Error saving data:", e)

@app.route("/")
def index():
    data = load_data()
    data.sort(key=lambda x: x.get("date", ""), reverse=True)
    today_str = date.today().isoformat()
    today_entries = [entry for entry in data if entry.get("date") == today_str]
    return render_template("index.html", users=users, today_entries=today_entries)

@app.route("/add", methods=["POST"])
def add_entry():
    bringers = request.form.getlist("bringers")
    eaters = request.form.getlist("eaters")

    new_entry = {
        "date": date.today().isoformat(),
        "bringers": bringers,
        "eaters": eaters
    }

    data = load_data()
    data.append(new_entry)
    save_data(data)

    return redirect(url_for("index"))

@app.route("/history")
def history():
    data = load_data()
    data.sort(key=lambda x: x["date"], reverse=True)
    return render_template("history.html", data=data, users=users)

@app.route("/stats")
def stats():
    data = load_data()
    monthly_data = defaultdict(lambda: {"bring_count": defaultdict(int), "eat_count": defaultdict(int)})

    for entry in data:
        month = entry.get("date", "")[:7]
        bringers = entry.get("bringers", [])
        eaters = entry.get("eaters", [])
        for b in bringers:
            monthly_data[month]["bring_count"][b] += 1
        for e in eaters:
            monthly_data[month]["eat_count"][e] += 1

    total_bring = defaultdict(int)
    total_eat = defaultdict(int)
    for month_vals in monthly_data.values():
        for user in users:
            total_bring[user] += month_vals["bring_count"].get(user, 0)
            total_eat[user] += month_vals["eat_count"].get(user, 0)

    efficiency = {}
    for user in users:
        eaten = total_eat[user]
        efficiency[user] = round(total_bring[user] / eaten, 2) if eaten > 0 else 0

    return render_template("stats.html", monthly_data=monthly_data, efficiency=efficiency, users=users)

if __name__ == "__main__":
    app.run(debug=True)
