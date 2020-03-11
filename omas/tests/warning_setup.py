"""Sets up warnings for OMAS tests"""
import warnings
import os

hard_warnings = True
print('Setting up OMAS warnings for user {}'.format(os.environ['USER']))


def set_omas_warnings():
    """Activates 'hard mode' warnings for OMAS tests"""
    import matplotlib

    # Turn all warnings into errors!
    warnings.filterwarnings('error')

    # Selectively downgrade certain warnings into just warnings, but make them go off every time instead of just once.
    warnings.filterwarnings('always', category=RuntimeWarning, message='.*may indicate binary incompatibility.*')
    warnings.filterwarnings('always', category=FutureWarning, message='The Panel class is removed.*')
    warnings.filterwarnings('always', category=UserWarning, message='Attempting to set identical left==right.*')
    warnings.filterwarnings('always', category=UserWarning, message='No contour levels were found.*')
    warnings.filterwarnings('always', category=matplotlib.cbook.deprecation.MatplotlibDeprecationWarning)
    warnings.filterwarnings('always', category=DeprecationWarning, message='Using or importing the ABCs.*')
    warnings.filterwarnings('always', category=RuntimeWarning, message='invalid value encountered.*')
    print('OMAS warnings set to hard mode')
    return


if hard_warnings:
    set_omas_warnings()