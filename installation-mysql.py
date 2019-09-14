#!/usr/bin/python3
import sys
import os
import mysql.connector


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
	print(loop_params[8])
	if loop_params[8] == "mod":
		sql = "ALTER TABLE "+table_md+" ADD is_ack INT DEFAULT 0;"
		print(sql)
		mycursor.execute(sql)
		sql = "UPDATE "+table_md+" SET is_ack = 1 WHERE is_ack = 0;"
		print(sql)
		mycursor.execute(sql)
	else:
		sql = """CREATE TABLE events_notify (
			id_event int(11) NOT NULL,
			is_ack tinyint(11) NOT NULL DEFAULT '0')
			ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
		print(sql)
		mycursor.execute(sql)
		sql = """ALTER TABLE events_notify
			ADD PRIMARY KEY (id_event);"""
		print(sql)
		mycursor.execute(sql)
		sql = """ALTER TABLE events_notify
			MODIFY id_event int(11) NOT NULL AUTO_INCREMENT;"""
		print(sql)
		mycursor.execute(sql)
		sql = "CREATE TRIGGER notify_trigger AFTER INSERT ON "+table_md+" FOR EACH ROW INSERT INTO events_notify (id_event, is_ack) VALUES (NULL, '0')"
		print(sql)
	mycursor.execute(sql)
	print("setup completed")


if __name__ == "__main__":
	my_params = myloading()
	config_db(my_params)
else:
	print("the program is being imported into another module")
