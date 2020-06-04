import os
import tempfile

_basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sdfj;*(*E^832JLJhfjdh&*&*^'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(
                                _basedir,
                                'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

del os
del tempfile
