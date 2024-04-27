from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, request, redirect, render_template, url_for, escape

from app.models.forms import BookForm

from app.models.users import User
from app.models.package import Package

package = Blueprint('packageController', __name__)

@package.route('/')
@package.route('/packages')
def packages():
    all_packages = Package.getAllPackages()
    return render_template('packages.html', panel="Package", all_packages=all_packages)

@package.route("/viewPackageDetail/<hotel_name>")
def viewPackageDetail(hotel_name):
    the_package = Package.getPackage(hotel_name=hotel_name)
    return render_template('packageDetail.html', panel="Package Detail", package=the_package)

# The following is added for vulnerability 
@package.route('/redirect')
def query_example():
    # Access the query parameter 'query' from the request
    query_param = request.args.get('query')
    #query_param = escape(request.args.get('query'))
    
    
    # Process the query parameter (e.g., perform validation, sanitize, etc.)
    # In this example, we'll simply return the query parameter value
    if query_param == "1":
        all_packages = Package.getAllPackages()
        return render_template('packages.html', panel="Package", all_packages=all_packages)
    else:
        return f"Received query parameter: {query_param}"

@package.route('/create_staycation', methods=['GET', 'POST'])
def create_staycation():
    if request.method == 'POST':
        # Get form data
        hotel_name = request.form.get('hotel_name')
        duration = int(request.form.get('duration'))
        unit_cost = float(request.form.get('unit_cost'))
        image_url = request.form.get('image_url')
        description = request.form.get('description')
        #description = escape(request.form.get('description'))


        # Create a new Staycation document
        Package.createPackage(hotel_name=hotel_name, duration=duration,
                        unit_cost=unit_cost, image_url=image_url,
                        description=description)

        return redirect(url_for('packageController.packages'))

    return render_template('staycation_form.html', panel="Create Staycation Package")
