import os
import numpy as np
import librosa
from tensorflow.keras.models import load_model
from typing import Dict, Any

def preprocess_audio(file_path: str, sr: int = 22050, n_fft: int = 1024, hop_length: int = 512, n_mfcc: int = 40) -> np.ndarray:
    """
    Preprocesses an audio file and returns its MFCC representation.
    
    :param file_path: Path to the audio file.
    :param sr: Sampling rate for the audio file.
    :param n_fft: Number of samples in each FFT.
    :param hop_length: Number of samples between successive frames.
    :param n_mfcc: Number of MFCC features to extract.
    :return: A 2D NumPy array representing the MFCC of the input audio.
    """
    # Load audio file as waveform
    audio, sr = librosa.load(file_path, sr=sr, mono=True)
    
    # Compute MFCCs from the audio
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)
    
    # Transpose to ensure shape is (time_steps, n_mfcc)
    return mfcc.T

def load_models(model_dir: str = '../models') -> Dict[str, Any]:
    """
    Loads all instrument models from a specified directory.
    
    :param model_dir: Directory where individual instrument models are stored.
    :return: Dictionary of loaded models keyed by instrument name.
    """
    models = {}
    for filename in os.listdir(model_dir):
        if filename.endswith('_model.h5'):
            instrument = filename.split('_model.h5')[0]
            model_path = os.path.join(model_dir, filename)
            models[instrument] = load_model(model_path)
            print(f'Loaded model for {instrument} from {model_path}')
    return models

def predict_instruments(file_path: str, models: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Loads an audio file, preprocesses it, and runs predictions on all loaded models.
    
    :param file_path: Path to the audio file to make predictions on.
    :param models: Dictionary of loaded models keyed by instrument.
    :return: Predictions for each instrument model with scores.
    """
    # Preprocess the audio file
    mfcc_features = preprocess_audio(file_path)
    
    # Reshape MFCC features to match model input
    mfcc_features = np.expand_dims(mfcc_features, axis=-1)  # To add a channel dimension
    mfcc_features = np.expand_dims(mfcc_features, axis=0)   # To match expected batch size input

    # Run each model and collect predictions
    predictions = {}
    for instrument, model in models.items():
        prediction_array = model.predict(mfcc_features)
        score = prediction_array[0][0]
        is_present = score > 0.5
        predictions[instrument] = {'is_present': is_present, 'score': score}

    return predictions

if __name__ == '__main__':
    # Load models
    models = load_models("models")

    # Path to the audio file to predict
    audio_file_path = 'data/raw/openmic-2018/audio/000/000046_3840.ogg'
    
    # Predict instruments and print results
    predictions = predict_instruments(audio_file_path, models)
    print(f"The following predictions were generated for datafile {audio_file_path}:\n{predictions}")