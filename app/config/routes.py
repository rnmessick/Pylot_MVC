from system.core.router import routes

routes['GET']['/'] = 'Welcome#index'
routes['GET']['/login_reg'] = 'Welcome#display_login_reg'



routes['POST']['/login'] = 'Users#login'
routes['GET']['/logout'] = 'Users#logout'
routes['POST']['/register'] = 'Users#register'
routes['GET']['/users/appointments/<int:id>'] = 'Users#dashboard'
routes['GET']['/appointments/<int:id>'] = 'Users#view_task'

routes['POST']['/appointments/add'] = 'Tasks#create_task'
routes['POST']['/appointments/<int:id>/edit/<int:tid>'] = 'Tasks#edit_task'
routes['GET']['/appointments/<int:id>/delete/<int:tid>'] = 'Tasks#delete_task'


"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
