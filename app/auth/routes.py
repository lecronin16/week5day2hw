from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserCreationForm
import requests

auth = Blueprint('auth', __name__, template_folder='authtemplates')


@auth.route('/select', methods=["GET", "POST"])
def pokeName():
    form = UserCreationForm()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            poke_name = form.poke_name.data
            response =requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_name}')
            data = response.json()
            poke_dict = {}
            pokemon = data['name']
            poke_dict[pokemon] = {
                'name' : data['name'],
                'ability' : data['abilities'][0]['ability']['name'],
                'base_experience' : data['base_experience'],
                'pic' : data['sprites']['front_shiny'],
                'attack_base' : data['stats'][1]['base_stat'],
                'hp_base' : data['stats'][0]['base_stat'],
                'defense_base' : data['stats'][2]['base_stat']
                }
            return poke_dict
            return redirect(url_for('auth.pokeDex'))
        else:
            print('validation failed')
    else:
        print('GET req made')

    return render_template('select.html', form = form)


# @auth.route('/poke')
# def pokeDex(poke_name):
#     url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
#     response = requests.get(url)
#     data = response.json()
#     poke_dict = {}
#     pokemon = data['name']
#     poke_dict[pokemon] = {
#         'name' : data['name'],
#         'ability' : data['abilities'][0]['ability']['name'],
#         'base_experience' : data['base_experience'],
#         'pic' : data['sprites']['front_shiny'],
#         'attack_base' : data['stats'][1]['base_stat'],
#         'hp_base' : data['stats'][0]['base_stat'],
#         'defense_base' : data['stats'][2]['base_stat']
#         }
#     return poke_dict
