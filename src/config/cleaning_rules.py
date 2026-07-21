"""

Smart City Road Accident Analytics
Cleaning Rules Configuration


This file contains all dataset cleaning rules.

Purpose:
- Centralized configuration
- Easy maintenance
- Cleaner.py remains generic
"""


# Missing Value Rules


MISSING_VALUE_RULES = {

    # Numeric Columns
    "estimated_response_time": {
        "method": "business_rule",
        "default": 0
    },

    "driver_age": {
        "method": "median"
    },

    "average_speed": {
        "method": "median"
    },

    "risk_score": {
        "method": "median"
    },

    # Categorical Columns
    "weather_name": {
        "method": "mode"
    },

    "road_quality": {
        "method": "mode"
    },

    "traffic_level": {
        "method": "mode"
    },

    "vehicle_type": {
        "method": "mode"
    },

    "driver_gender": {
        "method": "mode"
    },

    "license_type": {
        "method": "mode"
    },

    "accident_severity": {
        "method": "business_rule",
        "default": "No Accident"
    },

    "property_damage": {
        "method": "business_rule",
        "default": "No"
    }
}



# Duplicate Handling


DUPLICATE_RULES = {

    "remove_duplicates": True

}



# Text Standardization


TEXT_STANDARDIZATION_RULES = {

    "strip_spaces": True,

    "title_case": [

        "state_name",
        "district_name",
        "weather_name",
        "vehicle_name",
        "vehicle_type",
        "road_name",
        "road_quality",
        "traffic_level"

    ],

    "upper_case": [

        "state_id",
        "district_id"

    ]

}



# Data Type Rules


DATA_TYPE_RULES = {

    "record_id": "string",

    "accident_datetime": "datetime",

    "weekday": "string",

    "month": "int",

    "hour": "int",

    "year": "int",

    "driver_age": "int",

    "average_speed": "float",

    "risk_score": "int",

    "estimated_response_time": "float"

}



# Validation Rules

VALIDATION_RULES = {

    "driver_age": {

        "min": 18,

        "max": 100

    },

    "month": {

        "min": 1,

        "max": 12

    },

    "hour": {

        "min": 0,

        "max": 23

    },

    "risk_score": {

        "min": 0,

        "max": 100

    },

    "average_speed": {

        "min": 0,

        "max": 250

    }

}



# Save Options


SAVE_OPTIONS = {

    "index": False,

    "encoding": "utf-8"

}