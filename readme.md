# 🍽️ Dorm Meals Management - Flask App

A smart and minimal Flask-based web application for managing and tracking **shared meal contributions** in dormitories.  
This system helps users record who brings meals, who eats, and provides detailed monthly statistics and efficiency charts for each participant.

---

## 🚀 Features

✅ **Meal Tracking System** – Add and manage daily meal data (who brought food, who ate).  
✅ **Statistics Dashboard** – Displays per-person stats, including:
- Total meals brought  
- Total meals eaten  
- Monthly separated reports  
- Efficiency chart (meals_brought / meals_eaten)  

✅ **History Section** – View past meal records day-by-day with contributor and participant details.  
✅ **Responsive Design** – Fully optimized for both mobile and desktop devices.  
✅ **Modern UI** – Clean, minimal, and intuitive interface.  

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python 3)
- **Frontend:** HTML5, TailwindCSS
- **Charting:** Chart.js
- **Database:** SQLite (local file storage)
- **Hosting:** PythonAnywhere

---

## 📂 Project Structure

```
dorm-meals-flask/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
│
└── templates/
    ├── index.html            # Main page (daily meals)
    ├── stats.html            # Statistics and efficiency dashboard
    └── history.html          # History of meals
```

---

## ⚙️ Deployment on PythonAnywhere

To deploy your project:

1. **Upload project files** to PythonAnywhere.
2. Create a **Flask app** via PythonAnywhere Dashboard.
3. Set the **working directory** to your project folder.
4. Point **WSGI configuration file** to your `app.py`.
5. Reload the web app — you're live 🎉  

> The app stores all data in a local SQLite database and requires no external setup.

---

## 📊 Efficiency Metric

Each participant’s **efficiency** is calculated as:

```
Efficiency = Meals Brought / Meals Eaten
```

The app visualizes this using a modern **bar chart**, allowing easy comparison between members.

---

## 👨‍💻 Developer

Developed with ❤️ by **MParsa Ahmadi**  
[GitHub Profile → @MParsaAhmadi](https://github.com/MParsaAhmadi)

---

## 📜 License

This project is released under the **MIT License** – feel free to use, modify, and share.