import os, sys
try:
    __import__("rnd64").check()
except Exception as e:
    exit(str(e))