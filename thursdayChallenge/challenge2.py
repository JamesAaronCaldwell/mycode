#! /usr/bin/python3


import requests
import pyexcel
import pandas

def main():

    r= requests.get("https://api.nasa.gov/planetary/apod?api_key=7cqHW801kCstlBsbcprRwwe01awpGk7XVVamgD0d")
    p = pandas.to_excel(r.json())
    print(r)
    print(p)
    #x = norm(r)
    pyexcel.to_excel('~/mycode/nasa.xlsx')
main()
