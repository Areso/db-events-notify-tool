#!/usr/bin/python3
import sys
import os
import mysql.connector


def myloading():
	cfgpath = "config.txt"
	fconf = open(cfgpath, 'r')
	tconf = fconf.read()
	fconf.close()
	conf_list = tconf.split('\n')
	username = conf_list[0]
	password = conf_list[1]
	hostname = conf_list[2]
	dbport   = conf_list[3]
	database = conf_list[4]
	table_md = conf_list[5]
	print(table_md)
	return conf_list


def config_db(loop_params):
	mydb = mysql.connector.connect(
		host=loop_params[2],
		user=loop_params[0],
		passwd=loop_params[1],
		database=loop_params[4]
	)
	table_md = loop_params[5]
	mydb.autocommit = True
	mycursor = mydb.cursor()
	sql = "ALTER TABLE "+table_md+" ADD is_ack INT DEFAULT 0;"
	print(sql)
	mycursor.execute(sql)
	sql = "UPDATE "+table_md+" SET is_ack = 1 WHERE is_ack = 0;"
	print(sql)
	mycursor.execute(sql)
	print("setup completed")

if __name__ == "__main__":
	my_params = myloading()
	config_db(my_params)
else:
	print("the program is being imported into another module")
