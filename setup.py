from setuptools import setup

setup(
    name='stylegan3',
    version='',
    package_dir={'stylegan3': ''},
    packages=['stylegan3.viz', 'stylegan3.dnnlib', 'stylegan3.metrics', 'stylegan3.training',
              'stylegan3.gui_utils', 'stylegan3.torch_utils', 'stylegan3.torch_utils.ops', 'dnnlib', 'training',
              'torch_utils', 'torch_utils.ops', 'viz', 'gui_utils', 'metrics'],
    py_modules=['stylegan3.legacy'],
    url='',
    license='',
    author='',
    author_email='',
    description=''
)
