from classifier import classifier
from os import listdir
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from time import time
start_time = time()
in_arg = get_input_args()
answers_dic = get_pet_labels(in_arg.dir)


def classify_images(img_path=in_arg.dir, model=in_arg.arch):
    clf_labels = dict()
    filenames = listdir(img_path)
    # print(filenames)
    i = 0
    for file in filenames:
        path = img_path+str(file)

        clf_label = classifier(path, model)
        clf_label = clf_label.lower().strip()

        pet_label = list(answers_dic.values())[i]
        compared = int(pet_label in clf_label)

        clf_labels[file] = [pet_label, pet_label, compared]
        i += 1
    return clf_labels


result_dic = classify_images()


def adjust_results4_isadog():
    dognames_dic = dict()

    with open('dognames.txt', 'r') as f:

        for line in f:
            dognames_dic[line.rstrip()] = 1

    for key in result_dic:
        if result_dic[key][0] in dognames_dic:
            if result_dic[key][1] in dognames_dic:
                result_dic[key].extend((1, 1))
            else:
                result_dic[key].extend((1, 0))

        else:
            if result_dic[key][1] in dognames_dic:
                result_dic[key].extend((0, 1))
            else:
                result_dic[key].extend((0, 0))


adjust_results4_isadog()
# print(result_dic)


def calculates_results_stats():
    result_stats = dict()
    result_stats['correct_dogs'] = []
    result_stats['pct_correct_dogs'] = []
    result_stats['n_correct_breed'] = []
    result_stats['pct_correct_breed'] = []

    count_dogs = 0
    correct_dogs = 0
    correct_breeds = 0

    for key, val in result_dic.items():

        count_dogs += val[3]
        correct_dogs += val[3] * val[4]
        correct_breeds += val[3] * val[2]

    result_stats['correct_dogs'] = count_dogs
    result_stats['pct_correct_dogs'] = round(
        correct_dogs * 100 / count_dogs, 1)
    result_stats['n_correct_breed'] = correct_breeds
    result_stats['pct_correct_breed'] = round(
        correct_breeds * 100 / count_dogs, 1)

    return result_stats


results_stats_dic = calculates_results_stats()
print(
    f'for model: {in_arg.arch} the result stat is:{results_stats_dic} in {time()- start_time} seconds')
