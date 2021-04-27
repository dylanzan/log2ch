import os
import queue
from clickhouse_driver import Client

REPORT_PATH= "../../../../PycharmProjects/report2Clickhouse/report/"
insert_by_hour_sql_str_pro="insert into fs_report.tracking_report_by_hour values({})"
insert_by_day_sql_str_pro="insert into fs_report.tracking_report_by_day values({})"

FINAL_HOST="121.5.252.185"
FINAL_PORT="9000"

class ReportHandler(object):

    contentQueue=queue.Queue()
    cretiveIdSet=set()
    creativeTrackingDict=dict()

    clickhouse_house=""
    clickhouse_port=""
    clickhouse_client=Client(host=clickhouse_house,port=clickhouse_port)

    def __init__(self,clickhouse_house,clickhouse_port):
        self.getCreativeIdsSet()
        self.clickhouse_house=clickhouse_house
        self.clickhouse_port=clickhouse_port

    def getFiles(self):
        return os.listdir(path=REPORT_PATH)

    #report's data to queue
    def contentToQueueProducer(self):
        files=self.getFiles()
        for file in files:
            file=open(REPORT_PATH+file)
            iter_f=iter(file)
            for line_str in iter_f:
                self.contentQueue.put(line_str)

    #获取文件夹中的所有creativeId
    def getCreativeIdsSet(self):
        files=self.getFiles()
        for file in files:
            file = open(REPORT_PATH + file)
            iter_f = iter(file)
            for line_str in iter_f:
                lines=str.split(line_str,":")
                creative_id=lines[2]
                #self.cretiveIdSet.add(creative_id)
                self.creativeTrackingDict[creative_id].append(dict())


    def reportHandlerConsumer(self):
        FINAL_IMP_KEY='imp'
        FINAL_CLK_KEY = 'clk'
        FINAL_WIN_KEY = 'win'
        FINAL_CST_KEY = 'cst'
        for creativeIdFromDict in range(self.creativeTrackingDict.keys()):
            for dataReprot in range(self.contentQueue):
                #typeDict={}  #{type:count}
                dataStrSplit = str.split(dataReprot, ":")
                tracking_type = dataStrSplit[0]
                # media_num = dataStrSplit[1]
                creative_id = dataStrSplit[2]
                date_statistics_str = dataStrSplit[4]
                num=str.split(date_statistics_str,"|")[1]
                if creativeIdFromDict==creative_id:
                    typeDict=dict(self.creativeTrackingDict[creative_id])
                    if tracking_type==FINAL_IMP_KEY:
                        if not typeDict:
                            impnum=typeDict.get(FINAL_IMP_KEY)
                            impsum=int(impnum)+int(num)
                            typeDict[FINAL_IMP_KEY]=impsum
                        else:
                            typeDict[FINAL_IMP_KEY]=num
                            self.creativeTrackingDict[creative_id]=typeDict
                    elif tracking_type==FINAL_CLK_KEY:
                        if not typeDict:
                            impnum=typeDict.get(FINAL_CLK_KEY)
                            impsum=int(impnum)+int(num)
                            typeDict[FINAL_CLK_KEY]=impsum
                        else:
                            typeDict[FINAL_CLK_KEY]=num
                            self.creativeTrackingDict[creative_id]=typeDict
                    elif tracking_type==FINAL_CST_KEY:
                        if not typeDict:
                            impnum=typeDict.get(FINAL_CST_KEY)
                            impsum=int(impnum)+int(num)
                            typeDict[FINAL_CST_KEY]=impsum
                        else:
                            typeDict[FINAL_CST_KEY]=num
                            self.creativeTrackingDict[creative_id]=typeDict
                    elif tracking_type==FINAL_WIN_KEY:
                        if not typeDict:
                            impnum=typeDict.get(FINAL_WIN_KEY)
                            impsum=int(impnum)+int(num)
                            typeDict[FINAL_WIN_KEY]=impsum
                        else:
                            typeDict[FINAL_WIN_KEY]=num
                            self.creativeTrackingDict[creative_id]=typeDict
        for creative_id in range(self.creativeTrackingDict.keys()):
            typeRes=dict(self.creativeTrackingDict.get(creative_id))
            res=dict(typeRes.get(FINAL_IMP_KEY))
            impSqlStr="[{}]".format(creative_id,",",FINAL_IMP_KEY,",",res.get(FINAL_IMP_KEY))
            clkSqlStr="[{}]".format(creative_id,",",FINAL_IMP_KEY,",",res.get(FINAL_IMP_KEY))
            winSqlStr="[{}]".format(creative_id,",",FINAL_IMP_KEY,",",res.get(FINAL_IMP_KEY))
            cstSqlStr="[{}]".format(creative_id,",",FINAL_IMP_KEY,",",res.get(FINAL_IMP_KEY))
            insertSqlStr=insert_by_day_sql_str_pro.format(impSqlStr,",",clkSqlStr,",",winSqlStr,",",cstSqlStr)
            self.clickhouse_client.execute(insertSqlStr)












    def Run(self):
        pass
