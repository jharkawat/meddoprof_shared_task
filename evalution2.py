# To produce final out in formate desired by WNUT shared Task 2020
# It will read file from data/proto/interactive/sentences for training to keep the information of files 
# In training we will providing data from single file containing all the sentences to allow shuffling across domain.
# use for generating out to test on the evaluation script provided by [organiser](https://github.com/jeniyat/WNUT_2020_NER/tree/master/code/eval)

"""Evaluate the model"""
import os
import torch
import utils
import random
import logging
import argparse
import numpy as np
import glob
from data_loader import DataLoader
from SequenceTagger import BertForSequenceTagging
from metrics import f1_score, get_entities, classification_report, accuracy_score
from os import listdir

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', default='meddo', help="Directory containing the dataset")
parser.add_argument('--seed', type=int, default=23, help="random seed for initialization")


def evaluate1(model, data_iterator, params,inputfile ,mark='Eval', verbose=False):
    """Evaluate the model on `steps` batches."""
    # set model to evaluation mode
    model.eval()

    idx2tag = params.idx2tag

    pred_tags = []

    # a running average object for loss
    loss_avg = utils.RunningAverage()

    for _ in range(params.eval_steps):
        # fetch the next evaluation batch
        batch_data, batch_token_starts = next(data_iterator)
        batch_masks = batch_data.gt(0)
        
       
        #loss_avg.update(loss.item())
        
        batch_output = model((batch_data, batch_token_starts), token_type_ids=None, attention_mask=batch_masks)[0]  # shape: (batch_size, max_len, num_labels)
        
        batch_output = batch_output.detach().cpu().numpy()
        

        pred_tags.extend([[idx2tag.get(idx) for idx in indices] for indices in np.argmax(batch_output, axis=2)])
   

    filepath_out=os.path.join('output_data',inputfile.split('/')[-1])
    f =open(filepath_out,"w")
    for i in pred_tags:
        s='    '
        j=s.join(i)  
        f.writelines('%s\n' %j)
    f.close()
    print("done one file")
        




def interAct(model, data_iterator, params, mark='Interactive', verbose=False):
    """Evaluate the model on `steps` batches."""
    # set model to evaluation mode
    model.eval()

    idx2tag = params.idx2tag

    true_tags = []
    pred_tags = []

    # a running average object for loss
    loss_avg = utils.RunningAverage()


    batch_data, batch_token_starts = next(data_iterator)
    batch_masks = batch_data.gt(0)
        
    batch_output = model((batch_data, batch_token_starts), token_type_ids=None, attention_mask=batch_masks)[0]  # shape: (batch_size, max_len, num_labels)
        
    batch_output = batch_output.detach().cpu().numpy()

    pred_tags.extend([[idx2tag.get(idx) for idx in indices] for indices in np.argmax(batch_output, axis=2)])
    
    return(get_entities(pred_tags))

if __name__ == '__main__':
    args = parser.parse_args()
    
    tagger_model_dir = 'experiments/' + args.dataset
    # Load the parameters from json file
    json_path = os.path.join(tagger_model_dir, 'params.json')
    assert os.path.isfile(json_path), "No json configuration file found at {}".format(json_path)
    params = utils.Params(json_path)

    # Use GPUs if available
    params.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Set the random seed for reproducible experiments
    random.seed(args.seed)
    torch.manual_seed(args.seed)
    params.seed = args.seed

    # Set the logger
    utils.set_logger(os.path.join(tagger_model_dir, 'evaluate.log'))

    # Create the input data pipeline
    logging.info("Loading the dataset...")

    # Initialize the DataLoader
    data_dir = 'data/' + args.dataset

    if args.dataset in ["proto"]:
        bert_class = 'dmis-lab/biobert-v1.1' # auto
        # bert_class = 'pretrained_bert_models/bert-base-cased/' # manual
    elif args.dataset in ["msra"]:
        bert_class = 'dmis-lab/biobert-v1.1' # auto
        # bert_class = 'pretrained_bert_models/bert-base-chinese/' # manual
    elif args.dataset in ["meddo"]:
        bert_class = 'mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'

    data_loader = DataLoader(data_dir, bert_class, params, token_pad_idx=0, tag_pad_idx=-1)

    # Load the model
    model = BertForSequenceTagging.from_pretrained(tagger_model_dir)
    model.to(params.device)
    
    #txtfiles of test data
    txtfiles = []
    for file in glob.glob("data/meddo/interactive/sentences/*.txt"):
        txtfiles.append(file)
    for i in txtfiles:
    
    # Load data
        test_data = data_loader.load_data_active('interactive', i)

    # Specify the test set size
        params.test_size = test_data['size']
        params.eval_steps = params.test_size // params.batch_size
        test_data_iterator = data_loader.data_iterator(test_data, shuffle=False)

        logging.info("- done.")

        logging.info("Starting evaluation...")
        test_metrics = evaluate1(model, test_data_iterator, params, i,mark='Test', verbose=True)

