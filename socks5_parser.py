"""
# Socks5 Address Parser

Simple socks5 address parser written in python.

"""
def socks_parse(address: str) -> dict:
    """
        Socks5 address parser

        Takes in a socks5 address string and creates a dictionary of its
        contents. If no port is given it defaults to 1080.

        Example inputs:
            >>> socks_parse('socks5://Username:Password@127.0.0.1:12345')
            {'username': 'Username', 'password': 'Password', 'hostname': '127.0.0.1', 'port': '12345'}

            >>> socks_parse('socks5://127.0.0.1:12345')
            {'username': '', 'password': '', 'hostname': '127.0.0.1', 'port': '12345'}

            >>> socks_parse('localhost')
            {'username': '', 'password': '', 'hostname': 'localhost', 'port': '1080'}
    """
    if address.startswith('socks5://'):
        address = address[9:]

    if '@' in address:
        credentials, address = address.split('@')
        if ':' in credentials:
            username, password = credentials.split(':')
        else:
            username, password = credentials, ''
    else:
        username, password = '', ''

    if ':' in address:
        hostname, port = address.split(':')
    elif address:
        hostname = address
        port = '1080'
    else:
        hostname = ''
        port = ''

    return {
        'username': username,
        'password': password,
        'hostname': hostname,
        'port': port,
    }


if __name__ == '__main__':
    import doctest
    doctest.testmod()
