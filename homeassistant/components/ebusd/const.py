"""Constants for ebus component."""
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPressure,
    UnitOfTemperature,
    UnitOfTime,
)

DOMAIN = "ebusd"

#  SensorTypes from ebusdpy module :
#  0='decimal', 1='time-schedule', 2='switch', 3='string', 4='value;status'

SENSOR_TYPES = {
    "700": {
        "ActualFlowTemperatureDesired": [
            "Hc1ActualFlowTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "MaxFlowTemperatureDesired": [
            "Hc1MaxFlowTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "MinFlowTemperatureDesired": [
            "Hc1MinFlowTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "PumpStatus": ["Hc1PumpStatus", None, "mdi:toggle-switch", 2, None],
        "HCSummerTemperatureLimit": [
            "Hc1SummerTempLimit",
            UnitOfTemperature.CELSIUS,
            "mdi:weather-sunny",
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "HolidayTemperature": [
            "HolidayTemp",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "HWTemperatureDesired": [
            "HwcTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "HWActualTemperature": [
            "HwcStorageTemp",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "HWTimerMonday": ["hwcTimer.Monday", None, "mdi:timer-outline", 1, None],
        "HWTimerTuesday": ["hwcTimer.Tuesday", None, "mdi:timer-outline", 1, None],
        "HWTimerWednesday": ["hwcTimer.Wednesday", None, "mdi:timer-outline", 1, None],
        "HWTimerThursday": ["hwcTimer.Thursday", None, "mdi:timer-outline", 1, None],
        "HWTimerFriday": ["hwcTimer.Friday", None, "mdi:timer-outline", 1, None],
        "HWTimerSaturday": ["hwcTimer.Saturday", None, "mdi:timer-outline", 1, None],
        "HWTimerSunday": ["hwcTimer.Sunday", None, "mdi:timer-outline", 1, None],
        "HWOperativeMode": ["HwcOpMode", None, "mdi:math-compass", 3, None],
        "WaterPressure": [
            "WaterPressure",
            UnitOfPressure.BAR,
            "mdi:water-pump",
            0,
            SensorDeviceClass.PRESSURE,
        ],
        "Zone1RoomZoneMapping": ["z1RoomZoneMapping", None, "mdi:label", 0, None],
        "Zone1NightTemperature": [
            "z1NightTemp",
            UnitOfTemperature.CELSIUS,
            "mdi:weather-night",
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "Zone1DayTemperature": [
            "z1DayTemp",
            UnitOfTemperature.CELSIUS,
            "mdi:weather-sunny",
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "Zone1HolidayTemperature": [
            "z1HolidayTemp",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "Zone1RoomTemperature": [
            "z1RoomTemp",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "Zone1ActualRoomTemperatureDesired": [
            "z1ActualRoomTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "Zone1TimerMonday": ["z1Timer.Monday", None, "mdi:timer-outline", 1, None],
        "Zone1TimerTuesday": ["z1Timer.Tuesday", None, "mdi:timer-outline", 1, None],
        "Zone1TimerWednesday": [
            "z1Timer.Wednesday",
            None,
            "mdi:timer-outline",
            1,
            None,
        ],
        "Zone1TimerThursday": ["z1Timer.Thursday", None, "mdi:timer-outline", 1, None],
        "Zone1TimerFriday": ["z1Timer.Friday", None, "mdi:timer-outline", 1, None],
        "Zone1TimerSaturday": ["z1Timer.Saturday", None, "mdi:timer-outline", 1, None],
        "Zone1TimerSunday": ["z1Timer.Sunday", None, "mdi:timer-outline", 1, None],
        "Zone1OperativeMode": ["z1OpMode", None, "mdi:math-compass", 3, None],
        "ContinuosHeating": [
            "ContinuosHeating",
            UnitOfTemperature.CELSIUS,
            "mdi:weather-snowy",
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "PowerEnergyConsumptionLastMonth": [
            "PrEnergySumHcLastMonth",
            UnitOfEnergy.KILO_WATT_HOUR,
            "mdi:flash",
            0,
            SensorDeviceClass.ENERGY,
        ],
        "PowerEnergyConsumptionThisMonth": [
            "PrEnergySumHcThisMonth",
            UnitOfEnergy.KILO_WATT_HOUR,
            "mdi:flash",
            0,
            SensorDeviceClass.ENERGY,
        ],
    },
    "ehp": {
        "HWTemperature": [
            "HwcTemp",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
        "OutsideTemp": [
            "OutsideTemp",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
    },
    "bai": {
        "HotWaterTemperature": [
            "HwcTemp",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
        "StorageTemperature": [
            "StorageTemp",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
        "DesiredStorageTemperature": [
            "StorageTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "OutdoorsTemperature": [
            "OutdoorstempSensor",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
        "WaterPressure": [
            "WaterPressure",
            UnitOfPressure.BAR,
            "mdi:pipe",
            4,
            SensorDeviceClass.PRESSURE,
        ],
        "AverageIgnitionTime": [
            "averageIgnitiontime",
            UnitOfTime.SECONDS,
            "mdi:av-timer",
            0,
            SensorDeviceClass.DURATION,
        ],
        "MaximumIgnitionTime": [
            "maxIgnitiontime",
            UnitOfTime.SECONDS,
            "mdi:av-timer",
            0,
            SensorDeviceClass.DURATION,
        ],
        "MinimumIgnitionTime": [
            "minIgnitiontime",
            UnitOfTime.SECONDS,
            "mdi:av-timer",
            0,
            SensorDeviceClass.DURATION,
        ],
        "ReturnTemperature": [
            "ReturnTemp",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
        "CentralHeatingPump": ["WP", None, "mdi:toggle-switch", 2, None],
        "HeatingSwitch": ["HeatingSwitch", None, "mdi:toggle-switch", 2, None],
        "DesiredFlowTemperature": [
            "FlowTempDesired",
            UnitOfTemperature.CELSIUS,
            None,
            0,
            SensorDeviceClass.TEMPERATURE,
        ],
        "FlowTemperature": [
            "FlowTemp",
            UnitOfTemperature.CELSIUS,
            None,
            4,
            SensorDeviceClass.TEMPERATURE,
        ],
        "Flame": ["Flame", None, "mdi:toggle-switch", 2, None],
        "PowerEnergyConsumptionHeatingCircuit": [
            "PrEnergySumHc1",
            UnitOfEnergy.KILO_WATT_HOUR,
            "mdi:flash",
            0,
            SensorDeviceClass.ENERGY,
        ],
        "PowerEnergyConsumptionHotWaterCircuit": [
            "PrEnergySumHwc1",
            UnitOfEnergy.KILO_WATT_HOUR,
            "mdi:flash",
            0,
            SensorDeviceClass.ENERGY,
        ],
        "RoomThermostat": ["DCRoomthermostat", None, "mdi:toggle-switch", 2, None],
        "HeatingPartLoad": [
            "PartloadHcKW",
            UnitOfEnergy.KILO_WATT_HOUR,
            "mdi:flash",
            0,
            SensorDeviceClass.ENERGY,
        ],
        "StateNumber": ["StateNumber", None, "mdi:fire", 3, None],
        "ModulationPercentage": [
            "ModulationTempDesired",
            PERCENTAGE,
            "mdi:percent",
            0,
            None,
        ],
    },
}
