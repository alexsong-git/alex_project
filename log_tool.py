from tool import read_txt
import os
import logging

def log_tool(log_file_path,name):
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
        print(f"已删除旧的日志文件：{log_file_path}")
    else:
        print(f"日志文件不存在，无需删除：{log_file_path}")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"{name}.log"),  # 将日志写入文件
            logging.StreamHandler()  # 同时输出日志到控制台
        ]
    )
    logger = logging.getLogger("selenium_test")
    logger.info('')
    logger.info('start')
    return logger
