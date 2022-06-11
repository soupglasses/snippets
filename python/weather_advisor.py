"""
A simple program to tell you how many breaks you need with current weather conditions.
"""
from dataclasses import dataclass


@dataclass
class Weather:
    "Simple weather information dataclass"
    temp: float  # between -10 to 125
    humidity: float  # 0 to 1
    weather: str  # sunny, cloudy, or raining


rules = (
    (lambda _: "Work inside" if _.weather == "raining" else None),
    (
        lambda _: (
            (
                lambda _: "Two 15 minute breaks"
                if _.humidity >= 0.8 and _.weather == "sunny"
                else None
            ),
            (
                lambda _: "One 15 minute break"
                if _.humidity > 0.9 and _.weather == "cloudy"
                else None
            ),
            "One 10 minute break",
        )
        if _.temp >= 90
        else None
    ),
    (
        lambda _: "Two 10 minute breaks"
        if 80 < _.temp < 90 and _.humidity > 0.9 and _.weather == "sunny"
        else None
    ),
    (
        lambda _: "One 10 minute break"
        if 80 < _.temp < 90 and (_.humidity > 0.9 or _.weather == "sunny")
        else None
    ),
    "No extra breaks",
)


def apply_rules(ruleset, data):
    if ruleset is None:
        return None
    if isinstance(ruleset, str):
        return ruleset
    if callable(ruleset):
        return ruleset(data)
    if isinstance(ruleset, (tuple, list)):
        return apply_rules(
            next((_ for rule in ruleset if (_ := apply_rules(rule, data))), None), data
        )

    raise Exception(f"Could not handle rule: {ruleset!r}")


if __name__ == "__main__":
    datapoints = [
        Weather(temp=125, humidity=1.0, weather="sunny"),
        Weather(temp=87, humidity=1.0, weather="sunny"),
        Weather(temp=65, humidity=1.0, weather="sunny"),
    ]
    for dp in datapoints:
        print(dp, apply_rules(rules, dp))
