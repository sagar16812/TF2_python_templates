#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.dont_write_bytecode = True

import tensorflow as tf

def get_loss_function():
    loss_func = tf.keras.losses.SparseCategoricalCrossentropy()
    return loss_func
