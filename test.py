import unittest
import db
from Task import TaskFunctions 


class Test(unittest.TestCase):
    def test_for_create_task(self):
        task = TaskFunctions()
        message = 'task-12'
        lastId = task.createTask(message)
        taskQuery = db.session.query(db.Task).filter(db.Task.id == lastId).first()
        self.assertEqual(taskQuery.message, message, "Task was not created")
    
    def test_for_delete_task(self):
        task = TaskFunctions()
        taskId = 1
        task.deleteTask(taskId)
        # check if task still exists
        taskQuery = db.session.query(db.Task).filter(db.Task.id == taskId).first()
        self.assertEqual(taskQuery, None, "Task was not deleted!")
    
    def test_for_deleting_non_existent_task(self):
        task = TaskFunctions()
        taskId = 54
        queryRes = task.deleteTask(taskId)
        self.assertEqual(queryRes, -1, "Task was deleted!")
    
    def test_for_update_task(self):
        task = TaskFunctions()
        taskNewMessage = 'newtask'
        taskId = task.createTask(taskNewMessage)
        print(task.updateTask(taskId, taskNewMessage))
        taskQuery = db.session.query(db.Task).filter(db.Task.id == taskId).first()
        self.assertEqual(taskQuery.message, taskNewMessage, "Task hasn't been updated!")
        task.getAllTasks()
    
    def test_for_stopping_task(self):
        task = TaskFunctions()
        taskId = task.createTask('sample-task-2')
        task.stopTask(taskId)
        newTask = db.session.query(db.Task).filter(db.Task.id == taskId).first()
        self.assertEqual(newTask.status, False, "Task didn't stopped!")
        self.assertNotEqual(newTask.stopped_at, None, "Task has no stopped_at timestamp")

    def test_for_killall_tasks(self):
        task = TaskFunctions()
        task.killAllTasks()
        queryRes = db.session.query(db.Task).all()
        self.assertEqual(len(queryRes), 0, "Not all tasks were deleted!")



if __name__ == '__main__':
    unittest.main()