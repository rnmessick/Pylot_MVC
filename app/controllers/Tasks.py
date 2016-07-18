
from system.core.controller import *

class Tasks(Controller):
    def __init__(self, action):
        super(Tasks, self).__init__(action)

        self.load_model('Task')
        self.db = self._app.db

    def create_task(self):
        user_id = session['user']['id'] 
    	self.models['Task'].create_task(request.form, user_id)
    	return redirect('/users/appointments/{}'.format(user_id))

    def delete_task(self,id, tid):
        user_id = session['user']['id'] 
        self.models['Task'].delete_task( id, tid)
        return redirect('/users/appointments/{}'.format(user_id))

    def edit_task(self, id):
        self.models['Task'].edit_task(request.form,id)
        return redirect('/users/appointments/{}'.format(id))



