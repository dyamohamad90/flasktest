# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(master password)@(db_identifier).amazonaws.com:3306/(db_name)
#https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:flasktest@flasktest.chdsnjoqqaid.ap-southeast-1.rds.amazonaws.com:3306/flaskdb'


# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
