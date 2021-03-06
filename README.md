## Spanish Pre-Trained Language Models for HealthCare Industry

The code for the paper "Spanish Pre-Trained Language Models for HealthCare Industry"  
Accepted to appear at Proceedings of the Iberian Languages Evaluation Forum (IberLEF 2021), CEUR Workshop Proceedings, 2021.  

**Authors**
[Jalaj Harkawat*](https://www.linkedin.com/in/jalaj-harkawat/) | [Tejas Vaidhya*](https://scholar.google.com/citations?user=dGedZKoAAAAJ&hl=en)  
 `* equal contribution`

[**Paper link**](http://ceur-ws.org/Vol-2943/meddoprof_paper7.pdf)

## Dependencies

| Dependency | Version | Installation Command |
| ---------- | ------- | -------------------- |
| Python     | 3.8     | `conda create --name covid_entities python=3.8` and `conda activate covid_entities` |
| PyTorch, cudatoolkit    | 1.5.0, 10.1   | `conda install pytorch==1.5.0 cudatoolkit=10.1 -c pytorch` |
| Transformers:hugs: (Huggingface) | 2.9.0 | `pip install transformers==2.9.0` |
| Scikit-learn | 0.23.1 | `pip install scikit-learn==0.23.1` |
| scipy        | 1.5.0  | `pip install scipy==1.5.0` |
| NLTK    | 3.5  | `pip install nltk==3.5` |

<!--
- python 3.8
```conda create --name covid_entities python=3.8``` & ```conda activate covid_entities```
- PyTorch 1.5.0, cudatoolkit=10.1
```conda install pytorch==1.5.0 cudatoolkit=10.1 -c pytorch```
- Huggingface transformers - 2.9.0
```pip install transformers==2.9.0```
- scikit-learn 0.23.1
```pip install scikit-learn==0.23.1```
- scipy 1.5.0
```pip install scipy==1.5.0```
- ekphrasis 0.5.1
```pip install nltk==3.5```
-->

## Environment Setup
```
conda env create -f env.yml
```

## Directory  Structure

- **data/** (contains data and preprocessing scripts; for more details ./data/README.md)
- **build_dataset_tags.py** (use to generate {test/train/Val}.bio files from conll files) 
- **data_loader.py** (customized dataloader for token level classification)
- **train.py** (contain code for training loop and validation)
- **metrics.py** (contains metrics implemenatation)
- **utils.py** (utility function like logging and running avgerage implementation)
- **SeqenceTagger.py** (model (forward and backward passes) implementation of pytorch)
- **evaluate.py** (evaluation loop for Valid and Test set)
- **inference.py** (scipt to run during inference time; provide output in txt )
## Dataset
MEDDOPROF: MEDical DOcuments PROFessions recognition shared task: [website link](https://temu.bsc.es/meddoprof/) | [Training data](https://zenodo.org/record/4775741/files/meddoprof-training-set.zip?download=1) | [Test dataset](https://zenodo.org/record/5077976/files/meddoprof-test-GS.zip?download=1)

## Preprocessing Instruction
1. Create the {test/train/Val}_bio files in the ```./data``` containing dataset in conll format  (more detail refer ```./data/README.md```)
2. Run ```python build_dataset_tags.py ```  
  This will generate ```./train```, ```./test``` and ```./Val folder``` inside ```data/{dataset_name}/{train, test, Val}```
3. Scripts for conll-standoff conversion ```data\meddo\meddoprof_shared_task\conllandstandoff_convertor```

## Training Instruction
1. Download pretrained model 
  - Finetuned-BETO: [link](https://github.com/jharkawat/meddoprof_shared_task/releases/download/v0.1/meddo.zip)
  - Multi-lang-bert-cased: [link](https://github.com/jharkawat/meddoprof_shared_task/releases/download/V.01/multi_meddo.zip)
  
 ```mkdir experiments``` and unzip file inside experiments.

2. For Training the model:
Input files from data/{dataset_name}/{train, test, Val}
    ``` python train.py```

3. To get the output for submission:
This script takes the sentences from (./data/{dataset_name}/interactive/sentences/.) and write ouput in ./output-data_bert (Berts output)

    ```python inference.py --dataset meddo```

## Post-Processing Instruction 
The post processing is done as per the submission requirement of [sharetask]()
- Use ```submit_format_generator.ipynb``` for generting conll formate  
    This will generate ```temp``` containing files in conll formate

**Task Specific Processing**
- Conversion to standoff format
    Run ```./data/meddo/meddoprof_shared_task/conllandstandoff_convertor/convert_conll_to_standoff/conll2standoff.py```
    The above scipt store generated standoff format data at ```./ouput-Standoff_Format```
- Use ```Post_processor.ipynb```
    output store in ```output-desire_submission_format```  

## Bibtex
```
@inproceedings{salvador2021nlp,
    title={NLP applied to occupational health: MEDDOPROF shared task at IberLEF 2021 on automatic recognition, classification and normalization of professions and occupations from medical texts},
    author={Lima-L??pez, Salvador and Farr??-Maduell,Eul??lia and Miranda-Escalada, Antonio and Briv??-Iglesias, Vicent and Krallinger, Martin},
    booktitle={Proceedings of the Iberian Languages Evaluation Forum (IberLEF 2021), CEUR Workshop Proceedings, 2021},
    year={2021}
}
```

## Miscellanous
- You may contact us by opening an issue on this repo. Please allow 2-3 days of time to address the issue.
- License: **MIT**
- Code Credits: [NER_Lab_Protocols](https://github.com/tejasvaidhyadev/NER_Lab_Protocols)
- **Citation**: coming soon
