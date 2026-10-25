
#include <iostream>
#include <iomanip>
#include <string>
#include <limits>
using namespace std;

const int ROADS = 4;

struct Road {
    string name;
    int vehicles;
    int emergency;
    int waitingTime;
};

// Calculate priority using the greedy formula
int calculatePriority(const Road& road) {
    return road.vehicles * 5
         + road.waitingTime * 2
         + road.emergency * 50;
}

// Read and validate integer input
int readNumber(string message, int minimum, int maximum) {
    int value;

    while (true) {
        cout << message;

        if (cin >> value &&
            value >= minimum && value <= maximum) {
            return value;
        }

        cout << "Invalid input. Please try again.\n";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
}

int main() {
    Road roads[ROADS] = {
        {"North", 0, 0, 0},
        {"East", 0, 0, 0},
        {"South", 0, 0, 0},
        {"West", 0, 0, 0}
    };

    cout << "============================================\n";
    cout << " TRAFFIC SIGNAL OPTIMIZATION\n";
    cout << " USING GREEDY ALGORITHM\n";
    cout << "============================================\n\n";

    // Step 1: Take traffic details from the user
    for (int i = 0; i < ROADS; i++) {
        cout << "--- " << roads[i].name << " Road ---\n";

        roads[i].vehicles = readNumber(
            "Waiting vehicles (0-10000): ", 0, 10000);

        roads[i].emergency = readNumber(
            "Emergency vehicles: ", 0, roads[i].vehicles);

        roads[i].waitingTime = readNumber(
            "Accumulated waiting time (0-100000): ",
            0, 100000);

        cout << '\n';
    }

    // Step 2: Display priority of every road
    cout << "\nTRAFFIC PRIORITY TABLE\n";

    cout << left << setw(10) << "Road"
         << setw(12) << "Vehicles"
         << setw(12) << "Emergency"
         << setw(12) << "Wait"
         << setw(12) << "Priority" << '\n';

    cout << string(58, '-') << '\n';

    for (int i = 0; i < ROADS; i++) {
        cout << left << setw(10) << roads[i].name
             << setw(12) << roads[i].vehicles
             << setw(12) << roads[i].emergency
             << setw(12) << roads[i].waitingTime
             << setw(12) << calculatePriority(roads[i])
             << '\n';
    }

    // Step 3: Greedy algorithm selects the highest priority
    int bestRoad = -1;
    int highestPriority = -1;

    for (int i = 0; i < ROADS; i++) {
        if (roads[i].vehicles > 0) {
            int priority = calculatePriority(roads[i]);

            if (priority > highestPriority) {
                highestPriority = priority;
                bestRoad = i;
            }
        }
    }

    // Step 4: Display the selected green signal
    cout << "\n========== GREEDY DECISION ==========\n";

    if (bestRoad == -1) {
        cout << "No vehicles are waiting.\n";
        cout << "No green signal needs to be assigned.\n";
    } else {
        int greenTime = 5 + roads[bestRoad].vehicles * 2;

        if (greenTime > 30) {
            greenTime = 30;
        }

        // Estimate one vehicle passing every 3 seconds
        int vehiclesServed = greenTime / 3;

        if (vehiclesServed > roads[bestRoad].vehicles) {
            vehiclesServed = roads[bestRoad].vehicles;
        }

        cout << "Selected road: "
             << roads[bestRoad].name << '\n';

        cout << "Priority score: "
             << highestPriority << '\n';

        cout << "Green light duration: "
             << greenTime << " seconds\n";

        cout << "Estimated vehicles served: "
             << vehiclesServed << '\n';

        cout << "Vehicles remaining: "
             << roads[bestRoad].vehicles - vehiclesServed
             << '\n';
    }

    // Step 5: Display DAA complexity
    cout << "\n========== DAA ANALYSIS ==========\n";
    cout << "Time Complexity: O(R)\n";
    cout << "Space Complexity: O(R)\n";
    cout << "R = Number of roads (4)\n";

    cout << "\nGreedy Strategy:\n";
    cout << "Select the waiting road with the highest priority.\n";

    cout << "\nThis is an educational traffic simulation.\n";

    return 0;
}
