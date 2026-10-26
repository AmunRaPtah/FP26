"""Helper functions for the FP26 project.

All data handling lives here, so the Quarto document stays readable.
"""

import csv


def read_vitals(path):
    """Read the vital-sign table from a CSV file.

    Returns a list of dictionaries, one per measurement, with the
    numeric columns converted to float.
    """
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        return [
            {
                "patient": row["patient"],
                "hour": float(row["hour"]),
                "heart_rate": float(row["heart_rate"]),
                "systolic": float(row["systolic"]),
            }
            for row in reader
        ]


def summarize(values):
    """Return the count, mean, minimum and maximum of a numeric list."""
    ordered = sorted(values)
    return {
        "n": len(ordered),
        "mean": sum(ordered) / len(ordered),
        "min": ordered[0],
        "max": ordered[-1],
    }


def by_patient(rows):
    """Group a list of measurements by patient id.

    Returns a dict mapping patient id to the list of that patient's rows.
    """
    groups = {}
    for row in rows:
        groups.setdefault(row["patient"], []).append(row)
    return groups


def plot_heart_rate(rows, path):
    """Plot heart rate over time, one line per patient, and save the figure."""
    import matplotlib.pyplot as plt

    figure, axis = plt.subplots(figsize=(7, 3.5))
    for patient, patient_rows in sorted(by_patient(rows).items()):
        patient_rows.sort(key=lambda r: r["hour"])
        axis.plot(
            [r["hour"] for r in patient_rows],
            [r["heart_rate"] for r in patient_rows],
            marker="o",
            label=patient,
        )
    axis.set_xlabel("Hour")
    axis.set_ylabel("Heart rate (bpm)")
    axis.set_title("Heart rate over the first 12 hours")
    axis.legend(frameon=False)
    figure.tight_layout()
    figure.savefig(path, dpi=150)
    return figure
