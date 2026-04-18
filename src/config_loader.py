from interfaces.core import Platform


def load_bot_config(path: str) -> dict:
    return {}


def get_platform_from_config(config: dict) -> Platform:
    return Platform.PUMP_FUN


def print_config_summary(config: dict) -> None:
    pass


def validate_platform_listener_combination(platform: Platform, listener_type: str) -> bool:
    return True


def get_supported_listeners_for_platform(platform: Platform) -> list[str]:
    return []
