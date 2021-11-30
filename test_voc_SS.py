import argparse
import json
from voc import parse_voc_annotation

argparser = argparse.ArgumentParser(description='train and evaluate YOLO_v3 model on any dataset')
argparser.add_argument('-c', '--conf', help='path to configuration file')   

args = argparser.parse_args()

config_path = args.conf

with open(config_path) as config_buffer:    
    config = json.loads(config_buffer.read())

###############################
#   Parse the annotations 
###############################
train_annot_folder, train_image_folder, train_cache, labels = config['train']['train_annot_folder'],config['train']['train_image_folder'],config['train']['cache_name'],config['model']['labels']

train_ints, train_labels = parse_voc_annotation(train_annot_folder, train_image_folder, train_cache, labels)
# print(train_labels)
# for train_int,train_label in list(zip(train_ints,train_labels)):
#     print(train_int,train_label)
for train_int in train_ints:
    print(train_int)   