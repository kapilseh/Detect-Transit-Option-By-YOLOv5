import os

# ID for Bus, Train, Airplane, Boat
object_ids = ['/m/01bjv', '/m/07jdr', '/m/0cmf2', '/m/019jd']

train_bboxes_filename = os.path.join('data/oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('data/validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('data/test-annotations-bbox.csv')

image_list_file_path = os.path.join('.', 'image_list_file')

if os.path.exists(image_list_file_path):
    os.remove(image_list_file_path)

image_list_file_list = []
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in object_ids and id not in image_list_file_list:
                image_list_file_list.append(id)
                with open(image_list_file_path, 'a') as fw:
                    fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], id))
            line = f.readline()

        f.close()