# -*- coding:utf-

# 让python2 使用中文编码

import logging
import threading
import datetime
import os

# 标准日志写法 
def log_thread_id():
    logging.warning("[Process id {0}]--[thread id {1}]--Time: {2}--[log_process_thread_id.py]--[log_thread_id]--[12]--[Warning]--FilePath: {3} \n [message: {4}]"
                    .format(os.getpid(), threading.currentThread().ident, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), os.getcwd(), "this is a warning message"))
    try:
        s = 14/0
    except Exception, e:
        logging.error("[Process id {0}]--[thread id {1}]--Time: {2}--[log_process_thread_id.py]--[log_thread_id]--[12]--[Error]--FilePath: {3} \n [message: {4}]"
                      .format(os.getpid(), threading.currentThread().ident,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), os.getcwd(), "this is a error message"), exc_info=True)

if __name__ == "__main__":
    log_thread_id()