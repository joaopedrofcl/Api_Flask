from flask import Flask
from flask_restplus import Api

class server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            
            version='1.0',
            title='API de Digimon',
            description='API criada para estudo que contém as informações dos principais digimons da franquia',
            doc='/docs'

        )
        pass

    def run(self, ):
        self.app.run(
            debug=True
        )

server = server()