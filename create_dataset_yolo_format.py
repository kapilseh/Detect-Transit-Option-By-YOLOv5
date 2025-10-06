import os
import shutil


DATA_ALL_DIR = os.path.join('.', 'data', 'raw_images')

DATA_OUT_DIR = os.path.join('.', 'data', 'processed_data')

for set_ in ['train', 'val', 'test']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_)]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.makedirs(dir_)

# ID for Bus, Train, Airplane, Boat
object_ids = ['/m/01bjv', '/m/07jdr', '/m/0cmf2', '/m/019jd']

train_bboxes_filename = os.path.join('.', 'data' , 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'data' , 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('.', 'data' , 'test-annotations-bbox.csv')


for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'val', 'test'][j]
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2 = line.split(',')[:8]
            if class_name in object_ids:
                print(id)
                if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'imgs', '{}.jpg'.format(id))):
                    shutil.copy(os.path.join(DATA_ALL_DIR, '{}.jpg'.format(id)),
                                os.path.join(DATA_OUT_DIR,  set_, '{}.jpg'.format(id)))
                with open(os.path.join(DATA_OUT_DIR, set_, '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1
                    annotation_idx = object_ids.index(class_name)
                    f_ann.write('{} {} {} {} {}\n'.format(annotation_idx, xc, yc, w, h))
                    f_ann.close()

            line = f.readline()
