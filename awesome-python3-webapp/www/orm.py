#!/usr/bin/env python3
# -*- coding: utf-8 -*-
​
__author__ = 'Michael Liao'
5
​
6
import asyncio, logging
7
​
8
import aiomysql
9
​
10
def log(sql, args=()):
11
    logging.info('SQL: %s' % sql)
12
​
13
async def create_pool(loop, **kw):
14
    logging.info('create database connection pool...')
15
    global __pool
16
    __pool = await aiomysql.create_pool(
17
        host=kw.get('host', 'localhost'),
18
        port=kw.get('port', 3306),
19
        user=kw['user'],
20
        password=kw['password'],
21
        db=kw['db'],
22
        charset=kw.get('charset', 'utf8'),
23
        autocommit=kw.get('autocommit', True),
24
        maxsize=kw.get('maxsize', 10),
25
        minsize=kw.get('minsize', 1),
26
        loop=loop
27
    )
28
​
29
async def select(sql, args, size=None):
30
    log(sql, args)
31
    global __pool
32
    async with __pool.get() as conn:
33
        async with conn.cursor(aiomysql.DictCursor) as cur:
34
            await cur.execute(sql.replace('?', '%s'), args or ())
35
            if size:
36
                rs = await cur.fetchmany(size)
37
            else:


# Traceback (most recent call last):
# ZeroDivisionError: division by zero
# invalid literal for int() with base 10: ' 7.6'
# token is invalid
# Unable to import 'aliyunsdkcore.client'
# from aliyunsdkcore.client import AcsClient
# ModuleNotFoundError: No module named 'aliyunsdkcore'
# multiprocessing
# Using variable 'ticket' before assignmentpylint(used-before-assignment)

