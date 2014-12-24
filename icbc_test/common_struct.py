#!/usr/bin/env python
#coding=utf8

import simplejson

#TOKEN = '845da90deb2caae6e0619ed72d8a7dad9fc8231ef84d188ece0c9311a9ba9644'
#淘宝tao84
#TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'

#当当测试
TOKEN = ''


#顺丰仓储测试
#TOKEN = '2c02df98ac3ef7bc978590e6e2bd3d79c9024b07e341a361268d32c6eafe97ea'

STORE_ITEM_SPECS_GET_sfwms6 = {
#    'method':'store.wms.item.add',
    'method':'store.wms.item.update',
    'certi_id':1437884333,
    'from_node_id':'1634343031',
    'from_api_v':'1.0',
    'to_node_id':'1738363832',
    'to_api_v':'1.0',
    'callback_url':'http://biz.ex-sandbox.com/callback.php',
    'v':'1.0',
    'timestamp':'',
    'format':'JSON',

    'item_lists':simplejson.dumps([{
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
            ])
}

