PLANT_RULES = {

    "aloe_vera": {

        "min_moisture": 20,
        "min_ph": 6.0,
        "max_ph": 7.5

    },

    "tomato": {

        "min_moisture": 50,
        "min_ph": 5.5,
        "max_ph": 6.8

    },

    "rose": {

        "min_moisture": 40,
        "min_ph": 6.0,
        "max_ph": 7.0

    }
}


def get_plant_status(
    plant_type,
    moisture,
    ph
):

    rules = PLANT_RULES[plant_type]

    issues = []

    if moisture < rules["min_moisture"]:

        issues.append(
            "💧 Needs Water"
        )

    if ph < rules["min_ph"]:

        issues.append(
            "🧪 Soil Too Acidic"
        )

    elif ph > rules["max_ph"]:

        issues.append(
            "🧪 Soil Too Alkaline"
        )

    if not issues:

        issues.append(
            "✅ Healthy"
        )

    return issues