
import argparse


def get_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='the Archithecher for CNN model')
    parser.add_argument('--dog_files', type=str,
                        default='dognames.txt', help='dog names file')

    return parser.parse_args()
