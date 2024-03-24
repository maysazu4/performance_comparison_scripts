import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit


def draw_results(results1, results2, slow, fast,file ):
    list_size = [val[0] for val in results1]
    time1 = [val[1] for val in results1]
    time2 = [val[1] for val in results2]
    plt.scatter(list_size, time1, label=slow,color = 'blue')
    plt.scatter(list_size, time2, label=fast,color = 'red')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title('Size vs Time')
    plt.legend()
    plt.grid(True)
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', slow ,fast])
        for i in range(len(list_size)):
            writer.writerow([list_size[i], time1[i] ,time2[i]])
    plt.show()