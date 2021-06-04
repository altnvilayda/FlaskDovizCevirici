from flask import Flask, render_template, request
import requests

api_key = ""
url = "http://data.fixer.io/api/latest?access_key=" + api_key


app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")

        amount = request.form.get("amount") #15
        response = request.get(url)
        app.logger.info(response)

        infos = response.json()
        firstValue = infos["rates"][firstCurrency]  #usd  1.231066
        secondValue = infos["rates"][secondCurrency] #tr    4.690815

        result = (secondValue/firstValue) * float(amount)

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
