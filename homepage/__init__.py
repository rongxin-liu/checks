import check50
import check50.c
import re


@check50.check()
def exists(self):
    """homepagereflect.txt exists."""
    check50.exists("homepagereflect.txt")
