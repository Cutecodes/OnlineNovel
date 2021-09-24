from flask import Blueprint,render_template,url_for,request,make_response,redirect

editor = Blueprint('editor',__name__,template_folder='templates')

