#!/usr/bin/python3
import sys
import os
import time
import mysql.connector
import subprocess


def myloading():
	cfgpath = "config-mysql.txt"
	fconf = open(cfgpath, 'r')
	tconf = fconf.read()
	fconf.close()
	conf_list = tconf.split('\n')
	
	cfgpath_logic = "config.txt"
	fconf_logic = open(cfgpath_logic, 'r')
	tconf_logic = fconf_logic.read()
	fconf_logic.close()
	conf_list_send = tconf_logic.split('\n')
	conf_list.append(conf_list_send[1])
	conf_list.append(conf_list_send[3])
	return conf_list


def main_loop(loop_params):
	while True:
		mydb = mysql.connector.connect(
			host=loop_params[2],
			user=loop_params[0],
			passwd=loop_params[1],
			database=loop_params[4]
		)
		table_md = loop_params[5]
		mycursor = mydb.cursor()
		print(loop_params[8])
		if loop_params[8] == "mod":
			sql = "select * from "+table_md+" where is_ack = 0"
		else:  # otherwise it is "trigger"
			sql = "select * from events_notify where is_ack = 0"
		print(sql)
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		nonsentorders = len(myresult)
		if nonsentorders > 0: 
			mycommand = 'python3 '+loop_params[7]+' '+loop_params[4]  # loop_params[6] is script name, loop_params[4] is dbname
			p = subprocess.Popen(mycommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,  shell=True)
			data = p.communicate()
			print(data)
			if loop_params[8] == "mod":
				sql = "UPDATE "+table_md+" SET is_ack = 1 WHERE is_ack = 0"
			else:  # otherwise it is "trigger"
				sql = "UPDATE events_notify SET is_ack = 1 WHERE is_ack = 0"
			print(sql)
			mycursor.execute(sql)
			mydb.commit()
		time.sleep(15)


if __name__ == "__main__":
	my_params = myloading()
	main_loop(my_params)
else:
	print("the program is being imported into another module")
