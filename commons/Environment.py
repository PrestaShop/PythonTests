class Environment(object):
    """
    Modelize an environment and access to DB Sessions
    """

    def __init__(self, name, url, login, password, store_source, my_env):
        """
        Constructor
        @param name: the name of the environment "Admin-dev"
        @param url: url of the platform (login page)
        @param login: login for the connection on the site (ADMIN page or CLIENT page)
        @param password: password for the connection
        """
        self._name = name
        self._url = url
        self._login = login
        self._password = password
        self._store_source = store_source
        self._my_env = my_env
        

    def __repr__(self):
        return "<Environment ('%s', '%s', '%s', '%s', '%s')>" % (self._url, self._login, self._password, self._store_source, self._my_env)

    @classmethod
    def fromfilepath(cls, name, path_to_env_file):
        """
        Overloading the default constructor
        """
        
        f = open(path_to_env_file, "r")
        for line in f:
                my_line = line.split('/*/')
                if my_line != "":
                    if my_line[0] == name.upper():                       
                        url = (my_line[1].split(',')[0]).split(':=')[1]
                        login = (my_line[1].split(',')[1]).split(':=')[1]
                        password = (my_line[1].split(',')[2]).split(':=')[1]
                        store_source = (my_line[1].split(',')[3]).split(':=')[1]
                        my_env = name.upper()
        
        return cls(name=name,
                   url=url,
                   login=login,
                   password=password,
                   store_source=store_source,
                   my_env=my_env)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        
    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value
        
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    
    @property
    def store_source(self):
        return self._store_source

    @store_source.setter
    def store_source(self, value):
        self._store_source = value
        
    @property
    def my_env(self):
        return self._my_env
    
    @my_env.setter
    def my_env(self, value):
        self._my_env = value
