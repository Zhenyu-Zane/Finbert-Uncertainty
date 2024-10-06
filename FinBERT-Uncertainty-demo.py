# -*- coding: utf-8 -*-
# Note: the following code is for demonstration purpose. Please use GPU for fast inference on large scale dataset.

from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import transformers
transformers.__version__

if __name__ == "__main__":
    finbert = BertForSequenceClassification.from_pretrained('./finbert-uncertainty',num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('./finbert-uncertainty')
    nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)
    results = nlp(['growth is strong and we have plenty of liquidity.', 
                   'there is a shortage of capital, and we need extra financing.',
                  'formulation patents might protect Vasotec to a limited extent.'])
    results
