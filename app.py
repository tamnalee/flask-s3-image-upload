from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config


app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# jwt 토큰 라이브러리 만들기
jwt = JWTManager(app)

api = Api(app)

# 경로와 리소스(API)