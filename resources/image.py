from datetime impoert data
from flask_restful import Resource
from flask import request
from mysql.connector.errors import Error
from flask_jwt_extended import get_jwt_identity, jwt_required
import mysql.connector
 
class FileUploadResource(Resource)

    def post(self) : 

# 1. 클라이언트로부터 데이터를 받아온다.
# 2. request.files에 파일을 받아온다.
# 3. 따라서 파일이 없는 상태로 API가 호출되면, 에러메세지를 클라이언트에 응답해주자.

# photo란, 클라이언트에서 보내는 key!!
if 'photo' not in request.files :
    return {'error' : '파일을 업로드 하세요'}, 400

#클라이언트로부터 파일을 받아온다.
file = request.files['photo']

#파일명을 우리가 변경해준다
# 파일명은, 유니크하게 만들어야 한다.
current_time = datatime.now()
new_file_name = current_time.format().replace(':' , '-')

# 유저가 올린 파일의 이름을, 내가만든 파일명으로 변경
file.filename = new_file_name


# S3에 업로드 하면된다.
# AWA에 라이브러리를 사용해야 한다.
# 이 파이썬 라이브러리를 boto3 라이브러리다.
# boto3 라이브러리 설치
# pip install boto3





return
        

        

