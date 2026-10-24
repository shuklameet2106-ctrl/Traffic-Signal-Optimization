import random
import time
from collections import deque
import matplotlib.pyplot as plt


# ============================================================
# TRAFFIC SIGNAL OPTIMIZATION USING GREEDY ALGORITHMS
# DAA Mini Project - B.Tech IT, Semester V
# ============================================================

DIRECTIONS = ["North", "South", "East", "West"]

GREEN_LIGHT_DURATION = 10
SIMULATION_STEPS = 100
MAX_ARRIVAL_RATE = 5


# ============================================================
# VEHICLE CLASS
# ============================================================

class Vehicle:
    def __init__(self, arrival_time, emergency=False):
        self.arrival_time = arrival_time
        self.emergency = emergency
        self.waiting_time = 0

    def __str__(self):
        if self.emergency:
            return "Emergency Vehicle"
        return "Normal Vehicle"


# ============================================================
# TRAFFIC ROAD CLASS
# ============================================================

class Road:
    def __init__(self, name):
        self.name = name
        self.vehicles = deque()
        self.total_vehicles = 0
        self.vehicles_served = 0
        self.total_waiting_time = 0
        self.maximum_waiting_time = 0
        self.green_time = 0

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        self.total_vehicles += 1

    def get_queue_length(self):
        return len(self.vehicles)

    def has_emergency_vehicle(self):
        return any(vehicle.emergency for vehicle in self.vehicles)

    def get_priority(self):
        """
        Greedy priority:
        1. Emergency vehicles receive the highest priority.
        2. Longer queues receive higher priority.
        3. Waiting time contributes to the priority.
        """
        if not self.vehicles:
            return 0

        emergency_count = sum(
            1 for vehicle in self.vehicles
            if vehicle.emergency
        )

        total_waiting = sum(
            vehicle.waiting_time for vehicle in self.vehicles
        )

        priority = (
            len(self.vehicles) * 10
            + total_waiting * 0.5
            + emergency_count * 100
        )

        return priority

    def serve_vehicles(self, current_time, maximum_vehicles=5):
        served = []

        for _ in range(min(maximum_vehicles, len(self.vehicles))):
            vehicle = self.vehicles.popleft()

            vehicle.waiting_time = (
                current_time - vehicle.arrival_time
            )

            self.total_waiting_time += vehicle.waiting_time

            self.maximum_waiting_time = max(
                self.maximum_waiting_time,
                vehicle.waiting_time
            )

            self.vehicles_served += 1
            served.append(vehicle)

        self.green_time += GREEN_LIGHT_DURATION

        return served


# ============================================================
# TRAFFIC INTERSECTION CLASS
# ============================================================

class TrafficIntersection:
    def __init__(self, algorithm="greedy"):
        self.roads = {
            direction: Road(direction)
            for direction in DIRECTIONS
        }

        self.algorithm = algorithm
        self.current_time = 0
        self.current_green_road = None

        self.history = {
            direction: []
            for direction in DIRECTIONS
        }

        self.waiting_history = []
        self.served_history = []
        self.signal_history = []

    def generate_vehicles(self):
        """
        Generate a random number of arriving vehicles.
        Each road has a different probability of receiving traffic.
        """
        arrival_probabilities = {
            "North": 0.65,
            "South": 0.55,
            "East": 0.75,
            "West": 0.45
        }

        for direction in DIRECTIONS:
            if random.random() < arrival_probabilities[direction]:
                number_of_vehicles = random.randint(
                    1, MAX_ARRIVAL_RATE
                )

                for _ in range(number_of_vehicles):
                    emergency = random.random() < 0.05

                    vehicle = Vehicle(
                        arrival_time=self.current_time,
                        emergency=emergency
                    )

                    self.roads[direction].add_vehicle(vehicle)

    def update_waiting_times(self):
        for road in self.roads.values():
            for vehicle in road.vehicles:
                vehicle.waiting_time += 1

    def select_greedy_road(self):
        """
        Greedy strategy:
        Select the road having the highest priority.
        """
        active_roads = [
            road for road in self.roads.values()
            if road.get_queue_length() > 0
        ]

        if not active_roads:
            return None

        selected_road = max(
            active_roads,
            key=lambda road: road.get_priority()
        )

        return selected_road

    def select_round_robin_road(self):
        """
        Fixed Round-Robin strategy:
        Select the next road in a predefined circular order.
        """
        if self.current_green_road is None:
            start_index = -1
        else:
            start_index = DIRECTIONS.index(
                self.current_green_road
            )

        for offset in range(1, len(DIRECTIONS) + 1):
            index = (start_index + offset) % len(DIRECTIONS)
            direction = DIRECTIONS[index]

            if self.roads[direction].get_queue_length() > 0:
                return self.roads[direction]

        return None

    def select_road(self):
        if self.algorithm == "greedy":
            return self.select_greedy_road()

        return self.select_round_robin_road()

    def record_statistics(self):
        total_waiting = sum(
            sum(vehicle.waiting_time for vehicle in road.vehicles)
            for road in self.roads.values()
        )

        total_served = sum(
            road.vehicles_served
            for road in self.roads.values()
        )

        self.waiting_history.append(total_waiting)
        self.served_history.append(total_served)

        for direction in DIRECTIONS:
            self.history[direction].append(
                self.roads[direction].get_queue_length()
            )

    def run_step(self, display=True):
        self.generate_vehicles()
        self.update_waiting_times()

        selected_road = self.select_road()

        if selected_road:
            self.current_green_road = selected_road.name

            served = selected_road.serve_vehicles(
                self.current_time,
                maximum_vehicles=5
            )

            self.signal_history.append(selected_road.name)

            if display:
                print(
                    f"Time {self.current_time:03d}: "
                    f"GREEN -> {selected_road.name:5s} | "
                    f"Served: {len(served)} | "
                    f"Remaining queue: "
                    f"{selected_road.get_queue_length()}"
                )
        else:
            if display:
                print(
                    f"Time {self.current_time:03d}: "
                    "No vehicles waiting."
                )

            self.signal_history.append("None")

        self.record_statistics()
        self.current_time += 1

    def run_simulation(self, steps=SIMULATION_STEPS, display=True):
        if display:
            print("\nStarting Traffic Simulation")
            print("=" * 65)
            print(f"Algorithm: {self.algorithm.upper()}")
            print(f"Simulation Steps: {steps}")
            print("=" * 65)

        for _ in range(steps):
            self.run_step(display=display)

        if display:
            self.display_results()

    def get_statistics(self):
        total_arrived = sum(
            road.total_vehicles for road in self.roads.values()
        )

        total_served = sum(
            road.vehicles_served for road in self.roads.values()
        )

        total_waiting = sum(
            road.total_waiting_time for road in self.roads.values()
        )

        remaining = sum(
            road.get_queue_length() for road in self.roads.values()
        )

        average_waiting = (
            total_waiting / total_served
            if total_served else 0
        )

        maximum_waiting = max(
            (road.maximum_waiting_time
             for road in self.roads.values()),
            default=0
        )

        return {
            "algorithm": self.algorithm,
            "total_arrived": total_arrived,
            "total_served": total_served,
            "remaining": remaining,
            "average_waiting": average_waiting,
            "maximum_waiting": maximum_waiting,
            "total_waiting": total_waiting
        }

    def display_results(self):
        stats = self.get_statistics()

        print("\nSIMULATION RESULTS")
        print("=" * 65)

        print(f"Algorithm              : {stats['algorithm'].upper()}")
        print(f"Total Vehicles Arrived : {stats['total_arrived']}")
        print(f"Total Vehicles Served  : {stats['total_served']}")
        print(f"Vehicles Still Waiting : {stats['remaining']}")

        print(
            f"Average Waiting Time   : "
            f"{stats['average_waiting']:.2f} time units"
        )

        print(
            f"Maximum Waiting Time   : "
            f"{stats['maximum_waiting']} time units"
        )

        print("\nROAD-WISE STATISTICS")
        print("-" * 65)

        for direction in DIRECTIONS:
            road = self.roads[direction]

            print(
                f"{direction:7s} | "
                f"Arrived: {road.total_vehicles:4d} | "
                f"Served: {road.vehicles_served:4d} | "
                f"Queue: {road.get_queue_length():4d} | "
                f"Green Time: {road.green_time}"
            )

        print("=" * 65)


# ============================================================
# PERFORMANCE COMPARISON
# ============================================================

def compare_algorithms(steps=SIMULATION_STEPS):
    print("\nRunning algorithm comparison...")

    # Use the same random seed for reproducibility.
    random.seed(42)

    greedy_simulation = TrafficIntersection("greedy")
    greedy_simulation.run_simulation(steps, display=False)

    random.seed(42)

    round_robin_simulation = TrafficIntersection("round_robin")
    round_robin_simulation.run_simulation(steps, display=False)

    greedy = greedy_simulation.get_statistics()
    round_robin = round_robin_simulation.get_statistics()

    print("\nALGORITHM PERFORMANCE COMPARISON")
    print("=" * 75)

    print(
        f"{'Metric':28s}"
        f"{'Greedy':20s}"
        f"{'Round-Robin':20s}"
    )

    print("-" * 75)

    metrics = [
        ("Vehicles Arrived", "total_arrived"),
        ("Vehicles Served", "total_served"),
        ("Vehicles Remaining", "remaining"),
        ("Average Waiting Time", "average_waiting"),
        ("Maximum Waiting Time", "maximum_waiting")
    ]

    for label, key in metrics:
        greedy_value = greedy[key]
        round_value = round_robin[key]

        if isinstance(greedy_value, float):
            greedy_text = f"{greedy_value:.2f}"
            round_text = f"{round_value:.2f}"
        else:
            greedy_text = str(greedy_value)
            round_text = str(round_value)

        print(
            f"{label:28s}"
            f"{greedy_text:20s}"
            f"{round_text:20s}"
        )

    print("=" * 75)

    if greedy["average_waiting"] < round_robin["average_waiting"]:
        print("Greedy has lower average waiting time in this run.")
    elif greedy["average_waiting"] > round_robin["average_waiting"]:
        print("Round-Robin has lower average waiting time in this run.")
    else:
        print("Both algorithms have equal average waiting time.")

    return greedy_simulation, round_robin_simulation


# ============================================================
# VISUALIZATION
# ============================================================

def plot_traffic_density(simulation):
    plt.figure(figsize=(10, 6))

    for direction in DIRECTIONS:
        plt.plot(
            range(len(simulation.history[direction])),
            simulation.history[direction],
            label=direction
        )

    plt.title(
        f"Traffic Queue Length - "
        f"{simulation.algorithm.upper()} Algorithm"
    )

    plt.xlabel("Simulation Step")
    plt.ylabel("Number of Waiting Vehicles")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_algorithm_comparison(greedy_sim, round_robin_sim):
    greedy = greedy_sim.get_statistics()
    round_robin = round_robin_sim.get_statistics()

    metrics = [
        ("Vehicles Served", "total_served"),
        ("Average Waiting Time", "average_waiting"),
        ("Maximum Waiting Time", "maximum_waiting"),
        ("Vehicles Remaining", "remaining")
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for index, (label, key) in enumerate(metrics):
        values = [greedy[key], round_robin[key]]

        axes[index].bar(
            ["Greedy", "Round-Robin"],
            values
        )

        axes[index].set_title(label)
        axes[index].set_ylabel("Value")
        axes[index].grid(axis="y", alpha=0.3)

    fig.suptitle("Traffic Signal Algorithm Comparison")
    plt.tight_layout()
    plt.show()


# ============================================================
# INTERACTIVE MENU
# ============================================================

def main():
    while True:
        print("\n")
        print("=" * 60)
        print(" TRAFFIC SIGNAL OPTIMIZATION USING GREEDY ALGORITHMS")
        print("=" * 60)
        print("1. Run Greedy Algorithm")
        print("2. Run Round-Robin Algorithm")
        print("3. Compare Both Algorithms")
        print("4. Display Traffic Density Graph")
        print("5. Exit")
        print("=" * 60)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                steps = int(
                    input("Enter simulation steps (default 100): ")
                    or SIMULATION_STEPS
                )

                if steps <= 0:
                    print("Please enter a positive number.")
                    continue

                simulation = TrafficIntersection("greedy")
                simulation.run_simulation(steps)

                show_graph = input(
                    "Display traffic density graph? (y/n): "
                ).strip().lower()

                if show_graph == "y":
                    plot_traffic_density(simulation)

            except ValueError:
                print("Invalid input. Enter a whole number.")

        elif choice == "2":
            try:
                steps = int(
                    input("Enter simulation steps (default 100): ")
                    or SIMULATION_STEPS
                )

                if steps <= 0:
                    print("Please enter a positive number.")
                    continue

                simulation = TrafficIntersection("round_robin")
                simulation.run_simulation(steps)

                show_graph = input(
                    "Display traffic density graph? (y/n): "
                ).strip().lower()

                if show_graph == "y":
                    plot_traffic_density(simulation)

            except ValueError:
                print("Invalid input. Enter a whole number.")

        elif choice == "3":
            try:
                steps = int(
                    input("Enter simulation steps (default 100): ")
                    or SIMULATION_STEPS
                )

                if steps <= 0:
                    print("Please enter a positive number.")
                    continue

                greedy_sim, round_sim = compare_algorithms(steps)

                plot_algorithm_comparison(greedy_sim, round_sim)

            except ValueError:
                print("Invalid input. Enter a whole number.")

        elif choice == "4":
            simulation = TrafficIntersection("greedy")
            simulation.run_simulation(
                SIMULATION_STEPS,
                display=False
            )

            plot_traffic_density(simulation)

        elif choice == "5":
            print("Thank you for using the Traffic Simulator!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()