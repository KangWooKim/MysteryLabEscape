import json
import pymysql

# RDS 데이터베이스 연결 정보
rds_host = "mysterylabescape.cfeku6yo6dx1.ap-northeast-2.rds.amazonaws.com"
name = "axis_heaven"
password = "your-password"  # 실제 비밀번호로 교체
db_name = "mysterylabescape"

def lambda_handler(event, context):
    connection = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name)
    
    if event['path'] == '/register':
        return register_player(event, connection)
    elif event['path'] == '/login':
        return login_player(event, connection)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported operation')
        }

def register_player(event, connection):
    data = json.loads(event['body'])
    username = data['username']
    password_hash = data['password']
    email = data['email']
    nickname = data['nickname']
    avatar_url = data['avatar_url']
    
    with connection.cursor() as cursor:
        sql = "INSERT INTO players (username, password_hash, email, nickname, avatar_url) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (username, password_hash, email, nickname, avatar_url))
        connection.commit()
    
    return {
        'statusCode': 201,
        'body': json.dumps('Player registered successfully')
    }

def login_player(event, connection):
    data = json.loads(event['body'])
    username = data['username']
    password_hash = data['password']
    
    with connection.cursor() as cursor:
        sql = "SELECT password_hash FROM players WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
    
    if result and result[0] == password_hash:
        return {
            'statusCode': 200,
            'body': json.dumps('Login successful')
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps('Login failed')
        }
