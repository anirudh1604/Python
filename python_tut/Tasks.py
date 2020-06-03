import datetime as datetime

from Databaseconnectivity import Databaseconnectivity
class Tasks :

    def setTask_id(self,num):
        self.task_id=num    
    def getTask_id(self):
        return self.task_id

    def setTitle(self,num):
        self.Title=num    
    def getTitle(self):
        return self.Title

    def setStart_Date(self,num):
        self.Start_Date=num    
    def getStart_Date(self):
        return self.Start_Date

    def setDue_Date(self,num):
        self.Due_Date=num    
    def getDue_Date(self):
        return self.Due_Date
    


    def setStatus(self,num):
        self.Status=num    
    def getStaus(self):
        return self.Status
    

    def setPriority(self,num):
        self.Priority=num    
    def getPriority(self):
        return self.Priority
    
    
    def setDescription(self,num):
        self.Description=num    
    def getDescription(self):
        return self.Description

task=Tasks()

task.setDescription("Desc")
task.setPriority(1)
task.setTask_id(28)
task.setTitle("Book2")
task.setStart_Date(datetime.date(2016,7,24))
task.setDue_Date(datetime.date(2016,8,24))
task.setStatus(1)



db_task=Databaseconnectivity()
db_task.insertTask(task)