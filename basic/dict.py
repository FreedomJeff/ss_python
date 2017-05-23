#!/usr/bin/env python
#-*- coding:utf-8 -*-
product_list = {
    'hawaii':{
        'china':['black','1099rmb'],   
        'america':['red','599$'],
    },   
    'pfone':{
        'north africa':['gray','1499'], 
        'mexico':['red','599$'],
    }, 
    'dallas':{
        'russia':['blue','1099'],
        'china':['purple', '399$'],
    }, 
}

print(product_list['hawaii']['china'])
for key in product_list:
    print(key, product_list[key])

product_list['dallas']['china'][0] += '_grey'
print(product_list['dallas']['china'])
