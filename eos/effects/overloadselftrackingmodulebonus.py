# Used by:
# Modules from group: Remote Tracking Computer (10 of 10)
# Modules from group: Tracking Computer (14 of 14)
# Modules from group: Tracking Disruptor (10 of 10)
# Variations of module: Omnidirectional Tracking Link I (8 of 8)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("maxRangeBonus", module.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
    module.boostItemAttr("falloffBonus", module.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
    module.boostItemAttr("trackingSpeedBonus", module.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
