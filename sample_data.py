import os
import pandas as pd


def generate_sample_data():

    base_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "data"
    )

    print("Looking for CSV files in:", base_path)

    patients = pd.read_csv(os.path.join(base_path, "patients.csv"))
    visits = pd.read_csv(os.path.join(base_path, "visits.csv"))
    admissions = pd.read_csv(os.path.join(base_path, "admissions.csv"))
    doctors = pd.read_csv(os.path.join(base_path, "doctors.csv"))
    lab_tests = pd.read_csv(os.path.join(base_path, "lab_tests.csv"))
    prescriptions = pd.read_csv(os.path.join(base_path, "prescriptions.csv"))
    staff = pd.read_csv(os.path.join(base_path, "staff.csv"))

    return {
        "patients": patients,
        "visits": visits,
        "admissions": admissions,
        "doctors": doctors,
        "lab_tests": lab_tests,
        "prescriptions": prescriptions,
        "staff": staff
    }