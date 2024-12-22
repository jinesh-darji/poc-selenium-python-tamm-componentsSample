# Test environment
import os

# Enviroment for running tests
ENV = "qa_pretest"
# ENV = "qa_prestg"

# Browser Settings
# Supported browsers: "chrome", "firefox", "ie", "safari", "remote"
# BROWSER = "chrome"
BROWSER = "chrome"

# Headless Settings
# Supported values: "y", "n"
HEADLESS = "y"

# Localization
# Supported locale: "en", "ar"
LOCALE = "en"

# Selenoid Settings (remote browser)
# SELENOID_HOST = "host"
# SELENOID_PORT = "4444"
# SELENOID_URL = "http://{host}:{port}/wd/hub".format(host=SELENOID_HOST, port=SELENOID_PORT)
# IS_VNC_ENABLED = True
# IS_VIDEO_ENABLED = False

# Mobile
# Android, iOS
MOBILE_PLATFORM_VERSION = "12.0"
# Android Emulator, iPhone X
#MOBILE_DEVICE_NAME = "Nexus_6P"
MOBILE_DEVICE_NAME = "Nexus_6P"
MOBILE_UDID = None
# MOBILE_UDID = "00008020-001E25901468002E"
# None
# "2.40"
MOBILE_CHROMEDRIVER_VERSION = "2.40"

CHECK_ACCESSIBILITY = False

APPIUM_HOST = "localhost"
APPIUM_PORT = "4723"
APPIUM_URL = "http://{host}:{port}/wd/hub".format(host=APPIUM_HOST, port=APPIUM_PORT)

# Waiting settings
IS_PRESENT_IMPLICITLY_WAIT_SEC = 1
IMPLICITLY_WAIT_SEC = 20
EXPLICITLY_WAIT_SEC = 20
PAGE_LOAD_TIMEOUT_SEC = 50
SCRIPT_TIMEOUT_SEC = 20
CUSTOM_WAIT_STEPTIME = 1
ELEMENTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pages', 'elements.json')
PATTERN_ENV_BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "environments", "{0}", "")
PATTERN_LOCALE_DICTIONARY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locale", "{0}",
                                              "dictionary.json")
PATTERN_LOCALE_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data", "{0}", "data.json")
TEST_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data/")
