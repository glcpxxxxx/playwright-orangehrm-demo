import json
import pytest
import random
from pathlib import Path

def get_valid_json_data() -> list:
    with open("./test_data/valid_data.json") as file:
        json_data = json.load(file)

    params = []
    for entry in json_data:
        if entry["expected"] == "success":
            # Mark this param as the dependency "valid_login"
            params.append(pytest.param(
                entry["username"],
                entry["password"],
                entry["expected"],
                marks=pytest.mark.depends(name="valid_login", scope="session")
            ))
        else:
            params.append((entry["username"], entry["password"], entry["expected"]))

    return params

def get_invalid_json_data() -> list:
    with open("./test_data/invalid_data.json") as file:
        json_data = json.load(file)
        
    # Convert list of dicts to list of tuples for pytest parametrize
    return [(entry["username"], entry["password"],entry["expected"]) for entry in json_data]

def get_existing_employee_name_json():
    with open("./test_data/existing_employee.json") as file:
        json_data = json.load(file)
    return [{"employee": entry["employee"], "expected": entry["expected"]} for entry in json_data]

def get_partial_days_json():
    with open("./test_data/partial_days.json") as file:
        partial_days = json.load(file)
    return partial_days

def get_leave_type_json():
    with open("./test_data/leave_type.json") as file:
        leavetype = json.load(file)
    return leavetype

def get_leave_duration_json():
    with open("./test_data/leave_duration.json") as file:
        leave_duration = json.load(file)
    return leave_duration

def get_claim_events_json():
    with open("./test_data/claim_events.json") as file:
        claim_events = json.load(file)
    return claim_events

def get_currency_json():
    with open("./test_data/currency.json") as file:
        currency = json.load(file)
        return currency

def get_job_title_json():
    with open("./test_data/job_titles.json") as file:
        job_title = json.load(file)
        return job_title
    
def get_hiring_manager_json():
    with open("./test_data/hiring_managers.json") as file:
        hiring_manager = json.load(file)
        return hiring_manager

# methods to get random value from different functions
def get_random_employee() -> dict:
    #Return one random employee from JSON."""
    return random.choice(get_existing_employee_name_json())

def get_random_leave_type() -> dict:
    #Return one random leave type from JSON."""
    return random.choice(get_leave_type_json())
 
def get_random_partial_days() -> dict:
    #Return one value partial day from JSON."""
    return random.choice(get_partial_days_json())
        
def get_random_leave_duration():
    #Return one random duration from JSON."""
    return random.choice(get_leave_duration_json())
    
def get_random_event_type():
    #Return one random event type from JSON."""
    return random.choice(get_claim_events_json())
    
def get_random_currency():
    #Return one random currency type from JSON."""
    return random.choice(get_currency_json())

def get_random_job_title():
    #Return one random job title type from JSON."""
    return random.choice(get_job_title_json())

def get_random_hiring_manager():
    return random.choice(get_hiring_manager_json())