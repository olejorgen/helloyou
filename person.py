# -*- coding: utf-8 -*-
#This is an object
__author__ = 'OleJorgen'
class Person(object):
    firstname = " "
    lastname = " "
    fullname = " "
    def __init__(self,firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.fullname=firstname+" "+lastname

    def print(self):
        print("Firstname "+self.firstname)
        print("Lastname "+self.lastname)
        print("Fullname "+self.fullname)
    def math(self,x,y):
        while (x<100):
            z=x*y
            x=x+1
            print(z)

