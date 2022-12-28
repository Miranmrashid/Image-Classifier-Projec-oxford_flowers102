# Image Classifier Projec oxford_flowers102
 
This was the second project in the Introduction to Machine Learning with TensorFlow Nanodegree Program from Udacity. In this project, I'll work through a Jupyter notebook first to implement an image classifier with TensorFlow to recognize different species of flowers, then it will be converted into a command line application.

**Tools used in this project:**

- PyTorch
- ArgParse
- Jason
- PIL
- NumPy
- Pandas
- matplotlib
- scikit-learn
- GPU required

#### Usage 
```console 
$ python predict.py ./test_images/orchid.jpg my_model.h5
```
#### Optional - Return the top 3 most likely classes 
```console 
$ python predict.py ./test_images/orchid.jpg my_model.h5 --top_k 3
```
#### Optional - Use a `label_map.json` file to map labels to flower names
```console 
$ python predict.py ./test_images/orchid.jpg my_model.h5 --category_names label_map.json
```



# Data
tensorflow_datasets was used to load the  [Oxford 102 Category Flower Dataset]( http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html ). This dataset has 3 splits: 'train', 'test', and 'validation'.


# A credit to Udacity
This project is part of the Udacity Nanodegree.
