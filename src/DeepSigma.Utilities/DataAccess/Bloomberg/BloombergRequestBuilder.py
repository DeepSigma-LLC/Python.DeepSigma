import blpapi
from blpapi import *
from src.MetaKit.DataAccess.Bloomberg.BloombergRequestType import BloombergRequestType
from src.MetaKit.DataAccess.Bloomberg.BloombergPeriodicity import BloombergPeriodicity
from src.MetaKit.Utilities.DateTimeUtilities import *
from typing import Set


class BloombergRequestBuilder:
    DataService: Service = None
    RequestType: BloombergRequestType = None
    Securities: Set[str] = {}
    Fields: Set[str] = {}
    StartDate: datetime = None
    EndDate: datetime = None
    _request: Request = None
    FillMissingValues: bool = False
    IntervalInMinutes: int = 15
    SelectedPeriodicity: BloombergPeriodicity = None

    def build_data_request(self) -> Request:
        """Builds a Bloomberg data request using the parameters configured in this class."""
        self._request = self.DataService.createRequest(self.RequestType.value)

        if self.RequestType == BloombergRequestType.IntradayBar:
            self.__set_securities_to_request(self.Securities)
            self.__set_event_type_to_request("TRADE")
            # self.AppendPeriodicityAdjustmentToRequest("ACTUAL")
            self.__set_interval_in_minutes(self.IntervalInMinutes)
            self.__set_start_datetime_to_request(self.StartDate)
            self.__set_end_datetime_to_request(self.EndDate)
        else:
            self.__append_securities_to_request(self.Securities)
            self.__append_fields_to_request(self.Fields)

            if self.EndDate is not None:
                self.__append_start_date_to_request(self.StartDate)
                self.__append_end_date_to_request(self.EndDate)

            if self.SelectedPeriodicity is not None:
                self.__append_periodicity(self.SelectedPeriodicity)

        if self.FillMissingValues:
            self.__append_fill_method_to_request()
        return self._request

    def __append_securities_to_request(self, securities: Set[str]) -> None:
        for security in securities:
            self.__append_security_to_request(security)

    def __append_security_to_request(self, security: str) -> None:
        securities_name: Name = Name("securities")
        securities_element: Element = self._request.getElement(securities_name)
        securities_element.appendValue(security)

    def __append_fields_to_request(self, fields: Set[str]) -> None:
        for field in fields:
            self.__append_field_to_request(field)

    def __append_field_to_request(self, field: str) -> None:
        fields_name: Name = Name("fields")
        field_element: Element = self._request.getElement(fields_name)
        field_element.appendValue(field)

    def __set_securities_to_request(self, securities: Set[str]) -> None:
        for security in securities:
            self.__set_security_to_request(security)

    def __set_security_to_request(self, security: str) -> None:
        security_name: Name = Name("security")
        self._request.set(security_name, security)

    def __set_event_type_to_request(self, event_type: str) -> None:
        event_type_name: Name = Name("eventType")
        self._request.set(event_type_name, event_type)

    def __set_interval_in_minutes(self, interval_in_minutes: int) -> None:
        interval_name: Name = Name("interval")
        self._request.set(interval_name, interval_in_minutes)

    def __append_fill_method_to_request(self) -> None:
        fill_method_name: Name = Name("nonTradingDayFillMethod")
        self._request.set(fill_method_name, "PREVIOUS_VALUE")

        fill_option_name: Name = Name("nonTradingDayFillOption")
        self._request.set(fill_option_name, "ALL_CALENDAR_DAYS")

    def __append_start_date_to_request(self, start_date: datetime) -> None:
        start_date_name: Name = Name("startDate")
        date_text = DateTimeUtilities.date_to_string(selected_date=start_date, default_format_str="%Y%m%d")
        self._request.set(start_date_name, date_text)

    def __set_start_datetime_to_request(self, start_date: datetime) -> None:
        date = datetime(start_date.year, start_date.month, start_date.day)
        start_date_time_name: Name = Name("startDateTime")
        self._request.set(start_date_time_name, date)

    def __set_end_datetime_to_request(self, end_date: datetime) -> None:
        date = datetime(end_date.year, end_date.month, end_date.day)
        end_date_time_name: Name = Name("endDateTime")
        self._request.set(end_date_time_name, date)

    def __append_end_date_to_request(self, end_date: datetime) -> None:
        end_date_name: Name = Name("endDate")
        date_text = DateTimeUtilities.date_to_string(selected_date=end_date, default_format_str="%Y%m%d")
        self._request.set(end_date_name, date_text)

    def __append_periodicity(self, periodicity: BloombergPeriodicity) -> None:
        periodicity_name: Name = Name("periodicitySelection")
        self._request.set(periodicity_name, self.__get_periodicity(periodicity))

    def __get_periodicity(self, periodicity: BloombergPeriodicity) -> Name:
        if periodicity == BloombergPeriodicity.Daily:
            return Name("DAILY")
        elif periodicity == BloombergPeriodicity.Weekly:
            return Name("WEEKLY")
        elif periodicity == BloombergPeriodicity.Monthly:
            return Name("MONTHLY")
        elif periodicity == BloombergPeriodicity.Quarterly:
            return Name("QUARTERLY")
        elif periodicity == BloombergPeriodicity.SemiAnnual:
            return Name("SEMI_ANNUALLY")
        elif periodicity == BloombergPeriodicity.Annual:
            return Name("YEARLY")
        else:
            raise NotImplementedError()
