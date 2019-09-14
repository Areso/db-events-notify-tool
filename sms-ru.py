#!/usr/bin/python3
import sys
import os
import requests
import time
import mysql.connector
import argparse


def myloading():
	cfgpath = "config-sms-ru.txt"
	fconf = open(cfgpath, 'r')
	tconf = fconf.read()
	fconf.close()
	conf_list = tconf.split('\n')
	phone = conf_list[0]
	apikey = conf_list[1]
	return conf_list


def send_message(msg_params):
	sms_url = 'https://sms.ru/sms/send?api_id=key&to=number&msg=message&json=1'
	sms_url = sms_url.replace('number', msg_params[0])
	sms_url = sms_url.replace('key', msg_params[1])
	message = 'there is new data in '+msg_params[2]+'!'
	#print(message)
	sms_url = sms_url.replace('message', message)
	# TODO try block. Sometimes SMS.RU get stuck
	sms_response = requests.get(sms_url)
	sms_response = str(sms_response)
	succesCodeIndex = sms_response.find('200')
	if succesCodeIndex != -1:
		returnAnswer = "OK"
	else:
		returnAnswer = "fail"
	print(returnAnswer)

def mainf():
	parser = argparse.ArgumentParser()
	parser.add_argument("db", help="database name", type=str)
	args = parser.parse_args()
	dbname = args.db
	my_params = myloading()
	my_params.append(dbname)
	send_message(my_params)
	
	
if __name__ == "__main__":
	mainf()
else:
	main(f)
	#print("the program is being imported into another module")
