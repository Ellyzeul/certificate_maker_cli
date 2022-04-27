import sys
from src.args import validate_args, display_help
from src.process import process


argv = sys.argv

if not validate_args(argv):
    exit()

csv_path = argv[1]
html_path = argv[2]
img_path = argv[3]
naming_pattern = argv[4]

process(csv_path, html_path, img_path, naming_pattern)
