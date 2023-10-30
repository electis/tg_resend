import logging

from dotenv import dotenv_values

logging.basicConfig(filename='tg_resend.log', level=logging.INFO, encoding='utf-8',
                    format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
logger = logging.getLogger()

class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


config = DotDict({
    **dotenv_values(".env.example"),
    **dotenv_values(".env"),
})
