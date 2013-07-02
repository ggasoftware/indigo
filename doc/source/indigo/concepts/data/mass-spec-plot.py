import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from matplotlib.collections import *

fig = plt.figure(figsize=(8, 3))
ax = fig.add_subplot(111)

values = []
for line in open("csid-370269-mass-spec.txt"):
    values.append([float(v) for v in line.split()])


norm = sum([y for x, y in values])
segments = []
for x, y in values:
    segments.append([(x, 0), (x, y / norm)])

line_segments = LineCollection(segments,
                                linewidths = 1,
                                linestyles = 'solid')


mab = (831.11242, 100.0 / norm)
mmono = (827.11832, 34.0 / norm)
molecularWeight = 831.397847

plt.plot([mmono[0], mab[0]], [mmono[1], mab[1]], 'o', color='b')
plt.text(mmono[0] + 0.2, mmono[1] + 0.005, "monoisotopic", size=10, ha='left')
plt.text(mab[0] - 0.2, mab[1] + 0.005, "mostAbundant", size=10, ha='right')

ax.add_collection(line_segments, autolim=True)
ax.autoscale_view()

plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=8)

plt.axvline(x=molecularWeight, color='red', linestyle='--')
plt.text(molecularWeight + 0.3, 0.2, "molecularWeight", size=10, ha='center', rotation='vertical', color='red')

def to_percent(y, position):
    s = str(100 * y)
    return s + '%'

formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)

plt.savefig('result.png')