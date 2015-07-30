#!/usr/bin/python

import re
import os
import sys
import string
import pdb

class parseOMLog:
    """this class is used to parse OMLog* and IMSRtLog* file"""
    def __init__(self, dirName=None, fileName=None):
        self.srcFileName = dirName+fileName
        self.dirName=dirName
        self.fileName=fileName

    def parseRtLog(self, newfilename=None, title=0, sep="~", subSep="`"):
        tarFileName = self.dirName+newfilename
        try:
            fileId = open(self.srcFileName,'r')
            tarFileId = open(tarFileName,'a')
        except IOError:
            print "file open fail\n"
            sys.exit()

        content = fileId.read()
        all_list = re.split('[\s]*END OF REPORT #[0-9]{6}\+\+-\n[^\s]{1}\n',content)
        out_title = ("FEName" + sep + "Day" + sep + "Time" + sep +
                     "MsgClass" + sep + "Blade" + sep + "OMLog Title" + sep +
                     "OMLog Description" + sep + "OMLog Log ID" + sep + "\n")
        if not os.path.getsize(tarFileName):
            tarFileId.write(out_title)
        for one_log in all_list:
            if not one_log:
                continue
            output = ""
            for one_line in one_log.split("\n"):
                if not one_line:
                    continue
                if re.match("^[\s]*\+\+\+", one_line):
                    _, node, day, time, msg_class, _, blade, _ = one_line.split()
                    output = node+sep+day+sep+time+sep+msg_class+sep+blade+sep
                elif len(one_line.split()) == 2 and one_line.split()[0] == "A":
                    output = output + one_line.split()[1] + sep
                elif one_line.split("=")[0].strip() == "Message Id":
                    output = output + sep + one_line.split("=")[1].strip(";") + sep
                else:
                    output = output + one_line
            output = output+"\n"
            tarFileId.write(output)
        tarFileId.close
        fileId.close


def main():
    """main function"""
    working_dir = sys.argv[1]
    if (not os.path.exists(working_dir)):
        print ("logfile dir doesn't exist, exit!")
        sys.exit()
    print "begin to parse....."
    if not working_dir.endswith("/"):
        working_dir = working_dir + "/"
    for _, _, file_list in os.walk(working_dir):
        for one_file in file_list:
            if re.match("IMSRtLog[0-9]+", one_file):
                imsrt_parser = parseOMLog(working_dir, one_file)
                imsrt_parser.parseRtLog("OMLOG")
                print "parsing " + one_file
        print "End parse"


if __name__ == "__main__":
    main()

