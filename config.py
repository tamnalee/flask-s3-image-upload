import secrets


class Config :
    JWT_SECRET_KEY = 'yhacademy1029##heelo'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True
    

    ACCESS_KEY = 'AKIA2NJ35QVMK6XUC4BT'
    SECREAT_ACCESS = 'pc0DKLmIVu27uVaRlD0A2JDSYeOdag4tpxKm/9dU'


    # S3 버킷이름과, 기본 URL 주소 셋팅
    S3_BUCKET = 'tamnalee-image-test'
    S3_LOCATION = 'https://tamnalee-image-test.s3.amazonws.com/'