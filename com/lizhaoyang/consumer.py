#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'lizhaoyang'

import threading,time

class Consumer(threading.Thread):

    def __init__(self,cond,name):
        super(Consumer,self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ': 我这两件商品一起买，可以便宜点吗')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我已经提交订单了，你修改下价格')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 收到，我支付成功了')
        self.cond.notify()
        self.cond.release()
        print(self.name + ': 等待收货')

class Producer(threading.Thread):

    def __init__(self, cond, name):
        super(Producer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ': 可以的，你提交订单吧')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 好了，已经修改了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 嗯，收款成功，马上给你发货')
        self.cond.release()
        print(self.name + ': 发货商品')

def main():
    cond = threading.Condition()
    consumer = Consumer(cond,"买家")
    producer = Producer(cond,"卖家")
    consumer.start()
    producer.start()



if __name__ == '__main__':
    main()
