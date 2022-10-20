import json
import time
import pymysql
from flask import Flask
from flask import request

app = Flask(__name__)


# app.config['JSON_AS_ASCII'] = False  #关闭ascii编码方式
@app.route('/aliPay', methods=['POST'])
def get_responseData():
    data = {
        "channel": "ALIPAY",
        "code": "200",
        "data": {
            "code": "200",
            "message": "SUCCESS",
            "channelTradeNum": "2022092722001454471458167881",
            "payAmount": 2750,
            "attach": "ZnJvbT1QQ1QmYnJhbmQ9S0ZDJmJ1PUtGQ19ERUwmcG9ydGFsVHlwZT1BUFAmc3RvcmU9SFpIMDg2",
            "payTime": "20220927142155",
            "userPayAmount": 2750,
            "payAccount": "133****4865",
            "payUserId": "2088512661854475",
            "respPaymentNum": "AF10021440805473808363744",
            "serviceCharge": 0,
            "yumDeliveryFeeDiscount": 0,
            "thirdDeliveryFeeDiscount": 0,
            "contributeDetail": [
                {
                    "key": "YUM",
                    "name": "百胜出资",
                    "amount": 0
                },
                {
                    "key": "ALIPAY",
                    "name": "支付宝出资",
                    "amount": 0
                },
                {
                    "key": "OTHER",
                    "name": "其他出资",
                    "amount": 0
                }
            ],
            "paymentPromotionDetail": [
            ],
            "isUseEnterprisePay": "false",
            "reqNo": "1440805473808363745",
            "rawNotifyMsg": "{\"gmt_create\":\"2022-09-27 14:21:55\",\"charset\":\"UTF-8\",\"seller_email\":\"hzh_kfc_fin_store_zfb.china@yum.com\",\"subject\":\"KFCAF10021440805473808363744\",\"body\":\"ZnJvbT1QQ1QmYnJhbmQ9S0ZDJmJ1PUtGQ19ERUwmcG9ydGFsVHlwZT1BUFAmc3RvcmU9SFpIMDg2\",\"buyer_id\":\"2088512661854475\",\"invoice_amount\":\"27.50\",\"notify_id\":\"2022092700222142156054471450438903\",\"fund_bill_list\":\"[{\\\"amount\\\":\\\"27.50\\\",\\\"fundChannel\\\":\\\"ALIPAYACCOUNT\\\"}]\",\"notify_type\":\"trade_status_sync\",\"trade_status\":\"TRADE_SUCCESS\",\"receipt_amount\":\"27.50\",\"app_id\":\"2017062007526455\",\"buyer_pay_amount\":\"27.50\",\"seller_id\":\"2088911678307804\",\"gmt_payment\":\"2022-09-27 14:21:55\",\"enterprise_pay_info\":\"{\\\"is_use_enterprise_pay\\\":\\\"false\\\",\\\"invoice_amount\\\":\\\"0.00\\\"}\",\"notify_time\":\"2022-09-27 14:21:56\",\"version\":\"1.0\",\"out_trade_no\":\"AF10021440805473808363744\",\"total_amount\":\"27.50\",\"trade_no\":\"2022092722001454471458167881\",\"auth_app_id\":\"2017062007526455\",\"buyer_logon_id\":\"133****4865\",\"point_amount\":\"0.00\"}"
        },
        "errorMsg": "fail",
        "msg": "success"
    }

    getPost_data = request.json
    data['data']['channelTradeNum'] = getPost_data['trade_no']
    data['data']['payAmount'] = int(float(getPost_data['invoice_amount']) * 100)
    data['data']['attach'] = getPost_data['body']
    creattime = time.strptime(getPost_data['gmt_create'], '%Y-%m-%d %H:%M:%S')
    otherstyletime = time.strftime("%Y%m%d%H%M%S", creattime)
    data['data']['payTime'] = otherstyletime
    data['data']['userPayAmount'] = int(float(getPost_data['invoice_amount']) * 100)
    data['data']['payAccount'] = getPost_data['buyer_logon_id']
    data['data']['payUserId'] = getPost_data['buyer_id']
    data['data']['respPaymentNum'] = getPost_data['out_trade_no']
    data['data']['rawNotifyMsg'] = json.dumps(json.dumps(getPost_data))

    # conn = pymysql.connect(
    #     host="172.25.221.71",
    #     port= 3307,
    #     user="payhub_dev",
    #     passwd="payhub@rlzxdl",
    #     db="payhub"
    # )
    # cur = conn.cursor()
    # sqlbypaymentnumselect = 'SELECT id FROM payhub.t_pay_core_request WHERE payment_num = "%s"' % (
    # getPost_data['out_trade_no'])
    # print(sqlbypaymentnumselect)
    # cur.execute(sqlbypaymentnumselect)
    # reqno = cur.fetchone()
    # print(reqno[0])
    # cur.close()
    # conn.close()

    data['data']['reqNo'] = "123"  # reqno[0]
    response = json.dumps(data)
    return response, 200, {"Content-Type": "application/json"}


@app.route('/123', methods=['GET'])
def get_responseData123():
    return "success!!!"


if __name__ == '__main__':
    # app.run(host='172.25.221.70', port=5001)
    # app.run(processes=5)
    app.run(host='127.0.0.1', port=5001)
    # app.run(processes=5)

