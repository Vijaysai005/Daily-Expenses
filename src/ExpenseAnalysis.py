import warnings
import pandas as pd
from datetime import datetime

warnings.simplefilter("ignore")


def to_datetime(date_time_string):
    return datetime.strptime(date_time_string, "%m/%d/%Y")


def to_datestring(date_time):
    return date_time.strftime("%m/%d/%Y")


def to_month(date):
    return date.month


def is_contains(df, date):
    current_date_df = df[df["DATE"] == date].reset_index(drop=True)
    if current_date_df.empty:
        return False
    else:
        return True


def analysis(filename="../Daily Expenditure - Daily Expenses.csv"):

    df = pd.read_csv(filename)
    current_date = datetime.now().date()

    df["DATE"] = df.apply(lambda x: to_datetime(x["DATE"]), axis=1)
    df["MONTH"] = df.apply(lambda x: to_month(x["DATE"]), axis=1)

    # Day Analysis
    current_date_df = df[df["DATE"] == current_date].reset_index(drop=True)

    daily_food_expense = current_date_df["FOOD"].get_values()
    daily_food_expense = daily_food_expense[0] if len(daily_food_expense) == 1 else None

    daily_travel_expense = current_date_df["TRAVEL"].get_values()
    daily_travel_expense = daily_travel_expense[0] if len(daily_travel_expense) == 1 else None

    daily_credit_expense = current_date_df["CREDIT"].get_values()
    daily_credit_expense = daily_credit_expense[0] if len(daily_credit_expense) == 1 else None

    daily_other_expense = current_date_df["OTHER"].get_values()
    daily_other_expense = daily_other_expense[0] if len(daily_other_expense) == 1 else None

    daily_expense = {}
    daily_expense.update({"food": daily_food_expense})
    daily_expense.update({"travel": daily_travel_expense})
    daily_expense.update({"credit": daily_credit_expense})
    daily_expense.update({"other": daily_other_expense})

    # print ("*********************************************")
    # print ("DATE: {}".format(current_date))
    # print ("Food expense is {} Rs.".format(daily_food_expense))
    # print ("Travel expense is {} Rs.".format(daily_travel_expense))
    # print ("Credit expense is {} Rs.".format(daily_credit_expense))
    # print ("Other expense is {} Rs.".format(daily_other_expense))
    # print ("*********************************************\n")

    # Month Analysis
    current_month_df = df[df["MONTH"] == current_date.month].reset_index(drop=True)

    monthly_food_expense = current_month_df["FOOD"].sum()
    monthly_travel_expense = current_month_df["TRAVEL"].sum()
    monthly_credit_expense = current_month_df["CREDIT"].sum()
    monthly_other_expense = current_month_df["OTHER"].sum()

    monthly_expense = {}
    monthly_expense.update({"food": monthly_food_expense})
    monthly_expense.update({"travel": monthly_travel_expense})
    monthly_expense.update({"credit": monthly_credit_expense})
    monthly_expense.update({"other": monthly_other_expense})

    expenses = {}
    expenses.update(
        {
            "daily": daily_expense,
            "monthly": monthly_expense,
            "month": current_date.strftime("%B"),
            "date": current_date
        }
    )
    # print ("MONTH: {}".format(current_date.month))
    # print ("Total food expense is {} Rs.".format(monthly_food_expense))
    # print ("Total travel expense is {} Rs.".format(monthly_travel_expense))
    # print ("Total credit expense is {} Rs.".format(monthly_credit_expense))
    # print ("Total other expense is {} Rs.".format(monthly_other_expense))
    # print ("*********************************************\n")
    return expenses


def generate_log():
    filename = "/tmp/analysis.log"

    expenses = analysis(filename="/home/vijay/Documents/Daily-Expenses/Daily Expenditure - Daily Expenses.csv")

    month_analysis = expenses.get("monthly", {})

    food = month_analysis.get("food", 0.0)
    travel = month_analysis.get("travel", 0.0)
    credit = month_analysis.get("credit", 0.0)
    other = month_analysis.get("other", 0.0)

    total = food + travel + credit + other
    month = expenses.get("month", None)

    daily_expense = expenses.get("daily", {})

    daily_food = daily_expense.get("food", 0.0)
    daily_travel = daily_expense.get("travel", 0.0)
    daily_credit = daily_expense.get("credit", 0.0)
    daily_other = daily_expense.get("other", 0.0)

    daily_total = food + travel + credit + other
    date = expenses.get("date", None)

    print("*********************************************")
    print("DATE: {}".format(date))
    print("Food expense is {} Rs.".format(daily_food))
    print("Travel expense is {} Rs.".format(daily_travel))
    print("Credit expense is {} Rs.".format(daily_credit))
    print("Other expense is {} Rs.".format(daily_other))
    print("Total expense on {} is {} Rs.".format(date, daily_total))
    print("*********************************************\n")

    print("MONTH: {}".format(month))
    print("Total food expense is {} Rs.".format(food))
    print("Total travel expense is {} Rs.".format(travel))
    print("Total credit expense is {} Rs.".format(credit))
    print("Total other expense is {} Rs.".format(other))
    print("Total expense is {} Rs in {}.".format(total, month))
    print("*********************************************\n")

    # with open(filename, "w") as doc:
    #     doc.write("*********************************************\n")
    #     doc.write("DATE: {}\n".format(date))
    #     doc.write("Food expense is {} Rs.\n".format(daily_food))
    #     doc.write("Travel expense is {} Rs.\n".format(daily_travel))
    #     doc.write("Credit expense is {} Rs.\n".format(daily_credit))
    #     doc.write("Other expense is {} Rs.\n".format(daily_other))
    #     doc.write("Total expense on {} is {} Rs.\n".format(date, daily_total))
    #     doc.write("*********************************************\n\n")
    #
    #     doc.write("MONTH: {}\n".format(month))
    #     doc.write("Total food expense is {} Rs.\n".format(food))
    #     doc.write("Total travel expense is {} Rs.\n".format(travel))
    #     doc.write("Total credit expense is {} Rs.\n".format(credit))
    #     doc.write("Total other expense is {} Rs.\n".format(other))
    #     doc.write("Total expense is {} Rs in {}.\n".format(total, month))
    #     doc.write("*********************************************\n")
    # doc.close()
    return


if __name__ == "__main__":
    analysis()