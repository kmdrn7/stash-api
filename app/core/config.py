import os
from pydantic import BaseSettings
from dotenv import dotenv_values, find_dotenv
import hvac


"""
- check if vault related environment variables exist
    - if exist, get config data from vault
    - else
        - if .env file exist, get config data from .env file
        - else, throw error setup configuration
- validate configuration
"""


class Settings(BaseSettings):

    configurations = {
        "APP_NAME": "Stash API",
        "APP_VERSION": "1.0.0",
        "OPENAPI_URL": "/openapi.json",
        "BITBUCKET_TOKEN": None
    }

    # For container usage
    def setupEnvironmentVariable(self):
        envvarConfig = {}
        for envKey in self.configurations.keys():
            if self.configurations[envKey] == None:
                if os.getenv(envKey) != None:
                    envvarConfig[envKey] = os.getenv(envKey)
                else:
                    raise Exception("Missing environment variable [%s]" % envKey)
        return envvarConfig

    def setup(self):

        usingVault = False

        if os.getenv("VAULT_ADDR") != None and \
                os.getenv("VAULT_PORT") != None and \
                os.getenv("VAULT_CONFIG") != None and \
                os.getenv("VAULT_TOKEN") != None:
            usingVault = True

        if usingVault:
            # For production usage using vault
            client = hvac.Client(
                url="{}:{}".format(
                    os.getenv("VAULT_ADDR"),
                    os.getenv("VAULT_PORT"),
                ),
                token=os.getenv("VAULT_TOKEN"),
            )
            loaded_conf = client.secrets.kv.v1.read_secret(
                path=os.getenv("VAULT_CONFIG"),
            )["data"]
        else:
            if find_dotenv(".env") != "": # Check for .env file if available
                loaded_conf = dotenv_values(".env") # Load .env file for development
            else:
                loaded_conf = self.setupEnvironmentVariable()

        print(loaded_conf)

        # Fill avaible configuration dictionary
        for config_key in self.configurations.keys():
            if self.configurations[config_key] is None:
                self.configurations[config_key] = loaded_conf[config_key]

        return self.configurations

    def get(self):
        return self.configurations


settings = Settings()
