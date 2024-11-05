# instrument-classification

Creates deep learning models for the classification of 20 instruments, trained using [OpenMic-2018](https://zenodo.org/records/1432913).

## Getting started

requirements:

- Python 3.11+

## Installation

Run `setup.sh` to create the required directories and download the OpenMic-2018 dataset, used to train the model.

```bash
$ sh setup.sh
```

Install ffmpeg.

> Please [download and follow the ffmpeg installation instructions](https://www.ffmpeg.org/download.html) relevant to your operating system.

Install the additional python libraries.

```bash
pip install -r requirements.txt
```

(Optional) Install the requirements to enable tensorflow GPU support on your machine. This could involve installing tensorflow-macos, or tensorflow-metal if using MacOS.

```bash
pip install tensorflow-metal
```

## Dataset

The [openmic-2018 Github repository](https://github.com/cosmir/openmic-2018) is a great resource to get started with this dataset, and includes an [example notebook](https://github.com/cosmir/openmic-2018/blob/master/examples/modeling-baseline.ipynb) to create and evaluate a random forest classifier for 20 different instruments.
Most important here are the pre-defined train-test split as recommended by the authors to ensure a balanced dataset. The OpenMic dataset contains both the original audio files (in .ogg) format, and pre-processed VGGish features.

## Training considerations

- We used the original .oog files as inputs, converted to MFCCs following the parameters defined by [Blaszke & Kostek](https://www.researchgate.net/publication/360046712_Musical_Instrument_Identification_Using_Deep_Learning_Approach).
- The model architecture resembles the one used in the same manuscript, with some adjustments.
- Data preprocessing follows that of the [openmic-2018 Github repository](https://github.com/cosmir/openmic-2018), including data loading and splitting.
- A single model per instrument was created.

Options considered but not implemented in this project:

- Instead of the raw audio files, I could have used the VGGish features from the OpenMic-2018 repository.
- Audio files could have been converted to other data types, including LogMel Spectrograms, before training.
- A single multi-label classifier could be created, rather than a model for each instrument.
- Instead of pre-processing the audio, we could use (Kapre)[https://github.com/keunwoochoi/kapre] to allow the model to do these conversions.

## Usage

To generate new models, run the `model-training.ipynb` notebook in the notebooks directory. Running all cells in this notebook creates 20 classifiers, once for each model in the OpenMic-2018 dataset. Each model is accompanied by it own evaluation report, with a summary shown in the 'metrics' section below. The individual models and reports are located in `models/`

To load the existing models and run a prediction on on of the raw .ogg files, run the following command.

```
python src/predict.py
```

## Metrics

The weighted average precision, recall and f1-scores are retrieved from the reports in the `models` directory.

| instrument        | precision | recall | f1-score | support |
| ----------------- | --------- | ------ | -------- | ------- |
| accordion         | 0.75      | 0.64   | 0.67     | 538     |
| banjo             | 0.66      | 0.67   | 0.66     | 478     |
| bass              | 0.72      | 0.73   | 0.72     | 463     |
| cello             | 0.40      | 0.53   | 0.37     | 485     |
| clarinet          | 0.70      | 0.78   | 0.70     | 640     |
| cymbals           | 0.90      | 0.89   | 0.89     | 436     |
| drums             | 0.89      | 0.88   | 0.87     | 424     |
| flute             | 0.79      | 0.69   | 0.57     | 562     |
| guitar            | 0.82      | 0.78   | 0.79     | 436     |
| mallet percussion | 0.60      | 0.60   | 0.57     | 478     |
| mandolin          | 0.70      | 0.62   | 0.63     | 627     |
| organ             | 0.71      | 0.74   | 0.71     | 431     |
| piano             | 0.84      | 0.78   | 0.79     | 415     |
| saxophone         | 0.68      | 0.59   | 0.54     | 629     |
| synthesizer       | 0.85      | 0.83   | 0.83     | 380     |
| trombone          | 0.54      | 0.66   | 0.56     | 720     |
| trumpet           | 0.45      | 0.59   | 0.44     | 785     |
| ukelele           | 0.67      | 0.67   | 0.67     | 590     |
| violin            | 0.78      | 0.78   | 0.77     | 631     |
| voice             | 0.82      | 0.79   | 0.77     | 374     |
