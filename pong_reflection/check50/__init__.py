from check50 import *

class Pset4(Checks):

    @check()
    def submitted(self):
        """You submitted 'PONG Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pong_reflection") for filename in files):
            raise Error("File not found")
