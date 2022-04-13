"""main module"""
class Parser:
    """main class"""
    def default_open_tag_callback(self):
        """function which manages open_tags"""

    def default_data_callback(self):
        """function which manages data"""

    def default_close_tag_callback(self):
        """function which manages close_tags"""

    def __init__(self, myopen, mydata, myclose):
        """function which manages initialisation"""
        self.default_open_tag_callback = myopen
        self.default_data_callback = mydata
        self.default_close_tag_callback = myclose

    def parse(self, html_str: str, parse_container):
        """function which manages parsing"""
        i = 0
        while i < (len(html_str)):
            start_tag_index = html_str.find('<', i)
            if start_tag_index == -1:
                self.default_data_callback(html_str[i:], parse_container[1])
                break
            if i < start_tag_index:
                self.default_data_callback(html_str[i:start_tag_index], parse_container[1])
                i = start_tag_index

            stop_tag_index = html_str.find('>', i) + 1
            if html_str[start_tag_index + 1] == '/':
                self.default_close_tag_callback(html_str[start_tag_index:stop_tag_index],
                                                parse_container[2])
                i = stop_tag_index
                continue

            self.default_open_tag_callback(html_str[start_tag_index:stop_tag_index],
                                           parse_container[0])
            i = stop_tag_index
            continue


def open_f(html, lst):
    """example function"""
    lst.append(html)


def close_f(html, lst):
    """example function"""
    lst.append(html)


def data_f(html, lst):
    """example function"""
    lst.append(html)


if __name__ == "__main__":
    CONTAINER = [[], [], []]
    STR = "<p>abcd</p><meta content_type><body>my_site_body<p>some_more</p></body>"
    P = Parser(open_f, data_f, close_f)
    P.parse(STR, CONTAINER)
    print(CONTAINER)
    print(P.__dict__)
