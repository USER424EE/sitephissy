import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# URL cible
url = "https://exemple.com"

# Requête principale
response = requests.get(url)
html_content = response.text

# Sauvegarde du HTML
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Parsing avec BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Création d'un dossier pour les CSS
os.makedirs("css", exist_ok=True)

# Récupération des feuilles de style
for link_tag in soup.find_all("link", rel="stylesheet"):
    css_url = link_tag.get("href")
    full_css_url = urljoin(url, css_url)  # Pour les chemins relatifs

    try:
        css_response = requests.get(full_css_url)
        css_filename = os.path.basename(css_url.split("?")[0])  # Nettoyage du nom

        with open(f"css/{css_filename}", "w", encoding="utf-8") as f:
            f.write(css_response.text)

        print(f"[✓] CSS téléchargée : {css_filename}")
    except Exception as e:
        print(f"[!] Erreur en téléchargeant {css_url}: {e}")

# Récupération du CSS inline dans les balises <style>
with open("css/inline_styles.css", "w", encoding="utf-8") as f:
    for style_tag in soup.find_all("style"):
        f.write(style_tag.text + "\n")

print("[✓] Récupération terminée.")
