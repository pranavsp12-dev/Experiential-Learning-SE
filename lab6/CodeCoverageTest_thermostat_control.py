
from thermostat_control import target_temperature, hvac_action, energy_alert


# Tests for target_temperature()

def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_before_6():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_after_22():
    assert target_temperature("sleep", True, 23) == 18


def test_sleep_during_day():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("normal", False, 12) == 18


def test_morning():
    assert target_temperature("normal", True, 7) == 22


def test_evening():
    assert target_temperature("normal", True, 18) == 21


def test_normal_daytime():
    assert target_temperature("normal", True, 12) == 20


# Tests for hvac_action()

def test_hvac_idle():
    assert hvac_action(20, 20, 10) == "idle"


def test_hvac_heat_boost():
    assert hvac_action(18, 22, 4) == "heat_boost"


def test_hvac_heat():
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_cool_boost():
    assert hvac_action(24, 20, 35) == "cool_boost"


def test_hvac_cool():
    assert hvac_action(24, 20, 25) == "cool"


# Tests for energy_alert()

def test_energy_no_readings():
    assert energy_alert([], 10) == "ok"


def test_energy_all_within_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"


def test_energy_warning():
    assert energy_alert([12, 8], 10) == "warning"


def test_energy_critical():
    assert energy_alert([12, 15, 20], 10) == "critical"
