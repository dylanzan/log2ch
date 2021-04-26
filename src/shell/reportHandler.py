import os
import queue

REPORT_PATH= "../../../../PycharmProjects/report2Clickhouse/report/"
insert_by_hour_sql_str_pro="insert into fs_report.tracking_report_by_hour"
insert_by_day_sql_str_pro="insert into fs_report.tracking_report_by_day"

class ReportHandler(object):


    contentQueue=queue.Queue()
    cretiveIdSet=set()

    def __init__(self):
        self.getCreativeIdsSet()

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
                self.cretiveIdSet.add(creative_id)



    def reportToCHConsumer(self):
        FINAL_IMP='imp'
        FINAL_CLK = 'clk'
        FINAL_WIN = 'win'
        FINAL_CST = 'cst'


        for creativeIdFromSet in range(self.cretiveIdSet):
            for dataReprot in range(self.contentQueue):
                typeDict={}  #{type:count}
                dataStrSplit = str.split(dataReprot, ":")
                tracking_type = dataStrSplit[0]
                # media_num = dataStrSplit[1]
                creative_id = dataStrSplit[2]
                date_statistics_str = dataStrSplit[4]
                if creativeIdFromSet == creative_id:
                    if tracking_type==FINAL_IMP:
                        num=int(str.split(date_statistics_str,"|")[1])
                        count=int(typeDict[FINAL_IMP])
                        typeDict[FINAL_IMP]=count+num
                if creativeIdFromSet == creative_id:
                    if tracking_type==FINAL_CLK:
                        num=int(str.split(date_statistics_str,"|")[1])
                        count=int(typeDict[FINAL_CLK])
                        typeDict[FINAL_CLK]=count+num
                if creativeIdFromSet == creative_id:
                    if tracking_type==FINAL_WIN:
                        num=int(str.split(date_statistics_str,"|")[1])
                        count=int(typeDict[FINAL_WIN])
                        typeDict[FINAL_WIN]=count+num
                if creativeIdFromSet == creative_id:
                    if tracking_type==FINAL_CST:
                        num=int(str.split(date_statistics_str,"|")[1])
                        count=int(typeDict[FINAL_CST])
                        typeDict[FINAL_CST]=count+num

                '''
                values_by_imp = []
                values_by_clk = []
                values_by_cst = []
                values_by_win = []
                values_by_impU1 = []
                values_by_impU2 = []
                values_by_impU3 = []
                values_by_impU4 = []
                values_by_impU5 = []
                values_by_impU6 = []
                values_by_impU7 = []
                values_by_impU8 = []
                values_by_impN1 = []
                values_by_impN2 = []
                values_by_impN3 = []
                values_by_impN4 = []
                values_by_impN5 = []
                values_by_impN6 = []
                values_by_impN7 = []
                values_by_impN8 = []
                values_by_impT1 = []
                values_by_impT2 = []
                values_by_impT3 = []
                values_by_impT4 = []
                values_by_impT5 = []
                values_by_impT6 = []
                values_by_impT7 = []
                values_by_impT8 = []
                dataStrSplit=str.split(dataReprot,":")
                tracking_type=dataStrSplit[0]
                #media_num = dataStrSplit[1]
                creative_id = dataStrSplit[2]
                date_statistics_str = dataStrSplit[4]
                if creativeIdFromSet==creative_id:
                    if tracking_type=="imp":
                        values_by_imp.append()
                    if tracking_type=="clk":
                        values_by_clk.append()
                    if tracking_type=="win":
                        values_by_win.append()
                    if tracking_type=="cst":
                        values_by_cst.append()
                    if tracking_type == "impU1":
                        values_by_impU1.append()
                    if tracking_type == "impU2":
                        values_by_impU2.append()
                    if tracking_type == "impU3":
                        values_by_impU3.append()
                    if tracking_type == "impU4":
                        values_by_impU4.append()
                    if tracking_type == "impU5":
                        values_by_impU5.append()
                    if tracking_type == "impU6":
                        values_by_impU6.append()
                    if tracking_type == "impU7":
                        values_by_impU7.append()
                    if tracking_type == "impU8":
                        values_by_impU8.append()
                    if tracking_type == "impN1":
                        values_by_impN1.append()
                    if tracking_type == "impN2":
                        values_by_impN2.append()
                    if tracking_type == "impN3":
                        values_by_impN3.append()
                    if tracking_type == "impN4":
                        values_by_impN4.append()
                    if tracking_type == "impN5":
                        values_by_impN5.append()
                    if tracking_type == "impN6":
                        values_by_impN6.append()
                    if tracking_type == "impN6":
                        values_by_impN6.append()
                    if tracking_type == "impN7":
                        values_by_impN7.append()
                    if tracking_type == "impN8":
                        values_by_impN8.append()
                    if tracking_type == "impT1":
                        values_by_impT1.append()
                    if tracking_type == "impT2":
                        values_by_impT2.append()
                    if tracking_type == "impT3":
                        values_by_impT3.append()
                    if tracking_type == "impT4":
                        values_by_impT4.append()
                    if tracking_type == "impT5":
                        values_by_impT5.append()
                    if tracking_type == "impT6":
                        values_by_impT6.append()
                    if tracking_type == "impT6":
                        values_by_impT6.append()
                    if tracking_type == "impT7":
                        values_by_impT7.append()
                    if tracking_type == "impT8":
                        values_by_impT8.append()
                '''







    def Run(self):
        pass



def if __name__ == '__main__':
    pass

