from sklearn.preprocessing import LabelEncoder

import data_generators
import data_loaders
import models
import os
import numpy as np

def main() :
    #data_loaders.exportCorpus()
    #data_generators.export_word2vec_dataset()

    cwd = os.getcwd()
    trainX, trainY = data_loaders.import_embeddings("train")
    valX, valY = data_loaders.import_embeddings("test")
    devX, devY = data_loaders.import_embeddings("dev")

    encoder = LabelEncoder()
    encoder.classes_ = np.load(cwd + "/dataset/labelEncoder.npz")['arr_0']

    model = models.train_mlp1((trainX, trainY), (valX, valY), encoder)
   # models.evaluate_model(model, (devX, devY), encoder)
    return

if __name__ == '__main__' :
    main()