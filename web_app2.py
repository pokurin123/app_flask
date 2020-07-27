from flask import Flask, render_template ,request
import pymysql
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
auth = HTTPBasicAuth()
# パスワード
users = {
    "user": "password",
}
# db
def getConnection():
    return pymysql.connect(
        host='localhost',
        db='subject_db',
        user='root',
        password='taiki0831',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
# セレクトボックスの中身
subjects = ["3学期「英語2C」 月曜2",#1
"3学期「データと経済統計」 月曜3-4限",#2
"3学期「人工知能デザイン演習1」 水曜1-2限",#3
"３学期「マーケティングデータ分析」 水曜3限",#4
"３学期「未来創造PJ」 水曜4-5限",#5
"３学期「英語2D」 金曜3限",#6
"３学期「データと計量経済学」 金曜4-５限",#7
"4学期 「英語2C」 月曜２限",#8
"４学期「人工知能システム」 水曜4-5限",#9
"４学期「マーケティングデータ分析」 水曜3限",#10
"４学期「未来創造PJ」 水曜4-5限",#11
"４学期「複合現実」 木曜3-4限",#12
"４学期「サイバーフィジカルシステム」 金曜1-2限",#13
"４学期「英語2D」 金曜3限",#14
"４学期「人工知能デザイン演習2」 金曜4-5限"#15
]

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route("/")
@auth.login_required
def home():
    return render_template("home.html",subjects=subjects)

@app.route("/result",methods=["POST"])
def result():
    connection = getConnection()
    subject_name = request.form["subjects"]
    #1
    if subject_name == "3学期「英語2C」 月曜2":
        sql = "select syllabus from subject_table where subject='3学期「英語2C」 月曜2'"
        sql1 = "select date1 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql2 = "select date2 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql3 = "select date3 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql4 = "select date4 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql5 = "select date5 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql6 = "select date6 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql7 = "select date7 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql8 = "select date8 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql9 = "select date9 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql10 = "select date10 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql11 = "select date11 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql12 = "select date12 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql13 = "select date13 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql14 = "select date14 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql15 = "select date15 from subject_table where subject='3学期「英語2C」 月曜2'"
        sql16 = "select date16 from subject_table where subject='3学期「英語2C」 月曜2'"
    #2
    elif subject_name == "3学期「データと経済統計」 月曜3-4限":
        sql = "select syllabus from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql1 = "select date1 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql2 = "select date2 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql3 = "select date3 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql4 = "select date4 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql5 = "select date5 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql6 = "select date6 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql7 = "select date7 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql8 = "select date8 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql9 = "select date9 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql10 = "select date10 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql11 = "select date11 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql12 = "select date12 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql13 = "select date13 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql14 = "select date14 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql15 = "select date15 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
        sql16 = "select date16 from subject_table where subject='3学期「データと経済統計」 月曜3-4限'"
    #3
    elif subject_name == "3学期「人工知能デザイン演習1」 水曜1-2限":
        sql = "select syllabus from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql1 = "select date1 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql2 = "select date2 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql3 = "select date3 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql4 = "select date4 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql5 = "select date5 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql6 = "select date6 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql7 = "select date7 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql8 = "select date8 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql9 = "select date9 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql10 = "select date10 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql11 = "select date11 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql12 = "select date12 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql13 = "select date13 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql14 = "select date14 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql15 = "select date15 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
        sql16 = "select date16 from subject_table where subject='3学期「人工知能デザイン演習1」 水曜1-2限'"
    #4
    elif subject_name == "３学期「マーケティングデータ分析」 水曜3限":
        sql = "select syllabus from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql1 = "select date1 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql2 = "select date2 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql3 = "select date3 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql4 = "select date4 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql5 = "select date5 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql6 = "select date6 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql7 = "select date7 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql8 = "select date8 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql9 = "select date9 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql10 = "select date10 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql11 = "select date11 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql12 = "select date12 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql13 = "select date13 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql14 = "select date14 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql15 = "select date15 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
        sql16 = "select date16 from subject_table where subject='３学期「マーケティングデータ分析」 水曜3限'"
    #5
    elif subject_name == "３学期「未来創造PJ」 水曜4-5限":
        sql = "select syllabus from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql1 = "select date1 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql2 = "select date2 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql3 = "select date3 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql4 = "select date4 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql5 = "select date5 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql6 = "select date6 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql7 = "select date7 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql8 = "select date8 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql9 = "select date9 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql10 = "select date10 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql11 = "select date11 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql12 = "select date12 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql13 = "select date13 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql14 = "select date14 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql15 = "select date15 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
        sql16 = "select date16 from subject_table where subject='３学期「未来創造PJ」 水曜4-5限'"
    #6
    elif subject_name == "３学期「英語2D」 金曜3限":
        sql = "select syllabus from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql1 = "select date1 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql2 = "select date2 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql3 = "select date3 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql4 = "select date4 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql5 = "select date5 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql6 = "select date6 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql7 = "select date7 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql8 = "select date8 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql9 = "select date9 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql10 = "select date10 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql11 = "select date11 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql12 = "select date12 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql13 = "select date13 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql14 = "select date14 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql15 = "select date15 from subject_table where subject='３学期「英語2D」 金曜3限'"
        sql16 = "select date16 from subject_table where subject='３学期「英語2D」 金曜3限'"
    #7
    elif subject_name == "３学期「データと計量経済学」 金曜4-５限":
        sql = "select syllabus from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql1 = "select date1 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql2 = "select date2 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql3 = "select date3 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql4 = "select date4 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql5 = "select date5 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql6 = "select date6 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql7 = "select date7 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql8 = "select date8 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql9 = "select date9 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql10 = "select date10 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql11 = "select date11 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql12 = "select date12 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql13 = "select date13 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql14 = "select date14 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql15 = "select date15 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
        sql16 = "select date16 from subject_table where subject='３学期「データと計量経済学」 金曜4-５限'"
    #8
    elif subject_name == "4学期 「英語2C」 月曜２限":
        sql = "select syllabus from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql1 = "select date1 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql2 = "select date2 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql3 = "select date3 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql4 = "select date4 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql5 = "select date5 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql6 = "select date6 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql7 = "select date7 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql8 = "select date8 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql9 = "select date9 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql10 = "select date10 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql11 = "select date11 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql12 = "select date12 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql13 = "select date13 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql14 = "select date14 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql15 = "select date15 from subject_table where subject='4学期 「英語2C」 月曜２限'"
        sql16 = "select date16 from subject_table where subject='4学期 「英語2C」 月曜２限'"
    #9
    elif subject_name == "４学期「人工知能システム」 水曜4-5限":
        sql = "select syllabus from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql1 = "select date1 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql2 = "select date2 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql3 = "select date3 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql4 = "select date4 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql5 = "select date5 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql6 = "select date6 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql7 = "select date7 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql8 = "select date8 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql9 = "select date9 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql10 = "select date10 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql11 = "select date11 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql12 = "select date12 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql13 = "select date13 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql14 = "select date14 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql15 = "select date15 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
        sql16 = "select date16 from subject_table where subject='４学期「人工知能システム」 水曜4-5限'"
    #10
    elif subject_name == "４学期「マーケティングデータ分析」 水曜3限":
        sql = "select syllabus from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql1 = "select date1 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql2 = "select date2 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql3 = "select date3 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql4 = "select date4 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql5 = "select date5 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql6 = "select date6 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql7 = "select date7 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql8 = "select date8 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql9 = "select date9 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql10 = "select date10 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql11 = "select date11 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql12 = "select date12 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql13 = "select date13 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql14 = "select date14 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql15 = "select date15 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
        sql16 = "select date16 from subject_table where subject='４学期「マーケティングデータ分析」 水曜3限'"
    #11
    elif subject_name == "４学期「未来創造PJ」 水曜4-5限":
        sql = "select syllabus from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql1 = "select date1 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql2 = "select date2 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql3 = "select date3 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql4 = "select date4 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql5 = "select date5 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql6 = "select date6 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql7 = "select date7 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql8 = "select date8 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql9 = "select date9 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql10 = "select date10 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql11 = "select date11 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql12 = "select date12 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql13 = "select date13 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql14 = "select date14 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql15 = "select date15 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
        sql16 = "select date16 from subject_table where subject='４学期「未来創造PJ」 水曜4-5限'"
    #12
    elif subject_name == "４学期「複合現実」 木曜3-4限":
        sql = "select syllabus from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql1 = "select date1 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql2 = "select date2 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql3 = "select date3 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql4 = "select date4 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql5 = "select date5 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql6 = "select date6 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql7 = "select date7 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql8 = "select date8 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql9 = "select date9 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql10 = "select date10 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql11 = "select date11 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql12 = "select date12 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql13 = "select date13 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql14 = "select date14 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql15 = "select date15 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
        sql16 = "select date16 from subject_table where subject='４学期「複合現実」 木曜3-4限'"
    #13
    elif subject_name == "４学期「サイバーフィジカルシステム」 金曜1-2限":
        sql = "select syllabus from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql1 = "select date1 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql2 = "select date2 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql3 = "select date3 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql4 = "select date4 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql5 = "select date5 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql6 = "select date6 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql7 = "select date7 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql8 = "select date8 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql9 = "select date9 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql10 = "select date10 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql11 = "select date11 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql12 = "select date12 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql13 = "select date13 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql14 = "select date14 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql15 = "select date15 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
        sql16 = "select date16 from subject_table where subject='４学期「サイバーフィジカルシステム」 金曜1-2限'"
    #14
    elif subject_name == "４学期「英語2D」 金曜3限":
        sql = "select syllabus from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql1 = "select date1 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql2 = "select date2 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql3 = "select date3 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql4 = "select date4 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql5 = "select date5 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql6 = "select date6 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql7 = "select date7 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql8 = "select date8 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql9 = "select date9 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql10 = "select date10 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql11 = "select date11 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql12 = "select date12 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql13 = "select date13 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql14 = "select date14 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql15 = "select date15 from subject_table where subject='４学期「英語2D」 金曜3限'"
        sql16 = "select date16 from subject_table where subject='４学期「英語2D」 金曜3限'"
    #15
    elif subject_name == "４学期「人工知能デザイン演習2」 金曜4-5限":
        sql = "select syllabus from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql1 = "select date1 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql2 = "select date2 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql3 = "select date3 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql4 = "select date4 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql5 = "select date5 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql6 = "select date6 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql7 = "select date7 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql8 = "select date8 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql9 = "select date9 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql10 = "select date10 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql11 = "select date11 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql12 = "select date12 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql13 = "select date13 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql14 = "select date14 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql15 = "select date15 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
        sql16 = "select date16 from subject_table where subject='４学期「人工知能デザイン演習2」 金曜4-5限'"
    cursor = connection.cursor()
    cursor.execute(sql)
    syllabus = cursor.fetchall()
    cursor.execute(sql1)
    date1 = cursor.fetchall()
    cursor.execute(sql2)
    date2 = cursor.fetchall()
    cursor.execute(sql3)
    date3 = cursor.fetchall()
    cursor.execute(sql4)
    date4 = cursor.fetchall()
    cursor.execute(sql5)
    date5 = cursor.fetchall()
    cursor.execute(sql6)
    date6 = cursor.fetchall()
    cursor.execute(sql7)
    date7 = cursor.fetchall()
    cursor.execute(sql8)
    date8 = cursor.fetchall()
    cursor.execute(sql9)
    date9 = cursor.fetchall()
    cursor.execute(sql10)
    date10 = cursor.fetchall()
    cursor.execute(sql11)
    date11 = cursor.fetchall()
    cursor.execute(sql12)
    date12 = cursor.fetchall()
    cursor.execute(sql13)
    date13 = cursor.fetchall()
    cursor.execute(sql14)
    date14 = cursor.fetchall()
    cursor.execute(sql15)
    date15 = cursor.fetchall()
    cursor.execute(sql16)
    date16 = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("result.html", syllabus = syllabus,
    date1 = date1,
    date2 = date2,
    date3 = date3,
    date4 = date4,
    date5 = date5,
    date6 = date6,
    date7 = date7,
    date8 = date8,
    date9 = date9,
    date10 = date10,
    date11 = date11,
    date12 = date12,
    date13 = date13,
    date14 = date14,
    date15 = date15,
    date16 = date16,
    subject_name=subject_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')