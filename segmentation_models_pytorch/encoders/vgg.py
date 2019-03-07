import torch.nn as nn
from torchvision.models.vgg import VGG
from torchvision.models.vgg import make_layers
from torchvision.models.vgg import cfg
from pretrainedmodels.models.torchvision_models import pretrained_settings


class VGGEncoder(VGG):

    def __init__(self, config, batch_norm=False, *args, **kwargs):
        super().__init__(
            make_layers(config, batch_norm=batch_norm), 
            *args, 
            **kwargs
        )
        self.pretrained = False
        del self.classifier

    def forward(self, x):
        features = []
        for module in self.features:
            if isinstance(module, nn.MaxPool2d):
                features.append(x)
            x = module(x)
        features.append(x)
        return features[::-1]

    def load_state_dict(self, state_dict, **kwargs):
        keys = list(state_dict.keys())
        for k in keys:
            if k.startswith('classifier'):
                state_dict.pop(k)
        super().load_state_dict(state_dict, **kwargs)


vgg_encoders = {

    'vgg11': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg11'],
        'params': {
            'config': cfg['A'],
            'batch_norm': False,
        },
    },

    'vgg11_bn': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg11_bn'],
        'params': {
            'config': cfg['A'],
            'batch_norm': True,
        },
    },

    'vgg13': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg13'],
        'params': {
            'config': cfg['B'],
            'batch_norm': False,
        },
    },

    'vgg13_bn': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg13_bn'],
        'params': {
            'config': cfg['B'],
            'batch_norm': True,
        },
    },

    'vgg16': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg16'],
        'params': {
            'config': cfg['D'],
            'batch_norm': False,
        },
    },

    'vgg16_bn': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg16_bn'],
        'params': {
            'config': cfg['D'],
            'batch_norm': True,
        },
    },

    'vgg19': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg19'],
        'params': {
            'config': cfg['E'],
            'batch_norm': False,
        },
    },

    'vgg19_bn': {
        'encoder': VGGEncoder,
        'out_shapes': (512, 512, 512, 256, 128),
        'pretrained_settings': pretrained_settings['vgg19_bn'],
        'params': {
            'config': cfg['E'],
            'batch_norm': True,
        },
    },
}
