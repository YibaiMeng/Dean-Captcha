import network
import training_data_nerual

training_data, validation_data, test_data = training_data_nerual.get_trainging_data()

print test_data
net = network.Network([120, 120, 36])

net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
