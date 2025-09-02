# ✈️ Airline Reservation System  

## 📌 Overview  
A **console-based Airline Reservation System** built with **Python** using **Object-Oriented Programming (OOP)**.  
This project simulates a simple airline booking system where users can:  
- Book and cancel tickets  
- Automatically assign seats  
- Manage overbookings with a **waitlist**  
- Print formatted **boarding passes**  

---

## 🏗️ Project Structure  
```
airline-reservation-system/
│
├── models/
│   ├── passenger.py   # Passenger class
│   ├── ticket.py      # Ticket class
│   ├── flight.py      # Flight class
│   └── airline.py     # Airline class
│
├── main.py            # Entry point with menu system
└── README.md
```

---

## 🛠️ Features  
- ✅ Book tickets with automatic seat assignment  
- ✅ Cancel tickets and move waitlisted passengers into confirmed seats  
- ✅ Track available and occupied seats  
- ✅ Waitlist handling for full flights  
- ✅ Print boarding passes for confirmed passengers  

---

## 🧑‍💻 Tech Stack  
- **Language:** Python 3  
- **Concepts:** Object-Oriented Programming (Classes, Methods, Encapsulation)  
- **Data Structures:** Lists, Dictionaries  
- **Dependencies:** None (no external libraries required)  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/airline-reservation-system.git
cd airline-reservation-system
```

### 2️⃣ Run the Program  
```bash
python main.py
```

---

## 📚 Example Run  
```
--- Airline Reservation Menu ---
1. Add Flight
2. Book Ticket
3. Cancel Ticket
4. Show Flight Details
5. Print Boarding Pass
6. Exit
```

---

## 🔮 Future Improvements  
- Add file persistence (save/load bookings)  
- Support multiple seat layouts (rows/columns like A/B/C)  
- Passenger & admin login system  
- GUI or web-based version for better UX  

---

✍️ Developed as a **Python OOP practice project** for learning and portfolio building.  
