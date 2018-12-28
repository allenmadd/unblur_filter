#make a keras model
#blur the images
#then at the output you want the unblurred

import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('Agg')
from matplotlib import rc
import matplotlib.pyplot as plt
from io import BytesIO
import random
from keras.layers import Input,BatchNormalization,Conv2D, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Model
from keras.utils.vis_utils import plot_model
from keras.optimizers import Adam
import os
from scipy.ndimage import gaussian_filter

rc('text', usetex=True)


def render_latex_formula(formula_string):

    plt.clf()
    plt.text(0.0, 0.0, formula_string, fontsize=20)
    plt.axis('off')


    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(5, 2)

    buf = BytesIO()
    plt.savefig(buf, format='png')

    buf.seek(0)

    pim = Image.open(buf)
    im = np.array(pim)[...,0]

    blacks = np.where(im==0)
    top = np.min(blacks[0])
    bottom = np.max(blacks[0])
    left = np.min(blacks[1])
    right = np.max(blacks[1])
    pim = pim.crop((left-10,top-10,right+10,bottom+10))
    background = Image.fromarray(np.ones((80,450,3),dtype=np.uint8)*255)
    background.paste(pim,(225-int(pim.size[0]*0.5),40-int(pim.size[1]*0.5)))
    background = np.array(background)
    return background


ops = ['+', '-', '*', '/']
latex_scripts = ['\leq', '\\times', '\infty', '\prime',
                 '\\approx', '\subset', '^{\circ}',
                 '\det', '\div', '\int', '\oint','\mp' ]
greek_letters = ['\\theta', '\lambda', '\delta', '\\alpha',
                 '\\beta', '\epsilon', '\pi', '\Psi', '\Pi',
                 '\Lambda', '\\upsilon', '\zeta', '\Phi',
                 '\Xi', '\sigma', '\\nu', '\gamma',
                 '\kappa']


math_mode = ['^', '_', '\sqrt[2]{x}', '\\frac{x}{y}', '\sum_{k=1}^n', '\prod_{k=1}^n', '\dot']
math_mode2 = ['\sqrt[2]{x}', '\\frac{x}{y}', '\sum_{k=1}^n', '\prod_{k=1}^n']


def math_string():
    num1 = str(random.randint(0, 120))
    num2 = str(random.randint(0, 120))
    operation = random.choice(ops)
    scripts = random.choice(latex_scripts)
    greek1 = random.choice(greek_letters)
    greek2= random.choice(greek_letters)
    math1 = random.choice(math_mode)
    math2= random.choice(math_mode2)

    stuff = ' '.join([num1, operation, greek1, scripts, greek2, math1, num2, math2, num1, greek2, scripts, greek1, operation, num2])
    return '${}$'.format(stuff)

def make_model():
    input = Input((None,None,3))
    x = Conv2D(5, (3, 3), padding="same")(input)
    # x = BatchNormalization()(x)
    # x = LeakyReLU(0.3)(x)
    x = Conv2D(20, (3, 3), padding="same")(x)
    # x = BatchNormalization()(x)
    # x = LeakyReLU(0.3)(x)
    x = Conv2D(3, (3, 3), padding="same")(x)
    x = Activation('sigmoid')(x)
    model = Model(input=[input],output=[x])
    model.compile(optimizer=Adam(lr=0.001), loss='mse')
    return model




if __name__ == '__main__':
    m = make_model()
    if os._exists('weights.h5'):
        m.load_weights('weights.h5')
    batch_size = 5 # our computers aren't good for this
    while True:
        #get images
        unblurred = []
        blurred = []
        for i in np.arange(0,batch_size):
            im = render_latex_formula(math_string())
            unblurred.append(im/255.0)
            blurred_im = gaussian_filter(im,sigma=3,order=0)
            blurred.append(blurred_im/255.0)
        X = np.array(blurred)
        Y = np.array(unblurred)
        l = m.train_on_batch(X,Y)
        print(l)
        m.save_weights('weights.h5')
