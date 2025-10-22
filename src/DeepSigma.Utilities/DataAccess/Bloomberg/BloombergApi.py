from blpapi import *
from src.MetaKit.DataAccess.Bloomberg.BloombergServiceConnection import BloombergServiceConnection
from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergDataPoint import BloombergDataPoint
from src.MetaKit.DataAccess.Bloomberg.BloombergRequestBuilder import BloombergRequestBuilder
from src.MetaKit.DataAccess.Bloomberg.BloombergRequestType import BloombergRequestType
from src.MetaKit.DataAccess.Bloomberg.BloombergMessageParser import BloombergMessageParser
from src.MetaKit.DataAccess.Bloomberg.BloombergPeriodicity import BloombergPeriodicity
from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergHistoricalDataPoint import BloombergHistoricalDataPoint
from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergHistoricalBarDataPoint import BloombergHistoricalBarDataPoint
from typing import Set


class BloombergApi(BloombergServiceConnection):
    def __init__(self):
        super().__init__()
        self.bbg_connection_error_msg: str = "Unable to establish connection to Bloomberg."

    def bdp(self, securities: Set[str], fields: Set[str]) -> BloombergDataPoint:
        self.start_session()
        if not self.is_session_started():
            self.kill_connection()
            raise ConnectionError(self.bbg_connection_error_msg)

        builder: BloombergRequestBuilder = BloombergRequestBuilder()
        builder.DataService = self.data_service
        builder.Securities = securities
        builder.Fields = fields
        builder.RequestType = BloombergRequestType.DataPoint
        _request: Request = builder.build_data_request()
        self.session.sendRequest(_request, None)

        results: BloombergDataPoint = BloombergDataPoint()
        self.__deserialization_message_event_loop(results, BloombergMessageParser.deserialize_response_loop_to_result)
        self.kill_connection()
        return results

    def bdh(self, securities: Set[str], bbg_field: str, start_date: datetime, end_date: datetime,
            selected_periodicity: BloombergPeriodicity = BloombergPeriodicity.Daily,
            fill_missing_values: bool = False) -> BloombergHistoricalDataPoint:
        self.start_session()
        if not self.is_session_started():
            self.kill_connection()
            raise ConnectionError(self.bbg_connection_error_msg)

        builder: BloombergRequestBuilder = BloombergRequestBuilder()
        builder.DataService = self.data_service
        builder.Securities = securities
        builder.Fields = [bbg_field]
        builder.RequestType = BloombergRequestType.Historical
        builder.StartDate = start_date
        builder.EndDate = end_date
        builder.SelectedPeriodicity = selected_periodicity
        builder.FillMissingValues = fill_missing_values
        _request: Request = builder.build_data_request()
        self.session.sendRequest(_request, None)

        results: BloombergHistoricalDataPoint = BloombergHistoricalDataPoint()
        self.__deserialization_message_event_loop(results,
                                                  BloombergMessageParser.deserialize_response_to_historical_result,
                                                  bbg_field)
        self.kill_connection()
        return results

    def bdh_intraday_bar(self, security: str, start_date: datetime, end_date: datetime, interval_in_minutes: int,
                         fill_missing_values: bool = False) -> BloombergHistoricalBarDataPoint:
        self.start_session()
        if not self.is_session_started():
            self.kill_connection()
            raise ConnectionError(self.bbg_connection_error_msg)

        builder: BloombergRequestBuilder = BloombergRequestBuilder()
        builder.DataService = self.data_service
        builder.Securities = [security]
        builder.RequestType = BloombergRequestType.IntradayBar
        builder.StartDate = start_date
        builder.EndDate = end_date
        builder.IntervalInMinutes = interval_in_minutes
        builder.FillMissingValues = fill_missing_values
        _request: Request = builder.build_data_request()
        self.session.sendRequest(_request, None)

        results: BloombergHistoricalBarDataPoint = BloombergHistoricalBarDataPoint()
        self.__deserialization_message_event_loop(results,
                                                  BloombergMessageParser.deserialize_response_to_historical_bar_result,
                                                  security)
        self.kill_connection()
        return results

    def __deserialization_message_event_loop(self, results, deserialization_method, func_search_field: str = "") -> None:
        """Deserialization method that processes each bloomberg API message in an event loop."""
        message_text: str = results.get_message()
        while True:
            event_obj: Event = self.session.nextEvent()
            for msg in event_obj:
                message_text += msg.toString()
                result_object = deserialization_method(msg, func_search_field)
                for x in result_object.get_data():
                    results.add(x)

            if event_obj.eventType() == Event.RESPONSE:
                break
        results.set_message(message_text)
