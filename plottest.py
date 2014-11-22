import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,2,3,4], "ro", linewidth = 40)
pylab.title("A sample title")
pylab.xlabel("The x Axis...", fontsize = 16)
pylab.ylabel("The y Axis...", fontsize = 16)
pylab.show()