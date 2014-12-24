#!/usr/bin/env python
#coding=utf8

import simplejson

PARAMS = {'data':
            {
                "code":"vip0001",
                "data_digest":"620e2c78d0ca5c1bc718b2be0cceab45",
                "params":simplejson.dumps({'p_billno':'','p_dates':'2013-01-01','p_datee':'2014-01-01','p_custname':'公司IT测试','p_cusite':'江苏南通公司'})
            }
        }
print PARAMS
PARAMS_bakdddk = {
    'code':'vip0001',#请求的方法
    'data_digest':'620e2c78d0ca5c1bc718b2be0cceab45',#报文密文
    'params':'''
        'p_billno':'',#运单编号
        'p_dates':'2013-01-01',#开始日期
        'p_datee':'2014-01-01',#结束日期
        'p_custname':'公司IT测试',#客户名称
        'p_cusite':'江苏南通公司'#网点名称
    }'''
}

#TOKEN = '845da90deb2caae6e0619ed72d8a7dad9fc8231ef84d188ece0c9311a9ba9644'
TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'
#顺丰测试
STORE_ITEM_SPECS_GET_dddfff = {
    'method':'store.sf.orderfilterservice',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1438323432',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
   
    'sysAccount':'5710919526',
    'passWord':'RU3s0;Km]~jtEd36D6Qq',

    'orderid':'TB1207300000202',
    'filter_type':'1',
    'd_address':'上海市徐汇区桂林路',

    'j_tel':'19822227777',
    'country':'CN',
    'province':'广东省',
    'city':'深圳市',
    'county':'福田区',
    'd_country':'CN',
    'd_province':'广东省',
    'd_city':'深圳市',
    'd_county':'福田区',
    'j_address':'广东省深圳市福田区新洲十一街万基商务大厦10楼',
    'd_tel':'12344445555',
    'j_custid':'111122223333'
}


STORE_ITEM_SPECS_GET_333jjff = {
    'method':'store.sf.orderconfirmservice',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1438323432',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'sysAccount':'5710919526',
    'passWord':'RU3s0;Km]~jtEd36D6Qq',

    'orderid':'TB1207300000202',
    'mailno':'388400675702',
    'dealtype':'2',
    'return_tracking':'111222333444',

    'weight':'3',
    'volume':'1,2,3'
}

STORE_ITEM_SPECS_GET = {
    'method':'store.sf.orderservice',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1438323432',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'sysAccount':'5710919526',
    'passWord':'RU3s0;Km]~jtEd36D6Qq',
    'orderid':'TB1207300000211',
    'express_type':'1',
    'j_company':'商派',
    'j_contact':'我打',
    'j_tel':'11111111222',
    'j_address':'上海市',
    'd_company':'shopex',
    'd_contact':'s_收件',
    'd_tel':'22222233333',
    'd_address':'北京',
    'parcel_quantity':'1',
    'pay_method':'1',
    'j_province':'上海',
    'j_city':'上海',
    'd_province':'北京',
    'd_city':'北京',
    
    'custid':'5322152645',
    'cargo':'手机，IPAD',
    'cargo_count':'1,1',
    'cargo_unit':'台，台',
    'cargo_weight':'1.5,2.0',
    'cargo_amount':'1000,2000',
    'cargo_total_weight':'3.5',
    'sendstarttime':'2014-06-10 11:22:33',
    'remark':'备注',
    
    'sf_cod':'COD',
    'sf_cod_value':'1111',
    'sf_cod_value1':'123455667',
    
    'sf_insure':'INSURE',
    'sf_insure_value':'2000',
    
    'sf_msg':'MSG',
    'sf_msg_value':'18911112222',
    
    'sf_pkfee':'PKFEE',
    'sf_pkfee_value':'20',

    'sf_sms':'SMS',
    'sf_sms_value':'18922221111',
    'sf_sms_value1':'测试测试',

    'sf_sinsure':'SINSURE',
    'sf_sinsure_value':'3000',

    'sf_sdelivery':'SDELIVERY',
    'sf_sdelivery_value':'4000',

    'sf_saddservice':'SADDSERVICE',
    'sf_saddservice_value':'5000'

}

STORE_ITEM_SPECS_GET_ddj345 = {
    'method':'store.logistics.partners.get',
    'certi_id':1748389234,
    'from_node_id':'1533373832',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'service_type':'online',
    'source_id':'',
    'target_id':'',
    'goods_value':''#,
#'is_need_carriage':'false'
}

STORE_ITEM_SPECS_GET_ddaff = {
    'method':'store.logistics.address.reachable',
    'certi_id':1748389234,
    'from_node_id':'1533373832',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'area_code':'',
    'address':'',
    'partner_ids':'1',
    'service_type':88,
    'source_area_code':'330110011'
}

STORE_ITEM_SPECS_GET_ddddfff = {
    'method':'store.wlb.waybill.update',
    'certi_id':1748389234,
    'from_node_id':'1533373832',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'cp_code':'ZTO'
}

STORE_ITEM_SPECS_GET_ajfddjdj = {
    'method':'store.wlb.waybill.search',
    'certi_id':1748389234,
    'from_node_id':'1533373832',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'seller_id':'123',
    'cp_code':''
}

STORE_ITEM_SPECS_GET_35566 = {
    'method':'store.wlb.waybill.get',
    'certi_id':1748389234,
    'from_node_id':'1533373832',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'trade_order_info_cols':simplejson.dumps([
            {
                "consignee_address": {
                    "address_detail": "朝阳路高井，财满街，财经中心9号楼21单元6013",
                    "area": "朝阳区",
                    "area_code": 0,
                    "city": "北京市",
                    "city_code": 0,
                    "division_id": 0,
                    "province": "北京",
                    "province_code": 0,
                    "town_code": 0
                },
                "consignee_name": "我亮",
                "consignee_phone": "12312312311",
                "item_name": "沙箱测试:集市商品同步测试0001",
                "order_channels_type": "TB",
                "trade_order_list": [
                    "SW-20140403-00654"
                ]
            }
    ]),
    'shipping_address':simplejson.dumps({"province":"上海",
                                        "city":"上海市",
                                        "area":"长宁区",
                                        "division_id":'310105',
                                        "address_detail":"测试ISV"}),
    'cp_code':'ZTO'
}



STORE_ITEM_SPECS_GET_bak = {
    'method':'store.wlb.waybill.get',
#    'method':'store.wlb.waybill.update',
#    'method':'store.logistics.offline.send',
#    'method':'store.wlb.waybill.search',
    'certi_id':1748389234,
    'from_node_id':'1533373832',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
#    'num_iid':'13394023856',
#    'bid':1003355684970018
    'cp_code':'hello world'
#    'tid':'200002',
#    'company_code':'POST',
#    'ogistics_no':'F5257222'
}

TOKEN_GET_STRUCT = {
    'client_id':'1010011902',
    'client_secret':'sandbox0109908169017efb33a71f15c',
    'grant_type':'authorization_code',
    'code':'MljBihigM0TaKSlJ7SbZdtxX13613',
#    'response_type':'token',
    'redirect_uri':'http://biz.ex-sandbox.com/callback.php'
}
