The director contains preprocessing scripts and dataset

## Dir structure
- Desired input for Bert datalaoder 
- Based on Huggingface ```Autotransformers```

 ```
 	{test, train, val}/
	  ├── sentences.txt (each line contains input sentences ) 
	  ├── tags.txt (each line contains tags corresponding to sentences in the sentences.txt)
	 
	 test_bio (conll format test data)
	 
	 train_bio (conll format test data)
		 
	 Val_bio (conll format test data)
		 
	 README.md (this file)
		 
	 meddoprof_shared_task (dataset provide by sharedtask organisers)
	  ├── conllandstandoff_convertor (scripts to convert conll to standoff and standoff to conll ) 
	  ├── data (data and proprocessing scripts)
	  ├── meddoprof_test_txt (test file)

	 interactive
	  ├── sentences (contains inference sentences)
	  ├── meddoprof_test_txt (test file) 
 ```
