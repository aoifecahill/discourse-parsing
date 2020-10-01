# Ensure there won't be logging complaints about no handlers being set
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

try:
    import zpar
except ImportError:
    raise ImportError("The 'python-zpar' package is missing. Run 'pip install python-zpar' to install it.") from None
