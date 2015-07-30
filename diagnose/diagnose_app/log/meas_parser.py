#!/bin/env python

import re
import os
import sys
import string
import pdb

class parse_meas:
    """this class is used to parse measlog*"""
    def __init__(self, dir, file_name):
        self.meas_file = dir + file_name
        self.dir = dir
        self.file_name = file_name

    def parse_log(self):
        """parse meas log"""        
        with open(self.meas_file, "r") as src_file:
            content = src_file.read()
            meas_list = re.split('[\s]*END OF REPORT #[0-9]{6}\+\+-\n[^\s]{1}\n', content)
            for one_meas in meas_list:
                lines=re.split("\n", one_meas)
                len_lines = len(lines)
                if len_lines < 5:
                    continue
                if "MS_PROCESS_MEAS" in lines[3].split():
                    self.parse_cpu_per_process(lines)
                if re.match("^[\s]*SPA =", lines[4]):
                    self.parse_one_table(lines)


    def parse_cpu_per_process(self, lines, sep="~"):
        """parse cpu per process and fill it in file"""
        len_lines = len(lines)
        record_num = len_lines - 10
        _, node, day, time, _, _, _, _ = lines[0].split()
        line_prefix = node + sep + day + sep + time + sep
        out_title = ""
        for col in ("NodeName", "Day", "Time", "Duration", "Station_ID", "Process", "CPU"):
            out_title = out_title + col + sep
        out_title = out_title+"\n"
        target_file = self.dir + "MS_PROCESS_MEAS"
        with open(target_file,'a') as target_file_id:
            if not os.path.getsize(target_file):
                target_file_id.write(out_title)
            for j in range(9, len_lines):
                output = line_prefix
                line = lines[j].split()
                len_line = len(line)
                for one_cnt in range(0, len_line):
                    output = output + line[one_cnt] + sep
                output = output+"\n"
                target_file_id.write(output)


    def parse_one_table(self, lines, sep="~"):
        """parse one meas and fill it in file"""

        table = lines[3].split()[3]
        if not table == "SDM_MEAS_LOAD_STATION_HSS":
            return
        len_lines = len(lines)
        out_title="FEName"+sep+"Day"+sep+"Time"+sep+"MsgClass"+sep+"Blade"+sep
        loop_num=0
        for j in lines:
            if(re.match("^[\s]*Measurement for table", j)):
                loop_num=loop_num+1
        record_num = ((len_lines-2)/loop_num) - 7
        for j in range(7, len_lines-record_num, 7+record_num):
            line = lines[j].split()
            len_line = len(line)
            for m in range(0, len_line):
                out_title = out_title + line[m] + sep
        out_title = out_title + "\n"
        target_file = self.dir + table
        with open(target_file, 'a') as target_file_id:
            if not os.path.getsize(target_file):
                target_file_id.write(out_title) 
            line = re.split('\s+', lines[0])
            line_prefix = line[2]+sep+line[3]+sep+line[4]+sep+line[5]+sep+line[7]+sep
            for j in range(0, record_num):
                output = line_prefix
                for k in range(9+j, len_lines, 7+record_num):
                    line = lines[k].split()
                    len_line = len(line)
                    for m in range(0, len_line):
                        output = output + line[m] + sep
                output = output+"\n"
                target_file_id.write(output)


def main():
    working_dir = sys.argv[1]
    if (not os.path.exists(working_dir)):
        print ("logfile dir doesn't exist, exit!")
        sys.exit()
    print "begin to parse....."
    if not working_dir.endswith("/"):
        working_dir = working_dir + "/"
    walkResult = os.walk(working_dir)
    for i in walkResult:
        for log_file in i[2]:
            if(re.match("measlog[0-9]+", log_file)):
                meas_parser = parse_meas(working_dir, log_file)
                print "parsing " + log_file
                meas_parser.parse_log()
    print "End parse"


if __name__ == "__main__":
    main()


