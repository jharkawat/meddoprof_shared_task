## Directory  Structure
- The director contains preprocessing scripts and dataset
- Desired input for Bert datalaoder 
```
data/meddo
    ├── {test, train, val}
    │    ├── sentences.txt
    │    └── tags.txt
    ├── test_bio (conll format test data)
    ├── train_bio (conll format train data)
    ├── val_bio (conll format valid data)
    ├── README.md (this file) 
    ├── meddoprof_shared_task (dataset provide by sharedtask organisers) 
    |	 ├── conllandstandoff_convertor (scripts to convert conll to standoff and standoff to conll )    
    |	 ├── data (data and proprocessing scripts)
    |	 └── meddoprof_test_txt (test file)
    |-interactive
    |	 ├── sentences (contains inference sentences)
    |	 └── meddoprof_test_txt (test file) 
    |
```
