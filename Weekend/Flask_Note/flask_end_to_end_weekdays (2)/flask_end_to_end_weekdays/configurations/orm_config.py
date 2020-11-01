#sqlalchemy configuration
from flask_end_to_end_weekdays.helper.app_queries import *
from flask_sqlalchemy import SQLAlchemy
from flask_end_to_end_weekdays.configurations.app_config import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOST,DB_NAME)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=P_USERNAME,pw=P_PASSWORD,url=P_HOST,db=P_DB)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False      # dont showcase warning msgs
app.config['SQLALCHEMY_ECHO']=False      # print queries
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:pymysql//root:root@localhost/flaskdb'
db = SQLAlchemy(app)


#ORM -- DATABASE INDEPENDENT --> AT POINT ANY POINT OF POINT TIME-- U CAN CHANGE-- DATABASE