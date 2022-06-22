# -*- coding: utf-8 -*-

from keras import backend as Keras
import tensorflow as tf


def tf_log10(x):
    """Compute the log base 10

    Parameters
    ----------
        x : int or float

    Returns
    -------
        float
    """

    numerator = tf.log(x)
    denominator = tf.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator


def PSNR(y_true, y_pred):
    """Compute the Peak Signal to Noise Ratio metrics
    The PSNR is computed on the error between the predicted value and the true value

    PSNR(x) = 10 * log_10( d^2 / mean_square_error(x) ) with d the maximal possible value of x

    Parameters
    ----------
        y_true : float
            true value
        y_pred : float
            predicted value

    Returns
    -------
        float
    """

    max_pixel = 255.0
    y_pred = Keras.clip(y_pred, 0.0, 255.0)
    return 10.0 * tf_log10((max_pixel ** 2) / (Keras.mean(Keras.square(y_pred - y_true))))


def custom_sparse_categorical_accuracy(y_true, y_pred):
    """Sparse categorical sparse accuracy re-implementation
    due to Keras categorical sparse accuracy error with our
    current Keras version.

    Parameters
    ----------
        y_true : float
            true value
        y_pred : float
            predicted value

    Returns
    -------
        float
    """
    return Keras.cast(Keras.equal(Keras.max(y_true, axis=-1),
                      Keras.cast(Keras.argmax(y_pred, axis=-1),
                      Keras.floatx())), Keras.floatx())
