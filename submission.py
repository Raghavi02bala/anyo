# imports
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(dataset_path)

def plot_baseline(data, type="Daily"):
    if type == "Monthly":
        # create a dataframe with just months and their respective monthly averages over different category
        data_monthly = data.groupby(["Month"]).mean(numeric_only=True)[["Monthly_Questions_Score"]].reset_index()
        y = data_monthly["Monthly_Questions_Score"].to_list()
    else:
        # create a dataframe with just months and their respective daily averages over different category
        # we can ignore the category wise grouping as it is "one question per category", so it's similar to monthly_question_score.
        data_monthly = data.groupby(["Month"]).mean(numeric_only=True)[["Daily_Questions_Score"]].reset_index()
        y = data_monthly["Daily_Questions_Score"].to_list()
    # return list type, so we can directly use in plot_line function
    return data_monthly["Month"].to_list(), y

def plot_line():
    # we get the month and monthly_questions_score
    x, y_monthly = plot_baseline(data, "Monthly") 
    # we get the month and daily_questions_score, we don't have to pass value for default argument
    x, y_daily = plot_baseline(data)  
    plt.plot(x, y_monthly, label = "line 1")
    plt.plot(x, y_daily, label = "line 2")
    plt.legend()
    plt.show()
    
