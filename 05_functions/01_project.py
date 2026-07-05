def generate_report():
    fetch_sales()
    filter_valid_data()
    summarize_data()
    print("report is done!")

def fetch_sales():
    print("fetching the data.")

def filter_valid_data():
    print("filtering the data.")

def summarize_data():
    print("summarizing data.")

generate_report()

print("------------------------------------------------")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registered!")

def get_input():
    print("Getting input from user.")

def validate_input():
    print("Validating user input.")

def save_to_db():
    print("Saving user input to the database.")

register_user()