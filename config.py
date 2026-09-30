import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

ssl_ca = os.getenv("DB_SSL_CA")

db_args = dict(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "ecommerce_db"),
    port=int(os.getenv("DB_PORT", "3306")),
)
if ssl_ca:
    db_args["ssl_ca"] = ssl_ca
    db_args["ssl_verify_cert"] = True

db = mysql.connector.connect(**db_args)
cursor = db.cursor(buffered=True)

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")