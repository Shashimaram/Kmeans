# import matplotlib.pyplot as plt

# # Execution times in milliseconds
# cpp_large_data = [2047, 2055, 2006]
# cpp_medium_data = [395, 380, 470]
# cpp_small_data = [38, 43, 35]

# cuda_large_data = [5480, 4103, 4099]
# cuda_medium_data = [918, 1502, 1497]
# cuda_small_data = [806, 450, 1497]

# # Convert times to microseconds
# cpp_large_data = [time * 1000 for time in cpp_large_data]
# cpp_medium_data = [time * 1000 for time in cpp_medium_data]
# cpp_small_data = [time * 1000 for time in cpp_small_data]

# # Plotting the lines
# attempts = range(1, 4)

# plt.plot(attempts, cpp_large_data, marker='o', label='C++ Large Data')
# plt.plot(attempts, cuda_large_data, marker='o', label='CUDA Large Data')

# plt.plot(attempts, cpp_medium_data, marker='o', label='C++ Medium Data')
# plt.plot(attempts, cuda_medium_data, marker='o', label='CUDA Medium Data')

# plt.plot(attempts, cpp_small_data, marker='o', label='C++ Small Data')
# plt.plot(attempts, cuda_small_data, marker='o', label='CUDA Small Data')

# # Adding labels and title
# plt.xlabel('Attempts')
# plt.ylabel('Execution Time (microseconds)')
# plt.title('Comparison of C++ and CUDA Execution Times for Different Data Sizes')

# # Display a legend
# plt.legend()

# # Display the plot
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Execution times in milliseconds
# cpp_large_data = [2047, 2055, 2006]
# cpp_medium_data = [395, 380, 470]
# cpp_small_data = [38, 43, 35]

# cuda_large_data = [5480, 4103, 4099]
# cuda_medium_data = [918, 1502, 1497]
# cuda_small_data = [806, 450, 1497]

# # Convert times to microseconds
# cpp_large_data = [time * 1000 for time in cpp_large_data]
# cpp_medium_data = [time * 1000 for time in cpp_medium_data]
# cpp_small_data = [time * 1000 for time in cpp_small_data]

# # Set up data for plotting
# attempts = np.arange(len(cpp_large_data))
# bar_width = 0.35

# # Plotting the grouped bar chart
# fig, ax = plt.subplots()

# cpp_bars = ax.bar(attempts - bar_width/2, cpp_large_data, bar_width, label='C++', color='blue')
# cuda_bars = ax.bar(attempts + bar_width/2, cuda_large_data, bar_width, label='CUDA', color='orange')

# ax.bar(attempts - bar_width/2, cpp_medium_data, bar_width, color='blue', alpha=0.7)
# ax.bar(attempts + bar_width/2, cuda_medium_data, bar_width, color='orange', alpha=0.7)

# ax.bar(attempts - bar_width/2, cpp_small_data, bar_width, color='blue', alpha=0.5)
# ax.bar(attempts + bar_width/2, cuda_small_data, bar_width, color='orange', alpha=0.5)

# # Adding labels and title
# ax.set_xlabel('Attempts')
# ax.set_ylabel('Execution Time (microseconds)')
# ax.set_title('Comparison of C++ and CUDA Execution Times for Different Data Sizes')
# ax.set_xticks(attempts)
# ax.set_xticklabels(['Attempt 1', 'Attempt 2', 'Attempt 3'])

# # Display a legend
# ax.legend()

# # Display the plot
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Execution times in milliseconds
# cpp_large_data = [2047, 2055, 2006]
# cpp_medium_data = [395, 380, 470]
# cpp_small_data = [38, 43, 35]

# cuda_large_data = [5480, 4103, 4099]
# cuda_medium_data = [918, 1502, 1497]
# cuda_small_data = [806, 450, 1497]

# # Convert times to microseconds
# cpp_large_data = [time * 1000 for time in cpp_large_data]
# cpp_medium_data = [time * 1000 for time in cpp_medium_data]
# cpp_small_data = [time * 1000 for time in cpp_small_data]

# # Set up data for plotting
# attempts = np.arange(1, 4)

# # Plotting the line graphs
# plt.plot(attempts, cpp_large_data, marker='o', label='C++ Large Data')
# plt.plot(attempts, cuda_large_data, marker='o', label='CUDA Large Data')

# plt.plot(attempts, cpp_medium_data, marker='o', label='C++ Medium Data')
# plt.plot(attempts, cuda_medium_data, marker='o', label='CUDA Medium Data')

# plt.plot(attempts, cpp_small_data, marker='o', label='C++ Small Data')
# plt.plot(attempts, cuda_small_data, marker='o', label='CUDA Small Data')

# # Adding labels and title
# plt.xlabel('Attempts')
# plt.ylabel('Execution Time (microseconds)')
# plt.title('Comparison of C++ and CUDA Execution Times for Different Data Sizes')

# # Display a legend
# plt.legend()

# # Display the plot
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Execution times in milliseconds
cpp_large_data = [2047, 2055, 2006]
cpp_medium_data = [395, 380, 470]
cpp_small_data = [38, 43, 35]

cuda_large_data = [5480, 4103, 4099]
cuda_medium_data = [918, 1502, 1497]
cuda_small_data = [806, 450, 1497]

# Convert times to microseconds
cpp_large_data = [time * 1000 for time in cpp_large_data]
cpp_medium_data = [time * 1000 for time in cpp_medium_data]
cpp_small_data = [time * 1000 for time in cpp_small_data]

# Set up data for plotting
attempts = np.arange(1, 4)

# Plotting individual line graphs
plt.figure(figsize=(12, 8))

# Plot for Large Data
plt.subplot(3, 1, 1)
plt.plot(attempts, cpp_large_data, marker='o', label='C++')
plt.plot(attempts, cuda_large_data, marker='o', label='CUDA')
plt.title('Large Data')
plt.xlabel('Attempts')
plt.ylabel('Execution Time (microseconds)')
plt.legend()

# Plot for Medium Data
plt.subplot(3, 1, 2)
plt.plot(attempts, cpp_medium_data, marker='o', label='C++')
plt.plot(attempts, cuda_medium_data, marker='o', label='CUDA')
plt.title('Medium Data')
plt.xlabel('Attempts')
plt.ylabel('Execution Time (microseconds)')
plt.legend()

# Plot for Small Data
plt.subplot(3, 1, 3)
plt.plot(attempts, cpp_small_data, marker='o', label='C++')
plt.plot(attempts, cuda_small_data, marker='o', label='CUDA')
plt.title('Small Data')
plt.xlabel('Attempts')
plt.ylabel('Execution Time (microseconds)')
plt.legend()

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()
