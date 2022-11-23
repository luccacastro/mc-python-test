import db
import datetime
import tabulate

class TaskFunctions():
    
    def convertToDict(self, queryRes):
        dictRes = []
        resData = {}
        for queryRow in queryRes.all():
            queryRow = queryRow.__dict__
            del queryRow['_sa_instance_state']
            dictRes.append(queryRow)
        resData['headers'] = dictRes[0].keys()
        resData['values'] = [x.values() for x in dictRes]
        return resData

    def createTask(self, message):
        new_task = db.Task(message)
        db.session.add(new_task)
        db.session.commit()
        lastTask = db.session.query(db.Task).order_by(db.Task.id.desc()).first()
        # print(taskQuery)
        return lastTask.id

    def getAllTasks(self):  
        queryRes = db.session.query(db.Task)
        if queryRes.count():
            taskData = self.convertToDict(queryRes)
            return tabulate.tabulate(taskData['values'], taskData['headers'])
        return 'No Tasks found'

    def deleteTask(self, taskId):
        taskQuery = db.session.query(db.Task).filter(db.Task.id == taskId).delete()
        if taskQuery:
            db.session.commit()
            return 0
        return -1


    def updateTask(self, taskId, newMessage):
        taskObj = db.session.query(db.Task).filter(db.Task.id == taskId).first()
        if taskObj:
            taskObj.message = newMessage
            db.session.add(taskObj)
            db.session.commit()
            return 'Task has been updated successfully'
        return f"Couldn't find task with such ID {taskId}"


    def stopTask(self, taskId):
        taskQuery = db.session.query(db.Task).filter(db.Task.id == taskId).first()
        if taskQuery:
            if taskQuery.status:
                taskQuery.status = False
                taskQuery.stopped_at = datetime.datetime.utcnow()
                db.session.add(taskQuery)
                db.session.commit()
                return 'Task has been stopped successfully'
            return 'Task already stopped'
        return f"Couldn't find task with such ID {taskId}"


    def killAllTasks(self):
        queryRes = db.session.query(db.Task).all()
        for item in queryRes:
            self.deleteTask(item.id)
        return 'All tasks have been deleted'
    
    def filterStop(self):
        filterQuery = db.session.query(db.Task).filter(not db.Task.status)
        if filterQuery.count():
            taskData = self.convertToDict(filterQuery)
            return tabulate.tabulate(taskData['values'], taskData['headers'])
        return 'No Tasks found'
