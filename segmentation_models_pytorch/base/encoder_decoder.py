import torch
import torch.nn as nn
from .model import Model


class EncoderDecoder(Model):

    def __init__(self, encoder, decoder, activation):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        
        if callable(activation):
            self.activation = activation
        elif activation == 'softmax':
            self.activation = nn.Softmax(dim=1)
        elif activation == 'sigmoid':
            self.activation = nn.Sigmoid()
        else:
            raise ValueError('Activation should be "sigmoid" or "softmax"')
        
        if encoder.pretrained:
            self.set_preprocessing_params(
                input_size=encoder.input_size,
                input_space=encoder.input_space,
                input_range=encoder.input_range,
                mean=encoder.mean,
                std=encoder.std,
            )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

    def predict(self, x):
        if self.training:
            self.eval()

        with torch.no_grad():
            x = self.forward(x)
            x = self.activation(x)

        return x
