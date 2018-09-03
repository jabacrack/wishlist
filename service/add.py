from service import app
from flask import request, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from service.models import  WishList
from urllib.parse import urlsplit, urlunsplit

class AddNewItem(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description')
    cost = StringField('cost')
    link = TextAreaField('link')
    picture = StringField('picture')

def parse_links(str:str):
    links = []
    for line in str.strip().splitlines():
        if line is None or "":
            pass
        link = line.strip()
        url_parts = urlsplit(link)
        if not url_parts.scheme:
            url_parts = list(url_parts)
            url_parts[0] = 'http'
            link = urlunsplit(url_parts)
        links.append(link)
    return '\n'.join(links)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddNewItem()
    if form.validate_on_submit():
        item = WishList()
        item.name = form.name.data
        item.description =form.description.data
        item.cost = form.cost.data
        item.links = parse_links(form.link.data)
        item.picture = form.picture.data
        item.save()

        flash('Wish added.')
        return redirect('/add')

    return render_template('add.html',
                           title='Add New',
                           form=form)