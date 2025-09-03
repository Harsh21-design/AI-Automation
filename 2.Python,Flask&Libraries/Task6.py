import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, redirect, url_for

Task6 = Flask(__name__)

@Task6.route("/")
def home():
    return redirect(url_for("dashboard"))

@Task6.route("/dashboard")
def dashboard():

    #Numpy-Pandas

    # Data loading
    dataset = pd.read_csv("static\\data\\titanic1.csv")
    df = pd.DataFrame(dataset)
    # print(df.to_string())
    # print(df.info())
    
    
    # Missing data handling 
    # print(df.isna().any())

    # print(df[['Age','Cabin']])
    meanAge = np.mean(df["Age"])
    df['Age'] = round(df['Age'].fillna(meanAge),2)

    df['Cabin'] = df['Cabin'].fillna('Unknown')
    # print(df[['Age','Cabin']])

    # Matplotlib(Histrogram Plotting)
    plt.figure(figsize=(6,4))
    df["Age"].hist()
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.grid(False)
    plt.savefig("static/data/age_dist.png")
    plt.close()

    #Matplotlib(Line/Scatter Graph Plotting)
    plt.figure(figsize=(15,5))
    
    #Line
    # sorted_df = df[['Age','Fare']].sort_values(by='Age')
    # plt.plot(sorted_df['Age'],sorted_df['Fare'],linestyle='-',color='red',marker='o', mec = 'b', mfc = 'b')
    # plt.plot(sorted_df['Age'],sorted_df['Fare'])
    # plt.show()
    
    #Scatter
    # colors = np.arange(1,892)
    # sizes = np.random.randint(50,100,size=len(df))
    # plt.scatter(df['Age'],df['Fare'],s=sizes,c=colors,cmap='viridis',alpha=0.5) #transparency of the dots with the alpha argument
    # plt.colorbar()

    plt.title("Age vs Fare(Ticket Pricing)")
    plt.xlabel("Age")
    plt.ylabel("Fare")
    
    plt.savefig("static/data/age_vs_ticket.png")
    plt.close()

    # Rendering 
    data_info = df.describe()
    data = df.to_string()
    # print(data)
    return render_template('dashboard.html',
    data_info=data_info.to_html(classes="table table-striped"),
    plot_url='static/data/age_dist.png',
    plot_url2='static/data/age_vs_ticket.png')


if __name__ == "__main__":
    Task6.run(debug=True)


