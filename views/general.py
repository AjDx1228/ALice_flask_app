from flask import Blueprint, render_template, request, jsonify, session 
from models.users import *

mod = Blueprint('general', __name__)

@mod.route('/main', methods=["GET"])
def main():
    print(request.remote_addr)
    return render_template('main.html')
