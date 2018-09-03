from service import app
from flask import request, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from service.models import  WishList
from typing import List

class WishView:
    def __init__(self, wish: WishList):
        self.name = wish.name
        self.description = wish.description
        self.cost = wish.cost
        self.links = wish.links.splitlines() if wish.links != '' and wish.links is not None else []
        self.picture = wish.picture

@app.route('/', methods=['GET'])
def index():
    wishes = WishList.select()
    wishes = [WishView(wish) for wish in wishes]
    return render_template('index.html',
                           title='Wishlist',
                           wishes=wishes)