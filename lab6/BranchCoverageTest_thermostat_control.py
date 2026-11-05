
from thermostat_control import target_temperature, hvac_action, energy_alert


# target_temperature() branch coverage

def test_away_branch():
    assert target_temperature("away", True, 12) == 16


def test_sleep_before_6():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_daytime():
    assert target_temperature("sleep", True, 12) == 20


def test_sleep_after_22():
    assert target_temperature("sleep", True, 22) == 18


def test_unoccupied_branch():
    assert target_temperature("normal", False, 12) == 18


def test_morning_true():
    assert target_temperature("normal", True, 7) == 22


def test_morning_lower_boundary():
    assert target_temperature("normal", True, 6) == 22


def test_morning_false():
    assert target_temperature("normal", True, 9) == 20


def test_evening_true():
    assert target_temperature("normal", True, 18) == 21


def test_evening_lower_boundary():
    assert target_temperature("normal", True, 17) == 21


def test_evening_false():
    assert target_temperature("normal", True, 22) == 20


# hvac_action() branch coverage

def test_idle_branch():
    assert hvac_action(20, 20.5, 10) == "idle"


def test_idle_boundary():
    assert hvac_action(20, 21, 10) == "heat"


def test_heat_boost_branch():
    assert hvac_action(18, 22, 4) == "heat_boost"


def test_heat_normal_branch():
    assert hvac_action(18, 22, 5) == "heat"


def test_cool_boost_branch():
    assert hvac_action(24, 20, 31) == "cool_boost"


def test_cool_normal_branch():
    assert hvac_action(24, 20, 30) == "cool"


# energy_alert() branch coverage

def test_empty_readings():
    assert energy_alert([], 10) == "ok"


def test_no_reading_exceeds_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"


def test_reading_exceeds_limit():
    assert energy_alert([12, 8], 10) == "warning"


def test_exactly_half_exceed_limit():
    assert energy_alert([12, 8, 9, 10], 10) == "warning"


def test_more_than_half_exceed_limit():
    assert energy_alert([12, 15, 20], 10) == "critical"


def test_all_readings_equal_limit():
    assert energy_alert([10, 10, 10], 10) == "ok"

