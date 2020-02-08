import re

def is_username_valid (username_in):
    if re.match("^(?=.{5,9}$)[a-z]+$", username_in) is not None:
        return True
    else:
        return False
    
def is_password_valid (password_in):
    if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password_in):
        return True
    else:
        return False