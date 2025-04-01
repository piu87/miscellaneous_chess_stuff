import requests
import matplotlib.pyplot as plt
import datetime


def fetch_rating_history(username, perf_type="bullet"):
    url = f"https://lichess.org/api/user/{username}/rating-history"
    response = requests.get(url)
    data = response.json() # converting the json file that the API sends

    for perf in data:
        if perf["name"].lower() == perf_type.lower():
            return perf["points"]

    else:
        return []


def create_graph(rating_data, username, perf_type):
    dates = [datetime.date(year, month + 1, day) for year, month, day, _ in rating_data] # getting the dates
    # the lichess API sends months back zero indexed, but the datetime library starts months with 1, hence "month + 1"
    ratings = [rating for _, _, _, rating in rating_data] # getting the ratings
    plt.figure(figsize=(10, 5)) # creating a simple line graph using the matplot library
    plt.plot(dates, ratings, marker="o", linestyle="-")
    plt.title(f"my {perf_type.capitalize()} rating")
    plt.xlabel("date") # notating the x axis
    plt.ylabel("rating") # notating the y axis
    plt.grid(True)
    plt.show()


username = "movee_or_losee" # specifying the username
perf_type = "bullet" # specifying the performance type aka the rating category that I want, in my case bullet
rating_history = fetch_rating_history(username, perf_type)
create_graph(rating_history, username, perf_type)


