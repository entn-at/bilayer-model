import runway
import numpy as np
import tensorflow as tf
from PIL import Image
from infer import InferenceWrapper

import argparse
from infer import InferenceWrapper


args_dict = {
    'project_dir': '.',
    'init_experiment_dir': './vc2-hq_adrianb_paper_main',
    'init_networks': 'identity_embedder, texture_generator, keypoints_embedder, inference_generator',
    'init_which_epoch': '2225',
    'num_gpus': 1,
    'experiment_name': 'vc2-hq_adrianb_paper_enhancer',
    'which_epoch': '1225',
    'spn_networks': 'identity_embedder, texture_generator, keypoints_embedder, inference_generator, texture_enhancer',
    'enh_apply_masks': False,
    'inf_apply_masks': False}

@runway.setup(options=args_dict)
def setup(opts):
  return InferenceWrapper(opts)

    
# translate is the function that is called when you input a image, specify the input and output types
@runway.command('translate', inputs={'source_imgs': runway.image, "target_imgs": runway.image}, outputs={'image': runway.image})
def translate(net, inputs):
    data_dict = net(inputs)
    imgs = data_dict['pred_enh_target_imgs']
    segs = data_dict['pred_target_segs']
    return imgs


if __name__ == '__main__':
    runway.run(port=8889)