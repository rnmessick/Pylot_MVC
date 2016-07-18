from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Task')
        self.db = self._app.db

       
    def register(self):
        # Validate registration information
        validation_result = self.models['User'].validate_reg_info(request.form)
        return self.handle_reg_response(validation_result)

    def handle_reg_response(self, result): # think we might want to not pass in id, but extract from session object
        if type(result) == list:
            session['val_errors'] = result
            return redirect('/')        
        else:
            flash("You have succesfully registered!")
            return redirect('/')


    def login(self):
        login_result = self.models['User'].login(request.form)
        return self.handle_login_response(login_result)

    def handle_login_response(self, result): # think we might want to not pass in id, but extract from session object
        if type(result) == list:
            session['val_errors'] = result
            return redirect('/')        
        else:
            return self.set_user_session(result)            

    def logout(self):
        session.clear()
        return redirect('/')

    def set_user_session(self, validation_result):
        session['user'] = validation_result 
        user_id = session['user']['id'] 

        return redirect('/users/appointments/{}'.format(user_id))

    def dashboard(self,id):
        # Grab all tasks
        tasks = self.models['Task'].fetch_tasks_by_date(id)
        other_tasks = self.models['Task'].fetch_tasks_by_user_id(id)
        return self.load_view('dashboard.html', tasks=tasks, other_tasks=other_tasks)

    def view_task(self, id):
        tasks = self.models['Task'].fetch_tasks_by_id(id)
        return self.load_view('edit.html', tasks=tasks)   

