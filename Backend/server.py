from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel): # for automated validation
   # expense_date : date we can omit this cuz we don't need the date in every query as we already know for which date we are querying
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date



@app.get("/expenses/{expense_date}", response_model = List[Expense])
def get_expenses(expense_date : date): # with ':' we give typehints
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from database")
    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date : date, expenses : List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message" : "Expenses updated successfully"}

@app.post("/analytics")
def get_analytics(date_range : DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None :
        raise HTTPException(status_code = 500, detail= "Failed to retrieve expense summary from database")

    total = sum([row['total'] for row in data])

    breakdown ={}
    for row in data:
        percentage = (row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']] ={
            'total' : row['total'],
            'percentage' : percentage
        }

    return breakdown

@app.get("/monthly_analytics")
def get_monthly_analytics():
    data = db_helper.fetch_monthly_expenses()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from database")
    return data





# To run this server in terminal :PS C:\Code\Project_Expense_Tracker\backend> uvicorn server:app --reload