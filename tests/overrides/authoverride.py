from service.api.auth import SimpleBearerAuth


class TestSimpleBearerAuth(SimpleBearerAuth):
    def _validate_token(self, token: str) -> bool:
        return token == "dfkjvndfkvnslaeriosuhvibfgbjfg"
