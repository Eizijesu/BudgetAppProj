import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask import Flask, request, render_template, jsonify

# Read CSV file
df = pd.read_csv("WebApp2.csv")

# Define features (income and expenses) and target (savings)
X = df[["Income", "Rent", "Utilities", "Groceries", "Transportation", "Entertainment"]]
y = df["Savings"]

# Create and fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Define Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"], endpoint="predict")
def predict():
    # Get user input from form
    income = float(request.form.get('income', 0.0))
    rent = float(request.form.get("rent", 0.0))
    
    # Check if the keys exist in the request form before accessing their values
    utilities = float(request.form.get("utilities", 0.0))
    groceries = float(request.form.get("groceries", 0.0))
    transportation = float(request.form.get("transportation", 0.0))
    entertainment = float(request.form.get("entertainment", 0.0))
    goal = float(request.form.get("goal", 0.0))

    # Create and fit linear regression model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model.fit(X_train, y_train)

    # Predict savings for test set
    y_pred = model.predict(X_test)

    # Perform budget optimization
    response = budget_optimizer(income, rent, utilities, groceries, transportation, entertainment, goal, y_pred[0])

    return jsonify(response)

def budget_optimizer(income, rent_input, utilities_input, groceries_input, transportation_input, entertainment_input, goal, predicted_savings):
    # Perform budget optimization and generate response

    response = {
        "predicted_savings": predicted_savings,
        # Include other relevant response data
    }

    return response

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
