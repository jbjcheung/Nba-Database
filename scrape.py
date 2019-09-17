import requests
from bs4 import BeautifulSoup
import MySQLdb
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


HOST = "*****"
USERNAME = ""*****""
PASSWORD = ""*****""
DATABASE = "mydb"

url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
soup.findAll('tr', limit=2)


rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]



try:
    connection = mysql.connector.connect(host=HOST, database=DATABASE, user=USERNAME, port=3307, password=PASSWORD)
    insert_query = """INSERT INTO stats2019(Player,Pos,Age,Team,G,GS,MP,FG,FGA,FGPercent,3P,3PA,3PPercent,2P,2PA,2PPercent,eFGPercent,FT,FTA,FTPercent,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor = connection.cursor()
    for i in range(len(player_stats)):
        if len(player_stats[i]) != 0:
            recordTuple = (player_stats[i][0],player_stats[i][1],player_stats[i][2],player_stats[i][3],player_stats[i][4],player_stats[i][5],player_stats[i][6],player_stats[i][7],player_stats[i][8],player_stats[i][9],player_stats[i][10],player_stats[i][11],player_stats[i][12],player_stats[i][13],player_stats[i][14],player_stats[i][15],player_stats[i][16],player_stats[i][17],player_stats[i][18],player_stats[i][19],player_stats[i][20],player_stats[i][21],player_stats[i][22],player_stats[i][23],player_stats[i][24],player_stats[i][25],player_stats[i][26],player_stats[i][27],player_stats[i][28])
            cursor.execute(insert_query, recordTuple)
    connection.commit()
    cursor.close()
    print(cursor.rowcount, "Data has been inserted")

	
	
	
except mysql.connector.Error as error:
    print("Failed to insert data".format(error))

