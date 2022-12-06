#!/usr/bin/env python
# -*- coding:utf-8 -*-
# AUTHOR: Ti Bai
# EMAIL: tibaiw@gmail.com
# AFFILIATION: MAIA Lab | UT Southwestern Medical Center
# DATETIME: 12/5/2022

import json
import os

if __name__ == '__main__':
    data_root = r'D:\data\2_uncurated_data\RawData\registration\Learn2Reg\OASIS'
    with open(os.path.join(data_root, r'OASIS_dataset.json'), 'r') as f:
        dataset_json = json.load(f)

    training_dataset = dataset_json['training']

    test_length = int(0.2 * len(training_dataset))
    test_dataset = training_dataset[-test_length:]
    training_dataset = training_dataset[:-test_length]

    train_image_list = [x['image'] for x in training_dataset]
    train_label_list = [x['label'] for x in training_dataset]
    train_mask_list = [x['mask'] for x in training_dataset]

    test_image_list = [x['image'] for x in test_dataset]
    test_label_list = [x['label'] for x in test_dataset]
    test_mask_list = [x['mask'] for x in test_dataset]

    with open('train_image_list.txt', 'w') as f:
        f.writelines([x + '\n' for x in train_image_list])

    with open('train_label_list.txt', 'w') as f:
        f.writelines([x + '\n' for x in train_label_list])

    with open('train_mask_list.txt', 'w') as f:
        f.writelines([x + '\n' for x in train_mask_list])

    with open('test_image_list.txt', 'w') as f:
        f.writelines([x + '\n' for x in test_image_list])

    with open('test_label_list.txt', 'w') as f:
        f.writelines([x + '\n' for x in test_label_list])

    with open('test_mask_list.txt', 'w') as f:
        f.writelines([x + '\n' for x in test_mask_list])

    print('Congrats! May the force be with you ...')