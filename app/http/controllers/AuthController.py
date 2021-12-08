"""A AuthController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from app.User import User


class AuthController(Controller):
    """AuthController Controller Class."""

    def __init__(self, request: Request, auth:Auth):
        """AuthController Initializer"""
        self.request = request
        self.auth = auth

    def login(self):
        username = self.request.input("username")
        password = self.request.input("password")
        result= self.auth.login(username,password)
        return result
      
    def signup(self):
      username = self.request.input("username")
      password = self.request.input("password")
      
      print(username,password)
      result = self.auth.register({"username": username, "password": password})
      return result
    
    def logout(self):
      self.auth.logout()
      return "Logged Out"
    
    def users(self):
      return User.all()