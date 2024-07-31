"""
Get history books from the Database
"""
import pandas as pd
import rentalCSV


#creating a database for history of books:

rentalCSV.rentedBooks("nji","ddd1_1" ,"the hunger games", "cder123", "01-05-2024")
rentalCSV.rentedBooks("nji","ddd1_1" ,"the hunger", "cder123", "01-05-2024")
rentalCSV.rentedBooks("ni","ddd1_1" ,"the hunger games", "cder123", "01-05-2024")


def historyBooks(username):

    df = pd.read_csv("rentedHistoryBooks.csv")
    books = df.loc[df["username"] == username]
    return books


hist_books = historyBooks("nji")
print(hist_books)