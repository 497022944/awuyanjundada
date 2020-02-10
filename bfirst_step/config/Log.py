# coding=utf-8
import logging,os,time

class Log:
    '''
    Log().info(msg)
    Log().debug(msg)
    Log().warning(msg)
    Log().error(msg)
    '''
    def __init__(self):
        # 初始化存放log文件文件夹
        dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.logdir = os.path.join(dir_path+'\\logs')
        print(self.logdir)
        if not os.path.exists(self.logdir):
            os.mkdir(self.logdir)
        # log名称
        self.logname = os.path.join(self.logdir,time.strftime("%Y_%m_%d")+'info'+'.log')
        # 创建logger
        self.logger = logging.getLogger()
        # 等级设为debug
        self.logger.setLevel(logging.DEBUG)
        # 赋值format
        self.format = logging.Formatter('[%(asctime)s] - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
    def __console(self,level,msg):
        # 创建filehandler
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)
        # 创建streamhandler
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.format)
        self.logger.addHandler(sh)
        if level == 'info':
            self.logger.info(msg)
        if level == 'debug':
            self.logger.debug(msg)
        if level == 'warning':
            self.logger.warning(msg)
        if level == 'error':
            self.logger.error(msg)
        ## 删除handler，要不然输出重复日志
        self.logger.removeHandler(fh)
        self.logger.removeHandler(sh)
    def info(self,msg):
        self.__console('info',msg)
    def warning(self,msg):
        self.__console('warning',msg)
    def error(self,msg):
        self.__console('error',msg)

if __name__ == '__main__':
    log = Log()
