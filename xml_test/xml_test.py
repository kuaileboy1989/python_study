#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Document

from common import PARAMS

def get_xml(doc, cur, bt, va):
    attr = va.get('attr') if va.has_key('attr') else {}
    child = va.get('child') if va.has_key('child') else {}
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
            next_node = doc.createElement(k_child)
            child_va = child[k_child]
            get_xml(doc, bt, next_node, child_va)
 

def xml_create():

    doc = Document()
    a = PARAMS
    for k in a:
        bt = doc.createElement(k)
        va = a[k]
        get_xml(doc, doc, bt, va)

        print bt.toprettyxml(indent = '    ')

def main():

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
#    main()
    xml_create()
