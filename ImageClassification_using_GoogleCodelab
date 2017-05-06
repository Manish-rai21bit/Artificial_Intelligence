## 1. Introduction

TensorFlow is a an open source library for numerical computation, specializing in machine learning applications.

In this lab, we will be using transfer learning, which means we are starting with a model that has been already trained on another problem. We will then be retraining it on a similar problem. Deep learning from scratch can take days, but transfer learning can be done in short order.

http://image-net.org/index

## 2. Requirements
* TensorFlow Installation
* Docker

What is Docker?
## 3. Setting up the image directory

You can download the images:

cd $HOME
mkdir tf_files
cd tf_files
curl -O http://download.tensorflow.org/example_images/flower_photos.tgz
tar xzf flower_photos.tgz

## 4. Start Docker with local files available
docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel

ls /tf_files/
#Should see: flower_photos  flower_photos.tgz

#### Retrieving the training code
The Docker image you are using contains the latest GitHub TensorFlow tools, but not every last sample. You need to retrieve the full sample set this way:

cd /tensorflow
git pull

Your sample code will now be in /tensorflow/tensorflow/examples/image_retraining/.

## 5. 4. (Re)training Inception

# In Docker
python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/retrained_graph.pb \
--output_labels=/tf_files/retrained_labels.txt \
--image_dir /tf_files/flower_photos

This script loads the pre-trained Inception v3 model, removes the old final layer, and trains a new one on the flower photos you've downloaded.

## 6. Using the Retrained Model

The retraining script will write out a version of the Inception v3 network with a final layer retrained to your categories to tf_files/output_graph.pb and a text file containing the labels to tf_files/output_labels.txt.

These files are both in a format that the C++ and Python image classification examples can use, so you can start using your new model immediately.

#### Classifying an image
Here is Python that loads your new graph file and predicts with it.

##### label_image.py

We can curl it :
# ctrl-D to exit Docker and then:
curl -L https://goo.gl/tx3dqg > $HOME/tf_files/label_image.py

Restart your Docker image:

docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel

Now run it on a new image
# In Docker
python /tf_files/label_image.py /tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg
