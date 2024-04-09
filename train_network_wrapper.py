import sys
import traceback
from train_network import setup_parser, train
from library.train_util import read_config_from_file

try:
    parser = setup_parser()
    args = parser.parse_args()
    args = read_config_from_file(args, parser)
    train(args)
except:
    print(traceback.format_exc())
    sys.exit(1)
