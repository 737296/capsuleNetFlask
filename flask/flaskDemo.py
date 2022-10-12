import pymysql as pymysql
from flask import request
from flask import Flask
import hashlib  # md5加密包
import json

app = Flask(__name__)
# 关闭ascii编码方式,解决转义符问题
app.config['JSON_AS_ASCII'] = False


@app.route('/123', methods=['POST'])
def hello_world():
    request.encoding = 'utf-8'

    data = {
        "name": "456",
        "age": 123
    }

    # 获取post请求中的body参数，并格式化成json格式，并存进getPost_data变量
    getPost_data = request.json

    # 将getPost_data中的参数name赋值给data中的name参数
    data['name'] = getPost_data['txt']["sex"]
    # 将data数据格式化成json格式，并赋值给response请求（也就是返回给请求的浏览器，postman之类的客户端）
    response = json.dumps(data)

    return response, 200, {"Content-Type": "application/json"}


@app.route('/sign', methods=['GET'])
def sing():
    # sign("wxd930ea5d5a258f4f", "10000100", "1000", "test", "ibuaiVcKdpRxkhJA")
    return sign("wxd930ea5d5a258f4f", "10000100", "1000", "test", "ibuaiVcKdpRxkhJA")


# 生成签名
def sign(appid, mch_id, device_info, body, nonce_str):
    # key为商户平台设置的密钥key
    key = "192006250b4c09247ec02edce69f6a2d"
    inputParam = ["appid=" + appid, "mch_id=" + mch_id, "device_info=" + device_info, "body=" + body,
                  "nonce_str=" + nonce_str]
    # 按照参数名ASCII字典序排序
    inputParam = sorted(inputParam)
    stringA = inputParam[0] + "&" + inputParam[1] + "&" + inputParam[2] + "&" + inputParam[3] + "&" + inputParam[4]
    stringSignTemp = stringA + "&key=" + key
    # md5加密
    sign = hashlib.md5(stringSignTemp.encode())
    return sign.hexdigest().upper()


@app.route('/selectDb', methods=['GET'])
def selectDb():
    conn = pymysql.connect(
        host="172.25.221.71",
        port=3307,
        user="payhub_dev",
        passwd="payhub@rlzxdl",
        db="payhub"
    )
    cur = conn.cursor()
    sqlbypaymentnumselect = 'SELECT id FROM payhub.t_pay_core_request WHERE payment_num = "%s"' % (
        "AF10021447268782980206905")
    print(sqlbypaymentnumselect)
    cur.execute(sqlbypaymentnumselect)
    reqno = cur.fetchone()
    print(reqno[0])
    cur.close()
    conn.close()

    # data['data']['respPaymentNum'] = getPost_data['data']['respPaymentNum']
    # data['data']['rawNotifyMsg'] = getPost_data['data']['rawNotifyMsg']

    return "1243"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
