
from system.core.model import Model

class Task(Model):
    def __init__(self):
        super(Task, self).__init__()


    def create_task(self, form_data, user_id):
          
        query = "INSERT into tasks (date, time, title, status, user_id) values(:date, :time, :title, :status, :user_id)"
        print "Form data:\n"
        print form_data
        print "\n"
        data = {
            'user_id': user_id,
            'title': form_data['title'],
            'status': form_data['status'],
            'date': form_data['date'],
            'time': form_data['time']
        }
        return self.db.query_db(query, data)

    def fetch_tasks_by_id(self, id):
        query = "SELECT * from tasks  where id =:id"
        data = {'id' : id}
        return self.db.query_db(query, data)

    def fetch_tasks_by_user_id(self, id):
        query = "SELECT tasks.id, title, time, status, date from tasks join users on users.id = tasks.user_id where users.id =:user_id AND date != CURDATE()"
        data = {'user_id' : id}
        return self.db.query_db(query, data) 


    def fetch_tasks_by_date(self, id):
        query = "SELECT tasks.id, title, time, status, date from tasks where user_id= :user_id AND date=CURDATE()"
        data = {'user_id' : id}
        return self.db.query_db(query, data)

    def delete_task(self, id, user_id):
        query = "DELETE from tasks where user_id = :user_id and tasks.id = :id"
        data = {
            'id' : id,
            'user_id' : user_id
        }
        return self.db.query_db(query, data)

    def edit_task(self, form_data, id ):
        query = "UPDATE tasks SET title = :title, status = :status, time= :time, date = :date WHERE id = :id "
        data = {
            'id' : id,    
            'title': form_data['title'],
            'date': form_data['date'],
            'time': form_data['time']
            }
        return self.db.query_db(query, data)
         # running out of time to make this work


