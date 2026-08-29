import streamlit as st
import numpy
from scipy import stats
import matplotlib.pyplot as plt

st.header("Mean, Median and Mode")

st.markdown("""

Mean - The average value \n
Median - The mid point value \n
Mode - The most common value

""")

notes = """

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# calculate mean value
x = numpy.mean(speed) 
# print(x) # 89.76923076923077

# calculate median value
# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
x = numpy.median(speed)
# print(x) # 87.0

# calculate mode value
# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86

x = stats.mode(speed) 
print(x) # ModeResult(mode=np.int64(86), count=np.int64(3))

"""

st.code(notes, language='python')

st.header("Standard Deviation")

st.markdown("""

Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

A high standard deviation means that the values are spread out over a wider range.

""")

notes = """
speedA = [86,87,88,86,87,85,86] # low standard deviation
speedB = [32,111,138,28,59,77,97] # high standard deviation

x1 = numpy.std(speedA)
x2 = numpy.std(speedB)

print(x1) # 0.9035079029052513
print(x2) # 37.84501153334721

"""

st.code(notes, language='python')

st.header("Variance")

notes = """
#1. Find the mean
(32+111+138+28+59+77+97) / 7 = 77.4

#2. Find difference from the mean
 32 - 77.4 = -45.4
111 - 77.4 =  33.6
138 - 77.4 =  60.6
 28 - 77.4 = -49.4
 59 - 77.4 = -18.4
 77 - 77.4 = - 0.4
 97 - 77.4 =  19.6

#3. For each difference, find square value
(-45.4)^2 = 2061.16
 (33.6)^2 = 1128.96
 (60.6)^2 = 3672.36
(-49.4)^2 = 2440.36
(-18.4)^2 =  338.56
(- 0.4)^2 =    0.16
 (19.6)^2 =  384.16

#4. The variance is the average number of these squared differences:
(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2 #variance

#if you take the square root of the variance, you get the standard deviation!


speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x) # 1432.2448979591834

"""

st.code(notes, language='python')

st.header("Percentiles")

st.markdown("""
Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

""")

notes = """

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)
print(x) # 43    0.75 percentile meaning that 75% of the people are 43 or younger

"""

st.code(notes, language='python')

st.header("Histogram")
st.markdown("""
To visualize the data set we can draw a histogram with the data we collected.

""")

notes = """
# create an array containing 200 random floats between 0 and 100
x = numpy.random.uniform(0, 100, 200)

print(x) # generate a list random float between 0 - 100

fig, ax = plt.subplots()
ax.hist(x, bins = 10)

st.pyplot(fig)
"""

st.header("Uniform Data Distribution")

x = numpy.random.uniform(0, 100, 200)

print(x) # generate a list random float between 0 - 100

fig, ax = plt.subplots()
ax.hist(x, bins = 10)

st.pyplot(fig)
st.code(notes, language='python')

st.header("Normal Data Distribution")

notes = """
# input - mean, standard deviation
x = numpy.random.normal(5.0, 1.0, 100000)
fig, ax = plt.subplots()
ax.hist(x, bins = 10000)

st.pyplot(fig)

"""

st.code(notes, language='python')

# input - mean, standard deviation
x = numpy.random.normal(5.0, 1.0, 100000)
fig, ax = plt.subplots()
ax.hist(x, bins = 10000)

st.pyplot(fig)


st.header("Scatter Plot")

notes = """
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

fig, ax = plt.subplots()
ax.scatter(x, y)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.set_title("Scatter Plot")
st.pyplot(fig)

"""

st.code(notes, language='python')

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

fig, ax = plt.subplots()
ax.scatter(x, y)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.set_title("Scatter Plot")
st.pyplot(fig)








