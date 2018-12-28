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
    return pim


ops = ['+', '-', '*', '/']
latex_scripts = ['\leq', '\\times', '\infty', '\prime',
                 '\\approx', '\subset', '^{\circ}',
                 '\det', '\div', '\int', '\oint','\mp' ]
greek_letters = ['\\theta', '\lambda', '\delta', '\\alpha',
                 '\\beta', '\epsilon', '\pi', '\Psi', '\Pi',
                 '\Lambda', '\\upsilon', '\zeta', '\Phi',
                 '\Xi', '\sigma', '\\nu', '\gamma',
                 '\kappa']


math_mode = ['^', '_', '\sqrt[n]{x}', '\\frac{x}{y}', '\sum_{k=1}^n', '\prod_{k=1}^n', '\dot']


def math_string():
    num1 = str(random.randint(0, 120))
    num2 = str(random.randint(0, 120))
    operation = random.choice(ops)
    scripts = random.choice(latex_scripts)
    greek1 = random.choice(greek_letters)
    greek2= random.choice(greek_letters)
    math1 = random.choice(math_mode)
    math2= random.choice(math_mode)

    stuff = ' '.join([num1, operation, greek1, scripts, greek2, math1, num2, math2, num1, greek2, scripts, greek1, operation, num2])
    return '${}$'.format(stuff)


if __name__ == '__main__':
    for i in np.arange(0,100):
        txte = math_string()
        print(txte)
        p = render_latex_formula(txte)
        p.save('images/{}.png'.format(i))

