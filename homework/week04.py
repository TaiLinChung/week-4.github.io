from flask import Flask #載入Flask
from flask import request  #載入request物件
from flask import render_template #載入render_template
from flask import redirect
from flask import session
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="any string but secret"

#使用GET方法，處理路徑/的對應函式
@app.route("/")
def index():
    return render_template("indexW04.html")


#使用POST方法，處理路徑/signin 的對應函式
@app.route("/signin", methods=["POST"])
def signin():
    #接收 POST 方法的 Query String
    account=request.form["account"]
    password=request.form["password"]
    session["account"]=account
    session["password"]=password

    if (account=="test" and password=="test") or  session["key"]=="pass":
        session["key"]="pass"
        return redirect("/member")
    elif (account=="" or password=="") and  session["key"]!="pass":
        session["errormessage"]="請輸入帳號、密碼"
        return redirect("/connect")
    else:
        session["key"]="close"
        session["errormessage"]="帳號、或密碼錯誤"
        return redirect("/connect")


##想法 做一個跳板丟訊息給/error，/error?message=errormessage
@app.route("/connect")
def connect():
    errormessage=session["errormessage"]
    # errormessage="6666666"
    return redirect("http://127.0.0.1:3000/error?message="+errormessage)

    
    
#想法，若未滿足 pass 則導回route("/")
#使用POST方法，處理路徑/member 的對應函式
@app.route("/member")
def member():
    if session["key"]=="pass":
        return render_template("memberW04.html")
    else:
        return redirect("/")


##-----把上面的帳密存起來，放到下面用
#利用要求字串(Query String)提供彈性:/error?message=自訂文字  
@app.route("/error")
def error():
    customize=request.args.get("message","帳號、或密碼錯誤")
    # print(str(customize))
    # return "error"
    return render_template("errorW04.html",content=str(customize))

@app.route("/signout")
def signout():
    session["key"]="close"
    return redirect("/") #導向回到主頁路徑

@app.route("/square" ,methods=["GET"])
def square1():
    number=request.args.get("number","")
    if number=="":
        # return redirect("/")
        return render_template("errorW04.html",content="請輸入要計算的數字")
    # number=int(number)
    # number=number*number
    # return render_template("caculate2W04.html",content=str(number))
    else:
        return redirect("http://127.0.0.1:3000/square/"+number)
##----------

@app.route("/square/<num>")
def square(num):
    # return num
    return render_template("caculateW04.html",content=str(num))


# ##實作跳轉網址
# @app.route("/connect")
# def connect():
#     return redirect("http://127.0.0.1:3000/getSum?message=帳號、密碼錯誤")


# @app.route("/getSum")
# def getSum():
#     maxNum=request.args.get("message",100)
#     # result=0
#     # for i in range(1,101):
#     #     result+=i
#     return str(maxNum)



#啟動網站伺服器，可透過port參數指定埠號
app.run(port=3000)
