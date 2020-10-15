__version__ = "0.5.0-alpha.0"

import json
from my_functions import caller_name


class Settings:
    """Class for reading and writing settings to JSON config file."""

    def __init__(self, logger, config_file=r"config.json"):
        """Create private variables and defines internal logger instance."""
        self.__log = logger
        self.__config_file = config_file
        self.__config_dict = {}

    def __update_config(self):
        """Reads class-scope __config_file and updates private config_dict"""
        with open(self.__config_file, "r") as f:
            config = json.load(f)
            self.__config_dict.update(config)

    def __write_config(self, config_dict):
        """Write config_dict to class-scope __config_file."""
        with open(self.config_file, "w") as f:
            self.__config_dict.update(config_dict)
            json.dump(self.__config_dict, f)
            self.__logger.debug(f"Settings written: {json.dumps(config_dict)}")

    # Begin public functions

    def set_config_file(self, config_file):
        """Updates private config file variable"""
        self.__config_file = config_file
        self.__log.debug(f"Config file set to: {self.__config_file}")

    def update_config(self):
        """Helper function to update private config_dict"""
        self.__update_config()

    def get_config(self):
        """Public function to retrieve the current settings"""
        self.__log.debug(f"Config requested by {caller_name()}.")
        return self.__config_dict

    def write_config(self, config_dict):
        """Public function to write a settings dictionary to file

        Uses the already assigned config file. To write to a different file,
        call 'set_config_file(filename)' first."""
        self.__log.debug(
            "update_config() called by {caller_name()}. Running __write_config()..."
        )
        self.__write_config(config_dict)