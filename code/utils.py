import tensorflow as tf
from tflearn.activations import relu

def weight_variable(shape): #The weight matrix is generated according to the size of the input
    initial = tf.truncated_normal(shape, stddev=0.1,dtype=tf.float32) #Outputs random values from a truncated normal distribution
    return tf.Variable(initial, dtype=tf.float32)

def bias_variable(shape): #Similarly, define the initial value as 0.1 and the size as SHAPE
    initial = tf.constant(0.1, shape=shape,dtype=tf.float32)
    return tf.Variable(initial, dtype=tf.float32)

def a_layer(x, units):#Initialize the weight matrix, calculate according to the input x value, and return the result after the activation function
    W = weight_variable([x.get_shape().as_list()[1], units]) #Returns the matrix size first, and then generates a list of the number of columns, returning the number of columns
    b = bias_variable([units])
    tf.add_to_collection('l2_reg', tf.contrib.layers.l2_regularizer(1.0)(W)) #Regularize the process to prevent overfitting and add values to the graph
    return relu(tf.matmul(x, W) + b)


def bi_layer(x0,x1,sym,dim_pred):
    if sym == False: 
        W0p = weight_variable([x0.get_shape().as_list()[1],dim_pred])
        W1p = weight_variable([x1.get_shape().as_list()[1],dim_pred])
        tf.add_to_collection('l2_reg', tf.contrib.layers.l2_regularizer(1.0)(W0p))
        tf.add_to_collection('l2_reg', tf.contrib.layers.l2_regularizer(1.0)(W1p))
        return tf.matmul(tf.matmul(x0, W0p),
                            tf.matmul(x1, W1p), transpose_b=True)
    else:
        W0p = weight_variable([x0.get_shape().as_list()[1],dim_pred])
        tf.add_to_collection('l2_reg', tf.contrib.layers.l2_regularizer(1.0)(W0p))
        return tf.matmul(tf.matmul(x0, W0p),
                            tf.matmul(x1, W0p),transpose_b=True)
