from view import View
from controller import Controller
from model import Model

controller = Controller(View(),Model())
controller.runner();
