from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from time import time

def getMysqlConnection():
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
	return mydb

def mycursor_execute(sql,mycursor):
	try:
		mycursor.execute(sql)
		return {"statut":True}
	except Exception as e:
		return {"statut":False,"erreur":e}

def mycursor_fetchall(mycursor):
	try:
		s = mycursor.fetchall()
		return {"statut":True,"retour":s}
	except Exception as e:
		return {"statut":False,"erreur":e}

def mydb_commit(mydb):
	try:
		mydb.commit()
		return {"statut":True}
	except Exception as e:
		return {"statut":False,"erreur":e}

from ajouter_valeurs import *

messages2_post_args = reqparse.RequestParser()
messages2_post_args.add_argument("Nom",type=str,required=True)
messages2_post_args.add_argument("Message",type=str,required=True)

class messages1(Resource):
	def post(self): #recuperer_message
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		mycursor.execute("SELECT Nom,Message_,Date_ FROM Message")
		resultat = [{"Nom":i[0],"Message":i[1],"Date":i[2]} for i in mycursor.fetchall()]

		mycursor.close()
		mydb.close()

		return {"retour":"ok","valeurs":resultat}


class messages2(Resource):
	def post(self): #ajouter_message
		body = messages2_post_args.parse_args()
		[Nom,Message] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		ajouter_Message(Nom,Message,int(time()),mycursor,mydb)

		mycursor.close()
		mydb.close()

		return {"retour":"ok"}




