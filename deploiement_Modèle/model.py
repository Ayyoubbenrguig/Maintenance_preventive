from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle

def normalise(normalisation_params, X):

    with open(normalisation_params, 'rb') as f:
        parametres = pickle.load(f)
    mu = parametres['mu']
    sigma = parametres['sigma']
    
    scaler = StandardScaler()
    scaler.mean_ = mu
    scaler.scale_ = sigma
    
    X_scaled = scaler.transform(X)
    return X_scaled

def load_model(model_weights):

    model = Sequential()
    model.add(Dense(units=64, activation="relu", input_shape=(7,)))
    model.add(Dense(units=128, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(units=64, activation="relu"))
    model.add(Dense(units=64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(units=1, activation="sigmoid"))
    
    model.load_weights(model_weights)
    
    return model

model = load_model('model/model.weights.h5')

def predict(features):

    normalise('model_data/normalisation_params.pkl', features)

    features = np.array(features)
    
    prediction_proba = model.predict(features)
    prediction = int(prediction_proba > 0.5) 
    return "Functional" if prediction == 1 else "Failure"

if __name__ == "__main__":

    # Example
    X = [[0,250.9,400, 2861,800,143,30000.7]]  
    resultat_prediction = predict(X)
    print("Résultat de la prédiction :", resultat_prediction)
