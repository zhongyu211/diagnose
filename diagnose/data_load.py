from django.db import connection,transaction
import os
import commands

class data_load:
    """
    this class use to load data from log to db
    """
    def __init__(self,logdir):
        self.logdir = logdir

    def run_cmd_list(self, cmd_list):
        for cmd in cmd_list:
            ret = os.system(cmd)
            if ret != 0:
                return False
        return True

    def log_rework(self):
        """
        this function is used for log rework, prepare the db data
        """
        if not os.access(self.logdir, os.F_OK):
            return
        #os.chrdir(self.logdir, os.F_OK)
        cmd_list = []
        cmd_list.append("mkdir -p data")
        cmd_list.append("./meas_parser.py %s" %(self.logdir))
        cmd_list.append("./omlog_parse.py %s" %(self.logdir))
        cmd_list.append("mv %s/*_MEAS* data" %(self.logdir))
        cmd_list.append("mv %s/OMLOG data" %(self.logdir))
        
        self.run_cmd_list(cmd_list)
        for parent,dirnames,filenames in os.walk("data"):
            for filename in filenames:
                fullname = parent + '/' + filename
                file_tmp = fullname + '.tmp'
                cmd_list = []
                cmd_list.append("sed '1d' %s > tmp" %(fullname))
                cmd_list.append("awk '{print FNR\"~\"$0}' tmp > %s" %(file_tmp))
                cmd_list.append("rm -rf tmp")
                self.run_cmd_list(cmd_list)

    def load_file(self):
        self.log_rework()
        files = commands.getoutput("ls data/*.tmp").split("\n")
        for file in files:
            tablename = 'diagnose_app_' + file.split('.tmp')[0].split('data/')[1].lower()
            #print tablename
            file_fullpath = os.getcwd() + '/' + file
            cursor = connection.cursor()
            cursor.execute('delete from %s' %(tablename))
            cursor.execute('LOAD DATA INFILE "%s" INTO TABLE %s FIELDS TERMINATED BY "~"' %(file_fullpath, tablename))
            transaction.commit_unless_managed()
        os.system("rm -rf data")
        
#dl=data_load("/home/alzhong")
#dl.load_file()


