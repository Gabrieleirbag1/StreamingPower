import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'terrien.settings')
django.setup()

from django.contrib.auth.models import User

def delete_user(username):
    try:
        user_to_delete = User.objects.get(username=username)
        user_to_delete.delete()
        print(f"Utilisateur {username} supprimé avec succès.")
    except User.DoesNotExist:
        print(f"Utilisateur {username} introuvable.")

if __name__ == "__main__":
    username_to_delete = input("Quel est le nom de l'utilisateur à supprimer ? \n")  # Remplacez par le nom d'utilisateur de l'utilisateur que vous voulez supprimer
    delete_user(username_to_delete)
