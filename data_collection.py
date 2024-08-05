from estimators import generate_serial_numbers, maximum_likelihood_estimation
import pandas as pd


parameters = [
    {
        "min_total_tanks": 100,
        "max_total_tanks": 10001,
        "step": 50,
        "num_serials": 10,
        "seed": "Testing",
    },
]


def main():
    for params in parameters:
        df = pd.DataFrame()
        df["Seed"] = None
        df["Total Tanks"] = None
        df["Amount of Serial Numbers"] = None
        df["Estimation"] = None

        for total_tanks in range(params["min_total_tanks"], params["max_total_tanks"], params["step"]):
            serial_numbers = generate_serial_numbers(total_tanks, params["num_serials"], params["seed"])
            estimation = maximum_likelihood_estimation(serial_numbers)
            df = df.append({
                "Seed": params["seed"],
                "Total Tanks": total_tanks,
                "Amount of Serial Numbers": params["num_serials"],
                "Estimation": estimation,
            },
                ignore_index=True)

        df.to_csv("data/MLE.csv", index=False)


if __name__ == "__main__":
    main()
