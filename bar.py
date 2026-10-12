import matplotlib.pyplot as plt

sub=["math","physiscs","english","hindi"]
marks=[20,34,56,77]
plt.pie(marks,labels=sub)

plt.title("marks distribution")

plt.show()