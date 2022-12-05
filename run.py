# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get the sales figures from the input
    """
    while True:
        print("Please enter some data")
        print("Should be 6 numbers")
        print("e.g 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

def validate_data(values):
    """
    Tries to convert all the strings vlaues into ints.
    Raise an error if they cant be converted or if 
    there are not exatly 6 values entered.
    """
    try:
        [int(v) for v in values]
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you entered {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True

get_sales_data()

