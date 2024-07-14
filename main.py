# 后续需要分组路由可以考虑用蓝图功能来注册
from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', active_page='index')


@app.route('/test')
def test():
    return render_template('test.html', active_page='test')


# 假设的汇率，实际应用中可能需要从API获取
USD_TO_RMB_RATE = 7.255
USD_TO_JPY_RATE = 157.23
USD_TO_GBP_RATE = 0.786
USD_TO_EUR_RATE = 0.933
USD_TO_AUD_RATE = 1.512
USD_TO_CAD_RATE = 1.374
USD_TO_HKD_RATE = 7.811
USD_TO_SGD_RATE = 1.353


@app.route('/exchange_rate_conversion')  # 汇率换算工具
def exchange_rate_conversion():
    RMB_TO_USD_RATE = 7.2556
    RMB_TO_GBP_RATE = 9.201
    RMB_TO_EUR_RATE = 7.7633
    RMB_TO_JPY_RATE = 0.0461
    RMB_TO_AUD_RATE = 4.7978
    RMB_TO_CAD_RATE = 5.2784
    RMB_TO_HKD_RATE = 0.9289
    RMB_TO_SGD_RATE = 5.3613

    normal_lists = [
        '1', '5', '10', '25', '50', '100', '200', '500', '1000', '5000', '10000', '50000'
    ]
    return render_template('exchange_rate_conversion.html',
                           normal_lists=normal_lists,
                           RMB_TO_USD_RATE=RMB_TO_USD_RATE,
                           RMB_TO_GBP_RATE=RMB_TO_GBP_RATE,
                           RMB_TO_EUR_RATE=RMB_TO_EUR_RATE,
                           RMB_TO_JPY_RATE=RMB_TO_JPY_RATE,
                           RMB_TO_AUD_RATE=RMB_TO_AUD_RATE,
                           RMB_TO_CAD_RATE=RMB_TO_CAD_RATE,
                           RMB_TO_HKD_RATE=RMB_TO_HKD_RATE,
                           RMB_TO_SGD_RATE=RMB_TO_SGD_RATE)


@app.route('/exchange_rate_conversion', methods=['POST'])  # 汇率换算工具
def exchange_rate_conversion_rate():
    # 从POST请求中获取货币类型和值
    global usd_value, rmb_value, jpy_value, gbp_value, eur_value, aud_value, cad_value, hkd_value, sgd_value
    currency_type = request.json.get('currency_type', '')
    value = request.json.get('value', 0)

    if currency_type == 'rmb':
        usd_value = round(float(value) / USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'usd':
        rmb_value = round(float(value) * USD_TO_RMB_RATE, 2)
        jpy_value = round(float(value) * USD_TO_JPY_RATE, 2)
        gbp_value = round(float(value) * USD_TO_GBP_RATE, 2)
        eur_value = round(float(value) * USD_TO_EUR_RATE, 2)
        aud_value = round(float(value) * USD_TO_AUD_RATE, 2)
        cad_value = round(float(value) * USD_TO_CAD_RATE, 2)
        hkd_value = round(float(value) * USD_TO_HKD_RATE, 2)
        sgd_value = round(float(value) * USD_TO_SGD_RATE, 2)
    elif currency_type == 'jpy':
        usd_value = round(float(value) / USD_TO_JPY_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'gbp':
        usd_value = round(float(value) / USD_TO_GBP_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'eur':
        usd_value = round(float(value) / USD_TO_EUR_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'aud':
        usd_value = round(float(value) / USD_TO_AUD_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'cad':
        usd_value = round(float(value) / USD_TO_CAD_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'hkd':
        usd_value = round(float(value) / USD_TO_HKD_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        sgd_value = round(usd_value * USD_TO_SGD_RATE, 2)
    elif currency_type == 'sgd':
        usd_value = round(float(value) / USD_TO_SGD_RATE, 2)
        rmb_value = round(usd_value * USD_TO_RMB_RATE, 2)
        jpy_value = round(usd_value * USD_TO_JPY_RATE, 2)
        gbp_value = round(usd_value * USD_TO_GBP_RATE, 2)
        eur_value = round(usd_value * USD_TO_EUR_RATE, 2)
        aud_value = round(usd_value * USD_TO_AUD_RATE, 2)
        cad_value = round(usd_value * USD_TO_CAD_RATE, 2)
        hkd_value = round(usd_value * USD_TO_HKD_RATE, 2)
    else:
        return jsonify({'error': 'Invalid currency_type'}), 400

        # 返回所有转换后的值和原始值
    response = {
        'original_value': value,
        'usd_value': usd_value if currency_type != 'usd' else value,
        'rmb_value': rmb_value if currency_type != 'rmb' else value,
        'jpy_value': jpy_value if currency_type != 'jpy' else value,
        'gbp_value': gbp_value if currency_type != 'gbp' else value,
        'eur_value': eur_value if currency_type != 'eur' else value,
        'aud_value': aud_value if currency_type != 'aud' else value,
        'cad_value': cad_value if currency_type != 'cad' else value,
        'hkd_value': hkd_value if currency_type != 'hkd' else value,
        'sgd_value': sgd_value if currency_type != 'sgd' else value
    }
    return jsonify(response)


@app.route('/unit_conversion')  # 单位换算工具
def unit_conversion():
    return render_template('unit_conversion.html', active_page='unit_conversion')


@app.route('/salary_calculator')  # 工资计算
def salary_calculator():
    return render_template('salary_calculator.html', active_page='salary_calculator')


@app.route('/case_conversion')  # 大小写转换，包含英文和数字的转换
def case_conversion():
    return render_template('case_conversion.html', active_page='case_conversion')


def generate_password(length=10, has_digits=True, has_uppercase=True, has_lowercase=True, has_special_chars=True):
    """
    Generate a random password based on the given criteria.

    :param length: Length of the password (default: 10)
    :param has_digits: Include digits in the password (default: True)
    :param has_uppercase: Include uppercase letters in the password (default: True)
    :param has_lowercase: Include lowercase letters in the password (default: True)
    :param has_special_chars: Include special characters in the password (default: True)
    :return: A randomly generated password
    """
    # Define character sets
    chars = []
    if has_digits:
        chars.append(string.digits)
    if has_uppercase:
        chars.append(string.ascii_uppercase)
    if has_lowercase:
        chars.append(string.ascii_lowercase)
    if has_special_chars:
        chars.append(string.punctuation)  # Includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # If no character set is selected, raise an error
    if not chars:
        raise ValueError("At least one character set must be included in the password")

        # Concatenate all character sets
    all_chars = ''.join(chars)

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password


@app.route('/random_password', methods=['GET', 'POST'])  # 随机密码生成
def random_password():
    if request.method == 'POST':
        number = request.form.get('number')
        digits = request.form.getlist('digits')
        uppercase = request.form.getlist('uppercase')
        lowercase = request.form.getlist('lowercase')
        special_chars = request.form.getlist('special_chars')

        password = generate_password(length=int(number),
                                     has_digits=bool(digits),
                                     has_uppercase=bool(uppercase),
                                     has_lowercase=bool(lowercase),
                                     has_special_chars=bool(special_chars))

        return render_template('random_password.html',
                               active_page='random_password',
                               password=password,
                               number=number,
                               has_digits=digits,
                               digits=digits,
                               uppercase=uppercase,
                               lowercase=lowercase,
                               special_chars=special_chars,
                               )
    else:
        password = generate_password(length=10, has_digits=True, has_uppercase=True, has_lowercase=True,
                                     has_special_chars=True)
        return render_template('random_password.html',
                               active_page='random_password',
                               password=password,
                               number=None,
                               hobbies=[],
                               digits=["True"],
                               uppercase=["True"],
                               lowercase=["True"],
                               special_chars=["True"])


@app.route('/time_calculator')  # 时间差计算器
def time_calculator():
    return render_template('time_calculator.html', active_page='time_calculator')


@app.route('/online_perpetual_calendar')  # 在线万年历
def online_perpetual_calendar():
    return render_template('online_perpetual_calendar.html', active_page='online_perpetual_calendar')


@app.route('/country_codes')  # 世界各国代码表
def country_codes():
    return render_template('country_codes.html', active_page='country_codes')


@app.route('/color_selector')  # 颜色选择器
def color_selector():
    return render_template('color_selector.html', active_page='color_selector')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
