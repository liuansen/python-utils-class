# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import random
import os

from flask import Flask, Response, render_template, request
import qrcode


app = Flask(__name__)


@app.route('/qr_code')
def hello_world():
    path = os.path.abspath('.')
    img_file = path + '/static'
    print path
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_text = ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm',
         'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd', 'c', 'b', 'a'], 8))
    qr_name = ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm',
         'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd', 'c', 'b', 'a'], 22))
    qr.add_data(qr_text)
    qr.make(fit=True)
    image_file = img_file + '/{name}.png'.format(name=qr_name)
    print image_file
    # 生成二维码
    img = qr.make_image()

    # 保存二维码
    img.save(image_file)
    file = "/static/{name}.png".format(name=qr_name)
    print qr_name
    return render_template('index.html', file=file)


if __name__ == '__main__':
    app.run()
