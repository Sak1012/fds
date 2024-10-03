import matplotlib.pyplot as plt

# Data
product_a_sales = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
product_b_sales = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
product_a_expenses = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
product_b_expenses = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
months = list(range(1, 13))

# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2)

# Plot Sales of Product A
axs[0, 0].plot(months, product_a_sales, 'tab:blue')
axs[0, 0].set_title('Product A Sales')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Sales (in 1000s)')

# Plot Sales of Product B
axs[0, 1].plot(months, product_b_sales, 'tab:orange')
axs[0, 1].set_title('Product B Sales')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Sales (in 1000s)')

# Plot Expenses of Product A
axs[1, 0].plot(months, product_a_expenses, 'tab:green')
axs[1, 0].set_title('Product A Expenses')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Expenses (in 1000s)')

# Plot Expenses of Product B
axs[1, 1].plot(months, product_b_expenses, 'tab:red')
axs[1, 1].set_title('Product B Expenses')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Expenses (in 1000s)')

plt.tight_layout()
plt.show()
