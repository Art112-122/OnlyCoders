from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.get("/")
def start():
    return render_template("home.html")






# @app.route('/login')
# def set_cookie():
#
#
#
#
#
#     # Створення відповіді і встановлення кукі
#     response = make_response("Кука з декількома значеннями була встановлена")
#     response.set_cookie('user_data', "")  # Кука діє 1 день
#     return response
#
#
# @app.route('/get_cookie')
# def get_cookie():
#     # Отримання куки
#     data_str = request.cookies.get('user_data')
#     return "Кука не знайдена"





if __name__ == '__main__':
    app.run(port=8080)
