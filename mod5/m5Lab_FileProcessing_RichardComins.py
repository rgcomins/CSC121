#"""
#This program reads data fromn a CSV file and performs manipulation of data written
#to both txt files and data files.
# 03 Mar 2025
 #CSC121 M5Lab
 #Richard Comins
 
#"""
import sales_processing  # Importing modularized functions

def main():
    
    input_file = "sales.csv"
    
    print("opened", input_file)
    total_sales = sales_processing.calculate_total_sales(input_file)
    
    print("writing to total_sales")
    sales_processing.write_sales_csv(total_sales, "total_sales.csv")
    sales_processing.write_sales_txt(total_sales, "total_sales.txt")

    customer_sales = sales_processing.calculate_customer_sales(input_file)
    
    print("writing to cus_total")
    sales_processing.write_customer_csv(customer_sales, "cus_total.csv")
    sales_processing.write_customer_txt(customer_sales, "cus_total.txt")

if __name__ == "__main__":
    main()
