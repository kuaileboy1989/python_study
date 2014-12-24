#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

URL = 'http://219.134.187.132:9090/bsp-ois/ws/expressService?wsdl'
TIMEOUT = 20
METHOD = 'sfexpressService'

PARAMS_jdd = [
    {   'tag':'Request',
        'attr':{'service':'OrderConfirmService', 'lang':'zh-CN'},
        'child':[
            {   'tag':'Head',
                'attr':{},
                'child':[],
                'value':'5710919526,RU3s0;Km]~jtEd36D6Qq'
            },
            {   'tag':'Body',
                'attr':{},
                'child':[
                    {   'tag':'OrderConfirm',
                        'attr':{
                            'orderid':'TB1207300000003',
                            'mailno':'11223344556677',
                            'dealtype':'1',
                            'return_tracking':'111222333'
                        },
                        'child':[
                            {   'tag':'OrderConfirmOption',
                                'attr':{
                                    'weight':'5',
                                    'volume':'1,2,3'
                                },
                                'child':[],
                                'value':''
                            }
                        ],
                        'value':''
                    }
               ],
                'value':''
            }
        ],
        'value':''
    }
]

PARAMS = [
    {   'tag':'Request',
        'attr':{'service':'OrderService', 'lang':'zh-CN'},
        'child':[
            {   'tag':'Head',
                'attr':{},
                'child':{},
                'value':'5710919526,RU3s0;Km]~jtEd36D6Qq'
            },
            {   'tag':'Body',
                'attr':{},
                'child':[
                    {   'tag':'Order',
                        'attr':{
                            'orderid':'TB1207300000100',
                            'express_type':'1',
                            'j_company':'商派',
                            'j_contact':'我打',
                            'j_tel':'15011112222',
                            'j_address':'上海市徐汇区',
                            'd_company':'shopex',
                            'd_contact':'s_收件',
                            'd_tel':'17011112222',
                            'd_address':'北京',
                            'parcel_quantity':'1',
                            'pay_method':'1',
                            'j_province':'上海',
                            'j_city':'上海',
                            'd_province':'北京',
                            'd_city':'北京'#,
#                            'is_docall':'1',
#                            'is_gen_bill_no':'1',
#                            'is_gen_eletric_pic':'1'
                        },
                        'child':[
                            {   'tag':'OrderOption',
                                'attr':{
                                    'custid':'5322152645',
#                                    'template':'adad',
#                                    'j_shippercode':'122334',
#                                    'd_deliverycode':'111222',
                                    'cargo':'手机,IPAD,充电器',
                                    'cargo_count':'1,1,2',
                                    'cargo_unit':'台,台,个',
                                    'cargo_weight':'1.5,1.0,3.0',
                                    'cargo_amount':'1000,2000,3000',
                                    'cargo_total_weight':'5.5',
                                    'sendstarttime':'2014-06-10 11:46:00',
#                                    'mailno':'755123456789',
#                                    'return_tracking':'111222333444555',
#                                    'j_mobile':'15011112222',
#                                    'd_mobile':'16011112222',
#                                    'j_county':'徐汇区',
#                                    'd_county':'朝阳区',
                                    'remark':'无备注'#,
#                                    'need_return_tracking_no':'1'
                                },
                                'child':[],
                                'value':''
                            }
                        ],
                        'value':''
                    }
               ],
                'value':''
            }
        ],
        'value':''
    }
]


PARAMS_djajsd = {
            'root':{
                    'attr':{'r_a':'i_am_r_a'},
                    'child':{
                            'child1':{
                                    'attr':{'c1_a':'i_am_c1_a'},
                                    'child':{
                                        'subchild':{}
                                    },
                                    'value':'i am child1'
                                    },
                            'child2':{
#                                    'attr':{'c2_a':'i_am_c2_a'},
#                                    'child':{},
#                                    'value':'i am child2'
                                    }
                            },
                    'value':'aaa'
                    }
    }

PARAMS_bak = {
            'root':{
                    'attr':{'r_a':'i_am_r_a'},
                    'child':{
                            'child1':{
                                    'attr':{'c1_a':'i_am_c1_a'},
                                    'child':{},
                                    'value':'i am child1'
                                    },
                            'child2':{
                                    'attr':{'c2_a':'i_am_c2_a'},
                                    'child':{},
                                    'value':'i am child2'
                                    }
                            },
                    'value':'aaa'
                    }
        }

