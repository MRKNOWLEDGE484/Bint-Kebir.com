from PIL import Image
import streamlit as slt
import json
from streamlit_lottie import st_lottie

### CONFIGURATION DE LA PAGE
slt.set_page_config(page_title="Bint Kebir.com", page_icon="kebir.jpg", layout="wide")

# Ajouter le filigrane avec le texte "Bint Kebir"
slt.markdown(
    """
    <style>
        .watermark {
            position: fixed;
            bottom: 20px;  /* Position légèrement modifiée */
            right: 20px;   /* Position légèrement modifiée */
            font-size: 40px;  /* Taille augmentée pour la visibilité */
            color: rgba(192,192,192,0.5);  /* Opacité améliorée */
            font-family: 'Arial', sans-serif;  /* Changer la police pour un look moderne */
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);  /* Ombre pour un effet futuriste */
        }
    </style>
    <div class="watermark">
        Bint Kebir
    </div>
    """,
    unsafe_allow_html=True
)

# Contenu principal de l'application
slt.title("Bienvenue sur Bint Kebir")
slt.write("Numéro: +223 70715573.")

### FONCTIONS UTILES
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

### CONTENU DU SITE
with slt.container():
    # Section Titre et Sous-titre stylisés
    slt.markdown("""
        <h3 style='color: gold; font-style: italic;'>Welcome</h3>
    """, unsafe_allow_html=True)

    slt.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Uncial+Antiqua&display=swap');
            h1 {
                font-family: 'Uncial Antiqua', cursive;
                text-align: center;
                color: gold;
                font-size: 60px;
                margin-top: 20px;
                font-weight: bold;
                text-decoration: underline;
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);  /* Ombre ajoutée */
            }
        </style>
        <h1>Produits de Bint Kebir</h1>
    """, unsafe_allow_html=True)

    # Texte centré avec liens stylisés et ajout des icônes
    slt.markdown("""
        <style>
            .centered {
                text-align: center;
                font-family: 'Arial', sans-serif;
                font-size: 20px;
                color: #444444;
            }
            .highlight {
                color: #D4AF37;
                font-weight: bold;
            }
            .links {
                font-size: 18px;
                font-family: 'Arial', sans-serif;
                color: #1DA1F2;
                text-decoration: none;
                display: inline-flex;
                align-items: center;
                margin: 5px 0;  /* Espacement ajouté entre les liens */
            }
            .links img {
                width: 30px;  /* Taille des icônes augmentée */
                height: 30px;
                margin-right: 8px;
            }
            .links:hover {
                text-decoration: underline;
                color: #D4AF37;
            }
        </style>

        <div class="centered">
            <p>Chez <span class="highlight">Bint Kebir</span>, nous vendons des parfums, épices de toutes sortes et <span class="highlight">woussoula</span>.</p>
            <p>Contactez-nous :</p>
            <p><a class="links" href="https://https://www.tiktok.com/tag/bintkebir target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e8/TikTok_logo_black.svg" alt="TikTok Icon"> Sur TikTok</a>
            </p>
            <p><a class="links" href="https://wa.me/22370715573" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp Icon"> Sur WhatsApp</a>
            </p>
            <p><a class="links" href="https://www.instagram.com/bintkebir_/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram Icon"> Sur Instagram</a>
            </p>
        </div>
    """, unsafe_allow_html=True)

### SECTION AVEC EMOJIS ET ANIMATION
with slt.container():
    slt.write("---")
    left_column, right_column = slt.columns(2)

    with left_column:
        slt.markdown("""
            <div style="text-align: center; font-size: 100px;">
                😄 😎
            </div>
            <div style="text-align: center; font-size: 24px; font-family: 'Arial', sans-serif; color: #444444; margin-top: 20px;">
                <p><span style="font-weight: bold; color: gold;">Voici nos woussoula</span></p>
            </div>
        """, unsafe_allow_html=True)

    with right_column:
        lottie_coding = load_lottiefile("animation.json")
        st_lottie(lottie_coding, height=300)

### SECTION AVEC IMAGE ET TEXTE
with slt.container():
    slt.write("---")
    slt.header("Mon projet")
    slt.write("##")
    image_column, text_column = slt.columns((1, 2))

    with image_column:
        bigimage = Image.open("imkebir1.jpg")
        slt.image(bigimage, use_column_width=True)  # Utilise la largeur de la colonne

    with text_column:
        slt.header("Voici nos différentes Boîtes de Woussoula")
        slt.markdown("[Lien de notre compte Instagram >](https://www.instagram.com/bintkebir_/#:~:text=809%20Followers,%20431%20Following,%20105%20Posts)")

### SECTION DES IMAGES AVEC CADRE ET PRIX
image1, image2 = slt.columns(2)

slt.markdown(
    """
    <style>
        .image-box {
            border: 3px solid #00bcd4; /* Couleur futuriste */
            padding: 10px;
            border-radius: 20px; /* Coins arrondis pour un look futuriste */
            box-shadow: 0 0 20px rgba(0, 188, 212, 0.5); /* Ombre pour un effet futuriste */
            text-align: center;
            margin-bottom: 20px;
            transition: transform 0.3s; /* Effet de transformation au survol */
            background-color: rgba(255, 255, 255, 0.1); /* Fond transparent */
        }
        .image-box:hover {
            transform: scale(1.05); /* Zoom au survol */
        }
        .price {
            font-size: 16px;
            font-weight: bold;
            color: #ff5733;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Image 1 avec cadre et prix stylisé (format rectangulaire)
with image1:
    big_image = Image.open("imkebir2.jpg")
    slt.image(big_image, use_column_width=True)  # Utilise la largeur de la colonne
    slt.markdown("""
        <div class="image-box">
            <p class="price">Boîte à 10,000 F CFA</p>
        </div>
    """, unsafe_allow_html=True)

# Image 2 avec cadre et prix stylisé (format rectangulaire)
with image2:
    big_image2 = Image.open("imkebir3.jpg")
    slt.image(big_image2, use_column_width=True)  # Utilise la largeur de la colonne
    slt.markdown("""
        <div class="image-box">
            <p class="price">Boîte à 5,000 F CFA</p>
        </div>
    """, unsafe_allow_html=True)

### SECTION DES PARFUMS AVEC STYLE MÉDIÉVAL
with slt.container():
    slt.write("---")
    slt.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Uncial+Antiqua&display=swap');
            .medieval-title {
                font-family: 'Uncial Antiqua', cursive;
                font-size: 48px;
                color: gold;
                text-align: center;
                margin-top: 20px;
                margin-bottom: 20px;
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
            }
        </style>
        <h1 class="medieval-title">Parfums</h1>
    """, unsafe_allow_html=True)
    
    slt.write("### Profitez de notre large choix de parfums! 🥰")

### SECTION DE CONTACT
with slt.container():
    slt.write("---")
    slt.header("Contactez-nous")
    slt.write("Si vous avez des questions ou des demandes, n'hésitez pas à nous contacter!")
