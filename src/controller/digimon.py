from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server
app, api = server.app, server.api


digimon_db = [
    
    {'nome':'Agumon' , 'nivel':'hookie' , 'tipo':'data'},
    {'nome':'Veemon' , 'nivel':'hookie' , 'tipo':'vacina'},
    {'nome':'Guilmon' , 'nivel':'hookie' , 'tipo':'virus'},
    {'nome':'Greymon' , 'nivel':'champion' , 'tipo':'data'},
    {'nome':'Flamedramon' , 'nivel':'Ultimate' , 'tipo':'vacina'},
    {'nome':'Growmon' , 'nivel':'champion' , 'tipo':'virus'}

]

@api.route('/digimons')
class DigimonList(Resource):
    def get(self, ):
        return digimon_db
