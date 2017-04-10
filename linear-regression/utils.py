from os import path
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def read(dataset='train', dir_path='./data'):
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """

    if dataset is 'train':
        fname_images = path.join(dir_path, 'train-images-idx3-ubyte')
        fname_labels = path.join(dir_path, 'train-labels-idx1-ubyte')
    elif dataset is 'test':
        fname_images = path.join(dir_path, 't10k-images-idx3-ubyte')
        fname_labels = path.join(dir_path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    with open(fname_labels, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.fromfile(f, dtype=np.int8)

    with open(fname_images, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        images = np.fromfile(f, dtype=np.uint8).reshape(len(labels), rows, cols)

    return images, labels

def show(image):
    """
    Render a given numpy.uint8 2D array of pixel data.
    """

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    plt.show()
