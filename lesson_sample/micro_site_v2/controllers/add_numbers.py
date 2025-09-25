from utils import render_template, parse_post
from app_logic import set_first_value, set_second_value, get_addition

def add_numbers(environ):
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        first_value = int(data.get("first_value", [0])[0])
        second_value = int(data.get("second_value", [0])[0])

        # 値をセット
        set_first_value(first_value)
        set_second_value(second_value)

        # 計算結果を取得
        addition = get_addition()

        # 結果をテンプレートに渡す
        return render_template("boundaries/add_numbers_data.html", addition=addition)

    # GETリクエストなどの場合の処理（必要に応じて）
    return render_template("boundaries/add_numbers_data.html", addition=None)