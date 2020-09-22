import tensorflow_datasets as tfds
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def get_data():
	imdb,info=tfds.load("imdb_reviews",with_info=True,as_supervised=True)
	train_set,test_set=imdb["train"],imdb["test"]

get_data()