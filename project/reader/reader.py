from flask import Blueprint,render_template,url_for,request,make_response,redirect

reader = Blueprint('reader',__name__,template_folder='templates')

