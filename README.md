"# NeuroSimulation" 

This Python script simulates a spatially structured neuronal network using the Brian2 spiking neural network simulator. 

## Description

The code models a network of 10 leaky integrate-and-fire neurons that are connected through synapses. These synapses have synaptic weights which depend on the spatial position of the neurons. The neurons have distinct positions and are initialized with different membrane potentials. The simulation runs for a duration of one second.

## Dependencies

The following packages are required to run the script:

- Python 3.9
- Brian2
- Matplotlib

You can install these packages using pip:

```bash
pip install brian2 matplotlib
```

## Usage

After installing the necessary dependencies, you can run the script with the following command:

```bash
python spatially_structured_network.py
```

This will run the simulation and generate a plot showing the membrane potential of the first neuron over time.

## File Structure

- `neuronmodel.py`: This is the main script that creates and simulates the neuronal network. It also generates the plot.

- `README.md`: This file contains information about the project, its dependencies, and how to run the script.


[Your Name]

## License

This project is licensed under the MIT License.
