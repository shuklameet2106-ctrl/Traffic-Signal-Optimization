# 🚦 Traffic Signal Optimization Using Greedy Algorithms

**DAA Mini Project | B.Tech Information Technology | Semester V**

A Python-based traffic simulation that models a four-way intersection and compares two traffic signal control algorithms: **Greedy Algorithm** and **Round-Robin Algorithm**.

## 📌 Project Overview

Traffic congestion is a common problem at road intersections. This project simulates vehicle arrivals and traffic signal operations on four roads — North, South, East, and West — to evaluate the performance of different signal scheduling strategies.

The Greedy Algorithm dynamically selects the road with the highest priority based on queue length, waiting time, and emergency vehicles. The Round-Robin Algorithm selects roads in a fixed circular order.

The project compares both algorithms using traffic performance metrics and graphical visualizations.

## ✨ Features

- 🚗 Dynamic vehicle arrival simulation.
- 🚦 Four-way traffic intersection (North, South, East, West).
- 🧠 Greedy-based traffic signal selection.
- 🔄 Fixed Round-Robin scheduling.
- 🚑 Priority consideration for emergency vehicles.
- ⏱️ Average and maximum vehicle waiting time calculation.
- 📊 Comparison of vehicles served and vehicles remaining.
- 📈 Traffic density graphs for individual algorithms.
- 📉 Graphical performance comparison of both algorithms.
- 🎮 Interactive command-line menu.
- 🔁 Reproducible algorithm comparison using a fixed random seed.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Structures:** Queue, Deque
- **Algorithms:** Greedy Algorithm, Round-Robin Scheduling
- **Libraries:** `random`, `time`, `collections`, `matplotlib`

## ⚙️ Algorithm Explanation

### 1. Greedy Algorithm

The Greedy Algorithm selects the road with the highest calculated priority at each simulation step.

The priority score is calculated as:

```text
Priority =
    (Queue Length × 10)
    + (Total Waiting Time × 0.5)
    + (Emergency Vehicle Count × 100)
```

**Selection criteria:**
1. Emergency vehicles increase a road's priority.
2. Roads with longer queues receive higher priority.
3. Waiting time contributes to the priority score.
4. The road with the highest priority is selected for the green signal.

This approach aims to reduce traffic waiting time by dynamically responding to traffic conditions.

### 2. Round-Robin Algorithm

The Round-Robin Algorithm selects the next road in a fixed circular order:

```text
North → South → East → West → North
```

The algorithm skips roads with empty queues and selects the next road that has waiting vehicles.

Unlike the Greedy Algorithm, it does not calculate a priority score for each road.

## 🔬 Simulation Parameters

| Parameter | Value |
|---|---|
| Number of roads | 4 |
| Default simulation steps | 100 |
| Green signal duration | 10 time units |
| Maximum vehicles per arrival event | 5 |
| Maximum vehicles served per signal turn | 5 |
| Emergency vehicle probability | 5% per generated vehicle |
| Traffic arrival | Random |
| Comparison seed | 42 |

Each road has its own probability of receiving traffic:

| Road | Arrival Probability |
|---|---:|
| North | 65% |
| South | 55% |
| East | 75% |
| West | 45% |

## 📊 Performance Metrics

The program compares the following metrics:

- **Vehicles Arrived:** Total number of vehicles generated during the simulation.
- **Vehicles Served:** Total number of vehicles that passed through the intersection.
- **Vehicles Remaining:** Number of vehicles still waiting at the end.
- **Average Waiting Time:** Average waiting time of served vehicles.
- **Maximum Waiting Time:** Highest recorded waiting time among served vehicles.

These metrics help evaluate the performance of the two scheduling algorithms.

## 📈 Graphical Visualizations

### Traffic Density Graph

Displays the number of waiting vehicles on each road across simulation steps.

### Algorithm Comparison Graph

Compares Greedy and Round-Robin using four bar charts:

- Vehicles Served
- Average Waiting Time
- Maximum Waiting Time
- Vehicles Remaining

## 📁 Project Structure

```text
Traffic-Signal-Optimization/
│
├── traffic_signal_optimization.py
└── README.md
```

## 🚀 Installation and Execution

### Prerequisites

Install Python 3.9 or later and ensure that `pip` is available.

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/Traffic-Signal-Optimization.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Traffic-Signal-Optimization
```

### Step 3: Install the Required Library

```bash
pip install matplotlib
```

### Step 4: Run the Program

```bash
python traffic_signal_optimization.py
```

## 🖥️ Program Menu

After running the program, the following interactive menu appears:

```text
============================================================
 TRAFFIC SIGNAL OPTIMIZATION USING GREEDY ALGORITHMS
============================================================
1. Run Greedy Algorithm
2. Run Round-Robin Algorithm
3. Compare Both Algorithms
4. Display Traffic Density Graph
5. Exit
============================================================
Enter your choice (1-5):
```

Choose an option by entering a number from 1 to 5.

| Option | Description |
|---|---|
| 1 | Run the Greedy Algorithm |
| 2 | Run the Round-Robin Algorithm |
| 3 | Compare both algorithms and display graphs |
| 4 | Display the Greedy traffic density graph |
| 5 | Exit the program |

## 🧪 Example Output

The comparison option displays a table similar to the following:

```text
ALGORITHM PERFORMANCE COMPARISON

Metric                      Greedy              Round-Robin
----------------------------------------------------------------
Vehicles Arrived            ...
Vehicles Served             ...
Vehicles Remaining          ...
Average Waiting Time        ...
Maximum Waiting Time        ...
----------------------------------------------------------------
```

The actual results depend on the simulation parameters and the generated traffic. During algorithm comparison, both algorithms use the same random seed to make the comparison reproducible.

## 🎯 Objectives

- Understand and implement the Greedy Algorithm.
- Apply queue-based data structures to a traffic simulation.
- Implement Round-Robin scheduling.
- Analyze algorithm performance using measurable metrics.
- Visualize traffic density and algorithm comparisons.
- Understand how algorithm selection can affect waiting time and traffic flow.

## 🔮 Future Enhancements

- Integrate real-time traffic data.
- Develop a graphical user interface.
- Add pedestrian crossing management.
- Introduce adaptive green signal durations.
- Implement vehicle detection using computer vision.
- Add a more advanced emergency vehicle prioritization system.
- Test additional scheduling algorithms.
- Evaluate performance across multiple random traffic scenarios.

## ⚠️ Limitations

- This project is a simulation and does not control real traffic signals.
- Vehicle arrivals are randomly generated.
- The simulation uses simplified vehicle-serving rules.
- The Greedy Algorithm does not guarantee a globally optimal solution.
- The results may vary when traffic conditions or simulation parameters change.
- The model does not account for real-world road geometry, vehicle speed, or pedestrian traffic.

## 🏁 Conclusion

The Traffic Signal Optimization project demonstrates how algorithmic strategies can be applied to traffic signal scheduling. By comparing a priority-based Greedy Algorithm with fixed Round-Robin scheduling, the simulation provides insights into vehicle throughput, queue lengths, and waiting times.

The project illustrates the practical application of algorithm design and analysis concepts in solving a simplified real-world traffic management problem.

## 👨‍💻 Author

**Meet Shukla**

B.Tech Information Technology — Semester V

A.D. Patel Institute of Technology (ADIT)

---

**Academic Project:** Design and Analysis of Algorithms (DAA)
