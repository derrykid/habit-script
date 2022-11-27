import pandas as pd
from random import choice
import subprocess
import os


def read_and_parse_word_list():
    df = pd.read_csv('/home/derry/Documents/awl.csv')
    df_vocab = df['vocabulary']
    df_form = df['form']
    return df_vocab, df_form


def create_dictionary(keys, values):
    result = {}  # empty dictionary
    for key, value in zip(keys, values):
        result[key] = value
    return result


def get_how_many_random_vocab(number):
    out = ""
    for i in range(number):
        dict_key = choice(list(vocabulary_dict.keys()))
        dict_value = vocabulary_dict[dict_key]
        out = out + f"{dict_key} : {dict_value} \n"
    return out


vocab, form = read_and_parse_word_list()
vocabulary_dict = create_dictionary(vocab, form)

output = get_how_many_random_vocab(5)

file = open("/home/derry/Documents/.vocab_today", "w")
file.write(output)
file.close()

subprocess.run(["/usr/bin/mousepad", "/home/derry/Documents/.vocab_today"])
