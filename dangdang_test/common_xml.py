#!/usr/bin/env python
#coding=utf8

'''
H201408011117004437出库单
I201408011117009786入库单
'''
#入库单测试
xml = {'logistics_interface':'''<wmsPurchaseOrderPushInfo>
<header>
<erp_order_num>test001</erp_order_num>
<receipt_id>I201408011117009786</receipt_id>
<close_date>2014-08-02 00:00:00</close_date>
</header>
<detailList>
<item>
<id>记录号</id>
<erp_order_line_num>1</erp_order_line_num>
<sku_no>test001</sku_no>
<qty>50</qty>
<lot>批号</lot>
<expiration_date>有效期</expiration_date>
<inventory_sts>10</inventory_sts>
<vendor>送货商</vendor>
<serialNumberList>
<serial_number>串号</serial_number>
</serialNumberList>
</item>
</detailList>
</wmsPurchaseOrderPushInfo>'''
}

#出库单测试
xml_2 = {
    'logistics_interface':'''<wmsSailOrderPushInfo>
        <header>
        <company>货主</company>
        <warehouse>仓库</warehouse> 
        43
        <erp_order>ERP 单号</erp_order>
        <shipment_id>H201408011117004437</shipment_id>
        <waybill_no>运单号</waybill_no>
        <actual_ship_date_time>2014-08-01 00:00:00</actual_ship_date_time>
        <carrier>承运商名</carrier>
        <carrier_service>承运商服务类型 / SF:时效类型</carrier_service>
        <user_def1>保留字段</user_def1>
        <user_def2>保留字段</user_def2>
        <user_def3>保留字段</user_def3>
        <user_def4>保留字段</user_def4>
        <user_def5>保留字段</user_def5>
        <user_def6>保留字段</user_def6>
        <user_def7>保留字段</user_def7>
        <user_def8>保留字段</user_def8>
        <user_def9>保留字段</user_def9>
        <user_def10>保留字段</user_def10>
        <user_def11>保留字段</user_def11>
        <user_def12>保留字段</user_def12>
        <user_def13>保留字段</user_def13>
        <user_def14>保留字段</user_def14>
        <user_def15>保留字段</user_def15>
        <user_def16>保留字段</user_def16>
        <user_def17>保留字段</user_def17>
        <user_def18>保留字段</user_def18>
        <user_def19>保留字段</user_def19>
        <user_def20>保留字段</user_def20>
        <user_stamp>操作人员</user_stamp>
        <status_time>状态产生时间</status_time>
        <status_code>状态代码</status_code>
        <status_remark>状态说明</status_remark>
        </header>
        <detailList>
        <item>
        <item>test001</item>
        <quantity>2</quantity>
        <quantity_um>单位</quantity_um>
        <user_def1>预留字段</user_def1>
        <user_def2>预留字段</user_def2>
        <user_def3>预留字段</user_def3>
        <user_def4>预留字段</user_def4>
        <user_def5>预留字段</user_def5>
        <user_def6>预留字段</user_def6>
        <user_def7>预留字段</user_def7>
        <user_def8>预留字段</user_def8>
        </item>
        </detailList>
        <containerList>
        <item>
        <container_id>箱号</container_id>
        <item>货品编码</item>
        <quantity>数量</quantity>
        <quantity_um>数量单位</quantity_um>
        <lot>批号</lot>
        <weight>重量</weight>
        <weight_um>重量单位</weight_um>
        <user_stamp>包装员</user_stamp> 
        44
        <user_def1>预留字段</user_def1>
        <user_def2>预留字段</user_def2>
        <user_def3>预留字段</user_def3>
        <user_def4>预留字段</user_def4>
        <user_def5>预留字段</user_def5>
        <user_def6>预留字段</user_def6>
        <user_def7>预留字段</user_def7>
        <user_def8>预留字段</user_def8>
        <serialNumberList>
        <serial_number>串号</serial_number>
        </serialNumberList>
        </item>
        </containerList>
        </wmsSailOrderPushInfo>'''
}

#库存测试
xml = {
    'logistics_interface':'''<wmsInventoryBalancePushInfo>
        <status>推送状态</status>
        <inventory_version>库存版本</inventory_version>
        <inventory_time>库存时间</inventory_time>
        <list>
        <item>
        <company>货主</company>
        <warehouse>仓库</warehouse>
        <item>test001</item>
        <on_hand_qty>30</on_hand_qty>
        <lot>批号</lot>
        <expiration_date>有效期</expiration_date>
        <inventorySts>10</inventorySts>
        <user_def1>预留字段</user_def1>
        <user_def2>预留字段</user_def2>
        <user_def3>预留字段</user_def3>
        <user_def4>预留字段</user_def4>
        <user_def5>预留字段</user_def5>
        <user_def6>预留字段</user_def6>
        <user_def7>预留字段</user_def7>
        <user_def8>预留字段</user_def8>
        </item>
        </list>
        </wmsInventoryBalancePushInfo>'''
}

xml = {
    'request':'''
        <?xml version="1.0" encoding="GBK"?>
        <request>
            <functionID>dangdang.order.goods.send</functionID>
            <time>2009-03-20 15:10:50</time>
            <OrdersList>
                <OrderInfo> 
                    <orderID>9338431941</orderID>
                    <logisticsName>温州货到付款刷卡</logisticsName> 
                    <logisticsTel>13612345678</logisticsTel> 
                    <logisticsOrderID>588377952337</logisticsOrderID>
                    <SendGoodsList>
                        <ItemInfo>
                            <itemID>588377952337</itemID>
                            <sendGoodsCount>1</sendGoodsCount>
                            <belongPromo>< belongPromo>
                            <productItemId></productItemId>
                        </ItemInfo>
                    </SendGoodsList>
                </OrderInfo> 
            </OrdersList>
        </request>
    '''
}
