import csv


products = [
    {"name": "Laptop", "price": "₹75,000", "rating": "4.5"},
    {"name": "Smartphone", "price": "₹25,999", "rating": "4.2"},
    {"name": "Wireless Earbuds", "price": "₹2,499", "rating": "4.0"},
    {"name": "Smartwatch", "price": "₹5,999", "rating": "4.3"},
    {"name": "Gaming Keyboard", "price": "₹3,299", "rating": "4.7"},
]

def save_to_csv(data, filename="products.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Rating"])
        for item in data:
            writer.writerow([item["name"], item["price"], item["rating"]])

# Main execution
save_to_csv(products)
print("✅ Simulated product data saved to products.csv")
