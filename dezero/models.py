from dezero import Layer, utils
import dezero.functions as F
import dezero.layers as L

# =============================================================================
# Model / Sequential / MLP
# =============================================================================


class Model(Layer):
    def plot(self, *inputs, to_file='model.png'):
        y = self.forward(*inputs)
        return utils.plot_dot_graph(y, verbose=True, to_file=to_file)


class MLP(Model):
    """Multi-Layer Perceptron class
    """
    def __init__(self, fc_output_sizes, activation=F.sigmoid):
        """

        Parameters
        ----------
        fc_output_sizes : tuple or list
            full connect output size for each layer
        activation : function
            activation function by default sigmoid function is used
        """
        super().__init__()
        self.activation = activation
        self.layers = []

        for i, out_size in enumerate(fc_output_sizes):
            layer = L.Linear(out_size)
            setattr(self, f'l{i}', layer)
            self.layers.append(layer)

    def forward(self, x):
        for layer in self.layers[:-1]:
            x.self.activation(layer(x))

        return self.layers[-1](x)
