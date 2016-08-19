import re
import datetime


class Dataset(object):

    @staticmethod
    def helper_eval(value):
        '''
        Provides some utilities for macro "now"
        '''
        if "#" in value:
            value = str(value)
        if value == None or type(value) != str:
            return value

        def _eval_re_now(r):
            t = r.string
            match = t[r.regs[0][0]:r.regs[0][1]]
            match_format = re.search('\\[[^#\\]]*]', match)
            '''
            formats : http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
            '''
            if match_format is None:
                match_format = '%d/%m/%y %H:%M'
            else:
                match_format_r = match_format.regs
                match_format = match[match_format_r[0][0] + 1:match_format_r[0][1] - 1]
            delta = datetime.timedelta(0)
            match_delta = re.search("[-+][0-9]+M", match)
            if not match_delta is None:
                minutes = int(match[match_delta.regs[0][0]:match_delta.regs[0][1]].replace(' ', '').replace('M', ''))
                delta = datetime.timedelta(minutes=minutes)
            match_delta = re.search("[-+][0-9]+H", match)
            if not match_delta is None:
                hours = int(match[match_delta.regs[0][0]:match_delta.regs[0][1]].replace(' ', '').replace('H', ''))
                delta = datetime.timedelta(hours=hours)
            match_delta = re.search("[-+][0-9]+d", match)
            if not match_delta is None:
                days = int(match[match_delta.regs[0][0]:match_delta.regs[0][1]].replace(' ', '').replace('d', ''))
                delta = datetime.timedelta(days=days)
            return (datetime.datetime.now() + delta).strftime(match_format)


        filters = {
            '#now\\[?[^#\\]]*]?[ 0-9MHd+-]*#': _eval_re_now,
        }
  
        t = value
        for regexp in filters:
            t = re.sub(regexp, filters[regexp], t)
        return t
