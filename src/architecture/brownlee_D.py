# TARGET: 32,32,3 CIFAR-10
# 
# REFERENCES
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-cifar-10-small-object-photographs-from-scratch/
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import LeakyReLU, Dropout
from keras.layers import BatchNormalization
from keras.optimizers import Adam, RMSprop

       
class DifferetiableNetwork(object):
    
    def __init__(self, creation_shape):
        self.net_config = self.get_new_config()
        self.net_config['creation_shape'] = creation_shape
        self.neural_net = self.get_new_model()
        
    def get_new_config(self):    
        config = {}
#         config['filter_size'] = 5
#         config['dropout'] = 0.4 # avoid generated images looking like noise
#         config['alpha'] = 0.2
#         config['depth'] = 64
        return config
              
    def get_new_model(self):
        
        sequence = Sequential()
        
        in_shape = (32,32,3)
        # normal
        sequence.add(Conv2D(64, (3,3), padding='same', input_shape=in_shape))
        sequence.add(LeakyReLU(alpha=0.2))
        # downsample
        sequence.add(Conv2D(128, (3,3), strides=(2,2), padding='same'))
        sequence.add(LeakyReLU(alpha=0.2))
        # downsample
        sequence.add(Conv2D(128, (3,3), strides=(2,2), padding='same'))
        sequence.add(LeakyReLU(alpha=0.2))
        # downsample
        sequence.add(Conv2D(256, (3,3), strides=(2,2), padding='same'))
        sequence.add(LeakyReLU(alpha=0.2))
        # classifier
        sequence.add(Flatten())
        sequence.add(Dropout(0.4))
        sequence.add(Dense(1, activation='sigmoid'))

    
    
#         sequence = Sequential()
        
#         # input: fully connected
#         sequence.add(Conv2D(filters = self.net_config['depth'],   # of filters
#                             kernel_size = self.net_config['filter_size'], 
#                             strides = 2, 
#                             padding = 'same', 
#                             kernel_initializer = glorot_uniform(seed=0),
#                             input_shape = self.net_config['creation_shape']))
#         sequence.add(LeakyReLU(alpha=self.net_config['alpha']))
#         sequence.add(Dropout(self.net_config['dropout']))

#         # hidden: convolutional
#         sequence.add(Conv2D(filters = self.net_config['depth'] * 2, 
#                             kernel_size = self.net_config['filter_size'], 
#                             strides = 2, 
#                             padding = 'same'),
#                             kernel_initializer = glorot_uniform(seed=0))
#         sequence.add(LeakyReLU(alpha=self.net_config['alpha']))
#         sequence.add(Dropout(self.net_config['dropout']))

#         # hidden: convolutional
#         sequence.add(Conv2D(filters = self.net_config['depth'] * 4, 
#                             kernel_size = self.net_config['filter_size'], 
#                             strides = 2, 
#                             padding = 'same'),
#                             kernel_initializer = glorot_uniform(seed=0))
#         sequence.add(LeakyReLU(alpha=self.net_config['alpha']))
#         sequence.add(Dropout(self.net_config['dropout']))
        
#         # hidden: convolutional
#         sequence.add(Conv2D(filters = self.net_config['depth'] * 8, 
#                             kernel_size = self.net_config['filter_size'], 
#                             strides = 1, 
#                             padding = 'same'),
#                             kernel_initializer = glorot_uniform(seed=0))
#         sequence.add(LeakyReLU(alpha=self.net_config['alpha']))
#         sequence.add(Dropout(self.net_config['dropout']))
        
#         # output
#         sequence.add(Flatten())
#         sequence.add(Dense(1))
#         sequence.add(Activation('sigmoid'))
        
        return sequence
                  
    def get_model(self):
        return self.neural_net
    
    def get_config(self):
        return self.net_config
