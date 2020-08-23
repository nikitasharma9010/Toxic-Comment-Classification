# These files contain the text that may or may not be toxic
# TRAIN_FILE = 'train.csv'               # no longer needed
TEST_FILE      = 'test.csv'
TRAIN_FILE_BIN = 'train.bin'

GLOVE    = './glove.6B/'
GLOVE50  = GLOVE + 'glove.6B.50d.txt'
GLOVE100 = GLOVE + 'glove.6B.100d.txt'
GLOVE200 = GLOVE + 'glove.6B.200d.txt'
GLOVE300 = GLOVE + 'glove.6B.300d.txt'

EMBEDDING_DIMS = 100
EMBEDDINGS_W2V = dict()

MAX_FEATURES = 20000
MAX_TEXT_LENGTH = 400

FILTERS_COUNT = 250
FILTER_SIZE   = 3
HIDDEN_DIMS   = 250

