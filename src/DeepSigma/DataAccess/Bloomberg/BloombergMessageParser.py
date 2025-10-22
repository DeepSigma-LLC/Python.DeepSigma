import datetime
from blpapi import *
from src import BloombergDataPoint
from src import BloombergHistoricalDataPoint
from src import BloombergHistoricalBarDataPoint
from src import BloombergDataPointStructure
from src import BloombergHistoricalDataStructure
from src import BloombergHistoricalBarDataStructure
from src import BloombergDataBar
from typing import List


class BloombergMessageParser:
    __security_name: name = Name("security")
    __bar_data_name: name = Name("barData")
    __security_data_name: Name = Name("securityData")
    __field_data_name: Name = Name("fieldData")
    __bar_tick_data_name: Name = Name("barTickData")

    @staticmethod
    def deserialize_response_loop_to_result(message: Message, need_only_for_func_inject: str = "") -> BloombergDataPoint:
        """Parses Bloomberg data point messages."""
        results: BloombergDataPoint = BloombergDataPoint()
        try:
            results = BloombergMessageParser.__deserialize_response_loop(message)
        except:
            pass
        return results

    @staticmethod
    def deserialize_response_to_historical_result(message: Message, target_field: str) -> BloombergHistoricalDataPoint:
        """Parses Bloomberg historical data messages."""
        results: BloombergHistoricalDataPoint = BloombergHistoricalDataPoint()
        try:
            results = BloombergMessageParser.__deserialize_historical_response(message, target_field)
        except:
            pass
        return results

    @staticmethod
    def deserialize_response_to_historical_bar_result(message: Message, security: str) -> BloombergHistoricalBarDataPoint:
        """Parses Bloomberg historical bar data messages."""
        results: BloombergHistoricalBarDataPoint = BloombergHistoricalBarDataPoint()
        try:
            results = BloombergMessageParser.__deserialize_historical_bar_response(message, security)
        except:
            pass
        return results

    @staticmethod
    def __deserialize_response_loop(message: Message) -> BloombergDataPoint:
        """Parses Bloomberg data point messages in a loop."""
        results: BloombergDataPoint = BloombergDataPoint()
        security_data: Element = BloombergMessageParser.__get_security_data_element(message)
        security_data_elements: List[Element] = BloombergMessageParser.__get_sub_values_as_elements_from_element(
            security_data)
        for securityDataElement in security_data_elements:
            field_data_elements: List[Element] = BloombergMessageParser.__get_sub_elements_from_element(
                securityDataElement)
            for fieldDataElement in field_data_elements:
                fields: List[Element] = BloombergMessageParser.__get_sub_elements_from_element(fieldDataElement)
                for field in fields:
                    result: BloombergDataPointStructure = BloombergDataPointStructure()
                    result.ticker = BloombergMessageParser.__get_security_name_from_security_element(securityDataElement)
                    result.parsed_message = message.toString()
                    result.field = str(field.name())
                    result.value = field.getValueAsString()
                    results.add(result)
        return results

    @staticmethod
    def __deserialize_historical_response(message: Message, target_field: str) -> BloombergHistoricalDataPoint:
        """Parses Bloomberg historical data messages."""
        results: BloombergHistoricalDataPoint = BloombergHistoricalDataPoint()
        result: BloombergHistoricalDataStructure = BloombergHistoricalDataStructure()
        security_data: Element = BloombergMessageParser.__get_security_data_element(message)
        security_data_elements: List[Element] = BloombergMessageParser.__get_sub_elements_from_element(security_data)
        matched_security_data_elements: List[Element] = [x for x in security_data_elements
                                                         if x.name() == BloombergMessageParser.__field_data_name]
        field_data_elements: List[Element] = BloombergMessageParser.__get_sub_values_as_elements_from_multiple_elements(
            matched_security_data_elements)
        fields: List[Element] = BloombergMessageParser.__get_sub_elements_from_multiple_elements(field_data_elements)

        result.ticker = BloombergMessageParser.__get_security_name_from_security_data(security_data)
        result.field = target_field
        result.parsed_message = message.toString()
        result.data = {}
        data_date: datetime = None
        for field in fields:
            if str(field.name()).lower() == "date":
                data_date = field.getValueAsDatetime()

            if str(field.name()).lower() == target_field.lower():
                return_value: float = field.getValueAsFloat()
                result.data[data_date] = return_value

        results.add(result)
        return results

    @staticmethod
    def __deserialize_historical_bar_response(message: Message, security: str) -> BloombergHistoricalBarDataPoint:
        """Parses Bloomberg historical bar data messages."""
        results: BloombergHistoricalBarDataPoint = BloombergHistoricalBarDataPoint()
        result: BloombergHistoricalBarDataStructure = BloombergHistoricalBarDataStructure()

        bar_data: Element = BloombergMessageParser.__get_bar_data_element(message)
        bar_data_elements: List[Element] = BloombergMessageParser.__get_sub_elements_from_element(bar_data)
        filtered_list_of_elements: List[Element] = [x for x in bar_data_elements
                                                    if x.name() == BloombergMessageParser.__bar_tick_data_name]
        field_data_elements: List[Element] = BloombergMessageParser.__get_sub_values_as_elements_from_multiple_elements(
            filtered_list_of_elements)

        for barFieldData in field_data_elements:
            fields: List[Element] = BloombergMessageParser.__get_sub_elements_from_element(barFieldData)
            bar: BloombergDataBar = BloombergDataBar()
            date_time: datetime = [x for x in fields if x.name() == Name("time")][0].getValueAsDatetime()
            bar.close = [x for x in fields if x.name() == Name("close")][0].getValueAsFloat()
            bar.open = [x for x in fields if x.name() == Name("open")][0].getValueAsFloat()
            bar.high = [x for x in fields if x.name() == Name("high")][0].getValueAsFloat()
            bar.low = [x for x in fields if x.name() == Name("low")][0].getValueAsFloat()
            bar.volume = [x for x in fields if x.name() == Name("volume")][0].getValueAsFloat()
            bar.number_of_events = [x for x in fields if x.name() == Name("numEvents")][0].getValueAsInteger()
            result.data[date_time] = bar

        result.ticker = security
        result.parsed_message = message.toString()
        results.add(result)
        return results

    @staticmethod
    def __get_security_data_element(message: Message) -> Element:
        """Extracts the security data element from a Bloomberg message."""
        return message.getElement(BloombergMessageParser.__security_data_name)

    @staticmethod
    def __get_bar_data_element(message: Message) -> Element:
        """Extracts the bar data element from a Bloomberg message."""
        return message.getElement(BloombergMessageParser.__bar_data_name)

    @staticmethod
    def __get_security_name_from_security_data(security_data: Element) -> str:
        """Extracts the security name from a Bloomberg security data element."""
        result: str = ""
        if security_data.hasElement(BloombergMessageParser.__security_name):
            return security_data.getElementAsString(BloombergMessageParser.__security_name)
        return result

    @staticmethod
    def __get_security_name_from_security_element(security_data_element: Element) -> str:
        """Extracts the security name from a Bloomberg security data element."""
        if security_data_element.hasElement(BloombergMessageParser.__security_name):
            return security_data_element.getElementAsString(BloombergMessageParser.__security_name)
        return ""

    @staticmethod
    def __get_sub_elements_from_element(element: Element) -> List[Element]:
        """Extracts sub-elements from a Bloomberg Element."""
        sub_elements: List[Element] = []
        for i in range(element.numElements()):
            sub_elements.append(element.getElement(i))
        return sub_elements

    @staticmethod
    def __get_sub_elements_from_multiple_elements(elements: List[Element]) -> List[Element]:
        """Extracts sub-elements from multiple Bloomberg Elements."""
        sub_elements: List[Element] = []
        for element in elements:
            sub_elements.extend(BloombergMessageParser.__get_sub_elements_from_element(element))
        return sub_elements

    @staticmethod
    def __get_sub_values_as_elements_from_element(element: Element) -> List[Element]:
        """Extracts sub-values as elements from a Bloomberg Element."""
        my_elements: List[Element] = []
        for i in range(element.numValues()):
            my_elements.append(element.getValueAsElement(i))
        return my_elements

    @staticmethod
    def __get_sub_values_as_elements_from_multiple_elements(elements: List[Element]) -> List[Element]:
        """Extracts sub-values as elements from multiple Bloomberg Elements."""
        sub_elements: List[Element] = []
        for element in elements:
            sub_elements.extend(BloombergMessageParser.__get_sub_values_as_elements_from_element(element))
        return sub_elements
