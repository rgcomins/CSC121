import csv

def calculate_total_sales(file_name):
    total_sales = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            product_id = row[0]
            sale_amount = float(row[2])
            total_sales[product_id] = total_sales.get(product_id, 0) + sale_amount
    return total_sales

def write_sales_csv(data, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product ID", "Total Sales ($)"])
        for key, value in data.items():
            writer.writerow([key, f"${value:.2f}"])

def write_sales_txt(data, file_name):
    with open(file_name, mode='w') as file:
        file.write("Product ID | Total Sales ($)\n")
        file.write("-" * 30 + "\n")
        for key, value in data.items():
            file.write(f"{key} | ${value:.2f}\n")
            
# Same as write_sales, but with different header        
def write_customer_csv(data, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Customer ID", "Total Sales ($)"])
        for key, value in data.items():
            writer.writerow([key, f"${value:.2f}"])

def write_customer_txt(data, file_name):
    with open(file_name, mode='w') as file:
        file.write("Customer ID | Total Sales ($)\n")
        file.write("-" * 30 + "\n")
        for key, value in data.items():
            file.write(f"{key} | ${value:.2f}\n")            

def calculate_customer_sales(file_name):
    customer_sales = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            customer_id = row[3]
            sale_amount = float(row[2])
            customer_sales[customer_id] = customer_sales.get(customer_id, 0) + sale_amount
    return customer_sales
