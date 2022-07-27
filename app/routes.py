from app import app
from flask import render_template

@app.route('/')
def home():
    favpokemon = [
    {'name':'Piplup',
    'img':'https://cdn.mos.cms.futurecdn.net/z7FMWtXppvebVdJchsrTz5.jpg'},
    {'name':'Togepi',
    'img':'https://www.geekmi.news/__export/1615993146734/sites/debate/img/2021/03/17/togepi.jpg_1753094345.jpg'},
    {'name':'Shaymin',
    'img':'https://static.pokemonpets.com/images/monsters-images-800-800/492-Shaymin-Land.webp'},
    {'name':'Vulpix',
    'img':'https://s3.narvii.com/image/bmypzglmcylyvo7qzf6cabrbpye47s5n_hq.jpg'},
    {'name':'Emolga',
    'img':'https://assets.pokemon.com/assets/cms2/img/watch-pokemon-tv/seasons/season14/season14_ep24_ss01.jpg'},]
    return render_template('home.html', favs = favpokemon)

@app.route('/select')
def select():
    return render_template('select.html')

