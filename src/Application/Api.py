from flask import Flask, render_template, request
import sys
import pandas as pd
sys.path.append("../")
from ExpenseAnalysis import is_contains, to_datetime, to_datestring, analysis


filename = "../Daily Expenditure - Daily Expenses.csv"
app = Flask(__name__)


@app.route("/data")
def get_data():
    return render_template("insert_data.html")


@app.route("/data", methods=["POST"])
def pass_data():
    df = pd.read_csv(filename)
    df["DATE"] = df.apply(lambda x: to_datetime(x["DATE"]), axis=1)

    date = request.form.get("date_insert", None)
    type = "insert"
    if not date:
        date = request.form.get("date_update", "")
        type = "update"

    food = request.form["food"]
    credit = request.form["credit"]
    travel = request.form["travel"]
    other = request.form["other"]

    # Converting datetimestring to datetime object
    date_ = to_datetime(date)

    if type == "insert":

        date_status = is_contains(df, date_)
        if date_status:
            return render_template("update_data.html")
        else:
            with open(filename, "a") as doc:
                doc.write("{},{},{},{}\n".format(date, food, travel, credit, other))
            doc.close()
        return render_template("thanks_insert.html")

    elif type == "update":

        df.loc[df["DATE"] == date_, "FOOD"] = food
        df.loc[df["DATE"] == date_, "TRAVEL"] = travel
        df.loc[df["DATE"] == date_, "CREDIT"] = credit
        df.loc[df["DATE"] == date_, "OTHER"] = other
        df["DATE"] = df.apply(lambda x: to_datestring(x["DATE"]), axis=1)

        df.to_csv(filename, index=False)
        return render_template("thanks_update.html")


@app.route("/analysis/month")
def analyze_data():
    expenses = analysis()
    month_analysis = expenses.get("monthly", {})

    food = month_analysis.get("food", 0.0)
    travel = month_analysis.get("travel", 0.0)
    credit = month_analysis.get("credit", 0.0)
    other = month_analysis.get("other", 0.0)

    total = food + travel + credit + other
    month = expenses.get("month", None)

    return render_template("monthly_analysis.html", food=food,
                           travel=travel, credit=credit,
                           other=other, total=total, month=month)


@app.route("/analysis/day")
def analyze_data_day():
    expenses = analysis()
    daily_expense = expenses.get("daily", {})

    food = daily_expense.get("food", 0.0)
    travel = daily_expense.get("travel", 0.0)
    credit = daily_expense.get("credit", 0.0)
    other = daily_expense.get("other", 0.0)

    total = food + travel + credit + other
    date = expenses.get("date", None)

    return render_template("daily_analysis.html", food=food,
                           travel=travel, credit=credit,
                           other=other, total=total, date=date)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

