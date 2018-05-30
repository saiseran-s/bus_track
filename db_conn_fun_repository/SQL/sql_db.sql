/* Database structure and relations */
--  a. MySQL database
 	A structured database is required for driver and bus data maintainance and to form relation with among them.
-- b. MongoDB
 	A noSQL database is required for writing the data received by the device listener.


creating foriegn key relationship
/* CREATE TABLE accounts(
    account_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT( 4 ) NOT NULL ,
    account_type ENUM( 'savings', 'credit' ) NOT NULL,
    balance FLOAT( 9 ) NOT NULL,
    PRIMARY KEY ( account_id ),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=INNODB;
*/
========================================================================================================
DATABASE NAME "auth"
========================================================================================================
1. table_1                          [Driver_details]
    a. col_1 [id]					      [int]
    b. col_2 [name]					    [varchar]
    c. col_3 [mobile No.]		   	[bigint]
    d. col_4 [license number]		[varchar]
	# e. col_5 [area/destination]	[varchar]
	  f. col_6 [address]		   		[varchar]

	create table table_1(col_1 int( 6 ) not null primary key auto_increment, col_2 varchar( 40 ) not null unique key, col_3 bigint( 11 ) not null unique key, col_4 varchar( 16 ) not null unique key, col_5 varchar( 25 ) not null)ENGINE = INNODB;

	insert into table_1(col_2,col_3,col_4,col_5) values("Raj Kiran",9933251485,"AP0420184518659","Samalkota");
	insert into table_1(col_2,col_3,col_4,col_5) values("Surya Rao",9949586214,"AP0420074752168","Peddapuram");
	insert into table_1(col_2,col_3,col_4,col_5) values("Lakshmi Narayana",9100548623,"AP0220145236487","Kakinada");
	insert into table_1(col_2,col_3,col_4,col_5) values("Appa Rao",8324568974,"AP0120154723658","Sitanagaram");
	insert into table_1(col_2,col_3,col_4,col_5) values("Nagababu",7613481664,"AP0120134582892","Ravulapalem");
	insert into table_1(col_2,col_3,col_4,col_5) values("Raju",9933278485,"AP0420184514559","Samalkota");
	insert into table_1(col_2,col_3,col_4,col_5) values("Surya Krishna",9949586354,"AP0420074751268","Peddapuram");
	insert into table_1(col_2,col_3,col_4,col_5) values("Narayana",9100548486,"AP0220145215487","Kakinada");
	insert into table_1(col_2,col_3,col_4,col_5) values("Appala Swami",8324458264,"AP0120154774858","Goppallai");
	insert into table_1(col_2,col_3,col_4,col_5) values("Samram Nagaraju",7613412457,"AP0120134748596","Ravulapalem");


2. table_2 								[Bus Data]
	a. l_1 [id]						[int]
	b. col_2 [Bus No.]					[varchar]
	c. col_3 [Bus Registration No.]		[varchar]
	d. col_4 [Driver_details(name)]		[varchar]
	e. col_5 [destination/area]			[varchar]

	create table table_2(l_1 int( 5 ) not null auto_increment, col_2 varchar( 4 ) not null unique key, col_3 varchar( 10 ) not null unique key, col_4 varchar( 40 ) not null, col_5 varchar( 25 ) not null,PRIMARY KEY (l_1),FOREIGN KEY (col_4) REFERENCES table_1(col_2))ENGINE=INNODB;

	inssert into table_2(col_2,col_3,col_4,col_5) values("431","AP05CC1547","Raj Kiran","Samalkota")



3. Table_3 [Relation between Driver_details and Bus Data]
