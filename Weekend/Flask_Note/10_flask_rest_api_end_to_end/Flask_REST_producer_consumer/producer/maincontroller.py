from flask_rest_api_end_to_end.producer.productcontroller import *
from flask_rest_api_end_to_end.producer.vendorcontroller import *
from flask_rest_api_end_to_end.producer.productvendorcontroller import *
from flask_rest_api_end_to_end.producer.config import db

if __name__ == '__main__':
    db.create_all()
    print('Tables created... and now service is starting..!')
    app.run(debug=True)
