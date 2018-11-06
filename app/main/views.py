from . import main

@main.route('/home')
def index():
	return 'home page'