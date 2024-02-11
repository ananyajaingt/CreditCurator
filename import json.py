import json
REGION="us-east-1"

def lambda_handler(event,context):
    student = event['body-json']['isStudent']
    income = event['body-json']['monthlyIncome']
    groceries = event['body-json']['groceries']
    food = event['body-json']['food']
    gas = event['body-json']['gas']
    travel = event['body-json']['travel']
    pay = event['body-json']['payFull']
    travelOft = event['body-json']['travelOften']
    history = event['body-json']['creditHistory']




    print(student)
    print(income)
    print(groceries)
    print(food)
    print(gas)
    print(travel)
    print(pay)
    print(travelOft)
    print(history)