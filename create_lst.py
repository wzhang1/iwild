import json
import random
json_f = open("train_annotations.json")
train_val = json.load(json_f)


ann_data = train_val["annotations"]

prefix = "train_val/"

postfix = ".jpg"

imgs = [aa['image_id'] for aa in ann_data]
labels = [aa['category_id'] for aa in ann_data]

count_t = 0
count_v = 0
train_f = open("train.lst", "w")
val_f = open("val.lst", "w")


for i,j in zip(imgs,labels):
    contents = "\t" + str(j)+ "\t" + prefix +str(i) + postfix + "\n"
    if random.random() < 0.2:
        val_f.write(str(count_t) +contents)
        count_t += 1
    else:
        train_f.write(str(count_v) +contents)
        count_v += 1
