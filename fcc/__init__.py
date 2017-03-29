import os

from .facility import Facility
from .politicalfile import PoliticalFile

from pymodm import connect
connect('mongodb://localhost/fcc')


MODULE_PATH = os.path.dirname(__file__)
os.chdir(MODULE_PATH)