"""
This is the app module
"""

# 3rd party modules
from flask import make_response, abort
import mysql.connector
import datetime
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="new4",
  database="mytest"
)

mycursor = mydb.cursor()


### For Customer 

def customerfind(cno):
    mycursor.execute("SELECT c_surname,c_name FROM customer where c_no=%s", (cno,))
    row_headers=[xf[0] for xf in mycursor.description] 
    myresult = mycursor.fetchall()
    json_data=[]
    for x in myresult:
       json_data.append(dict(zip(row_headers,x)))
       #print json.dumps(json_data)
    if len(myresult) >= 1:
         return json.dumps(json_data)
    else:
        return abort(404, "Customer {cno} not found".format(cno=cno))


def customerdelete(cno):
    try:
    	sql_Delete_query = """Delete from customer where c_no = %s"""
    	mycursor.execute(sql_Delete_query,(cno,))
        mydb.commit()
    	return make_response("Customer {cno} successfully deleted".format(cno=cno), 200)
    except mysql.connector.Error as error:
    	return abort(406, "Failed to delete Customer {cno}".format(cno=cno))

### For Order 

def orderstatus(oid):
    mycursor.execute("SELECT o_currentstat FROM od where o_no=%s", (oid,))
    row_headers=[xf[0] for xf in mycursor.description] 
    myresult = mycursor.fetchall()
    json_data=[]
    for x in myresult:
       json_data.append(dict(zip(row_headers,x)))
    if len(myresult) >= 1:
         return json.dumps(json_data)
    else:
        abort(404, "Order {oid} not found".format(oid=oid))
    return person


def ordercreate(order):

    cid = order.get("cid", None)
    ptype = order.get("pizza", None)

    # Does the person exist already ?

    mycursor.execute("SELECT c_no,c_name,c_surname FROM customer where c_no=%s", (cid,))
    row_headers=[xf[0] for xf in mycursor.description] 
    myresult = mycursor.fetchall()
    if myresult != None:
        now = datetime.datetime.now()
        str_now = now.date().isoformat()
        sql = "INSERT INTO od (o_date,o_currentstat,o_customer,o_pizztype) VALUES (%s,%s,%s,%s)"
        val = (str_now,0,cid,ptype)
        try: 
	     mycursor.execute(sql, val)
	     mydb.commit()
             return make_response("Your order successfully created",201)
        except mysql.connector.Error as error:
	     #return error
    	     return abort(404, "Failed to add your order")
    else:

        abort(406, "Error Customer ID {cid}".format(cid=cid),)

### For Menu

def findfood(fno):
    mycursor.execute("SELECT f_name FROM food where f_no=%s", (fno,))
    row_headers=[xf[0] for xf in mycursor.description] 
    myresult = mycursor.fetchall()
    json_data=[]
    for x in myresult:
       json_data.append(dict(zip(row_headers,x)))
    if len(myresult) >= 1:
         return json.dumps(json_data)
    else:
        return abort(404, "Food {fno} not found".format(fno=fno))


def deletefood(fno):
    try:
    	sql_Delete_query = """Delete from food where f_no = %s"""
    	mycursor.execute(sql_Delete_query,(fno,))
        mydb.commit()
    	return make_response("Food {fno} successfully deleted".format(fno=fno), 200)
    except mysql.connector.Error as error:
    	return abort(406, "Failed to delete Food {fno}".format(fno=fno))
