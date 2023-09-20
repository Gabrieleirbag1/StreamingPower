from bs4 import BeautifulSoup

# Ouvrir le fichier HTML existant
with open('/home/frigiel/Documents/VSCODE/Django/Films/propterre/templates/propterre/series.html', 'r') as fichier:
    contenu = fichier.read()

# Créer un objet BeautifulSoup
soup = BeautifulSoup(contenu, 'html.parser')



# Seriestout
seriestout = soup.new_tag('div')
seriestout['class'] = 'seriestout' 

seriestout

# imgdiv0
imgdiv0 = soup.new_tag('div')
imgdiv0['class'] = 'imgdiv0' 
imgdiv0['draggable'] = 'false'
imgdiv0

#img
img = soup.new_tag('img')
img['class'] = 'd-block w-100'
img['id'] = 'manageimg'
img['draggable'] = 'false'
img['src'] = "{% static 'propterre/images/affiches/mandalorian.jpg' %}"
img.string = ""
img

imgdiv2 = soup.new_tag('div')
imgdiv2 ['class']='imgdiv2'

# Créer la structure HTML à insérer dans imgdiv2
saisons = soup.new_tag('div') 
saisons['class']='saisons'
ul = soup.new_tag('ul')
ul["class"]='nav nav-tabs'
ul['id']='myTab'
ul['role']='tablist'

# Créer les boutons pour chaque saison
saisons_buttons = [
    {'id': 'saison1', 'text': 'Saison 1', 'active': True},
    {'id': 'saison2', 'text': 'Saison 2', 'active': False},
    {'id': 'saison3', 'text': 'Saison 3', 'active': False}
]

li = soup.new_tag('li')
li['class']='nav-item'
li['role']='presentation'

button = soup.new_tag('button')
button['class']='nav-link active active1' 
button['id'] = "testsaison1"
button['data-bs-toggle'] = 'tab'
button['data-bs-target'] = '#home-tab-pane3'
button['type'] = 'button'
button['role'] = 'tab'
button['aria-controls'] = 'home-tab-pane3'
button['aria-selected'] = 'true'
button.string = 'Saison 1'


# Créer le contenu des saisons
tab_content = soup.new_tag('div')
tab_content['class']='tab-content boutonsseries'
tab_content['id']='myTabContent'

saison1_tab = soup.new_tag('div')
saison1_tab['class']='tab-pane active show fade'
saison1_tab['id']='home-tab-pane3'
saison1_tab['role']='tabpanel'
saison1_tab['aria-labelledby']='testsaison1'
saison1_tab['tabindex']='0'

a_saison = soup.new_tag('a', href='1')

saison1_btn = soup.new_tag('button')
saison1_btn['class']='custom-btn btn-15'
saison1_btn['id']='btn15'
saison1_btn.string = 'Épisode 1'

# Trouver la balise carou2 existante
carou2 = soup.find('div', class_='carou2')


# insertion seriestout dans carou2, imgdiv2 dans seriestout
carou2.append(seriestout)
seriestout.append(imgdiv0)
seriestout.append(imgdiv2)
imgdiv0.append(img)

tab_content.append(saison1_tab)
saisons.append(ul)
saisons.append(tab_content)
imgdiv2.append(saisons)

li.append(button)
ul.append(li)

a_saison.append(saison1_btn)
saison1_tab.append(a_saison)

#ajout de \n
carou2.insert_before('\n')
carou2.insert_after('\n')
seriestout.insert_after('\n')
seriestout.insert_before('\n')
imgdiv0.insert_before('\n')
imgdiv0.insert_after('\n')
img.insert_before('\n')
img.insert_after('\n')
imgdiv2.insert_before('\n')
imgdiv2.insert_after('\n')
saisons.insert_after('\n')
saisons.insert_before('\n')

ul.insert_before('\n')
ul.insert_after('\n')
li.insert_after('\n')
li.insert_before('\n')
button.insert_before('\n')
button.insert_after('\n')
tab_content.insert_before('\n')
tab_content.insert_after('\n')
saison1_tab.insert_before('\n')
saison1_tab.insert_after('\n')
saison1_btn.insert_after('\n')
saison1_btn.insert_before('\n')

a_saison.insert_before('\n')
a_saison.insert_after('\n')



# Sauvegarder le fichier modifié
with open('/home/frigiel/Documents/VSCODE/Django/Films/propterre/templates/propterre/series.html', 'w') as fichier:
    fichier.write(str(soup))









""" 
<div class="seriestout">
    <div class="imgdiv0" draggable="false"> 
        <img src="{% static 'propterre/images/affiches/mandalorian.jpg' %}"  class="d-block w-100" id='manageimg' draggable="false"> </div>


    <div class='imgdiv2'>
        <div class="saisons">
            <ul class="nav nav-tabs" id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                <button class="nav-link active active1" id="saison1" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Saison 1</button>
                </li>
                <li class="nav-item" role="presentation">
                <button class="nav-link active1" id="saison2" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Saison 2</button>
                </li>
                <li class="nav-item" role="presentation">
                <button class="nav-link active1" id="saison3" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Saison 3</button>
                </li>
            </ul>
            <div class="tab-content boutonsseries" id="myTabContent">
                <div class="tab-pane fade" id="home-tab-pane" role="tabpanel" aria-labelledby="saison1" tabindex="0">
                    <a href="1"> <button class="custom-btn btn-15" id="btn15">Épisode 1</button> </a>
                </div>
            </div>
        </div>
    </div>
</div>
"""

