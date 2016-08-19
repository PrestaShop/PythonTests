#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
from commons.Context import Context
from commons import  ui



class Test(object):
    _dataset_cache = None
    _junit = None
        

    class TestAssertException(Exception):

        def __init__(self, message):
            self._message = message

        @property
        def message(self):
            return self._message
        @message.setter
        def message(self, value):
            self._message = value

        def __str__(self):
            return self._message

        def __repr__(self):
            return "<TestAssertException ('{m}')>".format(m=self.message.replace('\n', " "))

    @staticmethod
    def assert_empty(iterable, error_message):
        """
        Giving an object that implements the __len__ method, check if __len__() == 0. If not
        raising an exception.
        @param iterable: any data structure that implements __len__
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(len(iterable) == 0, error_message)
        except Test.TestAssertException as e:
            e.message += " Item Not Empty, Length {l} (i)".format(l=len(iterable), i=iterable)
            raise e

    @staticmethod
    def assert_not_empty(iterable, error_message):
        """
        Giving an object that implements the __len__ method, check if __len__() > 0. If not
        raising an exception.
        @param iterable: any data structure that implements __len__
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(len(iterable) > 0, error_message)
        except Test.TestAssertException as e:
            e.message += " Item Empty"
            raise e

    @staticmethod
    def assert_equals(expected, actual, error_message, debug_message = None):
        """
        Giving objects that implement the __eq__ method, expected == actual. If not
        raising an exception.
        @param expected: any object that implements __eq__ that will act as a point of reference
        @param actual: any object that implements __eq__ that will compared against "expected"
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(expected == actual, error_message, debug_message)
        except Test.TestAssertException as e:
            padding = lambda x = 0: " " * (len("TestAssertException:") + x)
            e.message = e.message + "\n" \
                                  + "\n" \
                                  + padding() \
                                  + " Expected: '{e}'\n {p1}vs\n{p2}Actual: '{a}'".format(e=expected,
                                                                                      a=actual,
                                                                                      p1=padding(),
                                                                                      p2=padding(1))
            Context().logger.error(str(e))
            raise e

    @staticmethod
    def assert_almost_equals(expected, actual, compare, error_message):
        """
        Use the comparison function on two objects : compare(expected, actual). If not, raising an exception.
        @param expected: any object that will act as a point of reference
        @param actual: any object that will compared against "expected"
        @param compare: comparison function that returns a boolean
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(compare(expected, actual), error_message)
        except Test.TestAssertException as e:
            padding = lambda x = 0: " " * (len("TestAssertException:") + x)
            e.message = e.message + "\n" \
                                  + "\n" \
                                  + padding() \
                                  + " Expected: {e}\n {p1}vs\n{p2}Actual: {a}".format(e=expected,
                                                                                      a=actual,
                                                                                      p1=padding(),
                                                                                      p2=padding(1))
            raise e

    @staticmethod
    def assert_not_equals(expected, actual, error_message):
        """
        Giving objects that implement the __eq__ method, expected != actual. If not
        raising an exception.
        @param expected: any object that implements __eq__ that will act as a point of reference
        @param actual: any object that implements __eq__ that will compared against "expected"
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(not(expected == actual), error_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " Inputs Have The Same Value {v}".format(v=expected)
            raise e

    @staticmethod
    def assert_is_not_none(actual, error_message):
        """
        Check that actual is not None
        @param actual: any object
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(actual is not None, error_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " Input Is None !"
            raise e

    @staticmethod
    def assert_is_none(actual, error_message):
        """
        Check that actual is None
        @param actual: any object
        @param error_message: str, the message that will be contained in the exception, if such is thrown
        @return None
        @throws Test.TestAssertException
            """
        try:
            Test.assert_that(actual is None, error_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " Input Is Not None !"
            raise e

    @staticmethod
    def assert_contains(expected, container, error_message):
        """
        @summary: Check that expected is in container
        @param expected: the expected containee
        @param container: an object that implements __getitem__ or a set
        @param error_message: str, a human readable error message
        @return None
        @throws Test.TestAssertException
        """
        try:
            if type(expected) != set or type(container) != set:
                cond = expected in container
            else:
                cond = expected.intersection(container) == expected
            Test.assert_that(cond, error_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " {v} Is Not Contained In {c}".format(v=expected, c=container)
            raise e

    @staticmethod
    def assert_not_contains(expected, container, error_message):
        """
        @summary: Check that expected is not in container
        @param expected: the expected containee
        @param container: an object that implements __getitem__
        @param error_message: str, a human readable error message
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(expected not in container, error_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                        + " "*len("TestAssertException:") \
                        + " {v} Is Contained In {c}".format(v=expected, c=container)
            raise e

    @staticmethod
    def assert_less_or_equal(limit, actual, error_message, debug_message):
        """
        @summary: check that a value is <= to a given limit
        @param limit: the max value
        @param actual: the value to test
        @param error_message: str, a human readable error message
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(actual <= limit, error_message, debug_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " {v} Is Not Less Or Equal Than {c}".format(v=actual, c=limit)
            raise e

    @staticmethod
    def assert_more_or_equal(limit, actual, error_message, debug_message):
        """
        @summary: check that a value is >= to a given limit
        @param limit: the max value
        @param actual: the value to test
        @param error_message: str, a human readable error message
        @return None
        @throws Test.TestAssertException
        """
        try:
            Test.assert_that(actual >= limit, error_message, debug_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " {v} Is Not More Or Equal Than {c}".format(v=actual, c=limit)
            raise e

    @staticmethod
    def assert_raises(exception_type, error_message, callable_obj, *args, **kwargs):
        """
        @summary: check that a callable throws an exception
        @param exception_type: an exception type
        @param callable_obj: any callable
        @param error_message: the log error message
        @param args: positional parameters for callable_obj
        @param kwargs: named parameters for callable_obj
        @return None
        @throws Test.TestAssertException
        """
        raising = False
        try:
            callable_obj(*args, **kwargs)
        except exception_type:
            raising = True
        try:
            Test.assert_that(raising, error_message)
        except Test.TestAssertException as e:
            e.message = e.message + "\n" \
                                  + " "*len("TestAssertException:") \
                                  + " Callable {c} Did Not Raise {r} With " \
                                    "(args, kwargs) ({p1}, {p2})".format(c=callable_obj.__name__,
                                                                         r=exception_type.__name__,
                                                                         p1=args, p2=kwargs)
            raise e

    @staticmethod
    def assert_that(predicate, error_message, debug_message=None):
        """
        @summary Given a predicate: throws an exception containing a user defined error message
        @param predicate: a condition that will valued either as True or False
        @param error_message: when predicate -> False, an exception is raised an contain an error message
        @return None
        @throws Test.TestAssertException
        """
        if not predicate:
            ui.take_screenshot()
            Context().logger.error(error_message)
            raise Test.TestAssertException(error_message)
        if debug_message is not None :
            Context().logger.debug("assertion passed : " + debug_message)

    @staticmethod
    def wait_until(predicate, timeout_seconds, period=0.25, show_log=True):
        """
        @summary Call repeatedly the predicate until it returns true or timeout_seconds passed.
        @param predicate: a condition, modelized as a callable,  that will valued either as True or False
        @param timeout_seconds: the timeout in second
        @param period: the time to sleep between 2 calls to predicate. Defaults to 0.25s.
        @return True if a call to predicate returned True before timeout_seconds passed, else False
        """
        if show_log:
            Context().logger.info("waiting until predicate is true for {end} seconds".format(end=timeout_seconds))
        ultimatum = time.time() + timeout_seconds
        while time.time() < ultimatum:
            Context().logger.debug("checking predicate for wait until : {spent} / {end}".format(spent=str(time.time() - (ultimatum - timeout_seconds)), end=timeout_seconds))
            if predicate():
                return True
            time.sleep(period)
        return False
    
    @staticmethod
    def wait_loader(predicate, timeout_seconds, period=0.25):
        """
        @summary Call repeatedly the predicate until it returns true or timeout_seconds passed.
        @param predicate: a condition, modelized as a callable,  that will valued either as True or False
        @param timeout_seconds: the timeout in second
        @param period: the time to sleep between 2 calls to predicate. Defaults to 0.25s.
        @return True if a call to predicate returned True before timeout_seconds passed, else False
        """
        Context().logger.info("waiting until predicate is true for {end} seconds".format(end=timeout_seconds))
        ultimatum = time.time() + timeout_seconds
        while time.time() < ultimatum:
            Context().logger.debug("checking predicate for wait until : {spent} / {end}".format(spent=str(time.time() - (ultimatum - timeout_seconds)), end=timeout_seconds))
            if predicate():
                Context().logger.info("Loader is display")
            else:
                return True
            time.sleep(period)
        return False

