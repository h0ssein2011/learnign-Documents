
# 1- read files from a folder
# 2 - process the file name to store the label
# 3 - Format the pet image labels such that they can be matched to:
# The classifier function labels
# The dog names in dognames.txt

from os import listdir


# def get_pet_labels(image_dir):
#     img_list = listdir(image_dir)
#     results_dict = dict()

#     for i in range(len(img_list)):
#         filename = img_list[i].lower().strip('.jpg').split('_')

#         pet_name = ''
#         for word in filename:
#             if word.isalpha():
#                 pet_name += word+' '
#         pet_name = pet_name.strip()
#         # print(pet_name)
#         if img_list[i] not in results_dict:
#             results_dict[img_list[i]] = [pet_name]
#     return results_dict


def get_pet_labels(image_dir):

    filename_list = listdir(image_dir)
    results_dic = dict()

    for i in range(len(filename_list)):
        if filename_list[i][0] != '.':
            pet_label1 = filename_list[i].strip('.jpg').lower().split('_')
            pet_name = ''

            for word in pet_label1:
                if word.isalpha():
                    pet_name += word + ' '
            pet_name = pet_name.strip()
            # pet_names.append(pet_name)

            if filename_list[i] not in results_dic:
                results_dic[filename_list[i]] = pet_name

    return results_dic
