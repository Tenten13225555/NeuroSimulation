from brian2 import *
import matplotlib as plt

# Define number of neurons and simulation time
N = 10
duration = 1*second

# Neuron parameters
E_l = -70*mV  # leak reversal potential
g_l = 10*nS  # leak conductance
E_e = 0*mV  # excitatory synaptic reversal potential
tau_e = 5*ms  # excitatory synaptic time constant

# Differential equations for the neuron model
eqs_neurons = '''
dv/dt = (g_l*(E_l - v) + g_e*(E_e - v) + 2*mV*xi) / (10*ms) : volt (unless refractory)
dg_e/dt = -g_e / tau_e : siemens  # post-synaptic excitatory conductance
x : meter  # position
'''

neuron = NeuronGroup(N, eqs_neurons, threshold='v>-50*mV', reset='v=-60*mV', refractory=5*ms, method='euler')

# Initialize each neuron with a different membrane potential and position
neuron.v = 'E_l + i*mV'
neuron.x = 'i*200*umetre'

# Create synapses with synaptic weights dependent on spatial position
eqs_synapses = '''
w : volt  # synaptic weight
dx = x_pre - x_post : meter (constant over dt)  # distance between pre- and post-synaptic neurons
'''
synapses = Synapses(neuron, neuron, model=eqs_synapses, on_pre='g_e_post += w')
synapses.connect(condition='i != j', p='exp(-abs(dx)/(500*umetre))')  # no self-connections, connect probability based on distance
synapses.w = '10*mV'

# Record the membrane potentials
M = StateMonitor(neuron, 'v', record=True)

# Run the simulation
run(duration)

# plot the output
plt.figure(figsize=(12, 4))
plt.plot(M.t/ms, M.v[0])
plt.xlabel('Time (ms)')
plt.ylabel('Membrane potential')
plt.title('Membrane potential of neuron 0 over time')
plt.show()
