from Helpers.ConsoleWriter import ConsoleWriter

# base class to be used to capture user commands.
class Command:
    def __init__(self, ebookstore_manager) -> None:
        self.ebookstore_manager = ebookstore_manager
        self.console_writer = ConsoleWriter()

    def run(self):
        # abstract base class function to be overridden in sub-classes.
        pass