#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# create a second list of strings
approved_animal = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished
