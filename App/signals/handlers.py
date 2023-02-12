#!/usr/bin/env python
# -* -coding:utf-8 -*-
# @author: 高晨
# @time: 2021/10/12 4:57 下午
# @file: handlers.py
# @desc:
from time import sleep

import django.dispatch
from django.core.signals import request_finished
from django.dispatch import receiver


my_signal = django.dispatch.Signal()

@receiver(request_finished,dispatch_uid="request")
def my_signal_handler2(sender, **kwargs):
    print(sender)
    print(kwargs.get('name'))
    print('my_signal received')
    sleep(5)




