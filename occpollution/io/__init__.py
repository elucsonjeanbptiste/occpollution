import os

# daily data for widgets
url_db = "https://opendata.arcgis.com/datasets/2ab16a5fb61f42c1a689fd9cc466383f_0.csv"
# annual data for map
url_db_an = "https://opendata.arcgis.com/datasets/e0f26f918c504608b10d128f65ce0efc_0.csv"
# monthly data
url_db_m = "https://opendata.arcgis.com/datasets/3acfa2aa5c0346a18ba7749c6885e503_0.csv"

path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Mesure_journaliere.csv")
path_target_an = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Mesure_annuelle.csv")
path_target_m = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Mesure_mensuelle.csv")
