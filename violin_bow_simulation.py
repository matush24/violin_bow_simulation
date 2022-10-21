import matplotlib.pyplot as plt

iterations, dt = 10000, 0.01        # integration steps, integration step size
t, x, v, a = [], [], [], []         # define fields to store time, x coordinate, velocity, acceleration
vb = 1                              # valocity of the violin bow
fs, fd = 1, 0.7                     # static friction coefficient, dynamic friction coefficient
N = 10                              # normal force
k = 0.5                             # elastic coefficient
m = 0.1                             # mass of the weight
accuracy = 1e-6                     # accuracy
alpha = 1                           # drag coefficient

x.append(0)
v.append(0)
t.append(0)

for i in range(iterations):
    if abs(v[-1] - vb) < accuracy and x[-1]*k < N*fs:               # if the weight isn't moving and static friction is greater than elastic force
        a.append(0)
        x.append(x[-1] +  v[-1]*dt)
        v.append(vb)
    elif abs(v[-1] - vb) < accuracy:                                # if the weight isn't moving and static friction is smaller than elastic force
        a.append((-x[-1]*k + N*fs)/m)
        x.append(x[-1] + v[-1]*dt)
        v.append(v[-1] + a[-1]*dt)
    else:                                                           # if the weight is moving
        a.append((-x[-1]*k + N*fd - alpha*v[-1]*abs(v[-1]))/m)
        x.append(x[-1] + v[-1]*dt)
        v.append(v[-1] + a[-1]*dt)
    t.append(t[-1] + dt)                                            # to track time and visualise x in time

plt.plot(t, x)                                                      # plot chart
plt.ylim(x[-1] - 0.02, x[-1] + 0.02)                                # set boundaries for the y axis
plt.show()                                                          # show chart
