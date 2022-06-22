import numpy as np
import dxchange
# import model
import cv2
from utils import *
import os
import tensorflow as tf
from keras import backend as Keras
from keras.models import load_model
from keras.models import model_from_json
def is_image_file(filename):
    return any(filename.endswith(extension) for extension in [".tiff",".tif"])
def red_stack_tiff(path):
    files = os.listdir(path)
    prj = []
    for n,file in enumerate(files):
        if is_image_file(file):
            p = dxchange.read_tiff(path + file)
            prj.append(p)
    pr = np.array(prj)
    return pr
def is_h5_file(filename):
    return any(filename.endswith(extension) for extension in [".hdf5"])
def evalue():
    opt = get_args()
    input_x = red_stack_tiff(opt.path_input)
    where_are_inf = np.isnan(input_x)
    input_x[where_are_inf] = 0.0
    xc,xr, xl = input_x.shape
    input_x = input_x.reshape(xc, xr, xl, 1)
    x_norm = preprocess_input(input_x)
    x_norm = expand_array_size_with_padding(
        x_norm, 1, 32)
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    Keras.set_session(tf.Session(config=config))
    json_file = open(opt.path_model, 'r')
    model = model_from_json(json_file.read())
    model.load_weights(opt.weights_path)
    y_pred = model.predict(x_norm, batch_size=1, verbose=0)
    y_pred = np.squeeze(y_pred)
    y_pred = y_pred[:,:xr,:xl]
    fil = 'out_'
    for i_na, re in enumerate(y_pred):
        if i_na < 10:
            dxchange.writer.write_tiff(re, opt.path_out + '%s000%s.tiff' % (fil, i_na))
        elif 9 < i_na < 100:

            dxchange.writer.write_tiff(re, opt.path_out + '%s00%s.tiff' % (fil, i_na))
        elif 99 < i_na < 1000:
            dxchange.writer.write_tiff(re, opt.path_out + '%s0%s.tiff' % (fil, i_na))
        else:
            dxchange.writer.write_tiff(re, opt.path_out + '%s%s.tiff' % (fil, i_na))
def get_args():
    parser = argparse.ArgumentParser(description='Evaluation the UNet on images and target masks',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path_input', type=str,default='./input/')
    parser.add_argument('--path_out',type=int, default='./put/')
    parser.add_argument('--weights_path',type=int, default='./model/u-net.json')
    parser.add_argument('--path_model', type=int, default='./model/u_net.hdf5')

    return parser.parse_args()

if __name__ == '__main__':
    evalue()



