#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
import suds
import traceback
import chardet

from common import *

def get_xml(doc, cur, bt, va):
    attr = va.get('attr') if va.has_key('attr') else {}
    child = va.get('child') if va.has_key('child') else []
    value = va.get('value') if va.has_key('value') else ''
    if attr:
        for k_attr in attr:
            bt.setAttribute(k_attr, attr[k_attr])
    if child and value:
        pass
    if not child and value:
        v = doc.createTextNode(value)
        bt.appendChild(v)
    cur.appendChild(bt)
    if child:
        for k_child in child:
            next_node = doc.createElement(k_child['tag'])
            child_va = k_child
            get_xml(doc, bt, next_node, child_va)
 

def xml_create():

    doc = Document()
    a = PARAMS
    for k in a:
        bt = doc.createElement(k['tag'])
        va = k
        get_xml(doc, doc, bt, va)

        print bt.toprettyxml(indent='\t', newl='\n')
        return bt.toprettyxml(indent='', newl='')

    return ''
def main():
    url = URL
    xml = xml_create()
#    return
    try:
        client = suds.client.Client(url, timeout=TIMEOUT)
#        print '***client:',client
        service_str = 'client.service.%s(\'%s\')'%(METHOD, xml)
        response = eval(service_str)
        print '***response:',response
    except Exception,e:
        traceback.print_exc(5)
        return 'error: 数据请求失败'

def main_bak():

    doc = Document()
    bt = doc.createElement('root')
    bt.setAttribute('test', 'iamvalue')
    doc.appendChild(bt)

    book = doc.createElement('book')
    book.setAttribute('genre', 'XML')
    bt.appendChild(book)

    title = doc.createElement('title')
#    title_text = doc.createTextNode('Python处理XML之Minidom')
#    title.appendChild(title_text)
    book.appendChild(title)

    print doc.toprettyxml(indent = '')

    return

if __name__ == "__main__":
    main()
#    xml_create()
