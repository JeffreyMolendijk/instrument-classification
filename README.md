# instrument-classification

A deep learning model that for instrument classification, trained using [OpenMic-2018](https://zenodo.org/records/1432913).

## Getting started

requirements:

- Python 3.11+

## Installation

Run `setup.sh` to create the required directories and download the OpenMic-2018 dataset.

```bash
$ sh setup.sh
```

Install ffmpeg and libsndfile.

> TODO

Install the additional requirements

```bash
pip install -r requirements.txt
```

## Dataset

[add dataset information]

(Optional) Download the training dataset to retrain the model locally. Please skip this step if you're only interested in making predictions with the model. Please download the [OpenMIC-2018 dataset .tar.gz file](https://zenodo.org/records/1432913) and place it in the `data/external/` directory. Extract the contents into the `data/raw/` directory using the following command.

```bash
$ tar xvzf openmic-2018-v1.0.0.tgz -C some/dir
```

## Usage

[training new model]

> python train.py

[making predictions]

> python predict.py

[running tests]

> pytest tests

## Metrics

[Add report here]

### Notes

- Training dataset is multi-instrument audio. https://brianmcfee.net/papers/ismir2018_openmic.pdf
- AudioSet object type used.
- There are x instruments in the dataset. For each audiotrack, we need to return a score or whether that instrument is present or absent. The results should be shown per instrument.
- https://github.com/cosmir/openmic-2018
- One vs many models?
- Good Kapre tutorial --> https://github.com/keunwoochoi/kapre/blob/master/examples/how-to-use-Kapre.ipynb
- AutoKeras. Can we combine this with Kapre?
- https://www.researchgate.net/publication/360046712_Musical_Instrument_Identification_Using_Deep_Learning_Approach
- VGGish vs extraction from audio

### Findings

Dataset unbalanced. Some need for balancing.
Start with 64 layer, then use 128. CNN benefit from pyramid shape.
