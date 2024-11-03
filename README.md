# instrument-classification

Creates a deep learning model for instrument classification, trained using [OpenMic-2018](https://zenodo.org/records/1432913).

## Getting started

requirements:

- Python 3.11+

## Installation

Run `setup.sh` to create the required directories and download the OpenMic-2018 dataset, used to train the model.

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

The [openmic-2018 Github repository](https://github.com/cosmir/openmic-2018) is a great resource to get started with this dataset, and includes an [example notebook](https://github.com/cosmir/openmic-2018/blob/master/examples/modeling-baseline.ipynb) to create and evaluate a random forest classifier for 20 different instruments.
Most important here are the pre-defined train-test split as recommended by the authors to ensure a balanced dataset. The OpenMic dataset contains both the original audio files (in .ogg) format, and pre-processed VGGish features.

## Training considerations

- Using either the original .ogg files as a starting point, or the pre-processed audio features.
- If using the original audio files, we could convert them into MFCCs, or other types of model inputs.
- Creating one model per instrument, or a single multi-label classification model.
- Instead of pre-processing the audio, we could use (Kapre)[https://github.com/keunwoochoi/kapre] to allow the model to do these conversions.
- Could use (existing publications)[https://www.researchgate.net/publication/360046712_Musical_Instrument_Identification_Using_Deep_Learning_Approach] as a starting point to design our model architecture.

## Usage

> TODO

## Metrics

> TODO

## Findings

- Number of instruments among dataset is unbalanced.
