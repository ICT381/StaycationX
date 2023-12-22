from flask import jsonify, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

# Specific to API
from flask_httpauth import HTTPBasicAuth
from bson import json_util
from flask_cors import cross_origin

from app.extensions import cors

from app.models.users import User
from app.models.package import Package
from app.models.token import UserTokens
# from app import app

api = Blueprint('api', __name__)

api_auth = HTTPBasicAuth()

@api.route('/api/user/gettoken', methods=['POST'])
# @cross_origin(origin='http://localhost:3000')
def api_gettoken():
    if request.method == 'POST': 

        # if testing using Python Jupyter Notebook
        # email = request.form.get('email')
        # password = request.form.get('password')

        try:
            data = request.json
            if data: # if using ReactJS
                email = data['email']
                password = data['password']
        except: # if using python
            email = request.form.get('email')
            password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User.getUser(email=email)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        if not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid password'}), 401

        token =  UserTokens.getToken(email = email)
        
        if token:
            return jsonify({'token': token}), 200

        current_datetime = datetime.now()
        datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        # Simulated token generation (replace with actual token logic)
        token = generate_password_hash(user.email+datetime_str, method='sha256')
        UserTokens.createToken(email = user.email, token=token)
        return jsonify({'token': token}), 200

# Protected route for authorized users
@api.route('/api/protected')
@api_auth.login_required
def protected():
    return jsonify({'message': 'You are authorized to see this message'}), 201

def extract_keys(dictionary, running_id=1):
    """
    Extracts specific keys from a dictionary and adds an "id" key with a running number.

    Args:
        dictionary: The dictionary to extract keys from.
        running_id: The initial value for the "id" key (default: 1).

    Returns:
        A new dictionary containing the extracted keys and the "id" key.
    """
    extracted_data = {
        key: dictionary[key]
        for key in ["hotel_name", "image_url", "description"]
        if key in dictionary
    }
    extracted_data["id"] = running_id
    return extracted_data
    
@api.route('/api/package/getAllPackages', methods=['POST'])
# @cross_origin(origin='http://localhost:3000')
@api_auth.login_required
def getAllPackages():
    allPackages = Package.getAllPackages()
    # products_dict = [json.loads(json_util.dumps(product.to_mongo())) for product in products]
    packages_list = [json.loads(json_util.dumps(package.to_mongo())) for package in allPackages]
    projected_list = [extract_keys(k, idx+1) for idx, k in enumerate(packages_list)]
    return jsonify({'data': projected_list}), 201

@api_auth.verify_password
def verify_password(email, token):
    user = UserTokens.getToken(email=email)
    if user and user.token==token:
        return True
    else:
        return False
