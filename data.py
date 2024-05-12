class Url:
    URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER_USER_HANDLE = '/api/auth/register'
    AUTHORIZATION_USER_HANDLE = '/api/auth/user'
    ORDERS_HANDLE = '/api/orders'


class Ingredients:
    FLUORESCENT_BUN = "61c0c5a71d1f82001bdaaa6d"
    KRATOR_BUN = "61c0c5a71d1f82001bdaaa6c"
    IMMORTAL_PROTOSTOMIA_MEAT = "61c0c5a71d1f82001bdaaa6f"
    BEEF_METEORITE = "61c0c5a71d1f82001bdaaa70"
    SPACE_SAUCE = "61c0c5a71d1f82001bdaaa73"
    TRADITIONAL_GALACTIC_SAUCE = "61c0c5a71d1f82001bdaaa74"


class Burger:
    SPACE_METEORITE_FLUORESCENT_BURGER = {
        "name": "Space метеоритный флюоресцентный бургер",
        "ingredients_list": [Ingredients.FLUORESCENT_BUN,
                             Ingredients.SPACE_SAUCE,
                             Ingredients.BEEF_METEORITE]
    }
    IMMORTAL_TRADITIONAL_GALACTIC_KRATOR_BURGER = {
        "name": "Бессмертный традиционный-галактический краторный бургер",
        "ingredients_list": [Ingredients.KRATOR_BUN,
                             Ingredients.IMMORTAL_PROTOSTOMIA_MEAT,
                             Ingredients.TRADITIONAL_GALACTIC_SAUCE]
    }
