"""
Sampling buffer for storing previous (input, output)-samples and
drawing from these samples for additional training data
"""
import numpy
import math
import random


class SamplingBuffer:

    def __init__(self, input_dim, output_dim, buffer_size, seed):
        """
        :param input_dim: dimensionality of input
        :param output_dim: dimensionality of output
        :param buffer_size: capacity of the buffer
        :param seed: random seed
        """
        self.input_dim = input_dim
        self.buffer_size = buffer_size
        self.input_buffer = numpy.zeros((buffer_size, input_dim), dtype=numpy.float64)
        self.output_buffer = numpy.zeros((buffer_size, output_dim), dtype=numpy.float64)
        self.index = 0
        random.seed(seed)

    def add_sample(self, sample_input, sample_output):
        """
        Add sample to buffer
        :param sample_input: input of sample
        :param sample_output: output of sample
        """
        # if buffer is not full add sample at current index
        if self.index < self.buffer_size:
            self.input_buffer[self.index, :] = sample_input[:]
            self.output_buffer[self.index, :] = sample_output[:]
            self.index = self.index + 1

        else:  # if buffer is full, add sample at random index
            index = random.randint(0, self.buffer_size - 1)
            self.input_buffer[index, :] = sample_input[:]
            self.output_buffer[index, :] = sample_output[:]

    def draw_sample(self):
        """
        Draw sample from buffer
        :return: previous (input, output)-sample
        """
        if self.index < self.buffer_size:
            index = random.randint(0, self.index -1)
            return self.input_buffer[index, :], self.output_buffer[index, :]
        else:
            index = random.randint(0, self.buffer_size-1)
            return self.input_buffer[index, :], self.output_buffer[index, :]
