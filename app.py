from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# -------------------- Currency List --------------------
currencies = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "CNY": "Chinese Yuan",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "INR": "Indian Rupee",
    "BRL": "Brazilian Real",
    "ZAR": "South African Rand",
    "AED": "UAE Dirham",
    "SAR": "Saudi Riyal",
    "EGP": "Egyptian Pound",
    "MAD": "Moroccan Dirham",
    "RUB": "Russian Ruble",
    "TRY": "Turkish Lira",
    "SEK": "Swedish Krona",
    "NOK": "Norwegian Krone",
    "DKK": "Danish Krone",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "NZD": "New Zealand Dollar",
    "THB": "Thai Baht",
    "IDR": "Indonesian Rupiah",
    "PLN": "Polish Zloty",
    "CZK": "Czech Koruna",
    "HUF": "Hungarian Forint",
    "CLP": "Chilean Peso",
    "PHP": "Philippine Peso"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    amount = ""
    from_currency = "USD"
    to_currency = "EUR"

    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            from_currency = request.form["from_currency"]
            to_currency = request.form["to_currency"]

            # -------------------- Fetch exchange rate from API --------------------
            url = f"https://open.er-api.com/v6/latest/{from_currency}"
            response = requests.get(url, timeout=10).json()

            if response.get("result") == "success" and "rates" in response:
                if to_currency in response["rates"]:
                    rate = response["rates"][to_currency]
                    result = round(amount * rate, 2)
                else:
                    error = f"Currency {to_currency} not found in API rates."
            else:
                error = "Failed to fetch exchange rates from API."

        except ValueError:
            error = "Please enter a valid number."
        except requests.RequestException as e:
            error = f"Connection error: {e}"

    return render_template(
        "index.html",
        currencies=currencies,
        result=result,
        error=error,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency
    )

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/notepad")
def notepad():
    return render_template("notepad.html")

if __name__ == "__main__":
    app.run(debug=True)