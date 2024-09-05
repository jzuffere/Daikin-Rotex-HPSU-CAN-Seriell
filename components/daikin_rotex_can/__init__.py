import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, binary_sensor, number, select, text_sensor, canbus, text
from esphome.const import *
from esphome.components.canbus import CanbusComponent
#from esphome.const import (
#    ENTITY_CATEGORY_CONFIG,
#)

daikin_rotex_can_ns = cg.esphome_ns.namespace('daikin_rotex_can')
DaikinRotexCanComponent = daikin_rotex_can_ns.class_('DaikinRotexCanComponent', cg.Component)
OperationModeSelect = daikin_rotex_can_ns.class_("OperationModeSelect", select.Select)
TargetHotWaterTemperatureNumber = daikin_rotex_can_ns.class_("TargetHotWaterTemperatureNumber", number.Number)
HeatingCurveNumber = daikin_rotex_can_ns.class_("HeatingCurveNumber", number.Number)
LogFilterText = daikin_rotex_can_ns.class_("LogFilterText", text.Text)

DEPENDENCIES = []

UNIT_BAR = "bar"
UNIT_LITER_PER_HOUR = "L/h"

AUTO_LOAD = ['binary_sensor', 'number', 'sensor', 'select', 'text', 'text_sensor']

CONF_CAN_ID = "canbus_id"
CONF_LOG_FILTER_TEXT = "log_filter"
CONF_ENTITIES = "entities"

########## Sensors ##########

CONF_TEMPERATURE_OUTSIDE = "temperature_outside"    # External temperature
CONF_TDHW1 = "tdhw1"
CONF_TARGET_HOT_WATER_TEMPERATURE = "target_hot_water_temperature"
CONF_TV = "tv"
CONF_TVBH = "tvbh"
CONF_TR = "tr"
CONF_WATER_PRESSURE = "water_pressure"
CONF_WATER_FLOW = "water_flow"
CONF_CIRCULATION_PUMP = "circulation_pump"
CONF_BYPASS_VALVE = "bypass_valve"
CONF_DHW_MIXER_POSITION = "dhw_mixer_position"
CONF_TARGET_SUPPLY_TEMPERATURE = "target_supply_temperature" # Vorlauf Soll
CONF_DAYTIME_SUPPLY_TEMPERATURE = "daytime_supply_temperature" # Temperatur Vorlauf Tag
CONF_THERMAL_POWER = "thermal_power" # Thermische Leistung
CONF_HEATING_CURVE = "heating_curve" # Heizkurve
CONF_EHS_FOR_CH = "ehs_for_ch"
CONF_TOTAL_ENERGY_PRODUCED = "total_energy_produced"
CONF_RUNTIME_COMPRESSOR = "runtime_compressor"
CONF_RUNTIME_PUMP = "runtime_pump"
CONF_MIN_TARGET_SUPPLY_TEMPERATURE = "min_target_supply_temperature" # Min Vorlauf Soll
CONF_MAX_TARGET_SUPPLY_TEMPERATURE = "max_target_supply_temperature" # Max Vorlauf Soll
CONF_SPREIZUNG_MOD_HZ = "spreizung_mod_hz"
CONF_SPREIZUNG_MOD_WW = "spreizung_mod_ww"

########## Text Sensors ##########

CONF_OPERATING_MODE = "operating_mode"
CONF_MODE_OF_OPERATING = "mode_of_operation"
CONF_HK_FUNCTION = "hk_function"
CONF_SG_MODE = "sg_mode"
CONF_SMART_GRID = "smart_grid"
CONF_ERROR_CODE = "error_code"

########## Binary Sensors ##########

CONF_STATUS_KOMPRESSOR = "status_kompressor"
CONF_STATUS_KESSELPUMPE = "status_kesselpumpe"

########## Selects ##########

CONF_OPERATING_MODE_SELECT = "operating_mode_select"

########## Numbers ##########

CONF_TARGET_HOT_WATER_TEMPERATURE_SET = "target_hot_water_temperature_set"
CONF_HEATING_CURVE_SET = "heating_curve_set" # Heizkurve setzen

########## Icons ##########

ICON_SUN_SNOWFLAKE_VARIANT = "mdi:sun-snowflake-variant"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(DaikinRotexCanComponent),
        cv.Required(CONF_CAN_ID): cv.use_id(CanbusComponent),

        ########## Texts ##########

        cv.Optional(CONF_LOG_FILTER_TEXT): 
        text.TEXT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(LogFilterText),
                cv.Optional(CONF_MODE, default="TEXT"): cv.enum(text.TEXT_MODES, upper=True),
            }
        ),

        cv.Required(CONF_ENTITIES): cv.Schema(
            {
                ########## Sensors ##########

                cv.Optional(CONF_TEMPERATURE_OUTSIDE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_TDHW1): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_TARGET_HOT_WATER_TEMPERATURE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_TV): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_TVBH): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_TR): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_WATER_PRESSURE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_PRESSURE,
                    unit_of_measurement=UNIT_BAR,
                    accuracy_decimals=2,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_WATER_FLOW): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_WATER,
                    unit_of_measurement=UNIT_LITER_PER_HOUR,
                    accuracy_decimals=0,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_CIRCULATION_PUMP): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_VOLUME_FLOW_RATE,
                    unit_of_measurement=UNIT_PERCENT,
                    accuracy_decimals=0,
                    state_class=STATE_CLASS_MEASUREMENT,
                    icon="mdi:pump"
                ).extend(),
                cv.Optional(CONF_BYPASS_VALVE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_VOLUME_FLOW_RATE,
                    unit_of_measurement=UNIT_PERCENT,
                    accuracy_decimals=0,
                    state_class=STATE_CLASS_MEASUREMENT,
                    icon="mdi:waves-arrow-left"
                ).extend(),
                cv.Optional(CONF_DHW_MIXER_POSITION): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_VOLUME_FLOW_RATE,
                    unit_of_measurement=UNIT_PERCENT,
                    accuracy_decimals=0,
                    state_class=STATE_CLASS_MEASUREMENT,
                    icon="mdi:waves-arrow-left"
                ).extend(),
                cv.Optional(CONF_TARGET_SUPPLY_TEMPERATURE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_DAYTIME_SUPPLY_TEMPERATURE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=1,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_THERMAL_POWER): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_POWER,
                    unit_of_measurement=UNIT_KILOWATT,
                    accuracy_decimals=2,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_HEATING_CURVE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    icon="mdi:thermometer-lines",
                    accuracy_decimals=2,
                    state_class=STATE_CLASS_MEASUREMENT
                ).extend(),
                cv.Optional(CONF_EHS_FOR_CH): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_ENERGY_STORAGE,
                    state_class=STATE_CLASS_MEASUREMENT,
                    unit_of_measurement=UNIT_KILOWATT_HOURS,
                    accuracy_decimals=0,
                    icon="mdi:thermometer-lines",
                ).extend(),
                cv.Optional(CONF_TOTAL_ENERGY_PRODUCED): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_ENERGY_STORAGE,
                    state_class=STATE_CLASS_MEASUREMENT,
                    unit_of_measurement=UNIT_KILOWATT_HOURS,
                    accuracy_decimals=0,
                    icon="mdi:thermometer-lines",
                ).extend(),
                cv.Optional(CONF_RUNTIME_COMPRESSOR): sensor.sensor_schema(
                    state_class=STATE_CLASS_MEASUREMENT,
                    unit_of_measurement=UNIT_HOUR,
                    accuracy_decimals=0,
                    icon="mdi:clock-time-two-outline",
                ).extend(),
                cv.Optional(CONF_RUNTIME_PUMP): sensor.sensor_schema(
                    state_class=STATE_CLASS_MEASUREMENT,
                    unit_of_measurement=UNIT_HOUR,
                    accuracy_decimals=0,
                    icon="mdi:clock-time-two-outline",
                ).extend(),
                cv.Optional(CONF_MIN_TARGET_SUPPLY_TEMPERATURE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=0,
                    icon="mdi:waves-arrow-left",
                ).extend(),
                cv.Optional(CONF_MAX_TARGET_SUPPLY_TEMPERATURE): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=0,
                    icon="mdi:waves-arrow-right",
                ).extend(),
                cv.Optional(CONF_SPREIZUNG_MOD_HZ): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=0,
                    icon="mdi:thermometer-lines",
                ).extend(),
                cv.Optional(CONF_SPREIZUNG_MOD_WW): sensor.sensor_schema(
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    unit_of_measurement=UNIT_CELSIUS,
                    accuracy_decimals=0,
                    icon="mdi:thermometer-lines",
                ).extend(),

                ######## Text Sensors ########

                cv.Optional(CONF_OPERATING_MODE): text_sensor.text_sensor_schema(
                    icon=ICON_SUN_SNOWFLAKE_VARIANT
                ).extend(),
                cv.Optional(CONF_MODE_OF_OPERATING): text_sensor.text_sensor_schema(
                    icon=ICON_SUN_SNOWFLAKE_VARIANT
                ).extend(),
                cv.Optional(CONF_HK_FUNCTION): text_sensor.text_sensor_schema(
                    icon="mdi:weather-partly-cloudy"
                ).extend(),
                cv.Optional(CONF_ERROR_CODE): text_sensor.text_sensor_schema(
                    icon="mdi:alert"
                ).extend(),
                cv.Optional(CONF_SG_MODE): text_sensor.text_sensor_schema(
                    icon="mdi:thermometer-lines",
                ).extend(),
                cv.Optional(CONF_SMART_GRID): text_sensor.text_sensor_schema(
                    icon="mdi:thermometer-lines",
                ).extend(),

                ########## Binary Sensors ##########

                cv.Optional(CONF_STATUS_KOMPRESSOR): binary_sensor.binary_sensor_schema(
                    icon="mdi:pump"
                ).extend(),
                cv.Optional(CONF_STATUS_KESSELPUMPE): binary_sensor.binary_sensor_schema(
                    icon="mdi:pump"
                ).extend(),

                ########## Selects ##########

                cv.Optional(CONF_OPERATING_MODE_SELECT): select.select_schema(
                    OperationModeSelect,
                    entity_category=ENTITY_CATEGORY_CONFIG,
                    icon=ICON_SUN_SNOWFLAKE_VARIANT
                ).extend(),

                ########## Number ##########

                cv.Optional(CONF_TARGET_HOT_WATER_TEMPERATURE_SET): number.number_schema(
                    TargetHotWaterTemperatureNumber,
                    entity_category=ENTITY_CATEGORY_CONFIG,
                    icon=ICON_SUN_SNOWFLAKE_VARIANT
                ).extend(),
                cv.Optional(CONF_HEATING_CURVE_SET): number.number_schema(
                    HeatingCurveNumber,
                    entity_category=ENTITY_CATEGORY_CONFIG,
                    icon=ICON_SUN_SNOWFLAKE_VARIANT
                ).extend(),
            }
        ),
    }
).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    if CONF_CAN_ID in config:
        cg.add_define("USE_CANBUS")
        canbus = yield cg.get_variable(config[CONF_CAN_ID])
        cg.add(var.set_canbus(canbus))

    ########## Texts ##########

    if log_filter := config.get(CONF_LOG_FILTER_TEXT):
        te = yield text.new_text(log_filter)
        cg.add(var.getAccessor().set_log_filter(te))

    if entities := config.get(CONF_ENTITIES):
        ########## Sensors ##########

        if temperature_outside := entities.get(CONF_TEMPERATURE_OUTSIDE):
            sens = yield sensor.new_sensor(temperature_outside)
            cg.add(var.getAccessor().set_temperature_outside(sens))

        if tdhw1 := entities.get(CONF_TDHW1):
            sens = yield sensor.new_sensor(tdhw1)
            cg.add(var.getAccessor().set_tdhw1(sens))

        if target_hot_water_temperature := entities.get(CONF_TARGET_HOT_WATER_TEMPERATURE):
            sens = yield sensor.new_sensor(target_hot_water_temperature)
            cg.add(var.getAccessor().set_target_hot_water_temperature(sens))

        if tv := entities.get(CONF_TV):
            sens = yield sensor.new_sensor(tv)
            cg.add(var.getAccessor().set_tv(sens))

        if tvbh := entities.get(CONF_TVBH):
            sens = yield sensor.new_sensor(tvbh)
            cg.add(var.getAccessor().set_tvbh(sens))

        if tr := entities.get(CONF_TR):
            sens = yield sensor.new_sensor(tr)
            cg.add(var.getAccessor().set_tr(sens))

        if water_pressure := entities.get(CONF_WATER_PRESSURE):
            sens = yield sensor.new_sensor(water_pressure)
            cg.add(var.getAccessor().set_water_pressure(sens))

        if water_flow := entities.get(CONF_WATER_FLOW):
            sens = yield sensor.new_sensor(water_flow)
            cg.add(var.getAccessor().set_water_flow(sens))

        if circulation_pump := entities.get(CONF_CIRCULATION_PUMP):
            sens = yield sensor.new_sensor(circulation_pump)
            cg.add(var.getAccessor().set_circulation_pump(sens))

        if bypass_valve := entities.get(CONF_BYPASS_VALVE):
            sens = yield sensor.new_sensor(bypass_valve)
            cg.add(var.getAccessor().set_bypass_valve(sens))

        if dhw_mixer_position := entities.get(CONF_DHW_MIXER_POSITION):
            sens = yield sensor.new_sensor(dhw_mixer_position)
            cg.add(var.getAccessor().set_dhw_mixer_position(sens))

        if target_supply_temperature := entities.get(CONF_TARGET_SUPPLY_TEMPERATURE):
            sens = yield sensor.new_sensor(target_supply_temperature)
            cg.add(var.getAccessor().set_target_supply_temperature(sens))

        if daytime_supply_temperature := entities.get(CONF_DAYTIME_SUPPLY_TEMPERATURE):
            sens = yield sensor.new_sensor(daytime_supply_temperature)
            cg.add(var.getAccessor().set_daytime_supply_temperature(sens))

        if thermal_power := entities.get(CONF_THERMAL_POWER):
            sens = yield sensor.new_sensor(thermal_power)
            cg.add(var.getAccessor().set_thermal_power(sens))

        if heating_curve := entities.get(CONF_HEATING_CURVE):
            sens = yield sensor.new_sensor(heating_curve)
            cg.add(var.getAccessor().set_heating_curve(sens))

        if ehs_for_ch := entities.get(CONF_EHS_FOR_CH):
            sens = yield sensor.new_sensor(ehs_for_ch)
            cg.add(var.getAccessor().set_ehs_for_ch(sens))

        if total_energy_produced := entities.get(CONF_TOTAL_ENERGY_PRODUCED):
            sens = yield sensor.new_sensor(total_energy_produced)
            cg.add(var.getAccessor().set_total_energy_produced(sens))

        if runtime_compressor := entities.get(CONF_RUNTIME_COMPRESSOR):
            sens = yield sensor.new_sensor(runtime_compressor)
            cg.add(var.getAccessor().set_runtime_compressor(sens))

        if runtime_pump := entities.get(CONF_RUNTIME_PUMP):
            sens = yield sensor.new_sensor(runtime_pump)
            cg.add(var.getAccessor().set_runtime_pump(sens))

        if min_target_supply_temperature := entities.get(CONF_MIN_TARGET_SUPPLY_TEMPERATURE):
            sens = yield sensor.new_sensor(min_target_supply_temperature)
            cg.add(var.getAccessor().set_min_target_supply_temperature(sens))

        if max_target_supply_temperature := entities.get(CONF_MAX_TARGET_SUPPLY_TEMPERATURE):
            sens = yield sensor.new_sensor(max_target_supply_temperature)
            cg.add(var.getAccessor().set_max_target_supply_temperature(sens))

        if spreizung_mod_hz := entities.get(CONF_SPREIZUNG_MOD_HZ):
            sens = yield sensor.new_sensor(spreizung_mod_hz)
            cg.add(var.getAccessor().set_spreizung_mod_hz(sens))

        if spreizung_mod_ww := entities.get(CONF_SPREIZUNG_MOD_WW):
            sens = yield sensor.new_sensor(spreizung_mod_ww)
            cg.add(var.getAccessor().set_spreizung_mod_ww(sens))

        ######## Text Sensors ########

        if operating_mode := entities.get(CONF_OPERATING_MODE):
            sens = yield text_sensor.new_text_sensor(operating_mode)
            cg.add(var.getAccessor().set_operating_mode(sens))

        if mode_of_operating := entities.get(CONF_MODE_OF_OPERATING):
            sens = yield text_sensor.new_text_sensor(mode_of_operating)
            cg.add(var.getAccessor().set_mode_of_operating(sens))

        if hk_function := entities.get(CONF_HK_FUNCTION):
            sens = yield text_sensor.new_text_sensor(hk_function)
            cg.add(var.getAccessor().set_hk_function(sens))

        if error_code := entities.get(CONF_ERROR_CODE):
            sens = yield text_sensor.new_text_sensor(error_code)
            cg.add(var.getAccessor().set_error_code(sens))

        if sg_mode := entities.get(CONF_SG_MODE):
            sens = yield text_sensor.new_text_sensor(sg_mode)
            cg.add(var.getAccessor().set_sg_mode(sens))

        if smart_grid := entities.get(CONF_SMART_GRID):
            sens = yield text_sensor.new_text_sensor(smart_grid)
            cg.add(var.getAccessor().set_smart_grid(sens))

        ######## Binary Sensors ########

        if status_kompressor := entities.get(CONF_STATUS_KOMPRESSOR):
            sens = yield binary_sensor.new_binary_sensor(status_kompressor)
            cg.add(var.getAccessor().set_status_kompressor(sens))

        if status_kesselpumpe := entities.get(CONF_STATUS_KESSELPUMPE):
            sens = yield binary_sensor.new_binary_sensor(status_kesselpumpe)
            cg.add(var.getAccessor().set_status_kesselpumpe(sens))

        ########## Selects ##########

        operating_mode_options = ["Bereitschaft", "Heizen", "Absenken", "Sommer", "Kühlen", "Automatik 1", "Automatik 2"]

        if operating_mode_select := entities.get(CONF_OPERATING_MODE_SELECT):
            s = yield select.new_select(operating_mode_select, options = operating_mode_options)
            yield cg.register_parented(s, var)
            cg.add(var.getAccessor().set_operating_mode_select(s))

        ########## Numbers ##########

        if target_hot_water_temperature_set := entities.get(CONF_TARGET_HOT_WATER_TEMPERATURE_SET):
            num = yield number.new_number(
                target_hot_water_temperature_set,
                min_value=35,
                max_value=70,
                step=1
            )
            yield cg.register_parented(num, var)
            cg.add(var.getAccessor().set_target_hot_water_temperature_set(num))

        if heating_curve_set := entities.get(CONF_HEATING_CURVE_SET):
            num = yield number.new_number(
                heating_curve_set,
                min_value=0,
                max_value=2.55,
                step=0.01
            )
            yield cg.register_parented(num, var)
            cg.add(var.getAccessor().set_heating_curve_set(num))

    cg.add(var.validateConfig())
