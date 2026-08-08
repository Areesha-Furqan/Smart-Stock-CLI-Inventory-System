<div align="center">

# 📦 SmartStock Inventory System

### A menu-driven CLI inventory manager built with pure Python — no frameworks, no fluff, just clean logic.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Storage](https://img.shields.io/badge/Storage-JSON-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## 🎬 Demo

> 🎥 **Demo video coming soon**

---

## 📌 Problem Statement

Small retail shops struggle with inventory chaos. Paper notebooks get lost, spreadsheets become messy, and expensive GUI software is overkill. Shop owners need a simple, reliable, and crash-proof way to track stock, receive restock alerts, and manage sales — without technical complexity.

**SmartStock** solves this with a clean command-line interface anyone can use, with automatic data persistence and bulletproof error handling.

---

## ✨ Key Features

| # | Feature | Description |
|:---:|---|---|
| 1️⃣ | **Add a New Product** | Enter name, category, price, quantity, and low-stock threshold. Auto-generates a unique ID. |
| 2️⃣ | **View All Products** | Displays every product in a clean, formatted table with `❗❗ LOW STOCK ❗❗` alerts. |
| 3️⃣ | **Search Products** | Case-insensitive, partial-match search by name or category. |
| 4️⃣ | **Reduce Stock Quantity** | Sell or remove stock. Prevents overselling; offers to sell remaining stock instead. |
| 5️⃣ | **Increase Stock Quantity** | Restock products when deliveries arrive. |
| 6️⃣ | **Remove Product Permanently** | Deletes a product with confirmation. Logs removals for audit history. |
| 7️⃣ | **Exit** | Gracefully exits with a goodbye message. |

---

## 🎨 Visual Menu

```
┌─────────────────────────────────────┐
│      📦 SmartStock Inventory System    │
├─────────────────────────────────────┤
│                                       │
│   (1) Add a New Product              │
│   (2) View All Products              │
│   (3) Search a Product               │
│   (4) Reduce Stock Quantity          │
│   (5) Increase Stock Quantity        │
│   (6) Remove a Product Permanently   │
│   (7) Exit                           │
│                                       │
└─────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3 |
| **Data Persistence** | JSON (automatic save/load) |
| **Error Handling** | `try/except` with bulletproof input loops |
| **Dependencies** | None — pure standard library |

---

## 📊 How It Works

### Data Structure

Each product is stored as a dictionary inside a list:

```python
{
    "id": 1,
    "name": "USB Cable",
    "price": "$5.99",
    "quantity": 15,
    "category": "Cables",
    "threshold": 5
}
```

### Persistence

- **Save** → After every modification (add, reduce, increase, delete), data is automatically saved to `inventory_data.json`.
- **Load** → On startup, the system loads all saved data. If no file exists, it starts fresh.
- **Deleted Products Log** → Removed products are stored in a `deleted_products` list within the same JSON file for audit purposes.

### Low-Stock Alert

When quantity drops to or below the threshold, the product displays a `❗❗ LOW STOCK ❗❗` warning in the view menu.

---

## 🖥️ How to Run

**Prerequisites:** Python 3.x installed on your system.

```bash
# 1. Clone this repository
git clone https://github.com/Areesha-Furqan/SmartStock-Inventory-System.git

# 2. Navigate to the project folder
cd SmartStock-Inventory-System

# 3. Run the script
python smart_inventory.py
```

Then just follow the on-screen menu prompts. 🎉

---

## 🛡️ Safety & Error Prevention

| Feature | Implementation |
|---|---|
| **Invalid Price/Quantity Input** | `while` loop with `try/except` keeps asking until a valid number is entered. |
| **Selling More Than Available** | Prevents overselling. Offers to sell all remaining stock instead. |
| **Product Not Found** | Displays a friendly "Product not available" message — no crashes. |
| **Deletion Confirmation** | Asks `"Are you sure? [y/n]"` before permanent removal. |
| **Empty Inventory** | Graceful handling with "No inventory stored yet" messages. |
| **Data Persistence** | Automatic save after every modification. Data survives restarts. |

---

## 💡 Why This Project Matters

SmartStock demonstrates real-world software engineering for small business operations:

- 🧩 **Practical Data Modeling** — products, stock levels, categories, and thresholds.
- ⚙️ **Business Logic** — preventing overselling, low-stock alerts, restock workflows.
- 🛡️ **Defensive Programming** — every user input is validated and handled gracefully.
- 🏗️ **Professional Code Organization** — functions with docstrings, parameters, and return values.
- 💾 **Persistent Storage** — JSON serialization ensures data survives between runs.
- 🎯 **User Experience** — clear menus, formatted output, intuitive workflows.

---

## 📚 Concepts Covered

| Concept | Implementation |
|---|---|
| List of Dictionaries | Primary data structure for inventory. |
| Functions | Modular design: `printmenu()`, `add_product()`, `view_products()`, etc. |
| Parameters & Return Values | Data passed and returned safely. |
| Error Handling | `try/except` for all user inputs. |
| File I/O | JSON load/save with `json.dump()` and `json.load()`. |
| Business Logic | Low-stock alerts, oversell prevention, restock workflows. |
| Deleted Products Log | Separate list for audit trail. |
| Docstrings | Every function documented. |

---

## 🔮 Future Enhancements

- [ ] **Edit Product Details** — update price, threshold, or category.
- [ ] **Sales History** — track when stock was reduced or increased.
- [ ] **Category-Based Reports** — view inventory grouped by category.
- [ ] **CSV Export** — export inventory to an Excel-friendly format.
- [ ] **Unit Price & Total Value** — calculate total inventory value.
- [ ] **Supplier Management** — track which supplier provides each product.

---

## 🏆 Acknowledgments

Built as part of my **Python Learning Journey** to demonstrate mastery of CLI application development, data persistence, and error handling. This project showcases my ability to translate real-world business requirements into clean, reliable code — as a junior backend developer just getting started. 🌱

---

## 📬 Connect with Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Areesha--Furqan-181717?style=for-the-badge&logo=github)](https://github.com/Areesha-Furqan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Areesha%20Furqan-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/areesha-furqan-100728346/)

</div>
