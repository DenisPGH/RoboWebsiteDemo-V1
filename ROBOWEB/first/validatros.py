from django.core.exceptions import ValidationError
# from ROBO.first.models import User
#from ROBO.first.helper import logged_user
from django.utils.deconstruct import deconstructible


def validator_min_lenght(text):
    """this function validate, if text is less than bestimt value"""
    how_much=8
    if len(text)<how_much:
        raise ValidationError(f"The text must be at least {how_much} long")

def vaidator_current_username(name):
    """ this function prove the correct user name"""
    right_name="Denislav"
    if name != right_name:
        raise ValidationError(f"There is no registration with {name}! ")

def validator_current_user_password():
    pass



@deconstructible
class MaxFileSizeInMbValidator():
    """dont work this"""
    def __init__(self,*args,**kwargs):
        self.max_size = 0.000000000001

    def __call__(self, value):
        filesize = value.file.size

        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError("Max file size is 1MB")


def max_file_size(value): # add this to some file where you can import it from
    """this function is for max size of uplaod images"""
    limit = 1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MB.')