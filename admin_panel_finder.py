#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def Space(j):
	i = 0
	while i<=j:
		print (" ")
		i+=1


def findAdmin():
	f = open("/home/daniktertri/coding/git_clone/admin-panel-finder/link.txt","r")
	link = input("Enter Site Name \n(ex : example.com or www.example.com )")
	print ("\n\nAvilable links : \n")
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print ("OK => ",req_link)

def Credit():
	Space(1); print ("#####################################")
	Space(1); print ("#   +++ Admin Panel Finder v2 +++   #")
	Space(1); print ("#     Script by Illûmïnåté Ðëmøñ    #")
	Space(1); print ("#    Script upgraded by daniktertri #")
	Space(1); print ("#    Bangladesh Black Hat Hackers   #")
	Space(1); print ("#####################################")

Credit()
findAdmin()
