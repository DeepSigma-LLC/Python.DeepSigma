from blpapi import *


class BloombergServiceConnection:
    def __init__(self):
        self.session: Session = None
        self.data_service: Service = None
        self.__session_started: bool = False

    def start_session(self) -> bool:
        """Starts Bloomberg session."""
        if self.session is not None:
            self.kill_connection()

        server_host: str = "localhost"
        server_port: int = 8194
        session_options: SessionOptions = SessionOptions()
        session_options.ServerHost = server_host
        session_options.ServerPort = server_port
        session_options.NumStartAttempts = 1
        self.session = Session(session_options)
        self.__session_started = self.session.start()

        if self.__session_started:
            service_open: bool = self.session.openService("//blp/refdata")
            self.data_service = self.session.getService("//blp/refdata")
            self.__session_started = service_open

        return self.__session_started

    def kill_connection(self) -> None:
        """Kills Bloomberg connection."""
        self.session.stop()
        self.__session_started = False

    def test_bloomberg_connection(self) -> bool:
        """Tests if Bloomberg is connected."""
        self.start_session()
        result: bool = self.__session_started
        self.kill_connection()
        return result

    def is_session_started(self) -> bool:
        """Returns boolean determining is session has be started."""
        return self.__session_started
