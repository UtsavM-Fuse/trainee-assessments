config_data = {
    "server_ip": "192.168.0.1",
    "port": "8080",
    "database": "mydb",
    "username": "admin",
    "password": "secretpassword",
}

with open("config.txt", "w") as file:
    for key, value in config_data.items():
        file.write(f"{key}={value}\n")


from typing import Dict


class ConfigurationManager:
    _instance = None

    def __new__(cls, config_file: str) -> "ConfigurationManager":
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._load_config(config_file)
        return cls._instance

    def _load_config(self, config_file: str) -> None:
        """
        Load configuration settings from the specified file.

        Args:
            config_file (str): The path to the configuration file.

        Raises:
            FileNotFoundError: If the specified file is not found.
        """
        try:
            with open(config_file, "r") as file:
                self._config_data = {}
                for line in file:
                    key, value = line.strip().split("=")
                    self._config_data[key.strip()] = value.strip()
        except FileNotFoundError:
            raise FileNotFoundError("Configuration file not found.")

    def get_config_value(self, key: str) -> str:
        """
        Get the value of the configuration setting for the given key.

        Args:
            key (str): The configuration setting key.

        Returns:
            str: The value of the configuration setting.

        Raises:
            KeyError: If the specified key is not found in the configuration.
        """
        if key in self._config_data:
            return self._config_data[key]
        raise KeyError(f"Configuration key '{key}' not found.")


# Client code
if __name__ == "__main__":
    # Create a configuration manager instance
    config_manager = ConfigurationManager("config.txt")

    # Access configuration settings
    try:
        print("Server IP:", config_manager.get_config_value("server_ip"))
        print("Port:", config_manager.get_config_value("port"))
        print("Database:", config_manager.get_config_value("database"))
        print("Username:", config_manager.get_config_value("username"))
        print("Password:", config_manager.get_config_value("password"))
    except FileNotFoundError as e:
        print("Error:", e)
    except KeyError as e:
        print("Error:", e)
