from imports import pd
# from global_variables import TRAIN_FILE     # no longer needed
from global_variables import TRAIN_FILE_BIN
from global_variables import TEST_FILE
import pickle

# train = pd.read_csv(TRAIN_FILE)             # no longer needed
train = pickle.load(open(TRAIN_FILE_BIN, 'rb'))
test  = pd.read_csv(TEST_FILE)