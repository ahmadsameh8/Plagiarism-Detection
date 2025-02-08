# Plagiarism Detection Across Languages: A Comprehensive Study of Arabic and English-to-Arabic Long Documents

## Overview

Plagiarism detection in Arabic texts remains a significant challenge due to the complex morphological structure, rich linguistic diversity, and scarcity of high-quality labeled datasets. This study proposes a robust framework for Arabic plagiarism detection by integrating Siamese Neural Networks (SNN) with state-of the-art transformer architectures, specifically AraT5 and Longformer. The system employs a hybrid workflow, combining transformer-based encoders and a classification objective to implicitly learn textual similarity.

## Requirements

These experiments were conducted on a system equipped with an AMD Ryzen 9 5900X processor, 128GB of RAM, and an NVIDIA RTX 3090 GPU. The experiments were implemented using Python version 3.11.0. 
To maintain a consistent environment for all experiments, the same hardware and software configurations were used throughout the study.

```bash
pip install -r requirements.txt
```

## Dataset
Link: https://araplagdet.misc-lab.org/

Format: The Dataset format is in three folders plagiarism annotation, source-documents, and suspicious documents and the annotations are stored in XML files. 

Extraction Process:

Convert it into CSV by running the following python code: 
```bash
python script.py --suspicious_folder "path/to/suspicious" --source_folder "path/to/source" --xml_base_folder "path/to/xml"
```
from this python file [DataToCsv.py](DataToCsv.py) which saves the data to a CSV file called ```plagiarism_detection_output_with_features.csv```, the previous python file extracts all features included. we only ended up using only ```source_content```, ```suspicious_content```, and ```Plagiarism type``` after pre-processing, and some manual feature engineering

Arguments:

```--suspicious_folder```: Path to the folder containing suspicious documents.

```--source_folder```: Path to the folder containing source documents.

```--xml_base_folder```: Path to the folder containing XML annotation files.

## Translation
In our benchmark tests, Argos Translate outperformed other translation models in syntax and semantics when benchmarked the following metrics: BLEU, chrF, BERTScore F1, and METEOR.

Argos Translate can be setup by following this Github repository: https://github.com/argosopentech/argos-translate

To run the Translation script in the [translation.py](translation.py)
```bash
python translate_script.py <input_csv> <column_name> --src_lang <source_language> --dest_lang <target_language> --output <output_csv>
```
Explanation of Arguments:
input.csv → Your CSV file with text to translate.
column_name → The column in input.csv to be translated.
--src_lang → (Optional) Source language (default: en).
--dest_lang → (Optional) Destination language (default: ar).
--output → (Optional) Output file name (default: translated_output.csv).


