def ajouter_Message(Nom,Message_,Date_,mycursor,mydb):
	val = (Nom,Message_,Date_)
	try:
		mycursor.execute("INSERT INTO Message (Nom,Message_,Date_) VALUES ("+",".join(["%s"]*len(val))+")", val)
	except Exception as e:
		return {"statut":False,"erreur":"pas reussi a insert into"}
	try:
		mydb.commit()
	except:
		return {"statut":False,"erreur":"pas reussi a commit"}
	return {"statut":True}

