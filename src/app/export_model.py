import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

SRC_PATH = Path(__file__).parent.parent
DATA_SET_TRAIN = SRC_PATH / "data" / "dataSet_train.csv.gz"
FEATURE = "feature"
TARGET = "target"
OUTPUT_PATH = SRC_PATH / "model" / "model.pkl"
STATE = 42

#Génére le Pipeline d'entrainement à changer en fontion du modéle et de l'encodage des features
def train_model()->Pipeline:


    df_train = pd.read_csv(DATA_SET_TRAIN, sep=";")
    X_train = df_train[FEATURE]
    y_train = df_train[TARGET]

    #Encodage des cibles, ne pas oublier de décoder lors de la prédiction
    lab_enc = LabelEncoder()
    y_train_encod = lab_enc.fit_transform(y_train)
  

    model = Pipeline(steps=[
        ("tfid",TfidfVectorizer(max_features=5000, stop_words='english')),
        ("clf", LogisticRegression(random_state=STATE, max_iter=1000, class_weight='balanced'))
    ])

    model.fit(X_train, y_train_encod)
    return model

def export_model(model, path = OUTPUT_PATH):
    with open(path, "wb") as f:
        pickle.dump(model, f)
    print(f"Modèle exporté vers {OUTPUT_PATH}")

if __name__ == "__main__":
    export_model(train_model())

    