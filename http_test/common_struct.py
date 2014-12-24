#!/usr/bin/env python
#coding=utf8

import simplejson

#TOKEN = '845da90deb2caae6e0619ed72d8a7dad9fc8231ef84d188ece0c9311a9ba9644'
#测试ocs token
TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'
TOKEN = '644e3b1da801425bd0f74e9262c41c17fa5bcc1b4ded9088bbaf9004fad50052'


#微信小店测试
TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'
STORE_ITEM_SPECS_GET_dd = {
    'method':'store.trade.fullinfo.get',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1838303832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'tid':'13310432383008095342'
}

STORE_ITEM_SPECS_GET_dd = {
    'method':'store.logistics.offline.send',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1838303832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'tid':'13310432383008215283',
    'company_code':'ZTO',
    'logistics_no':'718678151450'
}

STORE_ITEM_SPECS_GET = {
    'method':'store.items.quantity.list.update',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1838303832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'product_id':'puye4uFjE7edTOyBa-dEfc0SAHtY',
    'sku_id':'$规格一:$规格值2',
    'sku_quantitys':'100',
#    'list_quantity':simplejson.dumps(
#                [
#                    {
##                        'itemId':'0000010922', 
#                        'bn':'0000010922', 
#                        'quantity':'333'
#                   }
#                ]
#            ),
}



#b2b--->ome测试
#TOKEN = '12f7ef48b33104d82b5ad875459a8a33341b77bab597b830960adddcbfa54898'
STORE_ITEM_SPECS_GET_dd = {
    "agent_address": "沿山路43号",
    "agent_birthdate": "1900-1-2",
    "agent_city": "深圳市",
    "agent_district": "南山区",
    "agent_email": "345515975@qq.com",
    "agent_level": "9",
    "agent_logo_url": "http://www.jgqqw.com/home/upload/sitelogo/13975579670.jpg",
    "agent_mobile": "15818184560",
    "agent_name": "刘小传-站13",
    "agent_phone": "4000710116",
    "agent_qq": "",
    "agent_sex": "1",
    "agent_shop_name": "桃花亭",
    "agent_shop_url": " http://ataohua.taobao.com",
    "agent_state": "广东省",
    "agent_uname": "15986120098@163.com",
    "agent_zip": "571205",
    "app_id": "shopex_b2b",
    "buyer_address": "沿山路43号",
    "buyer_city": "深圳市",
    "buyer_district": "南山区",
    "buyer_email": "345515975@qq.com",
    "buyer_memo": "，，山东省 临沂市 ，公欣，15266695467，山东省 临沂市 蒙阴县 旧寨乡 刘家上峪村 ，276212",
    "buyer_mobile": "15818184560",
    "buyer_name": "刘小传-站13",
    "buyer_obtain_point_fee": "0.000",
    "buyer_phone": "4000710116",
    "buyer_state": "广东省",
    "buyer_uname": "15986120098@163.com",
    "buyer_zip": "571205",
    "callback_url": "http://www.jgqqw.com/index.php?ctl=matrix&act=update_callback_status&type=CREATEORDER&type_id=20141126116947",
    "certi_id": "1552929636",
    "created": "2014-11-26 11:09:43",
    "currency": "CNY",
    "currency_rate": "1.0000",
    "date": "1416971385",
    "discount_fee": "0.000",
    "format": "json",
    "from_api_v": "3.2",
    "from_node_id": "1490702738",
    "goods_discount_fee": "0",
    "has_invoice": "false",
    "invoice_fee": "0.000",
    "invoice_title": "",
    "is_cod": "false",
    "is_protect": "false",
    "lastmodify": "2014-11-26 11:09:43",
    "logistics_no": "",
    "method": "store.trade.add",
    "modified": "2014-11-26 11:09:43",
    "msg_id": "547543CDC0A802153FB022B4BED9B518",
    "node_type": "ecos.ome",
    "order_source": "local",
    "orders": "{\"order\":[{\"iid\":\"3544\",\"title\":\"净果空包（净果国际发空包专用链接）\",\"weight\":\"10.000\",\"bn\":\"80016\",\"orders_bn\":\"80016\",\"items_num\":1,\"total_order_fee\":0,\"oid\":\"20141126116947\",\"status\":\"TRADE_ACTIVE\",\"type\":\"goods\",\"order_items\":{\"item\":[{\"iid\":\"3544\",\"bn\":\"80016\",\"price\":\"0.000\",\"name\":\"净果空包（净果国际发空包专用链接）\",\"weight\":\"10.000\",\"num\":\"1\",\"total_item_fee\":0,\"sku_properties\":\"\",\"sendnum\":0,\"item_type\":\"product\",\"sale_price\":0,\"discount_fee\":0,\"score\":null,\"item_status\":\"normal\"}]}}]}",
    "orders_discount_fee": "0",
    "orders_number": "1",
    "out_time": "0",
    "pay_cost": "0.000",
    "pay_status": "PAY_NO",
    "payed_fee": "0.000",
    "payment_lists": "[]",
    "payment_tid": "8",
    "payment_type": "预存款支付",
    "pmt_goods": "0.00",
    "pmt_order": "0.00",
    "promotion_details": "[{\"promotion_name\":null,\"promotion_fee\":\"0.00\"}]",
    "protect_fee": "0.000",
    "real_time": "false",
    "receiver_address": "山东省临沂市蒙阴县 蒙阴县 旧寨乡 刘家上峪村",
    "receiver_city": "临沂市",
    "receiver_district": "蒙阴县",
    "receiver_mobile": "",
    "receiver_name": "公欣",
    "receiver_phone": "15266695467",
    "receiver_state": "山东省",
    "receiver_time": "任意日期 任意时间段",
    "receiver_zip": "276212",
    "seller_address": "",
    "seller_city": "深圳市",
    "seller_district": "",
    "seller_email": "",
    "seller_mobile": "13800138000",
    "seller_name": "先生",
    "seller_phone": "",
    "seller_state": "广东",
    "seller_zip": "518000",
    "ship_status": "SHIP_NO",
    "shipper_address": "",
    "shipper_city": "深圳市",
    "shipper_district": "",
    "shipper_mobile": "13800138000",
    "shipper_name": "先生",
    "shipper_phone": "",
    "shipper_state": "广东",
    "shipper_zip": "518000",
    "shipping_fee": "4.000",
    "shipping_tid": "8",
    "shipping_type": "净果空包专用快递（天天快递）",
    "status": "TRADE_ACTIVE",
    "task": "14169713858324",
    "tid": "20141126116947",
    "timestamp": 1416971213.901798,
    "to_node_id": "1410785130",
    "total_goods_fee": "0",
    "total_trade_fee": "4.000",
    "total_weight": "10.000",
    "trade_memo": "",
    "trade_valid_time": "0",
    "v": "1",



    'certi_id':1437884333,
    'from_node_id':'1974318433',
    'to_node_id':'1533959836',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'timestamp':'',
    'format':'JSON',
    'other_list':simplejson.dumps(
            [
                {
                    'type':"test",
                    'ceshi':"测试"
                }
            ]
        )
    
}

#360buy测试
#TOKEN = '9c094e24c261930bf35126e049997fae45428353df7af34d2fdde255b1ec7282'
STORE_ITEM_SPECS_GET_dd = {
    "method": "store.etms.waybill.send",
    'certi_id':1437884333,
    'from_node_id':'1735353732',
    'to_node_id':'1139343035',
    'from_api_v':'1.0',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    "orderId": "6779",
    
    "app_id": "ecos.ome",
    "city": "普陀区",
    "collectionMoney": "39",
    "collectionValue": "1",
    "county ": "内环中环之间",
    "customerCode": "010K3168",
    "date": "2014-11-03 10:07:32",
    "deliveryId": "000766206615",
    "packageCount": "1",
    "province": "上海",
    "receiveAddress": "上海普陀区内环中环之间曹杨路1350弄40号艺达果业",
    "receiveMobile": "18321777609",
    "receiveName": "郑怀春",
    "salePlat": "0010001",
    "senderAddress": "高新区凤凰路龙园小区4-1-803",
    "senderMobile": "18668930188",
    "senderName": "司邦得京东",
    "senderPostcode": "250000",
    "senderTel": "0531-68651308",
    "thrOrderId": "4614449414",
    "vloumn": "0",
    "weight": "0.02",

    "360buy_business_type": "SOP",
    "company_code": "DDWL",
    "company_name": "京东货到付款",
    "date": "2014-11-03 14:35:17",
    "logistics_no": "001456461355-1-1-",
    "method": "store.logistics.offline.send",
    "node_type": "360buy",
    "tid": "4596339372",
}

#alibaba测试
#TOKEN = "2fb09d18a6e745aa2f05db259b28004ebc80a68c1f58d6966ac0febd4cdcaa55"
STORE_ITEM_SPECS_GET_dkd = {
    'method':'store.logistics.offline.send',
    'certi_id':1437884333,
    'from_node_id':'1433706136',
    'from_api_v':'1.0',
    'to_node_id':'',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'tid':'111951424',
    'company_code':'TTKDEX',
    'logistics_no':'EEEEFFFFTEST',


    "app_id":"ecos.ome",
    "callback_url":"http://neiyie.erp.shopexdrp.cn/index.php/openapi/rpc_callback/async_result_handler/id/14145679665902669021679-1414567966/app_id/ome",
    "certi_id":"1491911237",
    "company_code":"ZTO",
    "company_name":"中通速递",
    "date":"2014-10-29 15:32:46",
    "format":"json",
    "from_api_v":"2.2",
    "from_node_id":"1433706136",
    "logistics_no":"768251869573",
    "memberId":"b2b-1941068751",
    "method":"store.logistics.offline.send",
    "msg_id":"5450981EC0A80215BB7C631D6634411C",
    "node_type":"alibaba",
    "orderEntryIds":"840908274991904",
    "remarks":"",
    "ship_date":"2014-10-29 15:32:41",
    "task":"14145679665902669021679",
    "tid":"aaa112233bbccddeeffgghhiijjkk",
    "timestamp":1414567966.6347229,
    "to_node_id":"1011983031",
    "tradeSourceType":"cbu-trade",
    "v":"1"


}

#夏元俊客户获取商品信息
#TOKEN = "623c6149a37efcfa692c635e23a40d161258c54fdb25754f0c13da4aa5a94640"
STORE_ITEM_SPECS_GET_dd = {
    'method':'store.items.all.get',
    'certi_id':1437884333,
    'from_node_id':'1745854139',
    'from_api_v':'2.2',
    'to_node_id':'1173743138',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1',
    'timestamp':'',
    'format':'JSON',

    "app_id": "ecos.ome",
    "approve_status": "instock",
    "banner": "sold_out",
    "certi_id": "1526766732",
    "date": "2014-10-28 11:40:03",
    "fields": "iid,outer_id,bn,num,title,default_img_url,modified,detail_url,approve_status,skus,price,barcode ",
    "format": "json",
    "from_api_v": "2.2",
    "from_node_id": "1745854139",
    "method": "store.items.all.get",
    "msg_id": "544F1013C0A802155E1FA3B186E7E968",
    "node_type": "taobao",
    "page_no": "104",
    "page_size": "40",
    "timestamp": 1414467603.6097391,
    "to_node_id": "1173743138",
    "v": "1"
}

#alibaba测试
#TOKEN = 'd582e1b70001c6dc2aa4e324791ea5ae5460a4e3bd7a09beae7afbaf0f39758b'
STORE_ITEM_SPECS_GET_dd = {
    'method':'store.trade.fullinfo.get',
    'certi_id':1437884333,
    'from_node_id':'1387719232',
    'from_api_v':'1.0',
    'to_node_id':'1351981032',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'tid':'845909871883604'
}

#TOKEN = '16f096eeac6440e1e0a9ea6abaab4f1619438a0d796cdcf715f2a294e10e3806'
STORE_ITEM_SPECS_GET_dd = {
    'method':'store.trade.fullinfo.get',
    'certi_id':1437884333,
    'from_node_id':'1234323432',
    'from_api_v':'1.0',
    'to_node_id':'1933383132',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'tid':'843459365482430'
#    'tid':'845909871883604'
}

#亚马逊库存更新测试
#TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'
STORE_ITEM_SPECS_GET_dd = {
    'method':'store.items.quantity.list.update',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1838343735',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'list_quantity':simplejson.dumps(
                [
                    {
#                        'itemId':'0000010922', 
                        'bn':'0000010922', 
                        'quantity':'333'
                   }
                ]
            ),
}




#蘑菇街测试
#TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'
STORE_ITEM_SPECS_GET_kdd = {
    'method':'store.items.quantity.list.update',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1931363132',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'list_quantity':simplejson.dumps(
                [
                    {
#                        'itemId':'0000010922', 
                        'bn':'A1010', 
                        'quantity':'1111'
                   }
                ]
            ),
}


STORE_ITEM_SPECS_GET_djdj = {
    'method':'store.trade.fullinfo.get',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1931363132',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'tid':'111951424'
}
STORE_ITEM_SPECS_GET_dkdk = {
    'method':'store.logistics.offline.send',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1931363132',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'tid':'111951424',
    'company_code':'TTKDEX',
    'logistics_no':'EEEEFFFFTEST'
}


#经销单手工补单
#TOKEN = '786feda828a250dba6c4c72735e366534b046be4d68af8e405ad0733fa4728a7'
STORE_ITEM_SPECS_GET_dkdk = {
    'to_node_id': u'1301350438', 
    'method': u'cloud.dealer.trades.list.get', 
    'end_time': u'1409645940', 
    'timestamp': u'1409300340', 
    'start_time': u'1409300339', 
    'from_node_id': u'1541907234', 
}

#icbc测试
STORE_ITEM_SPECS_GET_dkdkdkkd = {
    'method':'store.trade.fullinfo.get',
    'certi_id':1437884333,
#    'from_node_id':'1634343031',
    'from_node_id':'1937363332',
    'from_api_v':'1.0',
#    'to_node_id':'1435363732',
#    'to_node_id':'1435363732',
    'to_node_id':'1430363932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
#    'tid':'120160620IM0077140'
    'tid':'020140902IM6829187'
}

STORE_ITEM_SPECS_GET_jddj = {
    'method':'store.items.quantity.list.update',
    'certi_id':1437884333,
    'from_node_id':'1937363332',
    'from_api_v':'1.0',
    'to_node_id':'1435363732',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
    'list_quantity':simplejson.dumps(
                [
                    {
#                        'itemId':'0000010922', 
                        'bn':'0000010922', 
                        'quantity':'333'
                   }
                ]
            ),
}


STORE_ITEM_SPECS_GET_kdkdk = {
    'method':'store.logistics.offline.send',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1435363732',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    'tid':'120160620IM0077140',
    'company_code':'ZTO',
    'logistics_no':'EEEEFFFFTEST',
    'ship_date':'2014-08-21 10:00:00',
    'item_list':simplejson.dumps(
                [
                    {
                        'itemId':'itemId_0001', 
                       'oid':'oid_0001', 
                       'product_name':'test_test'
                   }
                ]
            ),
}

#当当测试
#OKEN = 'd28fec4de8e56ed2cfea9f3dc52bd3b56fde0dc57a5ed6131c38240954312bde'

STORE_ITEM_SPECS_GET_dkdk = {
#    'method':'store.logistics.offline.send',
    'method':'store.items.quantity.list.update',
    'certi_id':1929715336,
    'from_node_id':'1139363332',
    'from_api_v':'1.0',
    'to_node_id':'1834363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
        'list_quantity':simplejson.dumps(
                [
                    {
#                        'itemId':'0000010922', 
                        'bn':'0000010922', 
                        'quantity':'333'
                   }
                ]
            ),


    "company_name": "优速物流",
    "ship_date": "2014-08-11 13:46:40",
    "logistics_no": "510025993284",
    "logisticstel": "13612345678",
    "tid": "9373508323",

    'item_list':simplejson.dumps(
            [{
                "oid":"9373508323",
                "itemId":"1209266006",
                "num":"1",
                "promotion_id":"9373508323003"
            },
            {
                "oid":"9373508323",
                "itemId":"1218246606",
                "num":"1",
                "promotion_id":"9373508323002"
            },
            {
                "oid":"9373508323",
                "itemId":"1297377806",
                "num":"1",
                "promotion_id":"9373508323001"
            }]
            )
}

#顺丰仓储测试
#TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'

STORE_ITEM_SPECS_GET_dd = {
    'method':'store.wms.item.add',
#    'method':'store.wms.item.update',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1336363232',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'item_lists':simplejson.dumps({'item':[{
                'item_code':'abcdef',
                'name':'篮球',
                'storage_template':'个',
                'quantity_um_1':'个'
            },
            {
                'item_code':'abcde',
                'name':'篮球',
                'storage_template':'个',
                'quantity_um_1':'个'           
            }
            ]})
}
STORE_ITEM_SPECS_GET_sfwms5 = {
    'method':'store.wms.item.inventory.get',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1738363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'item_lists':simplejson.dumps({
                'item_code':'87654321',
                'inventory_type':'10'
            })
}
STORE_ITEM_SPECS_GET_sfwms4 = {
    'method':'store.vendors.get',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1738363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'vendor':'SHP_V1',
    'vendor_name':'test',
    'address':'桂林路',
    'state':'上海',
    'city':'上海',
    'country':'中国',
    'interface_action_code':'SAVE'
}

STORE_ITEM_SPECS_GET_sfwms3 = {
#    'method':'store.wms.outorder.cancel',
#    'method':'store.wms.saleorder.cancel',
#    'method':'store.wms.returnorder.cancel',
    'method':'store.wms.transferorder.cancel',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1738363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'out_order_code':'erp_order_003'
}


STORE_ITEM_SPECS_GET_sfwms2 = {
    'method':'store.wms.outorder.create',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1738363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'erp_order':'erp_order_003',
    'created':'2014-07-25 00:00:00',
    'ship_to_name':'收件公司',
    'receiver_name':'收件人',
    'ship_to_country':'中国',
    'receiver_address':'桂林路369号',
    'receiver_zip':'200233',
    'receiver_mobile':'15011112222',
    'monthly_account':'7550144315',
    'items':simplejson.dumps([{
                'item_line_num':'2',
                'item_code':'87654321',
                'item_name':'测试商品',
                'uom':'个',
                'item_quantity':'1'
            }
            ])
}



STORE_ITEM_SPECS_GET_djaj8333888888 = {
    'method':'store.wms.inorder.create',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1738363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'out_order_code':'INTERFACE_001',
    'order_type':'IN_PURCHASE',
    'created':'2014-07-25 00:00:00',
    'expect_end_time':'2014-07-30 00:00:00',
    'source_id':'SHP_V1',
    'items':simplejson.dumps([{
                'item_code':'87654321',
                'total_quantity':'10'
            }
            ])
}

#crm测试taobao: taobao.sellercenter.subusers.get 查询指定账户的子账号列表
#TOKEN = 'f90e20920b0a2083ca01ad77559f19959abd3f1906fbb76f4839346b4491df0a'
STORE_ITEM_SPECS_GET_kkdskskdjgjg9eee = {
    'method':'store.logistics.trace.search',
    'certi_id':1420775636,
    'from_node_id':'1030313432',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'tid':'cntaobaotao840105',
    'seller_nick':'taobao840105',
#    'is_split':'2014-07-21',
#    'sub_tid':'utf-8'
}
STORE_ITEM_SPECS_GET_jdksgjkcrm = {
    'method':'store.wangwang.eservice.chatpeers.get',
    'certi_id':1420775636,
    'from_node_id':'1030313432',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'chat_id':'cntaobaotao840105',
    'start_date':'2014-07-20',
    'end_date':'2014-07-21',
    'charset':'utf-8'
}
STORE_ITEM_SPECS_GET_jdjdjs9333 = {
    'method':'store.sellercenter.subusers.get',
    'certi_id':1420775636,
    'from_node_id':'1030313432',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'nick_name':'tao840105'
}

#淘宝金融测试
STORE_ITEM_SPECS_GET_djdjjsjsslsllggbb = {
    'method':'store.tmc.message.produce',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1132393932',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    #阿里金融订单数据回流
    'topic':'alipay_xiaodai_Order',
    'consign_time':'2014-06-01 00:00:00',
    'num':222,
    'num_iid':'456',
    'pay_time':'2014-06-01 00:00:00',
    'price':'456',
    'reflow_date':'2014-06-01 00:00:00',
    'sale_platform':'销售平台',
    'seller_company':'商家公司名称',
    'seller_nick':'店铺nick',
    'tid':'223344',
    'type':'type'
    #阿里金融采购单数据回流
#    'topic':'alipay_xiaodai_PurchaseOrder',
#    'num':'222',
#    'num_iid':'456',
#    'purchase_date':'2014-05-01 00:00:00',
#    'purchase_id':'123456',
#    'purchase_price':'22',
#    'reflow_date':'2014-06-01 00:00:00',
#    'seller_company':'商家公司名称'
    #阿里金融商品数据回流
#    'topic':'alipay_xiaodai_Item',
#    'cost_price':'123',
#    'fenxiao_price':'456',
#    'name':'商品名称',
#    'num':2000,
#    'num_iid':'12345',
#    'online_price':'333',
#    'reflow_date':'2014-06-01 00:00:00',
#    'seller_company':'商家公司名称',
#    'tag_price':'555'
    #阿里金融损益数据回流
#    'topic':'alipay_xiaodai_ProfitLoss',
#    'account':'标准会计科目',
#    'amount':'123456',
#    'balance_date':'2014-05-01 00:00:00',
#    'reflow_date':'2014-06-01 00:00:00',
#    'seller_company':'test',
#    'type':'减项'
}


#韵达测试
STORE_ITEM_SPECS_GET_83838383jjd = {
    'method':'store.yd.searchorderservice',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1273396838',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'sysAccount':'1998853005',
    'passWord':'123456',
    'version':'1.0',
    'request':'data',
    'orders':simplejson.dumps([
        {
            'khddh':'AAA1000012375',
            'mailno':'5000001313232',
            'print_file':'0',
            'json_data':'1',
            'json_encrypt':'0'
        }    
    ])

}

STORE_ITEM_SPECS_GET_yuddd = {
    'method':'store.yd.modifyorderservice',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1273396838',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'sysAccount':'1998853005',
    'passWord':'123456',
    'version':'1.0',
    'request':'data',
    'orders':simplejson.dumps([
        {
            'khddh':'AAA1000012370',
            'nbckh':'2001124',
            's_name':'王小虎',
            's_company':'凯利',
            's_city':'江苏省，徐州市，新沂市',
            's_address':'江苏省徐州市新沂市湖东路999号',
            's_postcode':'221435',
            's_phone':'8592652',
            's_mobile':'13761960078',
            's_branch':'',
            'r_name':'陆大有',
            'r_company':'千千',
            'r_city':'上海市，上海市，青浦区',
            'r_address':'上海市青浦区盈港东路6655号',
            'r_postcode':'201700',
            'r_phone':'57720341',
            'r_mobile':'13761960075',
            'r_branch':'',
            'weight':'11',
            'size':'20,20,20',
            'value':'20',
            'collection_value':'',
            'special':'',
            'items':[
                {
                    'name':'外套',
                    'number':1,
                    'remark':'黑色'
                }    
            ],
            'remark':'',
            'cus_area1':'订单号：123123    \n  批次号：152201 ',
            'cus_area2':'',
            'pdf_flag':'0',
            'wave_no':'abcd123456123456',
            'receiver_force':'1'
        }    
    ])

}

STORE_ITEM_SPECS_GET_ddjjgdsafsd = {
    'method':'store.yd.orderservice',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1273396838',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'sysAccount':'1998853005',
    'passWord':'123456',
    'version':'1.0',
    'request':'data',
    'orders':simplejson.dumps([
        {
            'khddh':'AAA1000012388',
            'nbckh':'2001124',
            's_name':'王小虎',
            's_company':'凯利',
            's_city':'江苏省，徐州市，新沂市',
            's_address':'江苏省徐州市新沂市湖东路999号',
            's_postcode':'221435',
            's_phone':'8592652',
            's_mobile':'13761960078',
            's_branch':'',
            'r_name':'陆大有',
            'r_company':'千千',
            'r_city':'上海市，上海市，青浦区',
            'r_address':'上海市青浦区盈港东路6655号',
            'r_postcode':'201700',
            'r_phone':'57720341',
            'r_mobile':'13761960075',
            'r_branch':'',
            'weight':'11',
            'size':'20,20,20',
            'value':'20',
            'collection_value':'',
            'special':'',
            'items':[
                {
                    'name':'外套',
                    'number':1,
                    'remark':'黑色'
                }    
            ],
            'remark':'',
            'cus_area1':'订单号：123123    \n  批次号：152201 ',
            'cus_area2':'',
            'callback_id':'abcd123456123456',
            'wave_no':'abcd123456123456',
            'receiver_force':'1'
        }    
    ])

}



#申通测试
STORE_ITEM_SPECS_GET_stosdjdj = {
    'method':'store.waybill.mailno.get',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1064384233',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'cusname':'test',
    'cusite':'cusite',
    'len':1
}



STORE_ITEM_SPECS_GET_djdjajgjd333355 = {
    'method':'store.waybill.data.add',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1064384233',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'billno':'220000000070',
    'senddate':'2014-02-27',
    'sendsite':'上海陈行公司',
    'sendcus': '东商',
    'sendperson': '李名学',
    'sendtel': '13662625320',
    'receivecus': '深圳天翼德',
    'receiveperson': '小桥',
    'receivetel': '10086',
    'goodsname': '苹果测试',
    'inputdate':'',
    'inputperson': '东商',
    'inputsite': '上海陈行公司',
    'lasteditdate': '',
    'lasteditperson': '',
    'lasteditsite':'',
    'remark': '测试备注',
    'receiveprovince': '广东省',
    'receivecity': '深圳市',
    'receivearea': '南山区',
    'receiveaddress': '收件地址',
    'sendprovince':'湖南省',
    'sendcity':'郴州市',
    'sendarea': '永兴县',
    'sendaddress': '寄件地址',
    'weight': '12',
    'productcode': '',
    'sendpcode': '',
    'sendccode': '',
    'sendacode': '',
    'receivepcode': '',
    'receiveccode': '',
    'receiveacode':'',
    'bigchar': '广东省深圳市',
    'orderno':'081120317'
}



STORE_ITEM_SPECS_GET_djssjsjdkdkdkdkjjjff = {
    'method':'store.waybill.print',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1064384233',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'heat':'方案一',
    'senderName':'李名学', 
    'senderCompanyName': '东商', 
    'senderProvince': '湖南省', 
    'senderCity': '郴州市', 
    'senderArea': '永兴县', 
    'senderAddress': '湖南郴州', 
    'senderTel': '13662625320', 
    'senderDate': '2014-2-27', 
    'cargoName': '苹果', 
    'receiverName': '李名学', 
    'receiverCompanyName': '中国电信', 
    'receiverTel': '10086', 
    'receiverProvince': '广东省', 
    'receiverCity': '深圳市', 
    'receiverArea': '宝安区', 
    'receiverAddress': '西乡固戍', 
    'weight': '12', 
    'orderId': '268000000042', 
    'remark': '测试备注', 
    'bigChar': '广东宝安', 
    'orderno': 'LBT081120317'
}

STORE_ITEM_SPECS_GET_333737hf = {
    'method':'store.waybill.search',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1064384233',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
   
    'p_billno':'',
    'p_dates':'2013-01-01',
    'p_datee':'2014-01-01',
    'p_custname':'公司IT测试',
    'p_cusite':'江苏南通公司'
}

#顺丰测试
STORE_ITEM_SPECS_GET_sddgjdj8988 = {
    'method':'store.sf.ordersearchservice',
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

    'orderid':'TB1207300000001'
}


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

#顺丰测试孙静token
#TOKEN = '16f096eeac6440e1e0a9ea6abaab4f1619438a0d796cdcf715f2a294e10e3806'

STORE_ITEM_SPECS_GET_dsjsdjjdsj = {    #孙静测试
    "method": "store.sf.orderservice",
    "certi_id": "1324795436",
    "from_node_id": "1234323432",
    'from_api_v':'1.0',
    "to_node_id": "1588336732",
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    "v": "1",
    "timestamp": 1404784162.120644,
    'format':'JSON',

#    "sysAccount": "ZJLSSMKJYXGS",
#    "passWord": "58TLGjY8BaYmy4W9",
    'sysAccount':'5771104090',
    'passWord':'DvmA25dvtjSUJFZuWwD6hoJWVPDThqib',
    "orderid": "201407230027715865",
    "express_type": "3",
    "j_company": "建行龙卡商城",
    "j_contact": "",
    "j_tel": "13222222222",
    "j_address": "上海上海市黄浦区s001",
    "d_company": "u001",
    "d_contact": "u001",
    "d_tel": "1322222222",
    "d_address": "海南白沙黎族自治县2333",
    "parcel_quantity": "1",
    "pay_method": "1",
    "j_province": "上海",
    "j_city": "上海",
    "d_province": "海南",
    "d_city": "白沙黎族自治县"
}

STORE_ITEM_SPECS_GET_iddd = {
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
    'orderid':'TB1207300000231',
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
#客户真实信息，debug使用#TODO
'''
TOKEN = "7b3d5fe93eab19759863b40dfb1230ae8a99ae10e7a9c03da9c91fce8d95fb3b"
STORE_ITEM_SPECS_GET_kdkd = {
    'method':'store.wlb.waybill.search',
    'certi_id':1887729037,
    'from_node_id':'1487739634',
    'from_api_v':'1.0',
    'to_node_id':'1712376336',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',
    
#    'seller_id':'奥兰达食品专营店',
#    'seller_id':'1689130392',
    'cp_code':'TTKDEX'
}
'''

STORE_ITEM_SPECS_GET_djjdjdjsss = {
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
    
#    'seller_id':'123',
    'cp_code':'ZTO'
}
'''
#何苦真实信息，debug使用
TOKEN = '31dd224ce85a0a7a9b24f5f0734004a7ca6b83d2b324771a1c731e12435d88b0'
STORE_ITEM_SPECS_GET = {
    'method':'store.wlb.waybill.get',
    'certi_id':1887729037,
    'from_node_id':'1053801536',
    'from_api_v':'1.0',
    'to_node_id':'1464810934',
    'to_api_v':'1.0',
    'callback_url':'http://bxsc.tg.taoex.com/index.php/openapi/ome.shop/shop_callback/shop_id/42c6d4a05f7a0101a1449ce795266889',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'trade_order_info_cols':simplejson.dumps([
            {
                "consignee_address": {
                    "address_detail":"大新寨镇东王各庄村",
                    "area": "抚宁县",
                    "city": "秦皇岛市",
                    "province": "河北"
                },
                "consignee_name": "张雅棋",
                "consignee_phone": "15732038486",
                "item_name": "芳华编织袋",
                "order_channels_type": "TM",
                "trade_order_list": [
                    "736638331548777"
                ]
            }
    ]),
    'shipping_address':simplejson.dumps({"province":"河南省",
                                        "city":"郑州市",
                                        "area":"新郑市",
                                        "address_detail":"西关服装城外28号电商物流中心"}),
    'cp_code':'ZTO'
}
'''


STORE_ITEM_SPECS_GET_kdkd = {
    'method':'store.wlb.waybill.get',
    'certi_id':1748389234,
    'from_node_id':'1634343031',
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
#    'code':'MljBihigM0TaKSlJ7SbZdtxX13613',hIK4XuVyp8cJD0W8wsLFP6Md4885
    'code':'hIK4XuVyp8cJD0W8wsLFP6Md4885',
#    'response_type':'token',
    'redirect_uri':'http://biz.ex-sandbox.com/callback.php'
}
