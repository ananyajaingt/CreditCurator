from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('curator.html')  # Assuming you have an index.html file in a folder named 'templates'
@app.route('/page2')
def page2():
    return render_template('curator.html')

@app.route('/page3')
def page3():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        # Extracting the data from the form
        input_data = request.form['input_data']
        print(input_data)
        
        # Call your algorithm function here, passing the input_data
        result = calcCards(input_data)
        
        # You can then pass the result to a template or simply return it as a response
        return render_template('result.html', result=result)
    else:
        return 'Method Not Allowed', 405

# if bank = discover, welcome bonus = cashback

def calcCards(userInfo):

    d = {"Card" : "", "Bank": "", "CB_Groceries" : 0, "CB_Food" : 0,"CB_Gas" : 0,"CB_Travel" : 0,"CB_Other" : 0,
        "P_Groceries" : 0,"P_Food" : 0,"P_Gas" : 0,"P_Travel" : 0,"P_Other" : 0, "Value_of_point": 0, "APR": 0, "annual_fee" : 0,
        "late_fee": 0, "travel": False, "isStudent": False, "FICO_Score": 0, "Welcome_CB": 0, "Welcome_points": 0,
        "Spending_min": 0, "Time_Days": 0, "EstimatedCB": 0, "EstimatedPoints": 0, "welcome_obtained": 0, "Score": 0,}

    main_dict = {'0': {'Card': 'The Platinum Card', 'Bank': 'American Express', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.0, 'P_Food': 1.0, 'P_Gas': 1.0, 'P_Travel': 5.0, 'P_Other': 1.0, 'Value_of_point': 0.007, 'APR': 0.2124, 'annual_fee': 695.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0.0, 'Welcome_points': 80000.0, 'Spending_min': 8000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '1': {'Card': 'American Express Green Card', 'Bank': 'American Express', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.0, 'P_Food': 3.0, 'P_Gas': 0.0, 'P_Travel': 3.0, 'P_Other': 1.0, 'Value_of_point': 0.007, 'APR': 0.2124, 'annual_fee': 150.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 0.0, 'Welcome_points': 40000.0, 'Spending_min': 3000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '2': {'Card': 'American Everyday Credit Card', 'Bank': 'American Express', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 1.0, 'P_Gas': 1.0, 'P_Travel': 1.0, 'P_Other': 1.0, 'Value_of_point': 0.007, 'APR': 0.1824, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0.0, 'Welcome_points': 10000.0, 'Spending_min': 2000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '3': {'Card': 'American Everyday Preferred Credit  Card', 'Bank': 'American Express', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 3.0, 'P_Food': 2.0, 'P_Gas': 1.0, 'P_Travel': 1.0, 'P_Other': 1.0, 'Value_of_point': 0.007, 'APR': 0.1824, 'annual_fee': 95.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 0.0, 'Welcome_points': 15000.0, 'Spending_min': 2000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '4': {'Card': 'Blue Cash Preferred Card', 'Bank': 'American Express', 'CB_Groceries': 0.06, 'CB_Food': 0.0, 'CB_Gas': 0.03, 'CB_Travel': 0.03, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.007, 'APR': 0.1924, 'annual_fee': 95.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 300.0, 'Welcome_points': 0.0, 'Spending_min': 3000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '5': {'Card': 'Blue Cash Everyday Card', 'Bank': 'American Express', 'CB_Groceries': 0.03, 'CB_Food': 0.01, 'CB_Gas': 0.03, 'CB_Travel': 0.01, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.007, 'APR': 0.0, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 2000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '6': {'Card': 'Cash Magnet Card', 'Bank': 'American Express', 'CB_Groceries': 0.015, 'CB_Food': 0.015, 'CB_Gas': 0.015, 'CB_Travel': 0.015, 'CB_Other': 0.015, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.007, 'APR': 0.1924, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 2000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '7': {'Card': 'Delta SkyMiles Gold American Express Card', 'Bank': 'American Express', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 2.0, 'P_Gas': 1.0, 'P_Travel': 1.0, 'P_Other': 0.0, 'Value_of_point': 0.007, 'APR': 0.2099, 'annual_fee': 150.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0.0, 'Welcome_points': 70000.0, 'Spending_min': 3000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '8': {'Card': 'Delta SkyMiles Platinum American Express Card', 'Bank': 'American Express', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 2.0, 'P_Gas': 1.0, 'P_Travel': 3.0, 'P_Other': 1.0, 'Value_of_point': 0.007, 'APR': 0.2099, 'annual_fee': 350.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0.0, 'Welcome_points': 90000.0, 'Spending_min': 4000.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '9': {'Card': 'Unlimited Cash Rewards', 'Bank': 'Bank of America', 'CB_Groceries': 0.015, 'CB_Food': 0.015, 'CB_Gas': 0.015, 'CB_Travel': 0.015, 'CB_Other': 0.02, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1824, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 100.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '10': {'Card': 'Travel Rewards', 'Bank': 'Bank of America', 'CB_Groceries': 0.02, 'CB_Food': 0.02, 'CB_Gas': 0.02, 'CB_Travel': 0.02, 'CB_Other': 0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1824, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0.0, 'Welcome_points': 25000.0, 'Spending_min': 1000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '11': {'Card': 'BankAmericard', 'Bank': 'Bank of America', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1624, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '12': {'Card': 'Premiuim Rewards', 'Bank': 'Bank of America', 'CB_Groceries': 0.015, 'CB_Food': 0.015, 'CB_Gas': 0.015, 'CB_Travel': 0.02, 'CB_Other': 0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.2024, 'annual_fee': 95.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 600.0, 'Welcome_points': 0.0, 'Spending_min': 4000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '13': {'Card': 'Sapphire Preffered', 'Bank': 'Chase', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.2149, 'annual_fee': 95.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 0.0, 'Welcome_points': 60000.0, 'Spending_min': 4000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '14': {'Card': 'Freedom Unlimited', 'Bank': 'Chase', 'CB_Groceries': 0.05, 'CB_Food': 0.03, 'CB_Gas': 0.05, 'CB_Travel': 0.05, 'CB_Other': 0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.2049, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 500.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '15': {'Card': 'Ink Business Unlimited Credit Card', 'Bank': 'Chase', 'CB_Groceries': 0.02, 'CB_Food': 0.02, 'CB_Gas': 0.02, 'CB_Travel': 0.02, 'CB_Other': 0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1849, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 750.0, 'Welcome_points': 0.0, 'Spending_min': 6000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '16': {'Card': 'Sapphire Reserve', 'Bank': 'Chase', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.0, 'P_Food': 3.0, 'P_Gas': 1.0, 'P_Travel': 3.0, 'P_Other': 1.0, 'Value_of_point': 0.01, 'APR': 0.2249, 'annual_fee': 550.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0.0, 'Welcome_points': 60000.0, 'Spending_min': 4000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '17': {'Card': 'IHG One Rewards Traveler Credit Card', 'Bank': 'Chase', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 3.0, 'P_Gas': 3.0, 'P_Travel': 5.0, 'P_Other': 3.0, 'Value_of_point': 0.01, 'APR': 0.2159, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0.0, 'Welcome_points': 100000.0, 'Spending_min': 2000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '18': {'Card': 'Platinum Mastercard', 'Bank': 'Capital One', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.01, 'APR': 0.3074, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 2, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '19': {'Card': 'Venture X Rewards', 'Bank': 'Capital One', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 2.0, 'P_Gas': 2.0, 'P_Travel': 7.5, 'P_Other': 2.0, 'Value_of_point': 0.008, 'APR': 0.1999, 'annual_fee': 395.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 0.0, 'Welcome_points': 75000.0, 'Spending_min': 4000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '20': {'Card': 'Venture Rewards', 'Bank': 'Capital One', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 2.0, 'P_Gas': 2.0, 'P_Travel': 5.0, 'P_Other': 2.0, 'Value_of_point': 0.008, 'APR': 0.1999, 'annual_fee': 95.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 0.0, 'Welcome_points': 75000.0, 'Spending_min': 4000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '21': {'Card': 'VentureOne Rewards', 'Bank': 'Capital One', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.25, 'P_Food': 1.25, 'P_Gas': 1.25, 'P_Travel': 5.0, 'P_Other': 1.25, 'Value_of_point': 0.008, 'APR': 0.1999, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 0.0, 'Welcome_points': 20000.0, 'Spending_min': 500.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '22': {'Card': 'Platinum Secured', 'Bank': 'Capital One', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.009, 'APR': 0.3074, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 1, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '23': {'Card': 'Quicksilver Rewards', 'Bank': 'Capital One', 'CB_Groceries': 0.015, 'CB_Food': 0.015, 'CB_Gas': 0.015, 'CB_Travel': 0.015, 'CB_Other': 0.02, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.009, 'APR': 0.1999, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 500.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '24': {'Card': 'SavorOne Rewards for Students', 'Bank': 'Capital One', 'CB_Groceries': 0.03, 'CB_Food': 0.03, 'CB_Gas': 0.01, 'CB_Travel': 0.01, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.009, 'APR': 0.1999, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': True, 'FICO_Score': 2, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '25': {'Card': 'VentureOne Rewards for Good Credit', 'Bank': 'Capital One', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.25, 'P_Food': 1.25, 'P_Gas': 1.25, 'P_Travel': 1.25, 'P_Other': 1.25, 'Value_of_point': 0.009, 'APR': 0.1999, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '26': {'Card': 'Diamond Preferred Card', 'Bank': 'Citi', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1824, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': False, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '27': {'Card': 'Premier Card', 'Bank': 'Citi', 'CB_Groceries': 0.03, 'CB_Food': 0.03, 'CB_Gas': 0.03, 'CB_Travel': 0.03, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.2124, 'annual_fee': 95.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 4, 'Welcome_CB': 600.0, 'Welcome_points': 0.0, 'Spending_min': 4000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '28': {'Card': 'Double Cash Card', 'Bank': 'Citi', 'CB_Groceries': 0.02, 'CB_Food': 0.02, 'CB_Gas': 0.02, 'CB_Travel': 0.02, 'CB_Other': 0.02, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1924, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 1500.0, 'Time_Days': 180.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '29': {'Card': 'Rewards+ Credit Card', 'Bank': 'Citi', 'CB_Groceries': 0.02, 'CB_Food': 0.01, 'CB_Gas': 0.01, 'CB_Travel': 0.01, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1874, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 1500.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '30': {'Card': 'Costco Anywhere Visa Credit Card by Citi', 'Bank': 'Citi', 'CB_Groceries': 0.01, 'CB_Food': 0.03, 'CB_Gas': 0.04, 'CB_Travel': 0.02, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.2049, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '31': {'Card': 'Secured Mastercard Credit Card', 'Bank': 'Citi', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.2774, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': False, 'isStudent': True, 'FICO_Score': 1, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '32': {'Card': 'Cash Back Credit Card', 'Bank': 'Discover', 'CB_Groceries': 0.05, 'CB_Food': 0.05, 'CB_Gas': 0.05, 'CB_Travel': 0.01, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1724, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '33': {'Card': 'Student Cash Back', 'Bank': 'Discover', 'CB_Groceries': 0.05, 'CB_Food': 0.05, 'CB_Gas': 0.05, 'CB_Travel': 0.01, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1724, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': True, 'FICO_Score': 2, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '34': {'Card': 'Secured it Credit Card', 'Bank': 'Discover', 'CB_Groceries': 0.01, 'CB_Food': 0.02, 'CB_Gas': 0.02, 'CB_Travel': 0.01, 'CB_Other': 0.01, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.0, 'APR': 0.1724, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 2, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '35': {'Card': 'Travel Credit Card', 'Bank': 'Discover', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.5, 'P_Food': 1.5, 'P_Gas': 1.5, 'P_Travel': 1.5, 'P_Other': 1.5, 'Value_of_point': 0.01, 'APR': 0.1724, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '36': {'Card': 'Active Cash Card', 'Bank': 'Wells Fargo', 'CB_Groceries': 0.02, 'CB_Food': 0.02, 'CB_Gas': 0.02, 'CB_Travel': 0.02, 'CB_Other': 0.02, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.01, 'APR': 0.2025, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 500.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '37': {'Card': 'Autograph Card', 'Bank': 'Wells Fargo', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 3.0, 'P_Gas': 3.0, 'P_Travel': 3.0, 'P_Other': 0, 'Value_of_point': 0.01, 'APR': 0.2024, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 200.0, 'Welcome_points': 0.0, 'Spending_min': 1000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '38': {'Card': 'Reflect Card', 'Bank': 'Wells Fargo', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.01, 'APR': 0.1824, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '39': {'Card': 'Choice Privileges Mastercard', 'Bank': 'Wells Fargo', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 3.0, 'P_Food': 3.0, 'P_Gas': 3.0, 'P_Travel': 5.0, 'P_Other': 0, 'Value_of_point': 0.01, 'APR': 0.2099, 'annual_fee': 0.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0.0, 'Welcome_points': 40000.0, 'Spending_min': 1000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '40': {'Card': 'Choice Privileges Select Mastercard', 'Bank': 'Wells Fargo', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 3.0, 'P_Food': 3.0, 'P_Gas': 3.0, 'P_Travel': 10.0, 'P_Other': 0, 'Value_of_point': 0.01, 'APR': 0.2099, 'annual_fee': 95.0, 'late_fee': 40.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0.0, 'Welcome_points': 60000.0, 'Spending_min': 1000.0, 'Time_Days': 90.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '41': {'Card': 'Premier World Mastercard', 'Bank': 'Synchrony', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 2.0, 'P_Food': 2.0, 'P_Gas': 2.0, 'P_Travel': 2.0, 'P_Other': 2.0, 'Value_of_point': 0.01, 'APR': 0.1924, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '42': {'Card': 'Plus World Mastercard', 'Bank': 'Synchrony', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 1.0, 'P_Food': 1.0, 'P_Gas': 1.0, 'P_Travel': 1.0, 'P_Other': 1.0, 'Value_of_point': 0.01, 'APR': 0.1924, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '43': {'Card': 'Preferred Mastercard', 'Bank': 'Synchrony', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.01, 'APR': 0.1674, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': False, 'isStudent': True, 'FICO_Score': 2, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '44': {'Card': 'Luxury Credit Card', 'Bank': 'Synchrony', 'CB_Groceries': 0.0, 'CB_Food': 0.08, 'CB_Gas': 0.0, 'CB_Travel': 0.08, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.01, 'APR': 0.2999, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': True, 'isStudent': False, 'FICO_Score': 5, 'Welcome_CB': 0, 'Welcome_points': 0, 'Spending_min': 0, 'Time_Days': 0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0},
             '45': {'Card': 'Outdoors Credit Card', 'Bank': 'Synchrony', 'CB_Groceries': 0.0, 'CB_Food': 0.0, 'CB_Gas': 0.0, 'CB_Travel': 0.0, 'CB_Other': 0.0, 'P_Groceries': 0.0, 'P_Food': 0.0, 'P_Gas': 0.0, 'P_Travel': 0.0, 'P_Other': 0.0, 'Value_of_point': 0.01, 'APR': 0.2999, 'annual_fee': 0.0, 'late_fee': 41.0, 'travel': False, 'isStudent': False, 'FICO_Score': 3, 'Welcome_CB': 199.0, 'Welcome_points': 0.0, 'Spending_min': 0.0, 'Time_Days': 1.0, 'EstimatedCB': 0, 'EstimatedPoints': 0, 'welcome_obtained': 0, 'Score': 0}}

    monthly_spending = userInfo['monthlyGroceries'] + userInfo['monthlyFood'] + userInfo['monthlyGas'] + userInfo['monthlyTravel'] + userInfo['monthlyOther']
    monthly_debt = monthly_spending - userInfo['monthlyIncome']
    if monthly_debt > 0:
        paymentRate = userInfo['onTimeRate'] - 0.15
        if paymentRate < 0:
            paymentRate = 0
            for entry in main_dict:
                main_dict[entry]["Score"] = main_dict[entry]["Score"] - ((1 - paymentRate) * monthly_debt * d1["APR"]) * 1.5

    d2 = main_dict.copy()
    for entry in main_dict:
        if main_dict[entry]["FICO_Score"] > userInfo['CreditLevel'] or main_dict[entry]["FICO_Score"] + 1 < userInfo['CreditLevel']:
            d2.pop(entry)
            continue
        if main_dict[entry]["annual_fee"] > userInfo['annualFeeMax']:
            d2.pop(entry)
            continue
        d2[entry]["EstimatedCB"] = (userInfo["monthlyGroceries"] * d2[entry]["CB_Groceries"]) + (userInfo["monthlyFood"] * d2[entry]["CB_Food"]) + (userInfo["monthlyGas"] * d2[entry]["CB_Gas"]) + (userInfo["monthlyTravel"] * d2[entry]["CB_Travel"]) + (userInfo["monthlyOther"] * d2[entry]["CB_Other"])
        d2[entry]["EstimatedPoints"] = (userInfo["monthlyGroceries"] * d2[entry]["P_Groceries"]) + (userInfo["monthlyFood"] * d2[entry]["P_Food"]) + (userInfo["monthlyGas"] * d2[entry]["P_Gas"]) + (userInfo["monthlyTravel"] * d2[entry]["P_Travel"]) + (userInfo["monthlyOther"] * d2[entry]["P_Other"])
        d2[entry]["Score"] = d2[entry]["EstimatedCB"] + (d2[entry]["EstimatedPoints"] * d2[entry]["Value_of_point"]) * 2
        if d2[entry]["Bank"] == "Discover":
            d2[entry]["Score"] = d2[entry]["Score"] + (d2[entry]["EstimatedCB"] + (d2[entry]["EstimatedPoints"] * d2[entry]["Value_of_point"])) / 10
        if (monthly_spending / 30) * d2[entry]["Time_Days"] >= d2[entry]["Spending_min"]:
            d2[entry]["Score"] = d2[entry]["Score"] + (d2[entry]["Welcome_CB"] + (d2[entry]["Welcome_points"] * d2[entry]["Value_of_point"])) / 10
    main_dict = d2

    d2 = main_dict.copy()
    if userInfo['travelsOften']:
        for entry in main_dict:
            if main_dict[entry]["travel"] == True:
                if main_dict[entry]["Score"] > 0:
                    main_dict[entry]["Score"] = main_dict[entry]["Score"] * 1.5
                else:
                    main_dict[entry]["Score"] = main_dict[entry]["Score"] + 200
    main_dict = d2

    for entry in main_dict:
            if main_dict[entry]["isStudent"] == userInfo['isStudent']:
                if main_dict[entry]["Score"] > 0:
                    main_dict[entry]["Score"] = main_dict[entry]["Score"] * 2
                else:
                    main_dict[entry]["Score"] = main_dict[entry]["Score"] + 200
    

    best = (None, -99999999)
    second = (None, -99999999)

    for entry in main_dict: 
        if main_dict[entry]["Score"] > best[1]:
            second = best
            best = (main_dict[entry], main_dict[entry]["Score"])
        elif main_dict[entry]["Score"] > second[1]:
            second = (main_dict[entry], main_dict[entry]["Score"])

    return (best, second)   
            
# Main Method 
#userInfo = {'isStudent': True, 'monthlyIncome': 2000, 'annualFeeMax': 0,
#               'travelsOften': True, 'CreditLevel': 4, 'monthlyGroceries': 500, 'monthlyFood': 200,
#              'monthlyGas': 100, 'monthlyTravel': 50, 'monthlyOther': 200, 'onTimeRate': .9}

#output =  calcCards(userInfo)

#print("The best card for you would be the " + output[0][0]["Card"] + " from " + output[0][0]["Bank"] + ".")
#print("Another good option is the " + output[1][0]["Card"] + " from " + output[1][0]["Bank"] + ".")
