#!/usr/bin/env python
# -*- coding: utf-8 -*-

from suds.client import Client
from suds.transport.https import HttpAuthenticated as HA

t = HA(username='admin', password='123')
test = Client()
