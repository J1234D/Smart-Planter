def get_plant_status(moisture, ph):
    issues = []

    if moisture < 30:
        issues.append("💧 Needs Water")

    if ph < 5.5:
        issues.append("🧪 Soil Too Acidic")

    elif ph > 7.5:
        issues.append("🧪 Soil Too Alkaline")

    if not issues:
        issues.append("✅ Healthy")

    return issues