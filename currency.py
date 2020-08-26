from flask import Flask, render_template, request
import urllib, json
import datetime

file = open("req.txt","w+")
modules = dir()
list=[]
for i in modules: # I am not sure if I should this
    if i[0]!="_":
        list.append(i)
file.write("Modules: "+str(list)+ "\n\n\n")
file.close()



url = "https://api.exchangeratesapi.io/latest"
def request_call():
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return{
    "CAD":str(round(data.get("rates").get("TRY")/data.get("rates").get("CAD"),4)),
    "HKD":str(round(data.get("rates").get("TRY")/data.get("rates").get("HKD"),4)),
    "ISK":str(round(data.get("rates").get("TRY")/data.get("rates").get("ISK"),4)),
    "PHP":str(round(data.get("rates").get("TRY")/data.get("rates").get("PHP"),4)),
    "DKK":str(round(data.get("rates").get("TRY")/data.get("rates").get("DKK"),4)),
    "HUF":str(round(data.get("rates").get("TRY")/data.get("rates").get("HUF"),4)),
    "CZK":str(round(data.get("rates").get("TRY")/data.get("rates").get("CZK"),4)),
    "AUD":str(round(data.get("rates").get("TRY")/data.get("rates").get("AUD"),4)),
    "RON":str(round(data.get("rates").get("TRY")/data.get("rates").get("RON"),4)),
    "SEK":str(round(data.get("rates").get("TRY")/data.get("rates").get("SEK"),4)),
    "IDR":str(round(data.get("rates").get("TRY")/data.get("rates").get("IDR"),4)),
    "INR":str(round(data.get("rates").get("TRY")/data.get("rates").get("INR"),4)),
    "BRL":str(round(data.get("rates").get("TRY")/data.get("rates").get("BRL"),4)),
    "RUB":str(round(data.get("rates").get("TRY")/data.get("rates").get("RUB"),4)),
    "HRK":str(round(data.get("rates").get("TRY")/data.get("rates").get("HRK"),4)),
    "JPY":str(round(data.get("rates").get("TRY")/data.get("rates").get("JPY"),4)),
    "THB":str(round(data.get("rates").get("TRY")/data.get("rates").get("THB"),4)),
    "CHF":str(round(data.get("rates").get("TRY")/data.get("rates").get("CHF"),4)),
    "SGD":str(round(data.get("rates").get("TRY")/data.get("rates").get("SGD"),4)),
    "PLN":str(round(data.get("rates").get("TRY")/data.get("rates").get("PLN"),4)),
    "BGN":str(round(data.get("rates").get("TRY")/data.get("rates").get("BGN"),4)),
    "CNY":str(round(data.get("rates").get("TRY")/data.get("rates").get("CNY"),4)),
    "NOK":str(round(data.get("rates").get("TRY")/data.get("rates").get("NOK"),4)),
    "NZD":str(round(data.get("rates").get("TRY")/data.get("rates").get("NZD"),4)),
    "ZAR":str(round(data.get("rates").get("TRY")/data.get("rates").get("ZAR"),4)),
    "USD":str(round(data.get("rates").get("TRY")/data.get("rates").get("USD"),4)),
    "ILS":str(round(data.get("rates").get("TRY")/data.get("rates").get("ILS"),4)),
    "GBP":str(round(data.get("rates").get("TRY")/data.get("rates").get("GBP"),4)),
    "KRW":str(round(data.get("rates").get("TRY")/data.get("rates").get("KRW"),4)),
    "MYR":str(round(data.get("rates").get("TRY")/data.get("rates").get("MYR"),4)),
    "MXN":str(round(data.get("rates").get("TRY")/data.get("rates").get("MXN"),4)),
    "EUR":str(round(data.get("rates").get("TRY"),4))}

def write_user_agent():
    current_time = datetime.datetime.now()
    f = open("req.txt", "a+")
    browser = request.user_agent.browser
    os = request.user_agent.platform
    version = request.user_agent.version
    f.write("Operating System: " + os + "\nBrowser: " + browser + "\nVersion: " + version + "\nDate and Time: " + str(
        current_time) + "\n\n")
    f.close()


app=Flask(__name__)

@app.route("/")
def index():
    write_user_agent()
    dict=request_call()
    return render_template('demo.html', variable_EUR=dict.get("EUR"), variable_USD=dict.get("USD"), variable_JPY=dict.get("JPY"),
                           variable_GBP=dict.get("GBP"), variable_CNY=dict.get("CNY"), variable_CAD=dict.get("CAD"),
                           USD=dict.get("USD"), EUR=dict.get("EUR"), CAD=dict.get("CAD"), HKD=dict.get("HKD"), ISK=dict.get("ISK"),
                           PHP=dict.get("PHP"), DKK=dict.get("DKK"), HUF=dict.get("HUF"), CZK=dict.get("CZK"), AUD=dict.get("AUD"),
                           RON=dict.get("RON"), SEK=dict.get("SEK"), IDR=dict.get("IDR"), INR=dict.get("INR"), BRL=dict.get("BRL"),
                           RUB=dict.get("RUB"), HRK=dict.get("HRK"), JPY=dict.get("JPY"), THB=dict.get("THB"), CHF=dict.get("CHF"),
                           SGD=dict.get("SGD"), PLN=dict.get("PLN"), BGN=dict.get("BGN"), CNY=dict.get("CNY"), NOK=dict.get("NOK"),
                           NZD=dict.get("NZD"), ZAR=dict.get("ZAR"), MXN=dict.get("MXN"), ILS=dict.get("ILS"), GBP=dict.get("GBP"),
                           KRW=dict.get("KRW"), MYR=dict.get("MYR"))

@app.route("/eur")
def euro():
    write_user_agent()
    dict = request_call()
    return render_template('money.html', title="EUR", money="EUR", oran=dict.get("EUR"))
@app.route("/usd")
def usd():
    write_user_agent()
    dict = request_call()
    return render_template('money.html', title="USD", money="USD", oran=dict.get("USD"))
@app.route("/jpy")
def jpy():
    write_user_agent()
    dict = request_call()
    return render_template('money.html', title="JPY", money="JPY", oran=dict.get("JPY"))
@app.route("/cny")
def cny():
    write_user_agent()
    dict = request_call()
    return render_template('money.html', title="CNY", money="CNY", oran=dict.get("CNY"))
@app.route("/gbp")
def gbp():
    write_user_agent()
    dict = request_call()
    return render_template('money.html', title="GBP", money="GBP", oran=dict.get("GBP"))
@app.route("/cad")
def cad():
    write_user_agent()
    dict = request_call()
    return render_template('money.html', title="CAD", money="CAD", oran=dict.get("CAD"))



if __name__ == "__main__":
    app.run(debug = True)

