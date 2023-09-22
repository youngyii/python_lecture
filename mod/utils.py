import math
import random

def mt_sqrt(x) :
    return math.sqrt(x)
            
def mt_sinpi() :
    return math.sin(math.pi / 2)

def mt_elog() :
    return math.log(math.e)
    
def mt_exp(x) :
    return math.exp(x)
    
def mt_pi() :
    return math.pi

#---------

def rd_int(x, y):
    return random.randint(x, y)

def rd_choice(x):
    return random.choice(x)

def rd_rd():
    return random.random()

def rd_nv():
    return random.normalvariate()