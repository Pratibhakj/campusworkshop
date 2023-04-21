"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch12v8bh4hstbhh6kukg-a.oregon-postgres.render.com",
        database="todo_8jd3",
        user="todo_8jd3_user",
        password="zLm6e13vy2QIcqJ5j1ND1T0IrHgzZ0ZD")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
