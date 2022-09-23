from flask import Flask
# from sqlalchemy import true


""" 
    flask constructor takes the name of current module (__name__) as argument 
"""
app=Flask(__name__)


"""
    the route() function of flask class is a decorator,which tells  the application which URL should call the associated function
    """
@app.route('/')
def home():
    return 'home'

#main driver function 
if __name__=='__main__':
    """ run() method of flask class runs the application on the local development server
    """
    app.run(host='0.0.0.0',port=6342,debug=True)

