from flask import Blueprint,render_template,url_for,request,make_response,redirect

author = Blueprint('author',__name__,template_folder='templates')

