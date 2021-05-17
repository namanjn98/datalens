# Data Lens

Visualise your dataset before training the model in one line!

Made changes to the bounding boxes or images? 
Save time by visualising the data and avoid mistakes before starting the training process

Installation:
~~~
pip install datalens
~~~

Usage: 
```
import datalens
image_dir_path = #PATH TO IMAGE DIRECTORY
annotations_dict = #CHECK BELOW
count = 10 #RANDOMLY SELECTED FROM THE DATASET

datalens.Visualise(image_dir_path = image_dir_path, annotations_dict = annotations_dict, count = count)
```

Use Case: 
- Dont forget to resize the bounding boxes
- Visualise what augmentation functions do to your data
