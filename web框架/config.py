"""Flask 配置：按环境拆分，create_app 里 from_object 加载。"""


class Config:
    SECRET_KEY = "please-change-me-in-production"
    JSON_ASCII = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
