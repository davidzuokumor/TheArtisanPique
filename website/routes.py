def home():
  return render_template('<h1>Home Page</h1>',title='Home Page')

def about():
return render_template('<h1>About Page</h1>',title='About Page')

def register():
return render_template('<h1>Register Page</h1>',title='Register Page')

def login():
return render_template('<h1>Login Page</h1>',title='Login Page')

def logout():
return render_template('<h1>Logout Page</h1>',title='Logout Page')

def profile():
return render_template('<h1>Profile Page</h1>',title='Profile Page')
