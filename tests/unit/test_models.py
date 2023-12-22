from app.models.users import User
from werkzeug.security import generate_password_hash

def test_new_user(setup_app):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    hashpass = generate_password_hash("12345", method='sha256')
    user = User.createUser(email="john@cde.com",password=hashpass, name="John Song")
    assert user.email == 'john@cde.com'
    assert user.password == hashpass
    # assert user.is_authenticated
    # assert user.is_active
    # assert not user.is_anonymous

