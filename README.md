Plagiarism Detection Across Languages: A Comprehensive Study of Arabic and English-to-Arabic Long Documents

Overview

Plagiarism detection in Arabic texts remains a significant challenge due to the complex morphological structure, rich linguistic diversity, and scarcity of high-quality labeled datasets. This study proposes a robust framework for Arabic plagiarism detection by integrating Siamese Neural Networks (SNN) with state-of the-art transformer architectures, specifically AraT5 and Longformer. The system employs a hybrid workflow, combining transformer-based encoders and a classification objective to implicitly learn textual similarity.
Dataset

# Dataset
Link: https://araplagdet.misc-lab.org/

Format: The Dataset format is in three folders plagiarism annotation, source-documents, and suspicious documents and the annotations are stored in XML files. 

Extraction Process:

Convert it into CSV by running the following python code: 
```bash
python script.py --suspicious_folder "path/to/suspicious" --source_folder "path/to/source" --xml_base_folder "path/to/xml"
```
from this python file [DataToCsv.py](DataToCsv.py)
Arguments:
```--suspicious_folder```: Path to the folder containing suspicious documents.
```--source_folder```: Path to the folder containing source documents.
```--xml_base_folder```: Path to the folder containing XML annotation files.



Requirements

these experiments were conducted on a system equipped with an AMD Ryzen 9 5900X processor, 128GB of RAM, and an NVIDIA RTX 3090 GPU. The experiments were implemented using Python version 3.11.0. 
To maintain a consistent environment for all experiments, the same hardware and software configurations were used throughout the study.

```bash
pip install -r requirements.txt
```




