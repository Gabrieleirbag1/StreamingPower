from bs4 import BeautifulSoup
import requests

def main():

    print("Bonjour et bienvenue \n")


    
    nom_film = input('Nom de la série ? - ')
    nom_film = nom_film.replace(" ", "-")
    nom_image = str(input(f'Nom image (avec extension) - '))
    nb_saisons = int(input(f'Combien de saisons ? - '))

   

    '''------------------------------------------------------------------------------------------------------------------'''
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
    img['src'] = "{% static 'propterre/images/affichesseries/" + nom_image + "'%}"
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


     # Créer le contenu des saisons
    tab_content = soup.new_tag('div')
    tab_content['class']='tab-content boutonsseries'
    tab_content['id']='myTabContent'

    x = 0

    for saison in range(nb_saisons):
        x += 1
        url = str(input(f'Url de la saison {x} ? - '))
        response = requests.get(url)
        html = response.text
        soup2 = BeautifulSoup(html, "html.parser")
        video_links = soup2.find_all(lambda tag: tag.name == "a" and not tag.find_parent("th") and tag.text.strip() != "Parent Directory")

        li = soup.new_tag('li')
        li['class']='nav-item'
        li['role']='presentation'


        button = soup.new_tag('button')
        button['class']='nav-link active1' #ajouter active show pour le premier
        button['id'] = f"{nom_film}saison{x}"
        button['data-bs-toggle'] = 'tab'
        button['data-bs-target'] = f'#{nom_film}{x}'
        button['type'] = 'button'
        button['role'] = 'tab'
        button['aria-controls'] = f'{nom_film}{x}'
        button['aria-selected'] = 'false'
        button.string = f'Saison {x}'


        saison1_tab = soup.new_tag('div')
        saison1_tab['class']='tab-pane fade'
        saison1_tab['id']=f'{nom_film}{x}'
        saison1_tab['role']='tabpanel'
        saison1_tab['aria-labelledby']=f'{nom_film}saison{x}'
        saison1_tab['tabindex']='0'

        y = 0
        for link in video_links:
            y += 1
            video_url = link.get("href")
            video_text = link.text #j'utiliserais des rejex pour récup le titre après
            
            if video_url:
                a_saison = soup.new_tag('a', href=f'{url}{video_url}')

            saison1_btn = soup.new_tag('button')
            saison1_btn['class']='custom-btn btn-15'
            saison1_btn['id']='btn15'
            saison1_btn.string = f'Épisode {y}' 

            a_saison.append(saison1_btn)
            saison1_tab.append(a_saison)
            
            saison1_btn.insert_after('\n')
            saison1_btn.insert_before('\n')
            a_saison.insert_before('\n')
            a_saison.insert_after('\n')

        
        li.append(button)
        ul.append(li)
        tab_content.append(saison1_tab)

 
         
        li.insert_after('\n')
        li.insert_before('\n')
        button.insert_before('\n')
        button.insert_after('\n')
        saison1_tab.insert_before('\n')
        saison1_tab.insert_after('\n')
       


    # Trouver la balise carou2 existante
    carou2 = soup.find('div', class_='carou2')

    # insertion seriestout dans carou2, imgdiv2 dans seriestout
    carou2.append(seriestout)
    seriestout.append(imgdiv0)
    seriestout.append(imgdiv2)
    imgdiv0.append(img)

    saisons.append(ul)
    saisons.append(tab_content)
    imgdiv2.append(saisons)

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
   
    tab_content.insert_before('\n')
    tab_content.insert_after('\n')

    # Sauvegarder le fichier modifié
    with open('/home/frigiel/Documents/VSCODE/Django/Films/propterre/templates/propterre/series.html', 'w') as fichier:
        fichier.write(str(soup))
    
    ajout(nom_film)

def ajout(nom_film):

    nom_film = nom_film.replace(" ", "-")
    with open('/home/frigiel/Documents/VSCODE/Django/Films/propterre/templates/propterre/series.html', 'r') as fichier:
        contenu = fichier.read()

    # Créer un objet BeautifulSoup
    soup = BeautifulSoup(contenu, 'html.parser')

    id_specific = f'{nom_film}{1}'
    saison1 = soup.find(id=id_specific)

    if saison1:
        saison1['class'] = ['tab-pane', 'active', 'show', 'fade']
   
    id_specific2 = f'{nom_film}saison{1}'
    saisonactive1 = soup.find(id=id_specific2)

    if saison1:
        saisonactive1['class'] = ['nav-link active active1']


    with open('/home/frigiel/Documents/VSCODE/Django/Films/propterre/templates/propterre/series.html', 'w') as fichier:
        fichier.write(str(soup))

if __name__ == "__main__":
    main()

