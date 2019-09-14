<html>
<body>
<h1>
db events notify tool
</h1>
This three step installation project allows you to be notified of new inserts in table of a database:
<ol>
<li>edit configs
<ul><li>edit config.txt (if needed)</li>
    <li>edit config-mysql.txt (you can find example in config-mysql-example.txt)</li>
    <li>edit config-sms-ru.txt (you can find example in config-mysql-example.txt)</li>
</ul></li>
<li>run python3 installation-mysql.py (if needed, install mysql.connector first)</li>
<li>add mysql-dbevents-notify.py in crontab or systemd to autorun watcher after reboot</li>
</ol>
<br>
The test insert to try on the tracker project:<br>
INSERT INTO `accounts`(`id_account`, `email`, `passwordh`, `id_company_fk`, `date_of_reg`, `is_blocked`) VALUES (null,"vasya@mail.ru","hash",null,null,0)
</body>
</html>